from pysb import *
Model()

Monomer('met',
	['name', 'loc', 'dna', 'met', 'prot', 'rna'],
	{ 'name' : [ 'ALLOLACTOSE', 'CAMP', 'alpha_L_arabinopyranose' ], 
	'loc' : ['cyt', 'cytosk', 'ex', 'mem', 'per', 'wall', 'bnuc', 'cproj', 'imem', 'omem']})
Monomer('prot',
	['name', 'loc', 'dna', 'met', 'prot', 'rna', 'up', 'dw'],
	{ 'name' : [ 'araC', 'crp', 'lacA', 'lacI', 'lacZ' ], 
	'loc' : ['cyt', 'cytosk', 'ex', 'mem', 'per', 'wall', 'bnuc', 'cproj', 'imem', 'omem']})
Monomer('dna',
	['name', 'type', 'loc', 'dna', 'met', 'prot', 'rna', 'up', 'dw'],
	{ 'name' : [ 'araB_109_125', 'araB_130_146', 'araB_267_283', 'araB_35_51', 'araB_56_72', 'araB_83_104', 'araC_267_283', 'araC_35_51', 'araC_56_72', 'araE_36_52', 'araE_57_73', 'araF_137_153', 'araF_158_174', 'araF_62_78', 'araF_83_99' ],
	'type' : ['BS'],
	'loc' : ['cyt']})
