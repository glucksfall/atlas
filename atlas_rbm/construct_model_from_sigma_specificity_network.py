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

from .utils import read_network, check_genome_graph, check_interaction_network
from .construct_model_from_genome_graph import monomers_from_genome_graph, observables_from_genome_graph

def polymerase_docking_rules(data, data_arq, verbose, toFile):
	RULE_LHS = []
	for i in data.index:
		# data
		agents = (data['SOURCE'].iloc[i] + ',' + data['TARGET'].iloc[i])
		names = agents.split(',')

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

			if 'pro' in name.lower():
				molecule = '{:s}\', type = \'{:s}'.format(molecule.split('-')[-2], molecule.split('-')[-1])
				LHS.append('dna(name = \'{:s}\', prot = dna_link, up = bs_link, dw = bs_link)'.format(molecule))
			elif 'SMALL' in name:
				LHS.append('met(name = \'{:s}\', prot = met_link)'.format(molecule.replace('SMALL-', '')))
			else:
				LHS.append('prot(name = \'{:s}\', dna = dna_link, met = met_link, up = prot_link, dw = prot_link)'.format(molecule))

		## look for where starts and ends a complex in the LHS
		complexes = [(m.start()+1, m.end()-1) for m in re.finditer(r'\[[A-Za-z0-9-_,]+\]', agents)]
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
			count_small = agent.count('met(')
			count_prots = agent.count('prot(')
			count_dnas = agent.count('dna(')

			if count_prots > 1:
				dw = [None] * count_prots
				for prot_index in range(count_prots-1):
					dw[prot_index] = starter_link
					starter_link += 1
				up = dw[-1:] + dw[:-1]
				## and replace indexes
				c = list(zip(up, dw))
				c = [elt for sublist in c for elt in sublist]
				LHS[index] = LHS[index].replace('prot_link', '{}').format(*c)

			if count_small >= 1 and count_prots >= 1:
				dw = [None] * (count_small + count_prots)
				for met_index in numpy.arange(0, count_small + count_prots, 2):
					dw[met_index] = starter_link
					dw[met_index-1] = starter_link
					starter_link += 1
				## and replace indexes
				LHS[index] = LHS[index].replace('met_link', '{}').format(*tuple(dw))

			if count_dnas > 1:
				dw = ['WILD'] * count_dnas
	#			 for dna_index in range(count_dnas-1):
	#				 dw[dna_index] = starter_link
	#				 starter_link += 1
				up = dw[-1:] + dw[:-1]
				## and replace indexes
				c = list(zip(up, dw))
				c = [elt for sublist in c for elt in sublist]
				LHS[index] = LHS[index].replace('bs_link', '{}').format(*c)

			if count_dnas >= 1 and count_prots >= 1: # a protein is complexed with the dna
				dw = [None] * (count_prots + count_dnas)
				for dna_index in range(count_prots + count_dnas):
					if dna_index == count_prots:
						dw[dna_index] = starter_link
						dw[dna_index-1] = starter_link
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
		RULE_LHS.append(LHS)

	RULE_RHS = []
	for i in data.index:
		## data
		agents = (data['SOURCE'].iloc[i] + ',' + data['TARGET'].iloc[i]).replace('[', '').replace(']', '')
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

			if 'pro' in name.lower():
				molecule = '{:s}\', type = \'{:s}'.format(molecule.split('-')[-2], molecule.split('-')[-1])
				RHS.append('dna(name = \'{:s}\', prot = dna_link, up = bs_link, dw = bs_link)'.format(molecule))
			elif 'SMALL' in name:
				RHS.append('met(name = \'{:s}\', prot = met_link)'.format(molecule.replace('SMALL-', '')))
			else:
				RHS.append('prot(name = \'{:s}\', dna = dna_link, met = met_link, up = prot_link, dw = prot_link)'.format(molecule))

		## join complexes
		RHS = ' %\n	'.join(RHS)

		## create numbered links
		agent = RHS
		count_small = agent.count('met(')
		count_prots = agent.count('prot(')
		count_dnas = agent.count('dna(')

		starter_link = 1
		if count_prots > 1:
			dw = [None] * count_prots
			for prot_index in range(count_prots-1):
				dw[prot_index] = starter_link
				starter_link += 1
			up = dw[-1:] + dw[:-1]
			## and replace indexes
			c = list(zip(up, dw))
			c = [elt for sublist in c for elt in sublist]
			RHS = RHS.replace('prot_link', '{}').format(*c)

		if count_small >= 1:
			dw = [None] * (count_small + count_prots)
			for met_index in numpy.arange(0, count_small + count_prots, 2):
				dw[met_index] = starter_link
				dw[met_index-1] = starter_link
				starter_link += 1
			## and replace indexes
			RHS = RHS.replace('met_link', '{}').format(*tuple(dw))

		if count_dnas > 1:
			dw = ['WILD'] * count_dnas
	#		 for dna_index in range(count_dnas-1):
	#			dw[dna_index] = starter_link
	#			starter_link += 1
			up = dw[-1:] + dw[:-1]
			## and replace indexes
			c = list(zip(up, dw))
			c = [elt for sublist in c for elt in sublist]
			RHS = RHS.replace('bs_link', '{}').format(*c)

		## always
		dw = [None] * (count_prots + count_dnas)
		for dna_index in range(count_prots + count_dnas):
			if dna_index == count_prots:
				dw[dna_index] = starter_link
				dw[dna_index-1] = starter_link
				starter_link += 1
		up = dw[-1:] + dw[:-1]
		## and replace indexes
		RHS = RHS.replace('dna_link', '{}').format(*dw)

		## final replace
		RHS = RHS.replace('prot_link', 'None')
		RHS = RHS.replace('met_link', 'None')
		RHS = RHS.replace('bs_link', 'WILD')
		RHS = RHS.replace('dna_link', 'None')

		RULE_RHS.append(RHS)

	for index in data.index:
		for dna_part1 in data_arq['UPSTREAM']:
			if data['TARGET'].iloc[index] == dna_part1.replace('[', ''):
				## complete rule
				code = 'Rule(\'docking_{:d}_{:s}\',\n' \
					'	{:s} |\n' \
					'	{:s},\n' \
					'	Parameter(\'fwd_docking_{:d}_{:s}\', {:f}),\n' \
					'	Parameter(\'rvs_docking_{:d}_{:s}\', {:f}))\n'

				code = code.format(
					index+1, dna_part1.replace('[', ''), RULE_LHS[index], RULE_RHS[index],
					index+1, dna_part1.replace('[', ''), data['FWD_DOCK_RATE'].iloc[index],
					index+1, dna_part1.replace('[', ''), data['RVS_DOCK_RATE'].iloc[index])

				code = code.replace('-', '_')
				if verbose:
					print(code)
				if toFile:
					with open(toFile, 'a+') as outfile:
						outfile.write(code)
				else:
					exec(code)

