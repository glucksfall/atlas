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

import re
import pandas

def read_network(file):
	with open(file, 'r') as infile:
		data = pandas.read_csv(infile, delimiter = '\t', header = 0, comment = '#')

	return data

def monomers_from_interaction_network(model, data, verbose = False):
	# find unique metabolites and correct names
	tmp = list(data.iloc[:, 0].values) + list(data.iloc[:, 1].values)
	tmp = [ ' '.join(x.replace('SMALL-', '').replace('PER-', '').replace('EX-', '').split(',')) for x in tmp if x.startswith('SMALL-')]

	metabolites = list(set(' '.join(tmp).split(' ')))
	if len(tmp) > 0:
		for index, met in enumerate(metabolites):
			if met[0].isdigit():
				metabolites[index] = '_' + met

		code = "Monomer('met',\n		['name', 'loc', 'prot'],\n" \
			"		{ 'name' :\n			[ " + \
			', '.join([ '\'' + x.replace('-', '_') + '\'' for x in sorted(metabolites)]) + " ], \n" \
			"		  'loc' : ['cyt', 'per', 'ex']})"

		if verbose:
			print(code)
		exec(code.replace('\n', ''))
	else:
		metabolites = []

	# find unique proteins, protein complexes and correct names
	tmp = list(data.iloc[:, 0].values) + list(data.iloc[:, 1].values)
	tmp = [ x for x in tmp if not x.startswith('SMALL-')]
	tmp = [ x.replace('[', '').replace(']', '').split(',') if x.startswith('[') else [x] for x in tmp ]
	tmp = [ i for j in tmp for i in j ]
	tmp = [ ' '.join(x.replace('PER-', '').replace('MEM-', '').split(', ')) for x in tmp if not x.startswith('SMALL-')]

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

	code = "Monomer('prot',\n		['name', 'loc', 'met', 'prot', 'up', 'dw'],\n" \
		  "		{ 'name' :\n			[ " + \
		  ', '.join([ '\'' + x.replace('-', '_') + '\'' for x in sorted(p_monomers)]) + " ], \n" \
		  "		  'loc' : ['cyt', 'mem', 'per', 'ex']})"

	if verbose:
		print(code)
	exec(code.replace('\n', ''))

	if len(complexes) > 0:
		code = "Monomer('cplx',\n		['name', 'loc', 'met', 'prot', 'up', 'dw'],\n" \
			"		{ 'name' :\n			[ " + \
			', '.join([ '\'' + x.replace('-', '_') + '\'' for x in sorted(complexes)]) + " ], \n" \
			"		  'loc' : ['cyt', 'mem', 'per', 'ex']})"

		if verbose:
			print(code)
		exec(code.replace('\n', ''))

	return metabolites, p_monomers, complexes

def from_ProtProt_network(data, i):
	## write LHS (problematic because we need to find complexes in the LHS)
	agents = (data.iloc[i, 0] + ',' + data.iloc[i, 1])
	names = agents.split(',')

	LHS = []
	next_in_complex = False
	for molecule in names:
		if molecule[0] == '[': # we are dealing with the first monomer of a complex
			next_in_complex = True
			LHS.append('prot(name = \'{:s}\', up = {{:s}}, dw = {{:s}})'.format(molecule[1:]))
		elif molecule[-1] == ']': # we are dealing with the last monomer of a complex
			next_in_complex = False
			LHS.append('prot(name = \'{:s}\', up = {{:s}}, dw = {{:s}})'.format(molecule[:-1]))
		elif next_in_complex:
			LHS.append('prot(name = \'{:s}\', up = {{:s}}, dw = {{:s}})'.format(molecule))
		else: # we have a monomer
			LHS.append('prot(name = \'{:s}\', up = None, dw = None)'.format(molecule))

	## look for where starts and ends a complex in the LHS
	monomers = [(m.start(), m.end()) for m in re.finditer(r'[A-Za-z-_]+', agents)]
	complexes = [(m.start()+1, m.end()-1) for m in re.finditer(r'\[[A-Za-z-_,]+\]', agents)]

	positions = []
	for cplx_pos in reversed(complexes):
		pos_i = None
		pos_f = None
		for index, kmer_pos in enumerate(monomers):
			if cplx_pos[0] == kmer_pos[0]:
				pos_i = index
			if cplx_pos[1] == kmer_pos[1]:
				pos_f = index
				positions.append((pos_i, pos_f))
				break

	## join complexes following start and end positions
	start_link = 1
	for position in positions:
		count_monomers = len(LHS[position[0]:position[1]+1])
		dw = list(range(start_link, start_link + count_monomers))
		up = [dw[-1]] + dw[:-1]
		up[0] = 'None'
		dw[-1] = 'None'

		for index, sub_position in enumerate(range(position[0], position[1]+1)):
			LHS[sub_position] = LHS[sub_position].format(str(up[index]), str(dw[index]))

		## join agents and remove from LHS list because they were joined into one
		LHS[position[0]] = ' %\n	'.join(LHS[position[0]:position[1]+1])
		for index in reversed(range(position[0]+1, position[1]+1)):
			LHS.pop(index)

		start_link += count_monomers -1

	## final join
	LHS = ' +\n	'.join(LHS)

	## write RHS (no problem, always bind molecules in a chain)
	agents = (data.iloc[i, 0] + ',' + data.iloc[i, 1])
	agents = agents.replace('[', '').replace(']', '')
	agents = agents.split(',')

	RHS = []
	# numbering links
	dw = list(range(1, len(agents)+1))
	up = [dw[-1]] + dw[:-1]
	up[0] = 'None'
	dw[-1] = 'None'

	for index, molecule in enumerate(agents):
		RHS.append('prot(name = \'{:s}\', up = {:s}, dw = {:s})' \
				.format(molecule, str(up[index]), str(dw[index])))
	RHS = ' %\n	'.join(RHS)

	return LHS, RHS

