from pysb import *
Model()

Monomer('met',
	['name', 'loc', 'dna', 'met', 'prot', 'rna'],
	{ 'name' : [ 'alpha_ALLOLACTOSE', 'beta_ALLOLACTOSE' ], 
	'loc' : ['cyt', 'cytosk', 'ex', 'mem', 'per', 'wall', 'bnuc', 'cproj', 'imem', 'omem']})
Monomer('prot',
	['name', 'loc', 'dna', 'met', 'prot', 'rna', 'up', 'dw'],
	{ 'name' : [ 'lacI' ], 
	'loc' : ['cyt', 'cytosk', 'ex', 'mem', 'per', 'wall', 'bnuc', 'cproj', 'imem', 'omem']})
Observable('obs_met_alpha_ALLOLACTOSE_cyt', met(name = 'alpha_ALLOLACTOSE', loc = 'cyt'))
Initial(met(name = 'alpha_ALLOLACTOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_alpha_ALLOLACTOSE_cyt', 0))
Observable('obs_met_beta_ALLOLACTOSE_cyt', met(name = 'beta_ALLOLACTOSE', loc = 'cyt'))
Initial(met(name = 'beta_ALLOLACTOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_beta_ALLOLACTOSE_cyt', 0))
Observable('obs_prot_lacI_cyt', prot(name = 'lacI', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Initial(prot(name = 'lacI', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter('t0_prot_lacI_cyt', 0))
Initial(prot(name = 'lacI', loc = 'cyt', dna = None, met = 2, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacI', loc = 'cyt', dna = None, met = 3, prot = None, rna = None, up = 1, dw = None) %
	met(name = 'alpha_ALLOLACTOSE', loc = 'cyt', dna = None, met = None, prot = 3, rna = None) %
	met(name = 'alpha_ALLOLACTOSE', loc = 'cyt', dna = None, met = None, prot = 2, rna = None),
	Parameter('t0_cplx_lacIx2_alpha_ALLOLACTOSEx2_cyt', 0))
Observable('obs_cplx_lacIx2_alpha_ALLOLACTOSEx2_cyt',
	prot(name = 'lacI', loc = 'cyt', dna = None, met = 2, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacI', loc = 'cyt', dna = None, met = 3, prot = None, rna = None, up = 1, dw = None) %
	met(name = 'alpha_ALLOLACTOSE', loc = 'cyt', dna = None, met = None, prot = 3, rna = None) %
	met(name = 'alpha_ALLOLACTOSE', loc = 'cyt', dna = None, met = None, prot = 2, rna = None))
Initial(prot(name = 'lacI', loc = 'cyt', dna = None, met = 2, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacI', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = None) %
	met(name = 'alpha_ALLOLACTOSE', loc = 'cyt', dna = None, met = None, prot = 2, rna = None),
	Parameter('t0_cplx_lacIx2_alpha_ALLOLACTOSEx1_cyt', 0))
Observable('obs_cplx_lacIx2_alpha_ALLOLACTOSEx1_cyt',
	prot(name = 'lacI', loc = 'cyt', dna = None, met = 2, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacI', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = None) %
	met(name = 'alpha_ALLOLACTOSE', loc = 'cyt', dna = None, met = None, prot = 2, rna = None))
Initial(prot(name = 'lacI', loc = 'cyt', dna = None, met = 2, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacI', loc = 'cyt', dna = None, met = 3, prot = None, rna = None, up = 1, dw = None) %
	met(name = 'beta_ALLOLACTOSE', loc = 'cyt', dna = None, met = None, prot = 3, rna = None) %
	met(name = 'beta_ALLOLACTOSE', loc = 'cyt', dna = None, met = None, prot = 2, rna = None),
	Parameter('t0_cplx_lacIx2_beta_ALLOLACTOSEx2_cyt', 0))
Observable('obs_cplx_lacIx2_beta_ALLOLACTOSEx2_cyt',
	prot(name = 'lacI', loc = 'cyt', dna = None, met = 2, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacI', loc = 'cyt', dna = None, met = 3, prot = None, rna = None, up = 1, dw = None) %
	met(name = 'beta_ALLOLACTOSE', loc = 'cyt', dna = None, met = None, prot = 3, rna = None) %
	met(name = 'beta_ALLOLACTOSE', loc = 'cyt', dna = None, met = None, prot = 2, rna = None))
Initial(prot(name = 'lacI', loc = 'cyt', dna = None, met = 2, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacI', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = None) %
	met(name = 'beta_ALLOLACTOSE', loc = 'cyt', dna = None, met = None, prot = 2, rna = None),
	Parameter('t0_cplx_lacIx2_beta_ALLOLACTOSEx1_cyt', 0))
Observable('obs_cplx_lacIx2_beta_ALLOLACTOSEx1_cyt',
	prot(name = 'lacI', loc = 'cyt', dna = None, met = 2, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacI', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = None) %
	met(name = 'beta_ALLOLACTOSE', loc = 'cyt', dna = None, met = None, prot = 2, rna = None))
Rule('PhysicalInteractionRule_1',
	prot(name = 'lacI', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacI', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = 1, dw = None) +
	met(name = 'alpha_ALLOLACTOSE', loc = 'cyt', dna = None, prot = None, met = None, rna = None) | 
	prot(name = 'lacI', loc = 'cyt', dna = None, prot = None, met = 2, rna = None, up = None, dw = 1) %
	prot(name = 'lacI', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = 1, dw = None) %
	met(name = 'alpha_ALLOLACTOSE', loc = 'cyt', dna = None, prot = 2, met = None, rna = None),
	Parameter('fwd_PhysicalInteractionRule_1', 10.000000),
	Parameter('rvs_PhysicalInteractionRule_1', 0.000100))
Rule('PhysicalInteractionRule_2',
	prot(name = 'lacI', loc = 'cyt', dna = None, prot = None, met = 2, rna = None, up = None, dw = 1) %
	prot(name = 'lacI', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = 1, dw = None) %
	met(name = 'alpha_ALLOLACTOSE', loc = 'cyt', dna = None, prot = 2, met = None, rna = None) +
	met(name = 'alpha_ALLOLACTOSE', loc = 'cyt', dna = None, prot = None, met = None, rna = None) | 
	prot(name = 'lacI', loc = 'cyt', dna = None, prot = None, met = 2, rna = None, up = None, dw = 1) %
	prot(name = 'lacI', loc = 'cyt', dna = None, prot = None, met = 3, rna = None, up = 1, dw = None) %
	met(name = 'alpha_ALLOLACTOSE', loc = 'cyt', dna = None, prot = 3, met = None, rna = None) %
	met(name = 'alpha_ALLOLACTOSE', loc = 'cyt', dna = None, prot = 2, met = None, rna = None),
	Parameter('fwd_PhysicalInteractionRule_2', 10.000000),
	Parameter('rvs_PhysicalInteractionRule_2', 0.000100))
Rule('PhysicalInteractionRule_3',
	prot(name = 'lacI', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacI', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = 1, dw = None) +
	met(name = 'beta_ALLOLACTOSE', loc = 'cyt', dna = None, prot = None, met = None, rna = None) | 
	prot(name = 'lacI', loc = 'cyt', dna = None, prot = None, met = 2, rna = None, up = None, dw = 1) %
	prot(name = 'lacI', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = 1, dw = None) %
	met(name = 'beta_ALLOLACTOSE', loc = 'cyt', dna = None, prot = 2, met = None, rna = None),
	Parameter('fwd_PhysicalInteractionRule_3', 10.000000),
	Parameter('rvs_PhysicalInteractionRule_3', 0.000100))
Rule('PhysicalInteractionRule_4',
	prot(name = 'lacI', loc = 'cyt', dna = None, prot = None, met = 2, rna = None, up = None, dw = 1) %
	prot(name = 'lacI', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = 1, dw = None) %
	met(name = 'beta_ALLOLACTOSE', loc = 'cyt', dna = None, prot = 2, met = None, rna = None) +
	met(name = 'beta_ALLOLACTOSE', loc = 'cyt', dna = None, prot = None, met = None, rna = None) | 
	prot(name = 'lacI', loc = 'cyt', dna = None, prot = None, met = 2, rna = None, up = None, dw = 1) %
	prot(name = 'lacI', loc = 'cyt', dna = None, prot = None, met = 3, rna = None, up = 1, dw = None) %
	met(name = 'beta_ALLOLACTOSE', loc = 'cyt', dna = None, prot = 3, met = None, rna = None) %
	met(name = 'beta_ALLOLACTOSE', loc = 'cyt', dna = None, prot = 2, met = None, rna = None),
	Parameter('fwd_PhysicalInteractionRule_4', 10.000000),
	Parameter('rvs_PhysicalInteractionRule_4', 0.000100))