def polymerase_sliding_from_promoters_rules(data, data_arq, verbose, toFile):
	RULE_LHS = []
	for idx, sigma in enumerate(data.index):
		for dna_part1, dna_part2 in zip(data_arq['UPSTREAM'], data_arq['DOWNSTREAM']):
			if data['TARGET'].iloc[sigma] == dna_part1.replace('[', ''):
				# data
				agents = (data['SOURCE'].iloc[sigma][:-1] + ',' + data['TARGET'].iloc[sigma]) + ']' + ',BS-' + dna_part2
				names = agents.split(',')

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

					if 'pro' in name.lower() or 'rbs' in name.lower():
						molecule = '{:s}\', type = \'{:s}'.format(molecule.split('-')[-2], molecule.split('-')[-1])
						LHS.append('dna(name = \'{:s}\', prot = dna_link, up = bs_link, dw = bs_link)'.format(molecule))
					elif 'SMALL' in name:
						LHS.append('met(name = \'{:s}\', prot = met_link)'.format(molecule.replace('SMALL-', '')))
					else:
						LHS.append('prot(name = \'{:s}\', dna = dna_link, met = met_link, up = prot_link, dw = prot_link)'.format(molecule))

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
					count_small = agent.count('met(')
					count_prots = agent.count('prot(')
					count_dnas = agent.count('dna(')

					if count_prots > 1:
						dw = [None] * count_prots
						for prot_index in range(count_prots-1):
							dw[prot_index] = starter_link
							starter_link += 1
						up = dw[-1:] + dw[:-1]
						## and replace indexes
						c = list(zip(up, dw))
						c = [elt for sublist in c for elt in sublist]
						LHS[index] = LHS[index].replace('prot_link', '{}').format(*c)

					if count_small >= 1 and count_prots >= 1:
						dw = [None] * (count_small + count_prots)
						for met_index in numpy.arange(0, count_small + count_prots, 2):
							dw[met_index] = starter_link
							dw[met_index-1] = starter_link
							starter_link += 1
						## and replace indexes
						LHS[index] = LHS[index].replace('met_link', '{}').format(*tuple(dw))

					if count_dnas > 1:
						dw = ['WILD'] * count_dnas
						#for dna_index in range(count_dnas-1):
							#dw[dna_index] = starter_link
							#starter_link += 1
						up = dw[-1:] + dw[:-1]
						## and replace indexes
						c = list(zip(up, dw))
						c = [elt for sublist in c for elt in sublist]
						LHS[index] = LHS[index].replace('bs_link', '{}').format(*c)

					if count_dnas >= 1 and count_prots >= 1: # a protein is complexed with the dna
						dw = [None] * (count_prots + count_dnas)
						for dna_index in range(count_prots + count_dnas):
							if dna_index == count_prots:
								dw[dna_index] = starter_link
								dw[dna_index-1] = starter_link
								starter_link += 1
						## and replace indexes
						LHS[index] = LHS[index].replace('True', 'False').replace('dna_link', '{}').format(*dw)

					## final replace
					LHS[index] = LHS[index].replace('prot_link', 'None')
					LHS[index] = LHS[index].replace('met_link', 'None')
					LHS[index] = LHS[index].replace('bs_link', 'WILD')
					LHS[index] = LHS[index].replace('dna_link', 'None')

				## LHS final join
				LHS = ' +\n	'.join(LHS) + ' + None'
				RULE_LHS.append(LHS)

	RULE_RHS = []
	for idx, sigma in enumerate(data.index):
		for dna_part1, dna_part2 in zip(data_arq['UPSTREAM'], data_arq['DOWNSTREAM']):
			if data['TARGET'].iloc[sigma] == dna_part1.replace('[', ''):
				# data
				agents = (','.join(data['SOURCE'].iloc[sigma].split(',')) + ',BS-' + dna_part2) + '],' + data['TARGET'].iloc[sigma].split(',')[-1][:-1] + ',BS-' + dna_part1
				names = agents.split(',')

				## form the RHS
				RHS = []
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

					if 'pro' in name.lower() or 'rbs' in name.lower() or 'cds' in name.lower():
						molecule = '{:s}\', type = \'{:s}'.format(molecule.split('-')[-2], molecule.split('-')[-1])
						RHS.append('dna(name = \'{:s}\', prot = dna_link, up = bs_link, dw = bs_link)'.format(molecule))
					elif 'SMALL' in name:
						RHS.append('met(name = \'{:s}\', prot = met_link)'.format(molecule.replace('SMALL-', '')))
					else:
						RHS.append('prot(name = \'{:s}\', dna = dna_link, met = met_link, up = prot_link, dw = prot_link)'.format(molecule))

				molecule = '{:s}\', type = \'{:s}'.format(dna_part2.split('-')[0], dna_part2.split('-')[1])
				RHS.append('rna(name = \'{:s}\', prot = None)'.format(molecule))

				## look for where starts and ends a complex in the RHS
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
					## join agents and remove from RHS list because they were joined into one position
					RHS[position[0]] = ' %\n	'.join(RHS[position[0]:position[1]+1])
					for index in reversed(range(position[0]+1, position[1]+1)):
						RHS.pop(index)

				## create numbered links
				starter_link = 1
				for index, agent in enumerate(RHS):
					count_small = agent.count('met(')
					count_prots = agent.count('prot(')
					count_dnas = agent.count('dna(')

					if count_prots > 1:
						dw = [None] * count_prots
						for prot_index in range(count_prots-1):
							dw[prot_index] = starter_link
							starter_link += 1
						up = dw[-1:] + dw[:-1]
						## and replace indexes
						c = list(zip(up, dw))
						c = [elt for sublist in c for elt in sublist]
						RHS[index] = RHS[index].replace('prot_link', '{}').format(*c)

					if count_small >= 1 and count_prots >= 1:
						dw = [None] * (count_small + count_prots)
						for met_index in numpy.arange(0, count_small + count_prots, 2):
							dw[met_index] = starter_link
							dw[met_index-1] = starter_link
							starter_link += 1
						## and replace indexes
						RHS[index] = RHS[index].replace('met_link', '{}').format(*tuple(dw))

					if count_dnas > 1:
						dw = ['WILD'] * count_dnas
						#for dna_index in range(count_dnas-1):
							#dw[dna_index] = starter_link
							#starter_link += 1
						up = dw[-1:] + dw[:-1]
						## and replace indexes
						c = list(zip(up, dw))
						c = [elt for sublist in c for elt in sublist]
						RHS[index] = RHS[index].replace('bs_link', '{}').format(*c)

					if count_dnas >= 1 and count_prots >= 1: # a protein is complexed with the dna
						dw = [None] * (count_prots + count_dnas)
						for dna_index in range(count_prots + count_dnas):
							if dna_index == count_prots:
								dw[dna_index] = starter_link
								dw[dna_index-1] = starter_link
								starter_link += 1
						## and replace indexes
						RHS[index] = RHS[index].replace('True', 'False').replace('dna_link', '{}').format(*dw)

					## final replace
					RHS[index] = RHS[index].replace('prot_link', 'None')
					RHS[index] = RHS[index].replace('met_link', 'None')
					RHS[index] = RHS[index].replace('bs_link', 'WILD')
					RHS[index] = RHS[index].replace('dna_link', 'None')

				## RHS final join
				RHS = ' +\n	'.join(RHS)
				RHS = RHS.split('\t')
				RHS[4], RHS[5] = RHS[5], RHS[4]
				RHS[4] = RHS[4][:-2] + '%\n'
				RHS = '\t'.join(RHS)
				RULE_RHS.append(RHS)

	for index, sigma in enumerate(data.index):
		for dna_part1, dna_part2 in zip(data_arq['UPSTREAM'], data_arq['DOWNSTREAM']):
			if data['TARGET'].iloc[sigma] == dna_part1.replace('[', ''):
				## complete rule
				code = 'Rule(\'sliding_{:d}_{:s}\',\n' \
					'	{:s} >>\n' \
					'	{:s},\n' \
					'	Parameter(\'fwd_sliding_{:d}_{:s}\', {:f}))\n' \

				code = code.format(
					index+1, dna_part1.replace('[', '') + '_' + dna_part2.split('-')[-1], RULE_LHS[index], RULE_RHS[index].replace('[', ''),
					index+1, dna_part1.replace('[', '') + '_' + dna_part2.split('-')[-1], data['FWD_SLIDE_RATE'].iloc[sigma])

				code = code.replace('-', '_')
				if verbose:
					print(code)
				if toFile:
					with open(toFile, 'a+') as outfile:
						outfile.write(code)
				else:
					exec(code)