def from_ProtMet_network(data, i):
	agents = (data.iloc[i, 0] + ',' + data.iloc[i, 1])
	names = agents.split(',')

	## form the LHS
	LHS = []
	next_in_complex = False
	for molecule in names:
		## defaults
		type = 'prot'
		link = 'met'
		loc = 'cyt'

		if 'SMALL' in molecule:
			type = 'met'
			link = 'prot'
		if 'PER' in molecule:
			loc = 'per'

		molecule = molecule.replace('PER-', '').replace('SMALL-', '')

		if molecule[0] == '[': # we are dealing with the first monomer of a complex
			molecule = molecule[1:]
			next_in_complex = True
			linked = '{:s}'
		elif molecule[-1] == ']': # we are dealing with the last monomer of a complex
			molecule = molecule[:-1]
			next_in_complex = False
			linked = '{:s}'
		elif next_in_complex: # we are dealing with a monomer part of a complex
			molecule = molecule
			linked = '{:s}'
		else:
			molecule = molecule
			linked = 'None'

		if type == 'prot':
			LHS.append('{:s}(name = \'{:s}\', loc = \'{:s}\', {:s} = {:s}, up = {{:s}}, dw = {{:s}})' \
					.format(type, molecule, loc, link, linked))
		else:
			LHS.append('{:s}(name = \'{:s}\', loc = \'{:s}\', {:s} = {:s})' \
					.format(type, molecule, loc, link, linked))

	## look for where a complex starts and ends in the LHS
	complexes = [(m.start()+1, m.end()-1) for m in re.finditer(r'\[[A-Za-z-_,]+\]', agents)]
	monomers = [(m.start(), m.end()) for m in re.finditer(r'[A-Za-z-_]+', agents)]

	positions = []
	for cplx_pos in reversed(complexes):
		pos_i = None
		pos_f = None
		for index, kmer_pos in enumerate(monomers):
			if cplx_pos[0] == kmer_pos[0]:
				pos_i = index
			if cplx_pos[1] == kmer_pos[1]:
				pos_f = index
				positions.append((pos_i, pos_f))
				break

	## join complexes following start and end positions
	for position in positions:
		## create numbered links
		count_monomers = len(LHS[position[0]:position[1]+1])
		count_small = ' '.join(LHS[position[0]:position[1]+1]).count('met(')
		count_prots = ' '.join(LHS[position[0]:position[1]+1]).count('prot(')

		up = ['None'] * count_monomers
		dw = ['None'] * count_monomers
		prot_met = ['None'] * count_monomers

		starter_link = 1
		if count_prots >= 1:
			## index prot-prot links
			for index in range(position[0], position[1]+1):
				if index == 0 and LHS[index].startswith('prot('):
					dw[index] = starter_link
				elif index == count_monomers-1 and LHS[index].startswith('prot('):
					up[index] = starter_link
					starter_link += 1
				else:
					if LHS[index].startswith('prot('):
						dw[index] = starter_link + 1
						up[index] = starter_link
						starter_link += 1

		if count_small >= 1:
			## index prot-met links
			for index in range(position[0], position[1]+1):
				if LHS[index].startswith('met('):
					prot_met[index] = starter_link
					prot_met[index-1] = starter_link
					starter_link += 1

		## replace {:s} with calculated links
		for index, sub_position in enumerate(range(position[0], position[1]+1)):
			if LHS[sub_position].startswith('prot'):
				LHS[sub_position] = \
					LHS[sub_position].format(str(prot_met[index]), str(up[index]), str(dw[index]))
			else:
				LHS[sub_position] = LHS[sub_position].format(str(prot_met[index]))

		## join agents and remove from LHS list because they were joined into one position
		LHS[position[0]] = ' %\n	'.join(LHS[position[0]:position[1]+1])
		for index in reversed(range(position[0]+1, position[1]+1)):
			LHS.pop(index)

	## LHS final join
	LHS = ' +\n	'.join(LHS)

	## write the RHS
	agents = (data.iloc[i, 0] + ',' + data.iloc[i, 1]).replace('[', '').replace(']', '')
	names = agents.split(',')

	RHS = []
	for index, name in enumerate(names):
		## defaults
		type = 'prot'
		link = 'met'
		loc = 'cyt'

		if 'SMALL' in name:
			type = 'met'
			link = 'prot'
		if 'PER' in name:
			loc = 'per'

		name = name.replace('PER-', '').replace('SMALL-', '')

		if type == 'prot':
			RHS.append(
				'{:s}(name = \'{:s}\', loc = \'{:s}\', {:s} = {{:s}}, up = {{:s}}, dw = {{:s}})' \
				.format(type, name, loc, link))
		else:
			RHS.append(
				'{:s}(name = \'{:s}\', loc = \'{:s}\', {:s} = {{:s}})' \
				.format(type, name, loc, link))

	## create numbered links
	count_monomers = len(RHS)
	count_small = ' '.join(RHS).count('met(')
	count_prots = ' '.join(RHS).count('prot(')

	up = ['None'] * count_monomers
	dw = ['None'] * count_monomers
	prot_met = ['None'] * count_monomers

	starter_link = 1
	if count_prots > 1:
		## index prot-prot links
		for index in range(count_monomers):
			if index == 0 and RHS[index].startswith('prot('):
				dw[index] = starter_link
			elif index == (count_monomers-count_prots) and RHS[index].startswith('prot('):
				up[index] = starter_link
				starter_link += 1
			else:
				if RHS[index].startswith('prot('):
					dw[index] = starter_link + 1
					up[index] = starter_link
					starter_link += 1

	## index prot-met links
	for index, agent in enumerate(RHS):
		if agent.startswith('met('):
			prot_met[index] = starter_link
			prot_met[index-1] = starter_link
			starter_link += 1

	for index in range(len(RHS)):
		if RHS[index].startswith('prot('):
			RHS[index] = RHS[index].format(str(prot_met[index]), str(up[index]), str(dw[index]))
		else:
			RHS[index] = RHS[index].format(str(prot_met[index]))

	RHS = ' %\n	'.join(RHS) # all agents are linked together

	return LHS, RHS

