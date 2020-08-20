# -*- coding: utf-8 -*-

'''
Project "Reconstruction of RBM from biological networks", Rodrigo Santibáñez, 2019-2020 @ NBL, UMayor
Citation:
DOI:
'''

__author__  = 'Rodrigo Santibáñez'
__license__ = 'gpl-3.0'

from pysb import *
from pysb.util import *
from pysb.core import *

import re
import numpy
import pandas

from .utils import location_keys, location_values

def read_network(infile_path):
	with open(infile_path, 'r') as infile:
		data = pandas.read_csv(infile, delimiter = '\t', header = 0, comment = '#')

	return data

def check_network(data):
	# find duplicated reactions (reactions must has a unique name)
	duplicated = len(data[data.duplicated(['REACTION'])].index)

	if duplicated > 0:
		data[data.duplicated(['REACTION'])].to_csv('./conflicting_reactions.txt', sep = '\t', index = False)
		data = data[~data.duplicated(['REACTION'], keep = 'first')]
		print('It was found duplicated reaction names in the network.\n' \
			'Please check the conflicting_reactions.txt and correct them if necessary.')

	return data

def monomers_from_metabolic_network(model, data, verbose = False):
	# find unique metabolites and correct names
	tmp = list(data['SUBSTRATES'].values) + list(data['PRODUCTS'].values)
	tmp = ','.join(tmp)
	for key in location_keys().keys():
		tmp = tmp.replace(key + '-', '')

	metabolites = list(set(tmp.split(',')))
	for index, met in enumerate(metabolites):
		if met[0].isdigit():
			metabolites[index] = '_' + met

	code = "Monomer('met',\n" \
		"	['name', 'loc', 'prot'],\n" \
		"	{{ 'name' : [ {:s} ],\n" \
		"	'loc' : [{:s}]}})"

	all_mets = [ '\'' + x.replace('-', '_') + '\'' for x in sorted(metabolites) ]
	all_locs = [ '\'' + x.lower() + '\'' for x in sorted(location_keys().keys()) ]
	code = code.format(', '.join(all_mets), ', '.join(all_locs))

	if verbose:
		print(code)
	exec(code.replace('\t', ' ').replace('\n', ' '))

	# find unique proteins, protein complexes, and correct names
	tmp = list(data['GENE OR COMPLEX'].values)
	tmp = [ x.replace('[', '').replace(']', '').split(',') if x.startswith('[') else [x] for x in tmp ]
	tmp = [ i for j in tmp for i in j ]
	#tmp = [ ' '.join(x.replace('EX-', '').replace('WALL-', '').replace('PER-', '').replace('MEM-', '').split(', ')) for x in tmp]
	tmp = [ ' '.join(x.split(',')) for x in tmp] # location no longer coded in the name

	complexes = []
	p_monomers = []
	proteins = list(set(' '.join(tmp).split(' ')))
	for index, protein in enumerate(proteins):
		if protein[0].isdigit():
			protein[index] = '_' + protein
		if 'CPLX' in protein:
			complexes.append(protein)
		else:
			if 'spontaneous' != protein:
				p_monomers.append(protein)

	code = "Monomer('prot',\n" \
		"	['name', 'loc', 'dna', 'met', 'prot', 'rna', 'up', 'dw'],\n" \
		"	{{ 'name' : [ {:s} ],\n" \
		"	'loc' : [{:s}]}})"

	all_proteins = [ '\'' + x.replace('-', '_') + '\'' for x in sorted(p_monomers)]
	code = code.format(', '.join(all_proteins), ', '.join(all_locs))

	if verbose:
		print(code)
	exec(code.replace('\t', ' ').replace('\n', ' '))

	if len(complexes) > 0:
		code = "Monomer('cplx',\n" \
			"	['name', 'loc', 'dna', 'met', 'prot', 'rna', 'up', 'dw'],\n" \
			"	{{ 'name' : [ {:s} ],\n" \
			"	'loc' : [{:s}]}})"

		all_cplx = [ '\'' + x.replace('-', '_') + '\'' for x in sorted(complexes)]
		code = code.format(', '.join(all_cplx), ', '.join(all_locs))

		if verbose:
			print(code)
		exec(code.replace('\t', ' ').replace('\n', ' '))

	return metabolites, p_monomers, complexes, list(data['GENE OR COMPLEX'].values)

