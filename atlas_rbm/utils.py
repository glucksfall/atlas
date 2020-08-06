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
import subprocess
import itertools

from .construct_model_from_metabolic_network import read_network
from .export import to_kappa

def checkPathwayTools(verbose = True):
	try:
		availableOrgs = pythoncyc.all_orgids()
	except:
		availableOrgs = False

	if availableOrgs:
		if verbose:
			print('PathwayTools is running. Available PGDB are: {:s}'.format(', '.join(availableOrgs)).replace('|',''))
		return True
	else:
		if verbose:
			print('PathwayTools is not running.\n' \
				'Please, execute utils.execPathwayTools(path) or utils.execPToolsDocker(dockername).')
		return False

def execPathwayTools(path = '/opt/pathway-tools/'):
	if not checkPathwayTools(verbose = False):
		from platform import system
		if 'Windows' in system():
			cmd = '{:s}/pathway-tools -lisp -python-local-only'.format(path)
		else:
			cmd = 'nohup {:s}/pathway-tools -lisp -python-local-only &'.format(path)
		cmd = re.findall(r'(?:[^\s,"]|"+(?:=|\\.|[^"])*"+)+', cmd)
		out, err = subprocess.Popen(cmd, shell = False, stdout = subprocess.PIPE, stderr = subprocess.PIPE).communicate()
		print('PathwayTools is running in background.')
	else:
		print('Doing nothing since PathwayTools is running.')
		return None
	while not checkPathwayTools(verbose = False):
		pass
	checkPathwayTools(verbose = True)
	return None

def execPToolsDocker(dockername = 'ptools'):
	if not checkPathwayTools(verbose = False):
		cmd = 'docker run --rm -d -v /opt:/opt --network host {:s}'.format(dockername)
		cmd = re.findall(r'(?:[^\s,"]|"+(?:=|\\.|[^"])*"+)+', cmd)
		out, err = subprocess.Popen(cmd, shell = False, stdout = subprocess.PIPE, stderr = subprocess.PIPE).communicate()
		print('Docker {:s} is running (ID {:s})'.format(dockername, out.decode()[:-1]))
	else:
		print('Doing nothing since PathwayTools is running.')
		return None
	while not checkPathwayTools(verbose = False):
		pass
	checkPathwayTools(verbose = True)
	return None

def selectOrganism(code):
	if checkPathwayTools(verbose = False):
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
		common = getData(code, gene)['common_name']
		common_names.append(common)
		genes_dict[common] = gene

	return pandas.DataFrame(index = common_names, columns = ['gene name'], data = genes)

# a complicated function to deal with many situations when retrieving data
# some functions in PythonCyc accept lists (and return a list), but not all,
# so instead of, we traverse the input and output lists and append results to a new list
def getData(code, string, verbose = False):
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

def analyzeConnectivity(model, path = 'kasa'):
	import pysb
	if isinstance(model, str):
		cmd = '{:s} {:s}'.format(path, model)
	elif isinstance(model, pysb.core.Model):
		import string, random
		name = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))
		to_kappa(model, '_{:s}.kappa'.format(name))
		cmd = '{:s} _{:s}.kappa'.format(path, name)
	else:
		raise Exception('Type of model not supported yet.')

	cmd = re.findall(r'(?:[^\s,"]|"+(?:=|\\.|[^"])*"+)+', cmd)
	out, err = subprocess.Popen(cmd, shell = False, stdout = subprocess.PIPE, stderr = subprocess.PIPE).communicate()
	#print(out, err)

	output = out.split(b'------------------------------------------------------------')
	if output[1] == b'\nevery rule may be applied\n':
		print('Every rule may be applied.')
	else:
		print('There are some non applyable rules:', output[2].decode())
	if output[2] == b'\nevery agent may occur in the model\n\n' or output[3] == b'\nevery agent may occur in the model\n\n':
		print('Every monomer and complex of monomers may occur in the model.')
		try:
			os.remove('_{:s}.kappa'.format(name))
		except:
			pass
	else:
		print('There are some non creatable agents:', output[4].decode()[:-2])

	os.remove('output/contact.dot')
	os.remove('output/influence.dot')
	os.remove('output/profiling.html')
	os.rmdir('output')

	return None

def analyseConnectivity(model, path = 'kasa'):
	analyzeConnectivity(model, path)

	return None

