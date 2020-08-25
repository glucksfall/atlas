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

from .utils import read_network, check_interaction_network, location_keys, location_values

def monomers_from_interaction_network(model, data, verbose = False, toFile = False):
	# find unique metabolites and correct names
	tmp = list(data['SOURCE'].values) + list(data['TARGET'].values)
	tmp = [ x.replace('[', '').replace(']', '').split(',') if x.startswith('[') else [x] for x in tmp ]
	tmp = [ i for j in tmp for i in j ]
	tmp = [ x for x in tmp if x.startswith('SMALL-') ]
	tmp = ','.join(tmp)
	for key in location_keys().keys():
		tmp = tmp.replace(key + '-', '')

	metabolites = sorted(set(tmp.split(',')))
	if len(tmp) > 0:
		for index, met in enumerate(metabolites):
			if met[0].isdigit():
				metabolites[index] = '_' + met

		code = "Monomer('met',\n" \
			"	['name', 'loc', 'prot'],\n" \
			"	{{ 'name' : [ {:s} ], \n" \
			"	'loc' : [{:s}]}})\n"

		all_mets = [ '\'' + x.replace('-', '_') + '\'' for x in sorted(metabolites) ]
		all_locs = [ '\'' + x.lower() + '\'' for x in sorted(location_keys().keys()) ]
		code = code.format(', '.join(all_mets), ', '.join(all_locs))

		if verbose:
			print(code)
		if toFile:
			with open(toFile, 'a+') as outfile:
				outfile.write(code)
		else:
			exec(code.replace('\n', ''))
	else:
		metabolites = []

	# find unique proteins and protein complexes, and correct names
	tmp = list(data['SOURCE'].values) + list(data['TARGET'].values)
	tmp = [ x for x in tmp if not (x.startswith('SMALL-') or x.startswith('BS-') or x.startswith('RNA-'))]
	tmp = [ x.replace('[', '').replace(']', '').split(',') if x.startswith('[') else [x] for x in tmp ]
	tmp = [ i for j in tmp for i in j ]
	tmp = [ x for x in tmp if not (x.startswith('SMALL-') or x.startswith('BS-') or x.startswith('RNA-'))]
	#tmp = [ ' '.join(x.replace('MEM-', '').replace('PER-', '').replace('WALL-', '').replace('EX-', '').split(',')) for x in tmp]
	tmp = [ ' '.join(x.split(',')) for x in tmp] # location no longer coded in the name

	complexes = []
	p_monomers = []
	proteins = sorted(set(' '.join(tmp).split(' ')))
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
		"	{{ 'name' : [ {:s} ], \n" \
		"	'loc' : [{:s}]}})\n"

	all_proteins = [ '\'' + x.replace('-', '_') + '\'' for x in sorted(p_monomers)]
	all_locs = [ '\'' + x.lower() + '\'' for x in sorted(location_keys().keys()) ]
	code = code.format(', '.join(all_proteins), ', '.join(all_locs))

	if verbose:
		print(code)
	if toFile:
		with open(toFile, 'a+') as outfile:
			outfile.write(code)
	else:
		exec(code.replace('\n', ''))

	if len(complexes) > 0:
		code = "Monomer('cplx',\n" \
			"	['name', 'loc', 'met', 'prot', 'up', 'dw'],\n" \
			"	{{ 'name' : [ {:s} ],\n" \
			"	'loc' : ['cyt', 'mem', 'per', 'wall', 'ex']}})\n"

		all_cplx = [ '\'' + x.replace('-', '_') + '\'' for x in sorted(complexes)]
		code = code.format(', '.join(all_cplx), ', '.join(all_locs))

		if verbose:
			print(code)
		if toFile:
			with open(toFile, 'a+') as outfile:
				outfile.write(code)
		else:
			exec(code.replace('\n', ''))

	# find DNA binding sites and types
	tmp = list(data['SOURCE'].values) + list(data['TARGET'].values)
	tmp = [ x.replace('[', '').replace(']', '').split(',') if x.startswith('[') else [x] for x in tmp ]
	tmp = [ i for j in tmp for i in j ]
	tmp = [ ' '.join(x.split(', ')) for x in tmp if (x.startswith('BS-') and x[3].isdigit()) ]
	dnas = sorted(set(' '.join(tmp).split(' ')))

	tmp = list(data['SOURCE'].values) + list(data['TARGET'].values)
	tmp = [ x.replace('[', '').replace(']', '').split(',') if x.startswith('[') else [x] for x in tmp ]
	tmp = [ i for j in tmp for i in j ]
	tmp = [ ' '.join(x.split(',')) for x in tmp if (x.startswith('BS-') and not x[3].isdigit()) ]

	dnas = dnas + [ x.split('-')[-2] for x in tmp ] # add other DNA names
	dnas = sorted(set(' '.join(dnas).split(' ')))
	tmp = [ x.split('-')[-1] for x in tmp ]
	types = sorted(set(' '.join(tmp).split(' ')))

	if len(dnas[0]) > 0:
		code = "Monomer('dna',\n" \
			"	['name', 'type', 'prot', 'rna', 'up', 'dw'],\n" \
			"	{{ 'name' : [ {:s} ],\n" \
			"	'type' : [{:s}]}})\n"

		code = code.format(
			', '.join([ '\'' + x.replace('-', '_') + '\'' for x in sorted(dnas) ]),
			', '.join([ '\'' + x.replace('-', '_') + '\'' for x in sorted(types) ]))

		if verbose:
			print(code)
		if toFile:
			with open(toFile, 'a+') as outfile:
				outfile.write(code)
		else:
			exec(code.replace('\n', ''))

	return metabolites, p_monomers, complexes, zip(list(data['SOURCE']), list(data['TARGET']))