def polymerase_sliding_from_others_rules(data, data_arq, verbose, toFile):
	architecture = data_arq['UPSTREAM'] + ',' + data_arq['DOWNSTREAM']
	operons = []
	for dna_part in architecture:
		if dna_part.startswith('['):
			operon = []
			operon.append(dna_part.split(',')[0][1:])
		elif dna_part.endswith(']'):
			operon.append(dna_part.split(',')[0])
			operon.append(dna_part.split(',')[1][:-1])
			operons.append(','.join(operon))
		else:
			operon.append(dna_part.split(',')[0])

	rna_forms = []
	for operon in list(set(operons)):
		a = [(m.start(0), m.end(0)) for m in re.finditer(r'\w+-pro\d?', operon)]
		b = [(m.start(0), m.end(0)) for m in re.finditer(r'\w+-ter\d?', operon)]
		for lst in itertools.product(a, b):
			rna_forms.append(operon[lst[0][0]:lst[1][1]].split(',')[1:])

	for rna_form in rna_forms:
		for idx, dna_part in enumerate(rna_form[:-1]):
			## form the LHS
			agents = (','.join(data['SOURCE'].iloc[i].split(',')[:-1]) + ',BS-' + rna_form[idx].replace('[', '')).replace(']', '') + ']' + ',BS-' + rna_form[idx+1]
			names = agents.split(',')

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

				if 'BS' in name:
					molecule = '{:s}\', type = \'{:s}'.format(molecule.split('-')[-2], molecule.split('-')[-1])
					LHS.append('dna(name = \'{:s}\', prot = dna_link, up = bs_link, dw = bs_link)'.format(molecule))
				elif 'SMALL' in name:
					LHS.append('met(name = \'{:s}\', prot = met_link)'.format(molecule.replace('SMALL-', '')))
				else:
					LHS.append('prot(name = \'{:s}\', dna = dna_link, met = met_link, up = prot_link, dw = prot_link)'.format(molecule))

			# match the synthesis of RNA in RHS
			if not len(rna_form[:-2]) == idx:
				LHS.append('None')

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
				LHS[position[0]] = ' %\n\t'.join(LHS[position[0]:position[1]+1])
				for index in reversed(range(position[0]+1, position[1]+1)):
					LHS.pop(index)

			## create numbered links
			starter_link = 1
			for index, agent in enumerate(LHS):
				count_small = agent.count('met(')
				count_prots = agent.count('prot(')
				count_dnas = agent.count('dna(')

				if count_prots > 1:
					dw = [None] * count_prots
					for prot_index in range(count_prots-1):
						dw[prot_index] = starter_link
						starter_link += 1
					up = dw[-1:] + dw[:-1]
					## and replace indexes
					c = list(zip(up, dw))
					c = [elt for sublist in c for elt in sublist]
					LHS[index] = LHS[index].replace('prot_link', '{}').format(*c)

				if count_small >= 1 and count_prots >= 1:
					dw = [None] * (count_small + count_prots)
					for met_index in numpy.arange(0, count_small + count_prots, 2):
						dw[met_index] = starter_link
						dw[met_index-1] = starter_link
						starter_link += 1
					## and replace indexes
					LHS[index] = LHS[index].replace('met_link', '{}').format(*tuple(dw))

				if count_dnas > 1:
					dw = ['WILD'] * count_dnas
		#             for dna_index in range(count_dnas-1):
		#                 dw[dna_index] = starter_link
		#                 starter_link += 1
					up = dw[-1:] + dw[:-1]
					## and replace indexes
					c = list(zip(up, dw))
					c = [elt for sublist in c for elt in sublist]
					LHS[index] = LHS[index].replace('bs_link', '{}').format(*c)

				if count_dnas >= 1 and count_prots >= 1: # a protein is complexed with the dna
					dw = [None] * (count_prots + count_dnas)
					for dna_index in range(count_prots + count_dnas):
						if dna_index == count_prots:
							dw[dna_index] = starter_link
							dw[dna_index-1] = starter_link
							starter_link += 1
					## and replace indexes
					LHS[index] = LHS[index].replace('True', 'False').replace('dna_link', '{}').format(*dw)

				## final replace
				LHS[index] = LHS[index].replace('prot_link', 'None')
				LHS[index] = LHS[index].replace('met_link', 'None')
				LHS[index] = LHS[index].replace('bs_link', 'WILD')
				LHS[index] = LHS[index].replace('dna_link', 'None')

			## LHS final join
			LHS = ' +\n\t'.join(LHS)
			RULE_LHS.append(LHS)

			## form the RHS
			agents = (','.join(data['SOURCE'].iloc[i].split(',')[:-1]) + ',BS-' + rna_form[idx+1].replace('[', '')).replace(']', '') + ']' + ',BS-' + rna_form[idx]
			names = agents.split(',')

			RHS = []
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

				if 'BS' in name:
					molecule = '{:s}\', type = \'{:s}'.format(molecule.split('-')[-2], molecule.split('-')[-1])
					RHS.append('dna(name = \'{:s}\', prot = dna_link, up = bs_link, dw = bs_link)'.format(molecule))
				elif 'SMALL' in name:
					RHS.append('met(name = \'{:s}\', prot = met_link)'.format(molecule.replace('SMALL-', '')))
				else:
					RHS.append('prot(name = \'{:s}\', dna = dna_link, met = met_link, up = prot_link, dw = prot_link)'.format(molecule))

			# synthesis of RNA
			if not len(rna_form[:-2]) == idx:
				molecule = '{:s}\', type = \'{:s}'.format(rna_form[idx+1].split('-')[0], rna_form[idx+1].split('-')[1])
				RHS.append('rna(name = \'{:s}\', prot = None)'.format(molecule))

			## look for where starts and ends a complex in the RHS
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
				## join agents and remove from RHS list because they were joined into one position
				RHS[position[0]] = ' %\n\t'.join(RHS[position[0]:position[1]+1])
				for index in reversed(range(position[0]+1, position[1]+1)):
					RHS.pop(index)

			## create numbered links
			starter_link = 1
			for index, agent in enumerate(RHS):
				count_small = agent.count('met(')
				count_prots = agent.count('prot(')
				count_dnas = agent.count('dna(')

				if count_prots > 1:
					dw = [None] * count_prots
					for prot_index in range(count_prots-1):
						dw[prot_index] = starter_link
						starter_link += 1
					up = dw[-1:] + dw[:-1]
					## and replace indexes
					c = list(zip(up, dw))
					c = [elt for sublist in c for elt in sublist]
					RHS[index] = RHS[index].replace('prot_link', '{}').format(*c)

				if count_small >= 1 and count_prots >= 1:
					dw = [None] * (count_small + count_prots)
					for met_index in numpy.arange(0, count_small + count_prots, 2):
						dw[met_index] = starter_link
						dw[met_index-1] = starter_link
						starter_link += 1
					## and replace indexes
					RHS[index] = RHS[index].replace('met_link', '{}').format(*tuple(dw))

				if count_dnas > 1:
					dw = ['WILD'] * count_dnas
		#             for dna_index in range(count_dnas-1):
		#                 dw[dna_index] = starter_link
		#                 starter_link += 1
					up = dw[-1:] + dw[:-1]
					## and replace indexes
					c = list(zip(up, dw))
					c = [elt for sublist in c for elt in sublist]
					RHS[index] = RHS[index].replace('bs_link', '{}').format(*c)

				if count_dnas >= 1 and count_prots >= 1: # a protein is complexed with the dna
					dw = [None] * (count_prots + count_dnas)
					for dna_index in range(count_prots + count_dnas):
						if dna_index == count_prots:
							dw[dna_index] = starter_link
							dw[dna_index-1] = starter_link
							starter_link += 1
					## and replace indexes
					RHS[index] = RHS[index].replace('True', 'False').replace('dna_link', '{}').format(*dw)

				## final replace
				RHS[index] = RHS[index].replace('prot_link', 'None')
				RHS[index] = RHS[index].replace('met_link', 'None')
				RHS[index] = RHS[index].replace('bs_link', 'WILD')
				RHS[index] = RHS[index].replace('dna_link', 'None')

			## RHS final join
			RHS = ' +\n\t'.join(RHS)
			RULE_RHS.append(RHS)

			## complete rule
			code = 'Rule(\'sliding_{:s}_to_{:s}\',\n' \
				'	{:s} >>\n' \
				'	{:s},\n' \
				'	Parameter(\'fwd_sliding_{:s}_to_{:2}\', {:f}))'

			code = code.format(rna_form[idx], rna_form[idx+1], LHS, RHS, rna_form[idx], rna_form[idx+1], 1).replace('-', '_')

			if verbose:
				print(code)
			if toFile:
				with open(toFile, 'a+') as outfile:
					outfile.write(code)
			else:
				exec(code)

