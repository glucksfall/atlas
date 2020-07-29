# -*- coding: utf-8 -*-

'''
Project "Reconstruction of RBM from biological networks", Rodrigo Santibáñez, 2019-2020 @ NBL, UMayor
Citation:
DOI:
'''

__author__  = 'Rodrigo Santibáñez'
__license__ = 'gpl-3.0'

import io
import os
import re
import pandas
import pythoncyc

from .construct_model_from_metabolic_network import read_network

def checkPathwayTools():
	availableOrgs = pythoncyc.all_orgids()
	if availableOrgs:
		return availableOrgs
	else:
		raise Exception("PathwayTools is not running.\n" \
			"Please, execute in a terminal (nohup) pathway-tools -lisp -python-local-only (&)")
		return False

def execPathwayTools(path):
	cmd = "nohup pathway-tools -lisp -python-local-only &"
	cmd = re.findall(r'(?:[^\s,"]|"+(?:=|\\.|[^"])*"+)+', cmd)
	out, err = subprocess.Popen(cmd, shell = False, stdout = subprocess.PIPE, stderr = subprocess.PIPE).communicate()
	print(out, err)
	return 0

def selectOrganism(code):
	if checkPathwayTools():
		return pythoncyc.select_organism(code)

def returnGenes(code):
	organism = selectOrganism(code)
	genes = [ x.frameid for x in organism.genes.instances ]
	return genes

def returnCommonNames(code):
	genes = returnGenes(code)
	# and common names
	common_names = []

	genes_dict = {}
	for gene in genes:
		common = get_data(code, gene)['common_name']
		common_names.append(common)
		genes_dict[common] = gene

	return pandas.DataFrame(index = common_names, columns = ['gene name'], data = genes)

# a complicated function to deal with many situations when retrieving data
# some functions in PythonCyc accept lists (and return a list), but not all,
# so instead of, we traverse the input and output lists and append results to a new list
def get_data(code, string, verbose = False):
	organism = selectOrganism(code)

	if verbose:
		print('query is', string)

	if string != None:
		if isinstance(string, list) and len(string) > 1:
			info = []
			for query in string:
				data = organism.get_frame_objects(query)
				if data != None:
					info.append(data[0])
				else:
					info.append(None)
			return info

		elif isinstance(string, list) and len(string) == 1:
			data = organism.get_frame_objects(string)
			if data != None:
				return data[0][0]
			else:
				return None

		else:
			data = organism.get_frame_objects([string])
			if data != None:
				return data[0]
			else:
				return None

	else:
		return None