def from_ProtProt_network(data, i): # a network of only proteins interactions
	## write LHS
	agents = data['SOURCE'].iloc[i] + ',' + data['TARGET'].iloc[i]
	names = agents.split(',')
	location = data['LOCATION'].iloc[i].replace('[', '').replace(']', '').split(',') # just in case the user wrote "[location]"

	# set locations for all agents
	if len(location) == 1: # all agents are located in the same compartment
		location = [ location_values()[location[0]] ] * len(names)
	elif len(location) == len(names): # agents are located in different compartments (e.g. araFGH)
		location = [ location_values()[x] for x in location ]
	else:
		location = [ location_values()[location[0]] ] * len(names) # fallback to warning
		print('WARNING: the location list has an incorrect length to determine location for all agents. Location for all agents will be {:s}'.format(location[0]))

	LHS = []
	next_in_complex = False
	for molecule, loc in zip(names, location):
		if molecule[0] == '[': # we are dealing with the first monomer of a complex
			next_in_complex = True
			LHS.append('prot(name = \'{:s}\', loc = \'{:s}\', dna = None, met = None, prot = None, rna = None, up = {{:s}}, dw = {{:s}})'.format(molecule[1:], loc.lower()))
		elif molecule[-1] == ']': # we are dealing with the last monomer of a complex
			next_in_complex = False
			LHS.append('prot(name = \'{:s}\', loc = \'{:s}\', dna = None, met = None, prot = None, rna = None, up = {{:s}}, dw = {{:s}})'.format(molecule[:-1], loc.lower()))
		elif next_in_complex:
			LHS.append('prot(name = \'{:s}\', loc = \'{:s}\', dna = None, met = None, prot = None, rna = None, up = {{:s}}, dw = {{:s}})'.format(molecule, loc.lower()))
		else: # we have a monomer
			LHS.append('prot(name = \'{:s}\', loc = \'{:s}\', dna = None, met = None, prot = None, rna = None, up = None, dw = None)'.format(molecule, loc.lower()))

	## look for where a complex starts and ends in the LHS
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

	## write RHS
	agents = data['SOURCE'].iloc[i] + ',' + data['TARGET'].iloc[i]
	agents = agents.replace('[', '').replace(']', '')
	agents = agents.split(',')

	RHS = []
	# numbering links
	dw = list(range(1, len(agents)+1))
	up = [dw[-1]] + dw[:-1]
	up[0] = 'None'
	dw[-1] = 'None'

	for index, (molecule, loc) in enumerate(zip(agents, location)):
		RHS.append('prot(name = \'{:s}\', loc = \'{:s}\', dna = None, met = None, prot = None, rna = None, up = {:s}, dw = {:s})' \
				.format(molecule, loc.lower(), str(up[index]), str(dw[index])))

	## final join
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

