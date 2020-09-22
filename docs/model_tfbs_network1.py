from pysb import *
Model()

Monomer('prot',
	['name', 'loc', 'dna', 'met', 'prot', 'rna', 'up', 'dw'],
	{ 'name' : [ 'lacI' ], 
	'loc' : ['cyt', 'cytosk', 'ex', 'mem', 'per', 'wall', 'bnuc', 'cproj', 'imem', 'omem']})
Monomer('dna',
	['name', 'type', 'loc', 'dna', 'met', 'prot', 'rna', 'up', 'dw'],
	{ 'name' : [ 'lacI_21_1', 'lacI_422_402', 'lacI_72_92' ],
	'type' : ['BS'],
	'loc' : ['cyt']})
Observable('obs_prot_lacI_cyt', prot(name = 'lacI', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Initial(prot(name = 'lacI', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter('t0_prot_lacI_cyt', 0))
Rule('PhysicalInteractionRule_1',
	prot(name = 'lacI', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacI', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = 1, dw = None) +
	dna(name = 'lacI_422_402', type = 'BS', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = WILD, dw = WILD) | 
	prot(name = 'lacI', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacI', loc = 'cyt', dna = 2, prot = None, met = None, rna = None, up = 1, dw = None) %
	dna(name = 'lacI_422_402', type = 'BS', loc = 'cyt', dna = None, prot = 2, met = None, rna = None, up = WILD, dw = WILD),
	Parameter('fwd_PhysicalInteractionRule_1', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_1', 0.010000))
Rule('PhysicalInteractionRule_2',
	prot(name = 'lacI', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacI', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = 1, dw = None) +
	dna(name = 'lacI_21_1', type = 'BS', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = WILD, dw = WILD) | 
	prot(name = 'lacI', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacI', loc = 'cyt', dna = 2, prot = None, met = None, rna = None, up = 1, dw = None) %
	dna(name = 'lacI_21_1', type = 'BS', loc = 'cyt', dna = None, prot = 2, met = None, rna = None, up = WILD, dw = WILD),
	Parameter('fwd_PhysicalInteractionRule_2', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_2', 0.010000))
Rule('PhysicalInteractionRule_3',
	prot(name = 'lacI', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacI', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = 1, dw = None) +
	dna(name = 'lacI_72_92', type = 'BS', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = WILD, dw = WILD) | 
	prot(name = 'lacI', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacI', loc = 'cyt', dna = 2, prot = None, met = None, rna = None, up = 1, dw = None) %
	dna(name = 'lacI_72_92', type = 'BS', loc = 'cyt', dna = None, prot = 2, met = None, rna = None, up = WILD, dw = WILD),
	Parameter('fwd_PhysicalInteractionRule_3', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_3', 0.010000))