def rules_from_metabolic_network(model, data, verbose = False):
	for idx in data.index:
		rxn = data.loc[idx]
		if isinstance(rxn['ENZYME LOCATION'], str):
			rxn['ENZYME LOCATION'] = rxn['ENZYME LOCATION'].replace('[', '').replace(']', '').split(',')

		# first: determine enzyme composition
		if 'CPLX' in rxn['GENE OR COMPLEX']: # the enzyme is an alias of a protein complex
			for location in rxn['ENZYME LOCATION']:
				location = location_values()[location].lower()
				enzyme = 'cplx(name = \'{:s}\', loc = \'{:s}\')'.format(rxn['GENE OR COMPLEX'].replace('-', '_'), location)

		elif rxn['GENE OR COMPLEX'].startswith('['): # an enzymatic complex described by its monomers
			monomers = rxn['GENE OR COMPLEX'][1:-1].split(',')
			enzyme = []

			## create link indexes
			dw = [None] * len(monomers)
			start_link = 1
			for index in range(len(monomers)-1):
				dw[index] = start_link
				start_link += 1
			up = dw[-1:] + dw[:-1]

			for index, monomer in enumerate(monomers):
				for location in rxn['ENZYME LOCATION']:
					location = location_values()[location].lower()
					enzyme.append('prot(name = \'{:s}\', loc = \'{:s}\', up = {:s}, dw = {:s})'.format(monomer, location, str(up[index]), str(dw[index])))

			enzyme = ' %\n	'.join(enzyme)

		else: # the enzyme is a monomer
			for location in rxn['ENZYME LOCATION']:
				location = location_values()[location].lower()
				enzyme = 'prot(name = \'{:s}\', loc = \'{:s}\')'.format(rxn['GENE OR COMPLEX'].replace('-', '_'), location)

		# second: correct reaction names starting with a digit
		name = rxn['REACTION'].replace('-', '_')
		if name[0].isdigit():
			name = '_' + name

		# third: correct metabolite names with dashes, prefix underscore for metabolite names starting by a digit, and create a list
		substrates = rxn['SUBSTRATES'].replace('-', '_').split(',')
		substrates = [ '_' + subs if subs[0].isdigit() else subs for subs in substrates ]
		products = rxn['PRODUCTS'].replace('-', '_').split(',')
		products = [ '_' + prod if prod[0].isdigit() else prod for prod in products ]

		# fourth: write LHS and RHS
		LHS = []
		RHS = []

		if rxn['GENE OR COMPLEX'] == 'spontaneous':
			locations = rxn['ENZYME LOCATION']
		else:
			locations = location_values().keys()

		for subs in substrates:
			islocated = False
			for loc in locations:
				loc = location_values()[loc]
				if loc in subs:
					LHS.append('met(name = \'{:s}\', loc = \'{:s}\', prot = None)'.format(subs.replace(loc + '_', ''), loc.lower()))
					islocated = True
			if not islocated:
				LHS.append('met(name = \'{:s}\', loc = \'{:s}\', prot = None)'.format(subs, 'cyt'))

		for prod in products:
			islocated = False
			for loc in locations:
				loc = location_values()[loc]
				if loc in prod:
					RHS.append('met(name = \'{:s}\', loc = \'{:s}\', prot = None)'.format(prod.replace(loc + '_', ''), loc.lower()))
					islocated = True
			if not islocated:
				RHS.append('met(name = \'{:s}\', loc = \'{:s}\', prot = None)'.format(prod, 'cyt'))

		# fifth: match the number of agents at both sides of the Rule (pySB checks and kappa v4 requires the matching)
		if len(substrates) < len(products):
			for index in range(len(substrates), len(products)):
				LHS.append('None')
		elif len(products) < len(substrates):
			for index in range(len(products), len(substrates)):
				RHS.append('None')

		# pretty print the Rule
		LHS = ' +\n	'.join(LHS)
		RHS = ' +\n	'.join(RHS)

		if rxn['GENE OR COMPLEX'] == 'spontaneous':
			for location in rxn['ENZYME LOCATION']:
				loc = location_values()[location]
				code = 'Rule(\'{:s}\',\n' \
					'	{:s} |\n'\
					'	{:s},\n' \
					'	Parameter(\'fwd_{:s}\', {:f}), \n' \
					'	Parameter(\'rvs_{:s}\', {:f}))'
				code = code.format(name + '_' + loc, LHS, RHS, name + '_' + loc, float(rxn['FWD_RATE']), name + '_' + loc, float(rxn['RVS_RATE']))
				code = code.replace('loc = \'cyt\'', 'loc = \'{:s}\''.format(loc.lower()))

				if verbose:
					print(code)
				exec(code.replace('\t', ' ').replace('\n', ' '))

		else: # reaction needs an enzyme
			code = 'Rule(\'{:s}\',\n' \
				'	{:s} +\n	{:s} | \n' \
				'	{:s} +\n	{:s}, \n' \
				'	Parameter(\'fwd_{:s}\', {:f}), \n' \
				'	Parameter(\'rvs_{:s}\', {:f}))'
			code = code.format(name, enzyme, LHS, enzyme, RHS, name, float(rxn['FWD_RATE']), name, float(rxn['RVS_RATE']))
			code = code.replace('-', '_')

			if verbose:
				print(code)
			exec(code.replace('\t', ' ').replace('\n', ' '))