def from_ProtDNA_network(data, i):
	description = []
	#RULE_LHS = []
	#for i in data.index:
	# data
	agents = (data.iloc[i, 0] + ',' + data.iloc[i, 1])
	names = agents.split(',')

	#if debug:
		#print(data.iloc[i, 0] + ' interacts with ' + data.iloc[i, 1])

	## form the LHS
	LHS = []
	next_in_complex = False
	for name in names:
		if name[0] == '[': # we are dealing with the first monomer of a complex
			molecule = name[1:]
			next_in_complex = True
		elif name[-1] == ']': # we are dealing with the last monomer of a complex
			molecule = name[:-1]
			next_in_complex = False
		elif next_in_complex: # we are dealing with a monomer part of a complex
			molecule = name
		else:
			molecule = name
			linked = 'None'

		if 'BS' in name:
			if 'pro' in name:
				molecule = '{:s}\', type = \'{:s}'.format(molecule.split('-')[-2], molecule.split('-')[-1])
			LHS.append('dna(name = \'{:s}\', prot = dna_link, up = bs_link, dw = bs_link)' \
					.format(molecule))
		elif 'SMALL' in name:
			LHS.append('met(name = \'{:s}\', prot = met_link)' \
					.format(molecule.replace('SMALL-', '')))
		else:
			LHS.append('prot(name = \'{:s}\', dna = dna_link, met = met_link, up = prot_link, dw = prot_link)' \
					.format(molecule))

	## look for where starts and ends a complex in the LHS
	complexes = [(m.start()+1, m.end()-1) for m in re.finditer(r'\[[A-Za-z0-9-_, ]+\]', agents)]
	monomers = [(m.start(), m.end()) for m in re.finditer(r'[A-Za-z0-9-_]+', agents)]

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
		## join agents and remove from LHS list because they were joined into one position
		LHS[position[0]] = ' %\n	'.join(LHS[position[0]:position[1]+1])
		for index in reversed(range(position[0]+1, position[1]+1)):
			LHS.pop(index)

	## create numbered links
	starter_link = 1
	for index, agent in enumerate(LHS):
		count_monomers = len(agent.split('%'))
		count_small = agent.count('met(')
		count_prots = agent.count('prot(')
		count_dnas = agent.count('dna(')

		if count_prots > 1:
			dw = [None] * count_prots
			for prot in range(count_prots-1):
				dw[prot] = starter_link
				starter_link += 1
			up = dw[-1:] + dw[:-1]
			## and replace indexes
			c = list(zip(up, dw))
			c = [elt for sublist in c for elt in sublist]
			LHS[index] = LHS[index].replace('prot_link', '{}').format(*c)

		if count_small >= 1 and count_prots >= 1:
			dw = [None] * (count_small + count_prots)
			for met in numpy.arange(0, count_small + count_prots, 2):
				dw[met] = starter_link
				dw[met-1] = starter_link
				starter_link += 1
			## and replace indexes
			LHS[index] = LHS[index].replace('met_link', '{}').format(*tuple(dw))

		if count_dnas > 1:
			dw = ['WILD'] * count_dnas
#			 for dna in range(count_dnas-1):
#				 dw[dna] = starter_link
#				 starter_link += 1
			up = dw[-1:] + dw[:-1]
			## and replace indexes
			c = list(zip(up, dw))
			c = [elt for sublist in c for elt in sublist]
			LHS[index] = LHS[index].replace('bs_link', '{}').format(*c)

		if count_dnas >= 1 and count_prots >= 1: # a protein is complexed with the dna
			dw = [None] * (count_prots + count_dnas)
			for dna in range(count_prots + count_dnas):
				if dna == count_prots:
					dw[dna] = starter_link
					dw[dna-1] = starter_link
					starter_link += 1
			## and replace indexes
			LHS[index] = LHS[index].replace('True', 'False').replace('dna_link', '{}').format(*dw)

		## final replace
		LHS[index] = LHS[index].replace('prot_link', 'None')
		LHS[index] = LHS[index].replace('met_link', 'None')
		LHS[index] = LHS[index].replace('bs_link', 'WILD')
		LHS[index] = LHS[index].replace('dna_link', 'None')

	## LHS final join
	LHS = ' +\n	'.join(LHS)
	#RULE_LHS.append(LHS)
	#description.append('# ' + data.iloc[i, 0] + ' interacts with ' + data.iloc[i, 1])

