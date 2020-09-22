from pysb import *
Model()

Monomer('prot',
	['name', 'loc', 'dna', 'met', 'prot', 'rna', 'up', 'dw'],
	{ 'name' : [ 'lacA', 'lacI', 'lacZ' ], 
	'loc' : ['cyt', 'cytosk', 'ex', 'mem', 'per', 'wall', 'bnuc', 'cproj', 'imem', 'omem']})
Observable('obs_prot_lacA_cyt', prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Initial(prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter('t0_prot_lacA_cyt', 0))
Observable('obs_prot_lacI_cyt', prot(name = 'lacI', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Initial(prot(name = 'lacI', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter('t0_prot_lacI_cyt', 0))
Observable('obs_prot_lacZ_cyt', prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Initial(prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter('t0_prot_lacZ_cyt', 0))
Initial(prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = None),
	Parameter('t0_cplx_lacAx3_cyt', 0))
Observable('obs_cplx_lacAx3_cyt',
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = None))
Initial(prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = None),
	Parameter('t0_cplx_lacAx2_cyt', 0))
Observable('obs_cplx_lacAx2_cyt',
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = None))
Initial(prot(name = 'lacI', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacI', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = None),
	Parameter('t0_cplx_lacIx2_cyt', 0))
Observable('obs_cplx_lacIx2_cyt',
	prot(name = 'lacI', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacI', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = None))
Initial(prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = None),
	Parameter('t0_cplx_lacZx4_cyt', 0))
Observable('obs_cplx_lacZx4_cyt',
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = None))
Initial(prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = None),
	Parameter('t0_cplx_lacZx2_cyt', 0))
Observable('obs_cplx_lacZx2_cyt',
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = None))
Rule('PhysicalInteractionRule_1',
	prot(name = 'lacZ', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = None, dw = None) +
	prot(name = 'lacZ', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = None, dw = None) | 
	prot(name = 'lacZ', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = 1, dw = None),
	Parameter('fwd_PhysicalInteractionRule_1', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_1', 0.000000))
Rule('PhysicalInteractionRule_2',
	prot(name = 'lacZ', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = 1, dw = None) +
	prot(name = 'lacZ', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = None, dw = 2) %
	prot(name = 'lacZ', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = 2, dw = None) | 
	prot(name = 'lacZ', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacZ', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = 2, dw = 3) %
	prot(name = 'lacZ', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = 3, dw = None),
	Parameter('fwd_PhysicalInteractionRule_2', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_2', 0.000000))
Rule('PhysicalInteractionRule_3',
	prot(name = 'lacA', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = None, dw = None) +
	prot(name = 'lacA', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = None, dw = None) | 
	prot(name = 'lacA', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = 1, dw = None),
	Parameter('fwd_PhysicalInteractionRule_3', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_3', 0.000000))
Rule('PhysicalInteractionRule_4',
	prot(name = 'lacA', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = None, dw = None) +
	prot(name = 'lacA', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = 1, dw = None) | 
	prot(name = 'lacA', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacA', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = 2, dw = None),
	Parameter('fwd_PhysicalInteractionRule_4', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_4', 0.000000))
Rule('PhysicalInteractionRule_5',
	prot(name = 'lacI', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = None, dw = None) +
	prot(name = 'lacI', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = None, dw = None) | 
	prot(name = 'lacI', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacI', loc = 'cyt', dna = None, prot = None, met = None, rna = None, up = 1, dw = None),
	Parameter('fwd_PhysicalInteractionRule_5', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_5', 0.000000))
