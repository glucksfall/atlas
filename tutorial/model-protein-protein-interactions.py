from pysb import *
Model()

Monomer('prot',
	['name', 'loc', 'dna', 'met', 'prot', 'rna', 'up', 'dw'],
	{ 'name' : [ 'lacA', 'lacZ' ], 
	'loc' : ['cyt', 'cytosk', 'ex', 'mem', 'per', 'wall', 'bnuc', 'cproj', 'imem', 'omem']})
Observable('obs_prot_lacA_cyt', prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Observable('obs_prot_lacA_imem', prot(name = 'lacA', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Observable('obs_prot_lacA_per', prot(name = 'lacA', loc = 'per', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Observable('obs_prot_lacA_mem', prot(name = 'lacA', loc = 'mem', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Observable('obs_prot_lacA_omem', prot(name = 'lacA', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Observable('obs_prot_lacA_ex', prot(name = 'lacA', loc = 'ex', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Observable('obs_prot_lacA_bnuc', prot(name = 'lacA', loc = 'bnuc', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Observable('obs_prot_lacA_wall', prot(name = 'lacA', loc = 'wall', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Observable('obs_prot_lacA_cproj', prot(name = 'lacA', loc = 'cproj', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Observable('obs_prot_lacA_cytosk', prot(name = 'lacA', loc = 'cytosk', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Observable('obs_prot_lacZ_cyt', prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Observable('obs_prot_lacZ_imem', prot(name = 'lacZ', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Observable('obs_prot_lacZ_per', prot(name = 'lacZ', loc = 'per', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Observable('obs_prot_lacZ_mem', prot(name = 'lacZ', loc = 'mem', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Observable('obs_prot_lacZ_omem', prot(name = 'lacZ', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Observable('obs_prot_lacZ_ex', prot(name = 'lacZ', loc = 'ex', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Observable('obs_prot_lacZ_bnuc', prot(name = 'lacZ', loc = 'bnuc', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Observable('obs_prot_lacZ_wall', prot(name = 'lacZ', loc = 'wall', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Observable('obs_prot_lacZ_cproj', prot(name = 'lacZ', loc = 'cproj', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Observable('obs_prot_lacZ_cytosk', prot(name = 'lacZ', loc = 'cytosk', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Initial(prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter('t0_prot_lacA_cyt', 0))
Initial(prot(name = 'lacA', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter('t0_prot_lacA_imem', 0))
Initial(prot(name = 'lacA', loc = 'per', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter('t0_prot_lacA_per', 0))
Initial(prot(name = 'lacA', loc = 'mem', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter('t0_prot_lacA_mem', 0))
Initial(prot(name = 'lacA', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter('t0_prot_lacA_omem', 0))
Initial(prot(name = 'lacA', loc = 'ex', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter('t0_prot_lacA_ex', 0))
Initial(prot(name = 'lacA', loc = 'bnuc', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter('t0_prot_lacA_bnuc', 0))
Initial(prot(name = 'lacA', loc = 'wall', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter('t0_prot_lacA_wall', 0))
Initial(prot(name = 'lacA', loc = 'cproj', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter('t0_prot_lacA_cproj', 0))
Initial(prot(name = 'lacA', loc = 'cytosk', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter('t0_prot_lacA_cytosk', 0))
Initial(prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter('t0_prot_lacZ_cyt', 0))
Initial(prot(name = 'lacZ', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter('t0_prot_lacZ_imem', 0))
Initial(prot(name = 'lacZ', loc = 'per', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter('t0_prot_lacZ_per', 0))
Initial(prot(name = 'lacZ', loc = 'mem', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter('t0_prot_lacZ_mem', 0))
Initial(prot(name = 'lacZ', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter('t0_prot_lacZ_omem', 0))
Initial(prot(name = 'lacZ', loc = 'ex', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter('t0_prot_lacZ_ex', 0))
Initial(prot(name = 'lacZ', loc = 'bnuc', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter('t0_prot_lacZ_bnuc', 0))
Initial(prot(name = 'lacZ', loc = 'wall', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter('t0_prot_lacZ_wall', 0))
Initial(prot(name = 'lacZ', loc = 'cproj', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter('t0_prot_lacZ_cproj', 0))
Initial(prot(name = 'lacZ', loc = 'cytosk', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter('t0_prot_lacZ_cytosk', 0))
Initial(prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = None),
	Parameter('t0_cplx_lacAx3_cyt', 0))
Observable('obs_cplx_lacAx3_cyt',
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = None))
Initial(prot(name = 'lacA', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacA', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = 2, dw = None),
	Parameter('t0_cplx_lacAx3_imem', 0))
Observable('obs_cplx_lacAx3_imem',
	prot(name = 'lacA', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacA', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = 2, dw = None))
Initial(prot(name = 'lacA', loc = 'per', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'per', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacA', loc = 'per', dna = None, met = None, prot = None, rna = None, up = 2, dw = None),
	Parameter('t0_cplx_lacAx3_per', 0))
Observable('obs_cplx_lacAx3_per',
	prot(name = 'lacA', loc = 'per', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'per', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacA', loc = 'per', dna = None, met = None, prot = None, rna = None, up = 2, dw = None))
Initial(prot(name = 'lacA', loc = 'mem', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'mem', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacA', loc = 'mem', dna = None, met = None, prot = None, rna = None, up = 2, dw = None),
	Parameter('t0_cplx_lacAx3_mem', 0))
Observable('obs_cplx_lacAx3_mem',
	prot(name = 'lacA', loc = 'mem', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'mem', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacA', loc = 'mem', dna = None, met = None, prot = None, rna = None, up = 2, dw = None))
Initial(prot(name = 'lacA', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacA', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = 2, dw = None),
	Parameter('t0_cplx_lacAx3_omem', 0))
Observable('obs_cplx_lacAx3_omem',
	prot(name = 'lacA', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacA', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = 2, dw = None))
Initial(prot(name = 'lacA', loc = 'ex', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'ex', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacA', loc = 'ex', dna = None, met = None, prot = None, rna = None, up = 2, dw = None),
	Parameter('t0_cplx_lacAx3_ex', 0))
Observable('obs_cplx_lacAx3_ex',
	prot(name = 'lacA', loc = 'ex', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'ex', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacA', loc = 'ex', dna = None, met = None, prot = None, rna = None, up = 2, dw = None))
Initial(prot(name = 'lacA', loc = 'bnuc', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'bnuc', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacA', loc = 'bnuc', dna = None, met = None, prot = None, rna = None, up = 2, dw = None),
	Parameter('t0_cplx_lacAx3_bnuc', 0))
Observable('obs_cplx_lacAx3_bnuc',
	prot(name = 'lacA', loc = 'bnuc', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'bnuc', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacA', loc = 'bnuc', dna = None, met = None, prot = None, rna = None, up = 2, dw = None))
Initial(prot(name = 'lacA', loc = 'wall', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'wall', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacA', loc = 'wall', dna = None, met = None, prot = None, rna = None, up = 2, dw = None),
	Parameter('t0_cplx_lacAx3_wall', 0))
Observable('obs_cplx_lacAx3_wall',
	prot(name = 'lacA', loc = 'wall', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'wall', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacA', loc = 'wall', dna = None, met = None, prot = None, rna = None, up = 2, dw = None))
Initial(prot(name = 'lacA', loc = 'cproj', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'cproj', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacA', loc = 'cproj', dna = None, met = None, prot = None, rna = None, up = 2, dw = None),
	Parameter('t0_cplx_lacAx3_cproj', 0))
Observable('obs_cplx_lacAx3_cproj',
	prot(name = 'lacA', loc = 'cproj', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'cproj', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacA', loc = 'cproj', dna = None, met = None, prot = None, rna = None, up = 2, dw = None))
Initial(prot(name = 'lacA', loc = 'cytosk', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'cytosk', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacA', loc = 'cytosk', dna = None, met = None, prot = None, rna = None, up = 2, dw = None),
	Parameter('t0_cplx_lacAx3_cytosk', 0))
Observable('obs_cplx_lacAx3_cytosk',
	prot(name = 'lacA', loc = 'cytosk', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'cytosk', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacA', loc = 'cytosk', dna = None, met = None, prot = None, rna = None, up = 2, dw = None))
Initial(prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = None),
	Parameter('t0_cplx_lacAx2_cyt', 0))
Observable('obs_cplx_lacAx2_cyt',
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = None))
Initial(prot(name = 'lacA', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = 1, dw = None),
	Parameter('t0_cplx_lacAx2_imem', 0))
Observable('obs_cplx_lacAx2_imem',
	prot(name = 'lacA', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = 1, dw = None))
Initial(prot(name = 'lacA', loc = 'per', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'per', dna = None, met = None, prot = None, rna = None, up = 1, dw = None),
	Parameter('t0_cplx_lacAx2_per', 0))
Observable('obs_cplx_lacAx2_per',
	prot(name = 'lacA', loc = 'per', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'per', dna = None, met = None, prot = None, rna = None, up = 1, dw = None))
Initial(prot(name = 'lacA', loc = 'mem', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'mem', dna = None, met = None, prot = None, rna = None, up = 1, dw = None),
	Parameter('t0_cplx_lacAx2_mem', 0))
Observable('obs_cplx_lacAx2_mem',
	prot(name = 'lacA', loc = 'mem', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'mem', dna = None, met = None, prot = None, rna = None, up = 1, dw = None))
Initial(prot(name = 'lacA', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = 1, dw = None),
	Parameter('t0_cplx_lacAx2_omem', 0))
Observable('obs_cplx_lacAx2_omem',
	prot(name = 'lacA', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = 1, dw = None))
Initial(prot(name = 'lacA', loc = 'ex', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'ex', dna = None, met = None, prot = None, rna = None, up = 1, dw = None),
	Parameter('t0_cplx_lacAx2_ex', 0))
Observable('obs_cplx_lacAx2_ex',
	prot(name = 'lacA', loc = 'ex', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'ex', dna = None, met = None, prot = None, rna = None, up = 1, dw = None))
Initial(prot(name = 'lacA', loc = 'bnuc', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'bnuc', dna = None, met = None, prot = None, rna = None, up = 1, dw = None),
	Parameter('t0_cplx_lacAx2_bnuc', 0))
Observable('obs_cplx_lacAx2_bnuc',
	prot(name = 'lacA', loc = 'bnuc', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'bnuc', dna = None, met = None, prot = None, rna = None, up = 1, dw = None))
Initial(prot(name = 'lacA', loc = 'wall', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'wall', dna = None, met = None, prot = None, rna = None, up = 1, dw = None),
	Parameter('t0_cplx_lacAx2_wall', 0))
Observable('obs_cplx_lacAx2_wall',
	prot(name = 'lacA', loc = 'wall', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'wall', dna = None, met = None, prot = None, rna = None, up = 1, dw = None))
Initial(prot(name = 'lacA', loc = 'cproj', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'cproj', dna = None, met = None, prot = None, rna = None, up = 1, dw = None),
	Parameter('t0_cplx_lacAx2_cproj', 0))
Observable('obs_cplx_lacAx2_cproj',
	prot(name = 'lacA', loc = 'cproj', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'cproj', dna = None, met = None, prot = None, rna = None, up = 1, dw = None))
Initial(prot(name = 'lacA', loc = 'cytosk', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'cytosk', dna = None, met = None, prot = None, rna = None, up = 1, dw = None),
	Parameter('t0_cplx_lacAx2_cytosk', 0))
Observable('obs_cplx_lacAx2_cytosk',
	prot(name = 'lacA', loc = 'cytosk', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'cytosk', dna = None, met = None, prot = None, rna = None, up = 1, dw = None))
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
Initial(prot(name = 'lacZ', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacZ', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	prot(name = 'lacZ', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = 3, dw = None),
	Parameter('t0_cplx_lacZx4_imem', 0))
Observable('obs_cplx_lacZx4_imem',
	prot(name = 'lacZ', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacZ', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	prot(name = 'lacZ', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = 3, dw = None))
Initial(prot(name = 'lacZ', loc = 'per', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'per', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacZ', loc = 'per', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	prot(name = 'lacZ', loc = 'per', dna = None, met = None, prot = None, rna = None, up = 3, dw = None),
	Parameter('t0_cplx_lacZx4_per', 0))
Observable('obs_cplx_lacZx4_per',
	prot(name = 'lacZ', loc = 'per', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'per', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacZ', loc = 'per', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	prot(name = 'lacZ', loc = 'per', dna = None, met = None, prot = None, rna = None, up = 3, dw = None))
Initial(prot(name = 'lacZ', loc = 'mem', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'mem', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacZ', loc = 'mem', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	prot(name = 'lacZ', loc = 'mem', dna = None, met = None, prot = None, rna = None, up = 3, dw = None),
	Parameter('t0_cplx_lacZx4_mem', 0))
Observable('obs_cplx_lacZx4_mem',
	prot(name = 'lacZ', loc = 'mem', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'mem', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacZ', loc = 'mem', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	prot(name = 'lacZ', loc = 'mem', dna = None, met = None, prot = None, rna = None, up = 3, dw = None))
Initial(prot(name = 'lacZ', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacZ', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	prot(name = 'lacZ', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = 3, dw = None),
	Parameter('t0_cplx_lacZx4_omem', 0))
Observable('obs_cplx_lacZx4_omem',
	prot(name = 'lacZ', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacZ', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	prot(name = 'lacZ', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = 3, dw = None))
Initial(prot(name = 'lacZ', loc = 'ex', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'ex', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacZ', loc = 'ex', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	prot(name = 'lacZ', loc = 'ex', dna = None, met = None, prot = None, rna = None, up = 3, dw = None),
	Parameter('t0_cplx_lacZx4_ex', 0))
Observable('obs_cplx_lacZx4_ex',
	prot(name = 'lacZ', loc = 'ex', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'ex', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacZ', loc = 'ex', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	prot(name = 'lacZ', loc = 'ex', dna = None, met = None, prot = None, rna = None, up = 3, dw = None))
Initial(prot(name = 'lacZ', loc = 'bnuc', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'bnuc', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacZ', loc = 'bnuc', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	prot(name = 'lacZ', loc = 'bnuc', dna = None, met = None, prot = None, rna = None, up = 3, dw = None),
	Parameter('t0_cplx_lacZx4_bnuc', 0))
Observable('obs_cplx_lacZx4_bnuc',
	prot(name = 'lacZ', loc = 'bnuc', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'bnuc', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacZ', loc = 'bnuc', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	prot(name = 'lacZ', loc = 'bnuc', dna = None, met = None, prot = None, rna = None, up = 3, dw = None))
Initial(prot(name = 'lacZ', loc = 'wall', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'wall', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacZ', loc = 'wall', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	prot(name = 'lacZ', loc = 'wall', dna = None, met = None, prot = None, rna = None, up = 3, dw = None),
	Parameter('t0_cplx_lacZx4_wall', 0))
Observable('obs_cplx_lacZx4_wall',
	prot(name = 'lacZ', loc = 'wall', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'wall', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacZ', loc = 'wall', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	prot(name = 'lacZ', loc = 'wall', dna = None, met = None, prot = None, rna = None, up = 3, dw = None))
Initial(prot(name = 'lacZ', loc = 'cproj', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'cproj', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacZ', loc = 'cproj', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	prot(name = 'lacZ', loc = 'cproj', dna = None, met = None, prot = None, rna = None, up = 3, dw = None),
	Parameter('t0_cplx_lacZx4_cproj', 0))
Observable('obs_cplx_lacZx4_cproj',
	prot(name = 'lacZ', loc = 'cproj', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'cproj', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacZ', loc = 'cproj', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	prot(name = 'lacZ', loc = 'cproj', dna = None, met = None, prot = None, rna = None, up = 3, dw = None))
Initial(prot(name = 'lacZ', loc = 'cytosk', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'cytosk', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacZ', loc = 'cytosk', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	prot(name = 'lacZ', loc = 'cytosk', dna = None, met = None, prot = None, rna = None, up = 3, dw = None),
	Parameter('t0_cplx_lacZx4_cytosk', 0))
Observable('obs_cplx_lacZx4_cytosk',
	prot(name = 'lacZ', loc = 'cytosk', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'cytosk', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacZ', loc = 'cytosk', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	prot(name = 'lacZ', loc = 'cytosk', dna = None, met = None, prot = None, rna = None, up = 3, dw = None))
Initial(prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = None),
	Parameter('t0_cplx_lacZx2_cyt', 0))
Observable('obs_cplx_lacZx2_cyt',
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = None))
Initial(prot(name = 'lacZ', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = 1, dw = None),
	Parameter('t0_cplx_lacZx2_imem', 0))
Observable('obs_cplx_lacZx2_imem',
	prot(name = 'lacZ', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = 1, dw = None))
Initial(prot(name = 'lacZ', loc = 'per', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'per', dna = None, met = None, prot = None, rna = None, up = 1, dw = None),
	Parameter('t0_cplx_lacZx2_per', 0))
Observable('obs_cplx_lacZx2_per',
	prot(name = 'lacZ', loc = 'per', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'per', dna = None, met = None, prot = None, rna = None, up = 1, dw = None))
Initial(prot(name = 'lacZ', loc = 'mem', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'mem', dna = None, met = None, prot = None, rna = None, up = 1, dw = None),
	Parameter('t0_cplx_lacZx2_mem', 0))
Observable('obs_cplx_lacZx2_mem',
	prot(name = 'lacZ', loc = 'mem', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'mem', dna = None, met = None, prot = None, rna = None, up = 1, dw = None))
Initial(prot(name = 'lacZ', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = 1, dw = None),
	Parameter('t0_cplx_lacZx2_omem', 0))
Observable('obs_cplx_lacZx2_omem',
	prot(name = 'lacZ', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = 1, dw = None))
Initial(prot(name = 'lacZ', loc = 'ex', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'ex', dna = None, met = None, prot = None, rna = None, up = 1, dw = None),
	Parameter('t0_cplx_lacZx2_ex', 0))
Observable('obs_cplx_lacZx2_ex',
	prot(name = 'lacZ', loc = 'ex', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'ex', dna = None, met = None, prot = None, rna = None, up = 1, dw = None))
Initial(prot(name = 'lacZ', loc = 'bnuc', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'bnuc', dna = None, met = None, prot = None, rna = None, up = 1, dw = None),
	Parameter('t0_cplx_lacZx2_bnuc', 0))
Observable('obs_cplx_lacZx2_bnuc',
	prot(name = 'lacZ', loc = 'bnuc', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'bnuc', dna = None, met = None, prot = None, rna = None, up = 1, dw = None))
Initial(prot(name = 'lacZ', loc = 'wall', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'wall', dna = None, met = None, prot = None, rna = None, up = 1, dw = None),
	Parameter('t0_cplx_lacZx2_wall', 0))
Observable('obs_cplx_lacZx2_wall',
	prot(name = 'lacZ', loc = 'wall', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'wall', dna = None, met = None, prot = None, rna = None, up = 1, dw = None))
Initial(prot(name = 'lacZ', loc = 'cproj', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'cproj', dna = None, met = None, prot = None, rna = None, up = 1, dw = None),
	Parameter('t0_cplx_lacZx2_cproj', 0))
Observable('obs_cplx_lacZx2_cproj',
	prot(name = 'lacZ', loc = 'cproj', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'cproj', dna = None, met = None, prot = None, rna = None, up = 1, dw = None))
Initial(prot(name = 'lacZ', loc = 'cytosk', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'cytosk', dna = None, met = None, prot = None, rna = None, up = 1, dw = None),
	Parameter('t0_cplx_lacZx2_cytosk', 0))
Observable('obs_cplx_lacZx2_cytosk',
	prot(name = 'lacZ', loc = 'cytosk', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'cytosk', dna = None, met = None, prot = None, rna = None, up = 1, dw = None))
Rule('PhysicalInteractionRule_1',
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None) | 
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = None),
	Parameter('fwd_PhysicalInteractionRule_1', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_1', 1.000000))
Rule('PhysicalInteractionRule_2',
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = None) | 
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = None),
	Parameter('fwd_PhysicalInteractionRule_2', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_2', 1.000000))
Rule('PhysicalInteractionRule_3',
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None) | 
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = None),
	Parameter('fwd_PhysicalInteractionRule_3', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_3', 1.000000))
Rule('PhysicalInteractionRule_4',
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 2) %
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = None) +
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = None) | 
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = None),
	Parameter('fwd_PhysicalInteractionRule_4', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_4', 1.000000))