#RULE_RHS = []
#for i in data.index:
	## data
	agents = (data.iloc[i, 0] + ',' + data.iloc[i, 1]).replace('[', '').replace(']', '')
	names = agents.split(',')

	## write the RHS
	RHS = []
	for index, name in enumerate(names):
		if name[0] == '[': # we are dealing with the first monomer of a complex
			molecule = name[1:]
			next_in_complex = True
		elif name[-1] == ']': # we are dealing with the last monomer of a complex
			molecule = name[:-1]
			next_in_complex = False
		elif next_in_complex: # we are dealing with a monomer part of a complex
			molecule = name
		else:
			molecule = name

		if 'BS' in name:
			if 'pro' in name:
				molecule = '{:s}\', type = \'{:s}'.format(molecule.split('-')[-2], molecule.split('-')[-1])
			RHS.append('dna(name = \'{:s}\', prot = dna_link, up = bs_link, dw = bs_link)' \
					   .format(molecule))
		elif 'SMALL' in name:
			RHS.append('met(name = \'{:s}\', prot = met_link)' \
					   .format(molecule.replace('SMALL-', '')))
		else:
			RHS.append('prot(name = \'{:s}\', dna = dna_link, met = met_link, up = prot_link, dw = prot_link)' \
					   .format(molecule))

	## join complexes
	RHS = ' %\n	'.join(RHS)

	## create numbered links
	agent = RHS
	count_monomers = len(agent.split('%'))
	count_small = agent.count('met(')
	count_prots = agent.count('prot(')
	count_dnas = agent.count('dna(')

	starter_link = 1
	if count_prots > 1:
		dw = [None] * count_prots
		for prot in range(count_prots-1):
			dw[prot] = starter_link
			starter_link += 1
		up = dw[-1:] + dw[:-1]
		## and replace indexes
		c = list(zip(up, dw))
		c = [elt for sublist in c for elt in sublist]
		RHS = RHS.replace('prot_link', '{}').format(*c)

	if count_small >= 1:
		dw = [None] * (count_small + count_prots)
		for met in numpy.arange(0, count_small + count_prots, 2):
			dw[met] = starter_link
			dw[met-1] = starter_link
			starter_link += 1
		## and replace indexes
		RHS = RHS.replace('met_link', '{}').format(*tuple(dw))

	if count_dnas > 1:
		dw = ['WILD'] * count_dnas
#		 for dna in range(count_dnas-1):
#			dw[dna] = starter_link
#			starter_link += 1
		up = dw[-1:] + dw[:-1]
		## and replace indexes
		c = list(zip(up, dw))
		c = [elt for sublist in c for elt in sublist]
		RHS = RHS.replace('bs_link', '{}').format(*c)

	## always
	dw = [None] * (count_prots + count_dnas)
	for dna in range(count_prots + count_dnas):
		if dna == count_prots:
			dw[dna] = starter_link
			dw[dna-1] = starter_link
			starter_link += 1
	up = dw[-1:] + dw[:-1]
	## and replace indexes
	RHS = RHS.replace('dna_link', '{}').format(*dw)

	## final replace
	RHS = RHS.replace('prot_link', 'None')
	RHS = RHS.replace('met_link', 'None')
	RHS = RHS.replace('bs_link', 'WILD')
	RHS = RHS.replace('dna_link', 'None')

	#RULE_RHS.append(RHS)

	return LHS, RHS