def polymerase_falloff_rules(data, data_arq, verbose, toFile):
	description = []
	RULE_LHS = []

	for dna_part1, dna_part2 in zip(data_arq.iloc[:,0], data_arq.iloc[:,1]):
		if 'ter' in dna_part2:
			# data
			agents = (','.join(data.iloc[i, 0].split(',')[0:4])).replace(']', '') + ',BS-' + dna_part2 + ']'
			names = agents.split(',')

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

				if 'BS' in name:
					if 'ter' in name:
						molecule = '{:s}\', type = \'{:s}'.format(molecule.split('-')[-2], molecule.split('-')[-1])
					LHS.append('dna(name = \'{:s}\', prot = dna_link, free = \'True\', up = bs_link, dw = bs_link)' \
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
				LHS[position[0]] = ' %\n    '.join(LHS[position[0]:position[1]+1])
				for index in reversed(range(position[0]+1, position[1]+1)):
					LHS.pop(index)

			## create numbered links
			starter_link = 1
			for index, agent in enumerate(LHS):
				count_small = agent.count('met(')
				count_prots = agent.count('prot(')
				count_dnas = agent.count('dna(')

				if count_prots > 1:
					dw = [None] * count_prots
					for prot_index in range(count_prots-1):
						dw[prot_index] = starter_link
						starter_link += 1
					up = dw[-1:] + dw[:-1]
					## and replace indexes
					c = list(zip(up, dw))
					c = [elt for sublist in c for elt in sublist]
					LHS[index] = LHS[index].replace('prot_link', '{}').format(*c)

				if count_small >= 1 and count_prots >= 1:
					dw = [None] * (count_small + count_prots)
					for met_index in numpy.arange(0, count_small + count_prots, 2):
						dw[met_index] = starter_link
						dw[met_index-1] = starter_link
						starter_link += 1
					## and replace indexes
					LHS[index] = LHS[index].replace('met_link', '{}').format(*tuple(dw))

				if count_dnas > 1:
					dw = ['WILD'] * count_dnas
		#             for dna in range(count_dnas-1):
		#                 dw[dna] = starter_link
		#                 starter_link += 1
					up = dw[-1:] + dw[:-1]
					## and replace indexes
					c = list(zip(up, dw))
					c = [elt for sublist in c for elt in sublist]
					LHS[index] = LHS[index].replace('bs_link', '{}').format(*c)

				if count_dnas >= 1 and count_prots >= 1: # a protein is complexed with the dna
					dw = [None] * (count_prots + count_dnas)
					for dna_index in range(count_prots + count_dnas):
						if dna_index == count_prots:
							dw[dna_index] = starter_link
							dw[dna_index-1] = starter_link
							starter_link += 1
					## and replace indexes
					LHS[index] = LHS[index].replace('True', 'False').replace('dna_link', '{}').format(*dw)

				## final replace
				LHS[index] = LHS[index].replace('prot_link', 'None')
				LHS[index] = LHS[index].replace('met_link', 'None')
				LHS[index] = LHS[index].replace('bs_link', 'WILD')
				LHS[index] = LHS[index].replace('dna_link', 'None')

			## LHS final join
			LHS = ' +\n    '.join(LHS)
			RULE_LHS.append(LHS)

			description.append('# ' + data.iloc[i, 0] + ' falloff from ' + dna_part2)

	description = []
	RULE_RHS = []

	for dna_part1, dna_part2 in zip(data_arq.iloc[:,0], data_arq.iloc[:,1]):
		if 'ter' in dna_part2:
			# data
			agents = ','.join(data.iloc[i, 0].split(',')[0:4]) + '],BS-' + dna_part2
			names = agents.split(',')

			## form the RHS
			RHS = []
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

				if 'BS' in name:
					if 'ter' in name:
						molecule = '{:s}\', type = \'{:s}'.format(molecule.split('-')[-2], molecule.split('-')[-1])
					RHS.append('dna(name = \'{:s}\', prot = dna_link, free = \'True\', up = bs_link, dw = bs_link)' \
							.format(molecule))
				elif 'SMALL' in name:
					RHS.append('met(name = \'{:s}\', prot = met_link)' \
							.format(molecule.replace('SMALL-', '')))
				else:
					RHS.append('prot(name = \'{:s}\', dna = dna_link, met = met_link, up = prot_link, dw = prot_link)' \
							.format(molecule))

			## look for where starts and ends a complex in the RHS
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
				## join agents and remove from RHS list because they were joined into one position
				RHS[position[0]] = ' %\n    '.join(RHS[position[0]:position[1]+1])
				for index in reversed(range(position[0]+1, position[1]+1)):
					RHS.pop(index)

			## create numbered links
			starter_link = 1
			for index, agent in enumerate(RHS):
				count_small = agent.count('met(')
				count_prots = agent.count('prot(')
				count_dnas = agent.count('dna(')

				if count_prots > 1:
					dw = [None] * count_prots
					for prot_index in range(count_prots-1):
						dw[prot_index] = starter_link
						starter_link += 1
					up = dw[-1:] + dw[:-1]
					## and replace indexes
					c = list(zip(up, dw))
					c = [elt for sublist in c for elt in sublist]
					RHS[index] = RHS[index].replace('prot_link', '{}').format(*c)

				if count_small >= 1 and count_prots >= 1:
					dw = [None] * (count_small + count_prots)
					for met_index in numpy.arange(0, count_small + count_prots, 2):
						dw[met_index] = starter_link
						dw[met_index-1] = starter_link
						starter_link += 1
					## and replace indexes
					RHS[index] = RHS[index].replace('met_link', '{}').format(*tuple(dw))

				if count_dnas > 1:
					dw = ['WILD'] * count_dnas
		#             for dna in range(count_dnas-1):
		#                 dw[dna] = starter_link
		#                 starter_link += 1
					up = dw[-1:] + dw[:-1]
					## and replace indexes
					c = list(zip(up, dw))
					c = [elt for sublist in c for elt in sublist]
					RHS[index] = RHS[index].replace('bs_link', '{}').format(*c)

				if count_dnas >= 1 and count_prots >= 1: # a protein is complexed with the dna
					dw = [None] * (count_prots + count_dnas)
					for dna_index in range(count_prots + count_dnas):
						if dna_index == count_prots:
							dw[dna_index] = starter_link
							dw[dna_index-1] = starter_link
							starter_link += 1
					## and replace indexes
					RHS[index] = RHS[index].replace('True', 'False').replace('dna_link', '{}').format(*dw)

				## final replace
				RHS[index] = RHS[index].replace('prot_link', 'None')
				RHS[index] = RHS[index].replace('met_link', 'None')
				RHS[index] = RHS[index].replace('bs_link', 'WILD')
				RHS[index] = RHS[index].replace('dna_link', 'None')

			## RHS final join
			RHS = ' +\n    '.join(RHS)
			RULE_RHS.append(RHS)

			description.append('# ' + data.iloc[i, 0] + ' falloff from ' + dna_part2)

	index = 0
	for idx, (dna_part1, dna_part2) in enumerate(zip(data_arq.iloc[:,0], data_arq.iloc[:,1])):
		dna_part1, dna_part2 = (dna_part1, dna_part2)
		if 'ter' in dna_part2:
			## complete rule
			code = 'Rule(\'falloff_{:s}\', \n' \
				'	{:s} >> \n' \
				'	{:s}, \n' \
				'	Parameter(\'fwd_falloff_{:s}\', {:f}))'

			code = code.format(dna_part2, RULE_LHS[index], RULE_RHS[index], dna_part2, data_arq.iloc[idx, 5])
			code = code.replace('-', '_')
			if verbose:
				print(code)
			exec(code)
			index += 1

def construct_model_from_sigma_specificity_network(promoters, architecture, verbose = False, toFile = False):
	if toFile:
		with open(toFile, 'w') as outfile:
			outfile.write('from pysb import *\nModel()\n\n')

	# check promoters
	if isinstance(promoters, str):
		data_promoters = read_network(promoters)
	elif isinstance(promoters, pandas.DataFrame):
		data_promoters = promoters
	elif isinstance(promoters, numpy.array):
		columns = [
			'SOURCE',
			'TARGET',
			'FWD_DOCK_RATE',
			'RVS_DOCK_RATE',
			'FWD_SLIDE_RATE'
			]
		data_promoters = pandas.DataFrame(data = promoters, columns = columns)
	else:
		raise Exception("The format of the promoter specifities network is not yet supported.")
	data_promoters = check_interaction_network(data_promoters)

	# check architecture
	if isinstance(architecture, str):
		data_architecture = read_network(architecture)
	elif isinstance(architecture, pandas.DataFrame):
		data_architecture = architecture
	elif isinstance(architecture, numpy.array):
		columns = [
			'UPSTREAM',
			'DOWNSTREAM',
			'RNAP_FWD_DOCK_RATE',
			'RNAP_RVS_DOCK_RATE',
			'RNAP_FWD_SLIDE_RATE',
			'RNAP_FWD_FALL_RATE',
			'RIB_FWD_DOCK_RATE',
			'RIB_RVS_DOCK_RATE',
			'RIB_FWD_SLIDE_RATE',
			'RIB_FWD_FALL_RATE'
			]
		data_architecture = pandas.DataFrame(data = architecture, columns = columns)
	else:
		raise Exception("The format of the architecture network is not yet supported.")
	data_architecture = check_genome_graph(data_architecture)

	model = Model()
	monomers_from_genome_graph(data_architecture, verbose, toFile)

	# write docking, slide, and falloff of RNA Polymerase from DNA
	polymerase_docking_rules(data_promoters, data_architecture, verbose, toFile)
	polymerase_sliding_from_promoters_rules(data_promoters, data_architecture, verbose, toFile)
	polymerase_sliding_from_others_rules(data_promoters, data_architecture, verbose, toFile)
	polymerase_falloff_rules(data_promoters, data_architecture, verbose, toFile)
	observables_from_genome_graph(data_architecture, verbose, toFile)

	return model