class metabolicNetwork:
	def FromGeneList(code, genes, fmt = 'genes', precalculated = None):
		if fmt not in ['genes', 'product', 'complex']:
			raise Exception('Valid format is: \'genes\', \'product\', or \'complex\'`')

		if isinstance(genes, str):
			genes = [genes]
		elif isinstance(genes, list):
			genes = genes
		else:
			raise Exception('Not supported data type yet.')

		# remove duplicated queries
		genes = sorted(set(genes))

		if precalculated is None:
			df_genes = returnCommonNames(code)
		else:
			df_genes = precalculated

		Network = ''
		#proteins = []
		# get reactions of gene:
		for gene in genes:
			prod = getData(code, df_genes.loc[gene, 'gene name'])['product'][-1]
			try:
				prod = getData(code, prod)['component_of'][-1] # the gene product act as complex
			except:
				prod = getData(code, df_genes.loc[gene, 'gene name'])['product'][0]
			#proteins.append(prod)

			enzrnxs = getData(code, prod)['catalyzes']

			rxns = []
			for enzrxn in enzrnxs:
				rxns.append(getData(code, enzrxn)['reaction'])
			rxns

			for rxn in rxns:
				if 'gene' in fmt:
					Network += '{:s}\t{:s}\t{:s}\t{:s}\t1.0\t1.0\n'.format(
						gene, rxn[0], ','.join(getData(code, rxn[0])['left']), ','.join(getData(code, rxn[0])['right']))
				elif 'product' in fmt:
					Network += '{:s}\t{:s}\t{:s}\t{:s}\t1.0\t1.0\n'.format(
						prod, rxn[0], ','.join(getData(code, rxn[0])['left']), ','.join(getData(code, rxn[0])['right']))
				elif 'complex' in fmt:
					organism = selectOrganism(code)
					monomers, stoichiometry = organism.monomers_of_protein(prod)

					genes = []
					for monomer, coefficient in zip(monomers, stoichiometry):
						gene = getData('ECOLI', organism.genes_of_protein(monomer)[0])['common_name']
						genes.append(gene)

					cplx = []
					for gene, coefficient in zip(genes, stoichiometry):
						cplx.append([gene for x in range(coefficient)])

					cplx = ','.join([x for y in cplx for x in y])
					cplx = '[{:s}]'.format(cplx)

					Network += '{:s}\t{:s}\t{:s}\t{:s}\t1.0\t1.0\n'.format(
						cplx, rxn[0], ','.join(getData(code, rxn[0])['left']), ','.join(getData(code, rxn[0])['right']))

		infile = io.StringIO(Network.replace('|',''))
		header = ['GENE OR COMPLEX', 'REACTION', 'SUBSTRATES', 'PRODUCTS', 'FWD_RATE', 'RVS_RATE']
		return pandas.read_csv(infile, delimiter = '\t', names = header)

	def addReaction(network, gene = 'spontaneous', reaction = 'RXN-', substrates = [], products = [], fwd_rate = 1.0, rvs_rate = 1.0):
		if reaction == 'RXN-':
			import string, random
			name = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))
			reaction = reaction + name

		if isinstance(substrates, list):
			substrates = ','.join(substrates)

		if isinstance(products, list):
			products = ','.join(products)

		network = network.append({
			'GENE OR COMPLEX' : gene,
			'REACTION' : reaction,
			'SUBSTRATES' : substrates,
			'PRODUCTS' : products,
			'FWD_RATE' : fwd_rate,
			'RVS_RATE' : rvs_rate
			}, ignore_index = True)

		return network

	def removeReaction(network, index = [], genes = [], reactions = []):
		if len(index) > 0:
			network = network.drop(labels = index, axis = 0)

		if len(genes) > 0:
			index = network.loc[network['GENE OR COMPLEX'].str.match(genes)].index
			network = network.drop(labels = index, axis = 0)

		if len(reactions) > 0:
			index = network.loc[network['REACTION'].str.match(reactions)].index
			network = network.drop(labels = index, axis = 0)

		return network

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
			raise Exception('Reactions and its rates do not have the same length')

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
				# check
				if c1 not in ['CYT', 'PER', 'EX']:
					break
				else:
					idx = network.loc[network[col].str.match(reaction), 'SUBSTRATES'].index
					for i in idx:
						substrates = network.loc[i, 'SUBSTRATES'].split(',')

						# remove previous compartment
						for j, met in enumerate(substrates):
							if met.startswith('PER-') or met.startswith('EX-'):
								substrates[j] = '-'.join(met.split('-')[1:])

						if c1 != 'CYT':
							network.loc[i, 'SUBSTRATES'] = ','.join([ c1 + '-' + x for x in substrates ])
						else:
							network.loc[i, 'SUBSTRATES'] = ','.join(substrates)

		if len(lst) > 0 and len(toLst) > 0:
			for reaction, c2 in zip(lst, toLst):
				# check
				if c2 not in ['CYT', 'PER', 'EX']:
					break
				else:
					idx = network.loc[network[col].str.match(reaction), 'PRODUCTS'].index
					for i in idx:
						products = network.loc[i, 'PRODUCTS'].split(',')

						# remove previous compartment
						for j, met in enumerate(products):
							if met.startswith('PER-') or met.startswith('EX-'):
								products[j] = '-'.join(met.split('-')[1:])

						if c2 != 'CYT':
							network.loc[i, 'PRODUCTS'] = ','.join([ c2 + '-' + x for x in products ])
						else:
							network.loc[i, 'PRODUCTS'] = ','.join(products)

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
			raise Exception('Genes or complexes list and Compartments list do not have the same length')

		for gene, compartment in zip(geneLst, compartmentLst):
			if compartment not in ['CYT', 'MEM', 'PER', 'WALL', 'EX']:
				break
			else:
				if gene.startswith('MEM-') or gene.startswith('PER-') or gene.startswith('WALL-') or gene.startswith('EX-'):
					gene = '-'.join(gene.split('-')[1:])

				if compartment != 'CYT':
					network.loc[network['GENE OR COMPLEX'].str.match(gene), 'GENE OR COMPLEX'] = compartment + '-' + gene
				else:
					network.loc[network['GENE OR COMPLEX'].str.match(gene), 'GENE OR COMPLEX'] = gene

		return network

	def expand_network(infile_path, path = 'expanded.txt'):
		if isinstance(infile_path, str):
			data = read_network(infile_path)
		elif isinstance(infile_path, pandas.DataFrame):
			data = infile_path
		else:
			raise Exception('Type of data not yet supported')

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