def observables_from_interaction_network(model, data, monomers, verbose = False, toFile = False):
	for name in sorted(monomers[1]):
		name = name.replace('-','_')
		for loc in location_keys().keys():
			code = 'Observable(\'obs_prot_{:s}_{:s}\', prot(name = \'{:s}\', loc = \'{:s}\', dna = None, met = None, prot = None, rna = None, up = None, dw = None))\n'
			code = code.format(name, loc.lower(), name, loc.lower())
			if verbose:
				print(code)
			if toFile:
				with open(toFile, 'a+') as outfile:
					outfile.write(code)
			else:
				exec(code.replace('\t', ''))

	for name in sorted(monomers[0]):
		name = name.replace('-','_')
		for loc in location_keys().keys():
			code = "Initial(met(name = \'{:s}\', loc = \'{:s}\', prot = None), Parameter(\'t0_met_{:s}_{:s}\', 0))\n"
			code = code.format(name, loc.lower(), name, loc.lower())
			if verbose:
				print(code)
			if toFile:
				with open(toFile, 'a+') as outfile:
					outfile.write(code)
			else:
				exec(code.replace('\t', ''))

	for name in sorted(monomers[1]):
		name = name.replace('-','_')
		for loc in location_keys().keys():
			code = 'Initial(prot(name = \'{:s}\', loc = \'{:s}\', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter(\'t0_prot_{:s}_{:s}\', 0))\n'
			code = code.format(name, loc.lower(), name, loc.lower())
			if verbose:
				print(code)
			if toFile:
				with open(toFile, 'a+') as outfile:
					outfile.write(code)
			else:
				exec(code.replace('\t', ''))

	for name in sorted(monomers[2]):
		name = name.replace('-','_')
		for loc in location_keys().keys():
			code = 'Initial(cplx(name = \'{:s}\', loc = \'{:s}\', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter(\'t0_cplx_{:s}_{:s}\', 0))\n'
			code = code.format(name, loc.lower(), name, loc.lower())
			if verbose:
				print(code)
			if toFile:
				with open(toFile, 'a+') as outfile:
					outfile.write(code)
			else:
				exec(code.replace('\t', ''))

	names = []
	for left, right in monomers[3]:
		names.append('[' + (left + ',' + right).replace('[','').replace(']','') + ']')

	for name in sorted(set(names)):
		if name.startswith('['):
			monomers = name[1:-1].split(',')

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

			for location in location_keys().keys():
				complex_pysb = []
				for index, monomer in enumerate(monomers):
					complex_pysb.append('prot(name = \'{:s}\', loc = \'{:s}\', dna = None, met = None, prot = None, rna = None, up = {:s}, dw = {:s})'.format(
						monomer, location.lower(), str(up[index]), str(dw[index])))

				complex_pysb = ' %\n	'.join(complex_pysb)

				code = 'Initial({:s},\n' \
					'	Parameter(\'t0_cplx{:s}_{:s}\', 0))\n'
				code = code.format(complex_pysb, cplx_composition, location.lower())

				if verbose:
					print(code)
				if toFile:
					with open(toFile, 'a+') as outfile:
						outfile.write(code)
				else:
					exec(code.replace('\t', ' ').replace('\n', ' '))

				code = 'Observable(\'obs_cplx{:s}_{:s}\',\n' \
					'	{:s})\n'
				code = code.format(cplx_composition, location.lower(), complex_pysb)

				if verbose:
					print(code)
				if toFile:
					with open(toFile, 'a+') as outfile:
						outfile.write(code)
				else:
					exec(code.replace('\t', ' ').replace('\n', ' '))

	return model

def construct_model_from_interaction_network(network, verbose = False, toFile = False):
	if toFile:
		with open(toFile, 'w') as outfile:
			outfile.write('from pysb import *\nModel()\n\n')

	if isinstance(network, str):
		data = read_network(network)
	elif isinstance(network, pandas.DataFrame):
		data = network
	elif isinstance(network, numpy.array):
		data = pandas.DataFrame(data = network)
	else:
		raise Exception("The network format is not yet supported.")
	data = check_interaction_network(data)

	model = Model()
	[metabolites, p_monomers, complexes, hypernodes] = \
		monomers_from_interaction_network(model, data, verbose, toFile)
	observables_from_interaction_network(model, data, [metabolites, p_monomers, complexes, hypernodes], verbose, toFile)

	RULE_LHS = []
	RULE_RHS = []
	for idx in data.index:
		if 'BS-' in data['SOURCE'].iloc[idx] or 'BS-' in data['TARGET'].iloc[idx]:
			LHS, RHS = from_ProtDNA_network(data, idx)
		elif 'SMALL-' in data['SOURCE'].iloc[idx] or 'SMALL-' in data['TARGET'].iloc[idx]:
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
			'	Parameter(\'rvs_{:s}\', {:f}))\n'
		code = code.format(name, RULE_LHS[index], RULE_RHS[index], name, data['FWD_RATE'].iloc[index], name, data['RVS_RATE'].iloc[index])
		code = code.replace('-', '_').replace('{:s}', 'None')

		if verbose:
			print(code)
		if toFile:
			with open(toFile, 'a+') as outfile:
				outfile.write(code)
		else:
			exec(code.replace('\t', ''))

	return model