def observables_from_interaction_network(model, data, monomers, verbose = False):
	for name in sorted(monomers[1]):
		name = name.replace('-','_')
		for loc in ['cyt', 'per', 'ex']:
			code = 'Observable(\'obs_prot_{:s}_{:s}\', prot(name = \'{:s}\', loc = \'{:s}\', met = None, prot = None, up = None, dw = None))'
			code = code.format(name, loc, name, loc)
			if verbose:
				print(code)
			exec(code.replace('\t', ''))

	for name in sorted(monomers[0]):
		name = name.replace('-','_')
		for loc in ['cyt', 'per', 'ex']:
			code = 'Initial(met(name = \'{:s}\', loc = \'{:s}\', prot = None), Parameter(\'t0_{:s}_{:s}\', 0))'
			code = code.format(name, loc, name, loc)
			if verbose:
				print(code)
			exec(code.replace('\t', ''))

	for name in sorted(monomers[1]):
		name = name.replace('-','_')
		for loc in ['cyt', 'mem', 'per', 'ex']:
			code = 'Initial(prot(name = \'{:s}\', loc = \'{:s}\', met = None, prot = None, up = None, dw = None), Parameter(\'t0_{:s}_{:s}\', 0))'
			code = code.format(name, loc, name, loc)
			if verbose:
				print(code)
			exec(code.replace('\t', ''))

	for name in sorted(monomers[2]):
		name = name.replace('-','_')
		for loc in ['cyt', 'mem', 'per', 'ex']:
			code = 'Initial(cplx(name = \'{:s}\', loc = \'{:s}\', met = None, prot = None, up = None, dw = None), Parameter(\'t0_{:s}_{:s}\', 0))'
			code = code.format(name, loc, name, loc)
			if verbose:
				print(code)
			exec(code.replace('\t', ''))

	return model

def construct_model_from_interaction_network(network, verbose = False):
	data = read_network(network)

	model = Model()
	[metabolites, p_monomers, complexes] = \
		monomers_from_interaction_network(model, data, verbose)
	observables_from_interaction_network(model, data, [metabolites, p_monomers, complexes], verbose)

	RULE_LHS = []
	RULE_RHS = []
	for idx in data.index:
		if 'SMALL-' in data.iloc[idx, 0] or 'SMALL-' in data.iloc[idx, 1]:
			LHS, RHS = from_ProtMet_network(data, idx)
		else:
			LHS, RHS = from_ProtProt_network(data, idx)
		RULE_LHS.append(LHS)
		RULE_RHS.append(RHS)

	for index, _ in enumerate(data.index):
		## complete rule
		name = 'PhysicalInteractionRule_{{:0{:d}d}}'.format(len(str(len(data.index))))
		name = name.format(index+1)
		code = 'Rule(\'{:s}\',\n' \
			'	{:s} | \n	{:s},\n' \
			'	Parameter(\'fwd_{:s}\', {:f}),\n' \
			'	Parameter(\'rvs_{:s}\', {:f}))'
		code = code.format(name, RULE_LHS[index], RULE_RHS[index], name, data.iloc[index, 2], name, data.iloc[index, 3])
		code = code.replace('-', '_').replace('{:s}', 'None')

		if verbose:
			print(code)
		exec(code.replace('\t', ''))

	return model