class interactionNetwork:
	def FromGeneList(code, genes, fmt = 'genes', precalculated = None):
		if fmt not in ['genes']:
			raise Exception('Valid format is: \'genes\'')

		if isinstance(genes, str):
			genes = [genes]
		elif isinstance(genes, list):
			genes = genes
		else:
			raise Exception('Not supported data type yet.')

		# remove duplicated queries
		genes = sorted(set(genes))

		if precalculated is None:
			df_genes = returnCommonNames(code)
		else:
			df_genes = precalculated

		Network = ''
		organism = selectOrganism(code)
		for gene in genes:
			prod = organism.all_products_of_gene(precalculated.loc[gene, 'gene name'])
			products = [ x.replace('|', '') for x in prod ]

			for product in products:
				monomers, stoichiometry = organism.monomers_of_protein(product)

				if len(stoichiometry) == 1 and stoichiometry[0] > 1:
					Network += '{:s}\t{:s}\t1.0\t1.0\tCYT\n'.format(gene, gene)
					for idx in range(3, stoichiometry[0]+1):
						Network += '{:s}\t[{:s}]\t1.0\t1.0\tCYT\n'.format(
							gene, ','.join([gene for x in range(idx-1)]))

				elif len(stoichiometry) > 1:
					genes = []
					for monomer, coefficient in zip(monomers, stoichiometry):
						code = organism.genes_of_protein(monomer)
						gene = getData('ECOLI', code[0])['common_name']
						genes.append(gene)

						if coefficient > 1:
							Network += '{:s}\t{:s}\t1.0\t1.0\tCYT\n'.format(gene, gene)
							for idx in range(3, coefficient+1):
								Network += '{:s}\t[{:s}]\t1.0\t1.0\tCYT\n'.format(
									gene, ','.join([gene for x in range(idx-1)]))

					for a,b in itertools.combinations(range(len(stoichiometry)), 2):
						if stoichiometry[a] == 1 and stoichiometry[b] == 1:
							Network += '{:s}\t{:s}\t1.0\t1.0\tCYT\n'.format(
								','.join([genes[a] for x in range(stoichiometry[a])]),
								','.join([genes[b] for x in range(stoichiometry[b])]))

						elif stoichiometry[a] == 1 and stoichiometry[b] > 1:
							Network += '{:s}\t[{:s}]\t1.0\t1.0\tCYT\n'.format(
								','.join([genes[a] for x in range(stoichiometry[a])]),
								','.join([genes[b] for x in range(stoichiometry[b])]))

						elif stoichiometry[a] > 1 and stoichiometry[b] == 1:
							Network += '[{:s}]\t{:s}\t1.0\t1.0\tCYT\n'.format(
								','.join([genes[a] for x in range(stoichiometry[a])]),
								','.join([genes[b] for x in range(stoichiometry[b])]))

						elif stoichiometry[a] > 1 and stoichiometry[b] > 1:
							Network += '[{:s}]\t[{:s}]\t1.0\t1.0\tCYT\n'.format(
								','.join([genes[a] for x in range(stoichiometry[a])]),
								','.join([genes[b] for x in range(stoichiometry[b])]))

					# random mechanism of assembly
					new = [[x] * y for x,y in zip(genes, stoichiometry)]
					new = [x for y in new for x in y]

					for new2 in itertools.permutations(new):
						for idx in range(1,len(new2)-1):
							Network += '{:s}\t[{:s}]\t1.0\t1.0\tCYT\n'.format(
								new2[idx+1], ','.join([x for x in new2[0:idx+1]]))

		infile = io.StringIO(Network.replace('|',''))
		header = ['SOURCE', 'TARGET', 'FWD_RATE', 'RVS_RATE', 'LOCATION']
		return pandas.read_csv(infile, delimiter = '\t', names = header)

	def addInteraction(network, source = ['A'], target = ['B'], fwd_rate = 1.0, rvs_rate = 1.0, location = 'CYT'):
		if isinstance(source, list):
			source = '[' + ','.join(source) + ']'

		if isinstance(target, list):
			target = '[' + ','.join(target) + ']'

		network = network.append({
			'SOURCE' : source,
			'TARGET' : target,
			'FWD_RATE' : fwd_rate,
			'RVS_RATE' : rvs_rate,
			'LOCATION' : location
			}, ignore_index = True)

		return network

	def removeInteraction(network, index = []):
		return network.drop(labels = index, axis = 0)