class metabolicNetwork:
	def FromGeneList(code, genes, fmt = 'genes'):
		df_genes = returnCommonNames(code)

		Network = ''
		#proteins = []
		# get reactions of gene:
		for gene in genes:
			prod = get_data(code, df_genes.loc[gene, 'gene name'])['product'][-1]
			try:
				prod = get_data(code, prod)['component_of'][-1] # the gene product act as complex
			except:
				prod = get_data(code, df_genes.loc[gene, 'gene name'])['product'][0]
			#proteins.append(prod)

			enzrnxs = get_data(code, prod)['catalyzes']

			rxns = []
			try:
				for enzrxn in enzrnxs:
					rxns.append(get_data(code, enzrxn)['reaction'])
				rxns

				for rxn in rxns:
					if 'gene' in fmt:
						Network += '{:s}\t{:s}\t{:s}\t{:s}\t1.0\t1.0\n'.format(
							gene, rxn[0], ','.join(get_data(code, rxn[0])['left']), ','.join(get_data(code, rxn[0])['right']))
					elif 'product' in fmt:
						Network += '{:s}\t{:s}\t{:s}\t{:s}\t1.0\t1.0\n'.format(
							prod, rxn[0], ','.join(get_data(code, rxn[0])['left']), ','.join(get_data(code, rxn[0])['right']))
					elif 'complex' in fmt:
						organism = selectOrganism(code)
						proteins, stoichiometry = organism.monomers_of_protein(prod)
						cplx = ','.join([gene for x in range(stoichiometry[0])])

						if stoichiometry[0] > 1:
							cplx = '[{:s}]'.format(cplx)

						Network += '{:s}\t{:s}\t{:s}\t{:s}\t1.0\t1.0\n'.format(
							cplx, rxn[0], ','.join(get_data(code, rxn[0])['left']), ','.join(get_data(code, rxn[0])['right']))

			except:
				continue

		infile = io.StringIO(Network.replace('|',''))
		header = ['GENE OR COMPLEX', 'REACTION', 'SUBSTRATES', 'PRODUCTS', 'FWD_RATE', 'RVS_RATE']
		return pandas.read_csv(infile, delimiter = '\t', names = header)

	def setReversibility(network, rxnLst, valLst):
		if isinstance(rxnLst, list):
			pass
		else:
			rxnLst = [rxnLst]

		if isinstance(valLst, list):
			pass
		else:
			valLst = [valLst]

		if not len(rxnLst) == len(valLst):
			raise Exception("Reactions and its rates do not have the same length")

		for reaction, rvs_rate in zip(rxnLst, valLst):
			network.loc[network['REACTION'].str.match(reaction), 'RVS_RATE'] = rvs_rate
		return network

	def setIrreversibility(network, rxnLst = [], geneLst = []):
		if isinstance(rxnLst, list):
			pass
		else:
			rxnLst = [rxnLst]

		if isinstance(geneLst, list):
			pass
		else:
			geneLst = [geneLst]

		for reaction in rxnLst:
			network.loc[network['REACTION'].str.match(reaction), 'RVS_RATE'] = 0.0

		for gene_or_cplx in geneLst:
			network.loc[network['GENE OR COMPLEX'].str.match(gene_or_cplx.replace('[', '\[').replace(']', '\]')), 'RVS_RATE'] = 0.0

		return network

	def setTransport(network, rxnLst = [], geneLst = [], fromLst = [], toLst = []):
		if isinstance(rxnLst, list):
			pass
		else:
			rxnLst = [rxnLst]

		if isinstance(geneLst, list):
			pass
		else:
			geneLst = [geneLst]

		if isinstance(fromLst, list):
			pass
		else:
			fromLst = [fromLst]

		if isinstance(toLst, list):
			pass
		else:
			toLst = [toLst]

		if len(rxnLst) > 0:
			col = 'REACTION'
			lst = rxnLst
		elif len(geneLst) > 0:
			col = 'GENE OR COMPLEX'
			lst = geneLst

		if len(lst) > 0 and len(fromLst) > 0:
			for reaction, c1 in zip(lst, fromLst):
				idx = network.loc[network[col].str.match(reaction), 'SUBSTRATES'].index
				for i in idx:
					network.loc[i, 'SUBSTRATES'] = \
						','.join([ c1 + '-' + x for x in network.loc[i, 'SUBSTRATES'].split(',') ])

		if len(lst) > 0 and len(toLst) > 0:
			for reaction, c2 in zip(lst, toLst):
				idx = network.loc[network[col].str.match(reaction), 'PRODUCTS'].index
				for i in idx:
					network.loc[i, 'PRODUCTS'] = \
						','.join([ c2 + '-' + x for x in network.loc[i, 'PRODUCTS'].split(',') ])

		return network

	def setCompartment(network, geneLst, compartmentLst):
		if isinstance(geneLst, list):
			pass
		else:
			geneLst = [geneLst]

		if isinstance(compartmentLst, list):
			pass
		else:
			compartmentLst = [compartmentLst]

		if not len(geneLst) == len(compartmentLst):
			raise Exception("Genes or complexes list and Compartments list do not have the same length")

		for gene, compartment in zip(geneLst, compartmentLst):
			network.loc[network['GENE OR COMPLEX'].str.match(gene), 'GENE OR COMPLEX'] = compartment + '-' + gene

		return network

	def expand_network(infile_path, path = 'expanded.txt'):
		if isinstance(infile_path, str):
			data = read_network(infile_path)
		elif isinstance(infile_path, pandas.DataFrame):
			data = infile_path
		else:
			raise Exception("Not yet supported type of data")

		with open(path, 'w+') as outfile:
			outfile.write('SOURCE\tTARGET\tEDGE_ATTRIBUTE\tSOURCE_NODE_ATTRIBUTE\tTARGET_NODE_ATTRIBUTE\n')

		with open(path, 'a') as outfile:
			for enzyme, reaction in zip(data.iloc[:,0], data.iloc[:,1]):
				outfile.write('{:s}\t{:s}\tNO_ARROW\tGENE_PROD\tRXN\n'.format(enzyme, reaction))

		with open(path, 'a') as outfile:
			for reaction, substrates, fwd, rvs in zip(data.iloc[:,1], data.iloc[:,2], data.iloc[:,4], data.iloc[:,5]):
				reversibility = 'NO_REVERSIBLE'
				if fwd != 0 and rvs != 0:
					reversibility = 'REVERSIBLE'
				for substrate in substrates.split(','):
					outfile.write('{:s}\t{:s}\t{:s}\tMET\tRXN\n'.format(substrate, reaction, reversibility))

		with open(path, 'a') as outfile:
			for reaction, products, fwd, rvs in zip(data.iloc[:,1], data.iloc[:,3], data.iloc[:,4], data.iloc[:,5]):
				reversibility = 'NO_REVERSIBLE'
				if fwd != 0 and rvs != 0:
					reversibility = 'REVERSIBLE'
				for product in products.split(','):
					outfile.write('{:s}\t{:s}\t{:s}\tRXN\tMET\n'.format(reaction, product, reversibility))

		return None