Observable('obs_met_ALLOLACTOSE_cyt', met(name = 'ALLOLACTOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None))
Initial(met(name = 'ALLOLACTOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_ALLOLACTOSE_cyt', 0))
Observable('obs_met_CAMP_cyt', met(name = 'CAMP', loc = 'cyt', dna = None, met = None, prot = None, rna = None))
Initial(met(name = 'CAMP', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_CAMP_cyt', 0))
Observable('obs_met_alpha_L_arabinopyranose_cyt', met(name = 'alpha_L_arabinopyranose', loc = 'cyt', dna = None, met = None, prot = None, rna = None))
Initial(met(name = 'alpha_L_arabinopyranose', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_alpha_L_arabinopyranose_cyt', 0))
Observable('obs_prot_araC_cyt', prot(name = 'araC', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Initial(prot(name = 'araC', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter('t0_prot_araC_cyt', 0))
Observable('obs_prot_crp_cyt', prot(name = 'crp', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Initial(prot(name = 'crp', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter('t0_prot_crp_cyt', 0))
Observable('obs_prot_lacA_cyt', prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Initial(prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter('t0_prot_lacA_cyt', 0))
Observable('obs_prot_lacI_cyt', prot(name = 'lacI', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Initial(prot(name = 'lacI', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter('t0_prot_lacI_cyt', 0))
Observable('obs_prot_lacZ_cyt', prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Initial(prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter('t0_prot_lacZ_cyt', 0))
Initial(prot(name = 'araC', loc = 'cyt', dna = None, met = 2, prot = None, rna = None, up = None, dw = 1) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', dna = None, met = None, prot = 3, rna = None) %
	prot(name = 'araC', loc = 'cyt', dna = None, met = 3, prot = None, rna = None, up = 1, dw = None) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', dna = None, met = None, prot = 2, rna = None),
	Parameter('t0_cplx_araCx2_alpha_L_arabinopyranosex2_cyt', 0))
Observable('obs_cplx_araCx2_alpha_L_arabinopyranosex2_cyt',
	prot(name = 'araC', loc = 'cyt', dna = None, met = 2, prot = None, rna = None, up = None, dw = 1) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', dna = None, met = None, prot = 3, rna = None) %
	prot(name = 'araC', loc = 'cyt', dna = None, met = 3, prot = None, rna = None, up = 1, dw = None) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', dna = None, met = None, prot = 2, rna = None))
Initial(prot(name = 'araC', loc = 'cyt', dna = None, met = 1, prot = None, rna = None, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', dna = None, met = None, prot = 1, rna = None),
	Parameter('t0_cplx_araCx1_alpha_L_arabinopyranosex1_cyt', 0))
Observable('obs_cplx_araCx1_alpha_L_arabinopyranosex1_cyt',
	prot(name = 'araC', loc = 'cyt', dna = None, met = 1, prot = None, rna = None, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', dna = None, met = None, prot = 1, rna = None))
Initial(prot(name = 'araC', loc = 'cyt', dna = None, met = 2, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'araC', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = None) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', dna = None, met = None, prot = 2, rna = None),
	Parameter('t0_cplx_araCx2_alpha_L_arabinopyranosex1_cyt', 0))
Observable('obs_cplx_araCx2_alpha_L_arabinopyranosex1_cyt',
	prot(name = 'araC', loc = 'cyt', dna = None, met = 2, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'araC', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = None) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', dna = None, met = None, prot = 2, rna = None))
Initial(prot(name = 'crp', loc = 'cyt', dna = None, met = 2, prot = None, rna = None, up = None, dw = 1) %
	met(name = 'CAMP', loc = 'cyt', dna = None, met = None, prot = 3, rna = None) %
	prot(name = 'crp', loc = 'cyt', dna = None, met = 3, prot = None, rna = None, up = 1, dw = None) %
	met(name = 'CAMP', loc = 'cyt', dna = None, met = None, prot = 2, rna = None),
	Parameter('t0_cplx_crpx2_CAMPx2_cyt', 0))
Observable('obs_cplx_crpx2_CAMPx2_cyt',
	prot(name = 'crp', loc = 'cyt', dna = None, met = 2, prot = None, rna = None, up = None, dw = 1) %
	met(name = 'CAMP', loc = 'cyt', dna = None, met = None, prot = 3, rna = None) %
	prot(name = 'crp', loc = 'cyt', dna = None, met = 3, prot = None, rna = None, up = 1, dw = None) %
	met(name = 'CAMP', loc = 'cyt', dna = None, met = None, prot = 2, rna = None))
Initial(prot(name = 'crp', loc = 'cyt', dna = None, met = 2, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'crp', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = None) %
	met(name = 'CAMP', loc = 'cyt', dna = None, met = None, prot = 2, rna = None),
	Parameter('t0_cplx_crpx2_CAMPx1_cyt', 0))
Observable('obs_cplx_crpx2_CAMPx1_cyt',
	prot(name = 'crp', loc = 'cyt', dna = None, met = 2, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'crp', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = None) %
	met(name = 'CAMP', loc = 'cyt', dna = None, met = None, prot = 2, rna = None))
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
Initial(prot(name = 'lacI', loc = 'cyt', dna = None, met = 2, prot = None, rna = None, up = None, dw = 1) %
	met(name = 'ALLOLACTOSE', loc = 'cyt', dna = None, met = None, prot = 3, rna = None) %
	prot(name = 'lacI', loc = 'cyt', dna = None, met = 3, prot = None, rna = None, up = 1, dw = None) %
	met(name = 'ALLOLACTOSE', loc = 'cyt', dna = None, met = None, prot = 2, rna = None),
	Parameter('t0_cplx_lacIx2_ALLOLACTOSEx2_cyt', 0))
Observable('obs_cplx_lacIx2_ALLOLACTOSEx2_cyt',
	prot(name = 'lacI', loc = 'cyt', dna = None, met = 2, prot = None, rna = None, up = None, dw = 1) %
	met(name = 'ALLOLACTOSE', loc = 'cyt', dna = None, met = None, prot = 3, rna = None) %
	prot(name = 'lacI', loc = 'cyt', dna = None, met = 3, prot = None, rna = None, up = 1, dw = None) %
	met(name = 'ALLOLACTOSE', loc = 'cyt', dna = None, met = None, prot = 2, rna = None))
Initial(prot(name = 'lacI', loc = 'cyt', dna = None, met = 2, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacI', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = None) %
	met(name = 'ALLOLACTOSE', loc = 'cyt', dna = None, met = None, prot = 2, rna = None),
	Parameter('t0_cplx_lacIx2_ALLOLACTOSEx1_cyt', 0))
Observable('obs_cplx_lacIx2_ALLOLACTOSEx1_cyt',
	prot(name = 'lacI', loc = 'cyt', dna = None, met = 2, prot = None, rna = None, up = None, dw = 1) %
	prot(name = 'lacI', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = None) %
	met(name = 'ALLOLACTOSE', loc = 'cyt', dna = None, met = None, prot = 2, rna = None))
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
Rule('PhysicalInteractionRule_01',
	prot(name = 'crp', loc = 'cyt', dna = None, met = 2, up = None, dw = 1) %
	met(name = 'CAMP', loc = 'cyt', prot = 3) %
	prot(name = 'crp', loc = 'cyt', dna = None, met = 3, up = 1, dw = None) %
	met(name = 'CAMP', loc = 'cyt', prot = 2) +
	dna(name = 'araB_83_104', type = 'BS', loc = 'cyt', prot = None, up = WILD, dw = WILD) | 
	prot(name = 'crp', loc = 'cyt', dna = None, met = 2, up = None, dw = 1) %
	met(name = 'CAMP', loc = 'cyt', prot = 3) %
	prot(name = 'crp', loc = 'cyt', dna = 4, met = 3, up = 1, dw = None) %
	met(name = 'CAMP', loc = 'cyt', prot = 2) %
	dna(name = 'araB_83_104', type = 'BS', prot = 4, up = WILD, dw = WILD),
	Parameter('fwd_PhysicalInteractionRule_01', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_01', 1.000000))
Rule('PhysicalInteractionRule_02',
	prot(name = 'araC', loc = 'cyt', dna = None, met = None, up = None, dw = None) +
	dna(name = 'araB_35_51', type = 'BS', loc = 'cyt', prot = None, up = WILD, dw = WILD) | 
	prot(name = 'araC', loc = 'cyt', dna = 1, met = None, up = None, dw = None) %
	dna(name = 'araB_35_51', type = 'BS', prot = 1, up = WILD, dw = WILD),
	Parameter('fwd_PhysicalInteractionRule_02', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_02', 1.000000))
Rule('PhysicalInteractionRule_03',
	prot(name = 'araC', loc = 'cyt', dna = None, met = None, up = None, dw = None) +
	dna(name = 'araB_56_72', type = 'BS', loc = 'cyt', prot = None, up = WILD, dw = WILD) | 
	prot(name = 'araC', loc = 'cyt', dna = 1, met = None, up = None, dw = None) %
	dna(name = 'araB_56_72', type = 'BS', prot = 1, up = WILD, dw = WILD),
	Parameter('fwd_PhysicalInteractionRule_03', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_03', 1.000000))
Rule('PhysicalInteractionRule_04',
	prot(name = 'araC', loc = 'cyt', dna = None, met = None, up = None, dw = None) +
	dna(name = 'araB_109_125', type = 'BS', loc = 'cyt', prot = None, up = WILD, dw = WILD) | 
	prot(name = 'araC', loc = 'cyt', dna = 1, met = None, up = None, dw = None) %
	dna(name = 'araB_109_125', type = 'BS', prot = 1, up = WILD, dw = WILD),
	Parameter('fwd_PhysicalInteractionRule_04', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_04', 1.000000))
Rule('PhysicalInteractionRule_05',
	prot(name = 'araC', loc = 'cyt', dna = None, met = None, up = None, dw = None) +
	dna(name = 'araB_130_146', type = 'BS', loc = 'cyt', prot = None, up = WILD, dw = WILD) | 
	prot(name = 'araC', loc = 'cyt', dna = 1, met = None, up = None, dw = None) %
	dna(name = 'araB_130_146', type = 'BS', prot = 1, up = WILD, dw = WILD),
	Parameter('fwd_PhysicalInteractionRule_05', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_05', 1.000000))
Rule('PhysicalInteractionRule_06',
	prot(name = 'araC', loc = 'cyt', dna = None, met = None, up = None, dw = None) +
	dna(name = 'araB_267_283', type = 'BS', loc = 'cyt', prot = None, up = WILD, dw = WILD) | 
	prot(name = 'araC', loc = 'cyt', dna = 1, met = None, up = None, dw = None) %
	dna(name = 'araB_267_283', type = 'BS', prot = 1, up = WILD, dw = WILD),
	Parameter('fwd_PhysicalInteractionRule_06', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_06', 1.000000))
Rule('PhysicalInteractionRule_07',
	prot(name = 'araC', loc = 'cyt', dna = 1, met = None, up = None, dw = None) %
	dna(name = 'araB_56_72', type = 'BS', loc = 'cyt', prot = 1, up = WILD, dw = WILD) +
	prot(name = 'araC', loc = 'cyt', dna = 2, met = None, up = None, dw = None) %
	dna(name = 'araB_267_283', type = 'BS', loc = 'cyt', prot = 2, up = WILD, dw = WILD) | 
	prot(name = 'araC', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	dna(name = 'araB_56_72', type = 'BS', prot = 2, up = WILD, dw = WILD) %
	prot(name = 'araC', loc = 'cyt', dna = 2, met = None, up = 1, dw = None) %
	dna(name = 'araB_267_283', type = 'BS', prot = None, up = WILD, dw = WILD),
	Parameter('fwd_PhysicalInteractionRule_07', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_07', 1.000000))
Rule('PhysicalInteractionRule_08',
	prot(name = 'araC', loc = 'cyt', dna = None, met = 1, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = 1) +
	dna(name = 'araC_35_51', type = 'BS', loc = 'cyt', prot = None, up = WILD, dw = WILD) | 
	prot(name = 'araC', loc = 'cyt', dna = 2, met = 1, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = 1) %
	dna(name = 'araC_35_51', type = 'BS', prot = 2, up = WILD, dw = WILD),
	Parameter('fwd_PhysicalInteractionRule_08', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_08', 1.000000))
Rule('PhysicalInteractionRule_09',
	prot(name = 'araC', loc = 'cyt', dna = 1, met = None, up = None, dw = None) %
	dna(name = 'araC_56_72', type = 'BS', loc = 'cyt', prot = 1, up = WILD, dw = WILD) +
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = None) | 
	prot(name = 'araC', loc = 'cyt', dna = 2, met = 1, up = None, dw = None) %
	dna(name = 'araC_56_72', type = 'BS', prot = 2, up = WILD, dw = WILD) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = 1),
	Parameter('fwd_PhysicalInteractionRule_09', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_09', 1.000000))
Rule('PhysicalInteractionRule_10',
	prot(name = 'araC', loc = 'cyt', dna = 1, met = None, up = None, dw = None) %
	dna(name = 'araC_267_283', type = 'BS', loc = 'cyt', prot = 1, up = WILD, dw = WILD) +
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = None) | 
	prot(name = 'araC', loc = 'cyt', dna = 2, met = 1, up = None, dw = None) %
	dna(name = 'araC_267_283', type = 'BS', prot = 2, up = WILD, dw = WILD) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = 1),
	Parameter('fwd_PhysicalInteractionRule_10', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_10', 1.000000))
Rule('PhysicalInteractionRule_11',
	prot(name = 'araC', loc = 'cyt', dna = 2, met = 1, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = 1) %
	dna(name = 'araB_56_72', type = 'BS', loc = 'cyt', prot = 2, up = WILD, dw = WILD) +
	prot(name = 'araC', loc = 'cyt', dna = 4, met = 3, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = 3) %
	dna(name = 'araB_35_51', type = 'BS', loc = 'cyt', prot = 4, up = WILD, dw = WILD) | 
	prot(name = 'araC', loc = 'cyt', dna = None, met = 2, up = None, dw = 1) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = 3) %
	dna(name = 'araB_56_72', type = 'BS', prot = 4, up = WILD, dw = WILD) %
	prot(name = 'araC', loc = 'cyt', dna = 4, met = 3, up = 1, dw = None) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = 2) %
	dna(name = 'araB_35_51', type = 'BS', prot = None, up = WILD, dw = WILD),
	Parameter('fwd_PhysicalInteractionRule_11', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_11', 1.000000))
Rule('PhysicalInteractionRule_12',
	prot(name = 'araC', loc = 'cyt', dna = None, met = 1, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = 1) +
	dna(name = 'araF_158_174', type = 'BS', loc = 'cyt', prot = None, up = WILD, dw = WILD) | 
	prot(name = 'araC', loc = 'cyt', dna = 2, met = 1, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = 1) %
	dna(name = 'araF_158_174', type = 'BS', prot = 2, up = WILD, dw = WILD),
	Parameter('fwd_PhysicalInteractionRule_12', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_12', 1.000000))
Rule('PhysicalInteractionRule_13',
	prot(name = 'araC', loc = 'cyt', dna = None, met = 1, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = 1) +
	dna(name = 'araF_137_153', type = 'BS', loc = 'cyt', prot = None, up = WILD, dw = WILD) | 
	prot(name = 'araC', loc = 'cyt', dna = 2, met = 1, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = 1) %
	dna(name = 'araF_137_153', type = 'BS', prot = 2, up = WILD, dw = WILD),
	Parameter('fwd_PhysicalInteractionRule_13', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_13', 1.000000))
Rule('PhysicalInteractionRule_14',
	prot(name = 'araC', loc = 'cyt', dna = None, met = 1, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = 1) +
	dna(name = 'araF_83_99', type = 'BS', loc = 'cyt', prot = None, up = WILD, dw = WILD) | 
	prot(name = 'araC', loc = 'cyt', dna = 2, met = 1, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = 1) %
	dna(name = 'araF_83_99', type = 'BS', prot = 2, up = WILD, dw = WILD),
	Parameter('fwd_PhysicalInteractionRule_14', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_14', 1.000000))
Rule('PhysicalInteractionRule_15',
	prot(name = 'araC', loc = 'cyt', dna = None, met = 1, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = 1) +
	dna(name = 'araF_62_78', type = 'BS', loc = 'cyt', prot = None, up = WILD, dw = WILD) | 
	prot(name = 'araC', loc = 'cyt', dna = 2, met = 1, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = 1) %
	dna(name = 'araF_62_78', type = 'BS', prot = 2, up = WILD, dw = WILD),
	Parameter('fwd_PhysicalInteractionRule_15', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_15', 1.000000))
Rule('PhysicalInteractionRule_16',
	prot(name = 'araC', loc = 'cyt', dna = 2, met = 1, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = 1) %
	dna(name = 'araF_83_99', type = 'BS', loc = 'cyt', prot = 2, up = WILD, dw = WILD) +
	prot(name = 'araC', loc = 'cyt', dna = 4, met = 3, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = 3) %
	dna(name = 'araF_62_78', type = 'BS', loc = 'cyt', prot = 4, up = WILD, dw = WILD) | 
	prot(name = 'araC', loc = 'cyt', dna = None, met = 2, up = None, dw = 1) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = 3) %
	dna(name = 'araF_83_99', type = 'BS', prot = 4, up = WILD, dw = WILD) %
	prot(name = 'araC', loc = 'cyt', dna = 4, met = 3, up = 1, dw = None) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = 2) %
	dna(name = 'araF_62_78', type = 'BS', prot = None, up = WILD, dw = WILD),
	Parameter('fwd_PhysicalInteractionRule_16', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_16', 1.000000))
Rule('PhysicalInteractionRule_17',
	prot(name = 'araC', loc = 'cyt', dna = None, met = 1, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = 1) +
	dna(name = 'araE_57_73', type = 'BS', loc = 'cyt', prot = None, up = WILD, dw = WILD) | 
	prot(name = 'araC', loc = 'cyt', dna = 2, met = 1, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = 1) %
	dna(name = 'araE_57_73', type = 'BS', prot = 2, up = WILD, dw = WILD),
	Parameter('fwd_PhysicalInteractionRule_17', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_17', 1.000000))
Rule('PhysicalInteractionRule_18',
	prot(name = 'araC', loc = 'cyt', dna = None, met = 1, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = 1) +
	dna(name = 'araE_36_52', type = 'BS', loc = 'cyt', prot = None, up = WILD, dw = WILD) | 
	prot(name = 'araC', loc = 'cyt', dna = 2, met = 1, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = 1) %
	dna(name = 'araE_36_52', type = 'BS', prot = 2, up = WILD, dw = WILD),
	Parameter('fwd_PhysicalInteractionRule_18', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_18', 1.000000))
Rule('PhysicalInteractionRule_19',
	prot(name = 'araC', loc = 'cyt', dna = 2, met = 1, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = 1) %
	dna(name = 'araE_57_73', type = 'BS', loc = 'cyt', prot = 2, up = WILD, dw = WILD) +
	prot(name = 'araC', loc = 'cyt', dna = 4, met = 3, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = 3) %
	dna(name = 'araE_36_52', type = 'BS', loc = 'cyt', prot = 4, up = WILD, dw = WILD) | 
	prot(name = 'araC', loc = 'cyt', dna = None, met = 2, up = None, dw = 1) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = 3) %
	dna(name = 'araE_57_73', type = 'BS', prot = 4, up = WILD, dw = WILD) %
	prot(name = 'araC', loc = 'cyt', dna = 4, met = 3, up = 1, dw = None) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = 2) %
	dna(name = 'araE_36_52', type = 'BS', prot = None, up = WILD, dw = WILD),
	Parameter('fwd_PhysicalInteractionRule_19', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_19', 1.000000))
Rule('PhysicalInteractionRule_20',
	prot(name = 'crp', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'crp', loc = 'cyt', dna = None, met = None, up = 1, dw = None) +
	met(name = 'CAMP', loc = 'cyt', prot = None) | 
	prot(name = 'crp', loc = 'cyt', dna = None, met = 2, up = None, dw = 1) %
	prot(name = 'crp', loc = 'cyt', dna = None, met = None, up = 1, dw = None) %
	met(name = 'CAMP', loc = 'cyt', prot = 2),
	Parameter('fwd_PhysicalInteractionRule_20', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_20', 1.000000))
Rule('PhysicalInteractionRule_21',
	prot(name = 'crp', loc = 'cyt', dna = None, met = 2, up = None, dw = 1) %
	met(name = 'CAMP', loc = 'cyt', prot = None) %
	prot(name = 'crp', loc = 'cyt', dna = None, met = 2, up = 1, dw = None) +
	met(name = 'CAMP', loc = 'cyt', prot = None) | 
	prot(name = 'crp', loc = 'cyt', dna = None, met = 2, up = None, dw = 1) %
	met(name = 'CAMP', loc = 'cyt', prot = 3) %
	prot(name = 'crp', loc = 'cyt', dna = None, met = 3, up = 1, dw = None) %
	met(name = 'CAMP', loc = 'cyt', prot = 2),
	Parameter('fwd_PhysicalInteractionRule_21', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_21', 1.000000))
Rule('PhysicalInteractionRule_22',
	prot(name = 'lacI', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'lacI', loc = 'cyt', dna = None, met = None, up = 1, dw = None) +
	met(name = 'ALLOLACTOSE', loc = 'cyt', prot = None) | 
	prot(name = 'lacI', loc = 'cyt', dna = None, met = 2, up = None, dw = 1) %
	prot(name = 'lacI', loc = 'cyt', dna = None, met = None, up = 1, dw = None) %
	met(name = 'ALLOLACTOSE', loc = 'cyt', prot = 2),
	Parameter('fwd_PhysicalInteractionRule_22', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_22', 1.000000))
Rule('PhysicalInteractionRule_23',
	prot(name = 'lacI', loc = 'cyt', dna = None, met = 2, up = None, dw = 1) %
	met(name = 'ALLOLACTOSE', loc = 'cyt', prot = None) %
	prot(name = 'lacI', loc = 'cyt', dna = None, met = 2, up = 1, dw = None) +
	met(name = 'ALLOLACTOSE', loc = 'cyt', prot = None) | 
	prot(name = 'lacI', loc = 'cyt', dna = None, met = 2, up = None, dw = 1) %
	met(name = 'ALLOLACTOSE', loc = 'cyt', prot = 3) %
	prot(name = 'lacI', loc = 'cyt', dna = None, met = 3, up = 1, dw = None) %
	met(name = 'ALLOLACTOSE', loc = 'cyt', prot = 2),
	Parameter('fwd_PhysicalInteractionRule_23', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_23', 1.000000))
Rule('PhysicalInteractionRule_24',
	prot(name = 'araC', loc = 'cyt', dna = None, met = None, up = None, dw = None) +
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = None) | 
	prot(name = 'araC', loc = 'cyt', dna = None, met = 1, up = None, dw = None) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = 1),
	Parameter('fwd_PhysicalInteractionRule_24', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_24', 1.000000))
Rule('PhysicalInteractionRule_25',
	prot(name = 'araC', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'araC', loc = 'cyt', dna = None, met = None, up = 1, dw = None) +
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = None) | 
	prot(name = 'araC', loc = 'cyt', dna = None, met = 2, up = None, dw = 1) %
	prot(name = 'araC', loc = 'cyt', dna = None, met = None, up = 1, dw = None) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = 2),
	Parameter('fwd_PhysicalInteractionRule_25', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_25', 1.000000))
Rule('PhysicalInteractionRule_26',
	prot(name = 'araC', loc = 'cyt', dna = None, met = 2, up = None, dw = 1) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = None) %
	prot(name = 'araC', loc = 'cyt', dna = None, met = 2, up = 1, dw = None) +
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = None) | 
	prot(name = 'araC', loc = 'cyt', dna = None, met = 2, up = None, dw = 1) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = 3) %
	prot(name = 'araC', loc = 'cyt', dna = None, met = 3, up = 1, dw = None) %
	met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = 2),
	Parameter('fwd_PhysicalInteractionRule_26', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_26', 1.000000))
Rule('PhysicalInteractionRule_27',
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, up = None, dw = None) +
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, up = None, dw = None) | 
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, up = 1, dw = None),
	Parameter('fwd_PhysicalInteractionRule_27', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_27', 0.000000))
Rule('PhysicalInteractionRule_28',
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, up = 1, dw = None) +
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, up = None, dw = 2) %
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, up = 2, dw = None) | 
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, up = 3, dw = None),
	Parameter('fwd_PhysicalInteractionRule_28', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_28', 0.000000))
Rule('PhysicalInteractionRule_29',
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, up = None, dw = None) +
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, up = None, dw = None) | 
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, up = 1, dw = None),
	Parameter('fwd_PhysicalInteractionRule_29', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_29', 0.000000))
Rule('PhysicalInteractionRule_30',
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, up = None, dw = None) +
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, up = 1, dw = None) | 
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, up = 2, dw = None),
	Parameter('fwd_PhysicalInteractionRule_30', 1.000000),
	Parameter('rvs_PhysicalInteractionRule_30', 0.000000))