def observables_from_metabolic_network(model, data, monomers, verbose = False):
	for name in sorted(monomers[0]):
		name = name.replace('-','_')
		for loc in location_keys().keys():
			code = 'Observable(\'obs_met_{:s}_{:s}\', met(name = \'{:s}\', loc = \'{:s}\', prot = None))'
			code = code.format(name, loc.lower(), name, loc.lower())
			if verbose:
				print(code)
			exec(code.replace('\t', ' ').replace('\n', ' '))

	for name in sorted(monomers[0]):
		name = name.replace('-','_')
		for loc in location_keys().keys():
			code = 'Initial(met(name = \'{:s}\', loc = \'{:s}\', prot = None), Parameter(\'t0_met_{:s}_{:s}\', 0))'
			code = code.format(name, loc.lower(), name, loc.lower())
			if verbose:
				print(code)
			exec(code.replace('\t', ' ').replace('\n', ' '))

	for name in sorted(monomers[1]):
		name = name.replace('-','_')
		for loc in location_keys().keys():
			code = 'Initial(prot(name = \'{:s}\', loc = \'{:s}\', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter(\'t0_prot_{:s}_{:s}\', 0))'
			code = code.format(name, loc.lower(), name, loc.lower())
			if verbose:
				print(code)
			exec(code.replace('\t', ' ').replace('\n', ' '))

	for name in sorted(monomers[2]):
		name = name.replace('-','_')
		for loc in location_keys().keys():
			code = 'Initial(cplx(name = \'{:s}\', loc = \'{:s}\', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter(\'t0_cplx_{:s}_{:s}\', 0))'
			code = code.format(name, loc.lower(), name, loc.lower())
			if verbose:
				print(code)
			exec(code.replace('\t', ' ').replace('\n', ' '))

	names = monomers[3]
	for name in sorted(set(names)):
		verbose = True
		if name.startswith('['):
			monomers = name[1:-1].split(',')
			complex_pysb = []

			from collections import Counter
			stoichiometry = Counter(monomers)
			cplx_composition = ''
			for key, value in stoichiometry.items():
				cplx_composition += '_{:s}x{:d}'.format(key, value)

			## create link indexes
			dw = [None] * len(monomers)
			start_link = 1
			for index in range(len(monomers)-1):
				dw[index] = start_link
				start_link += 1
			up = dw[-1:] + dw[:-1]

			for location in utils.location_keys().keys():
				complex_pysb = []
				for index, monomer in enumerate(monomers):
					complex_pysb.append('prot(name = \'{:s}\', loc = \'{:s}\', dna = None, met = None, prot = None, rna = None, up = {:s}, dw = {:s})'.format(
						monomer, location.lower(), str(up[index]), str(dw[index])))

				complex_pysb = ' %\n	'.join(complex_pysb)

				code = 'Initial({:s},\n\tParameter(\'t0_cplx{:s}_{:s}\', 0))'
				code = code.format(complex_pysb, cplx_composition, location.lower())

				if verbose:
					print(code)
				exec(code.replace('\t', ' ').replace('\n', ' '))

				code = 'Observable(\'obs_cplx{:s}_{:s}\',\n\t{:s})'
				code = code.format(cplx_composition, location.lower(), complex_pysb)

				if verbose:
					print(code)
				exec(code.replace('\t', ' ').replace('\n', ' '))
				print()

	return None

def construct_model_from_metabolic_network(network, verbose = False):
	if isinstance(network, str):
		data = read_network(network)
	elif isinstance(network, pandas.DataFrame):
		data = network
	elif isinstance(network, numpy.array):
		data = pandas.DataFrame(data = network)
	else:
		raise Exception("The network data type is not yet supported.")
	data = check_network(data)

	model = Model()
	[metabolites, p_monomers, complexes, hypernodes] = \
		monomers_from_metabolic_network(model, data, verbose)
	observables_from_metabolic_network(model, data, [metabolites, p_monomers, complexes, hypernodes], verbose)
	rules_from_metabolic_network(model, data, verbose = verbose)

	return model
