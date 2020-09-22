from pysb import *
Model()

Monomer('met',
	['name', 'loc', 'dna', 'met', 'prot', 'rna'],
	{ 'name' : [ 'ACETYL_COA', 'CO_A', 'CPD_3561', 'CPD_3785', 'CPD_3801', 'D_ARABINOSE', 'Fructofuranose', 'MELIBIOSE', 'PROTON', 'WATER', '_6_Acetyl_beta_D_Galactose', 'alpha_ALLOLACTOSE', 'alpha_GALACTOSE', 'alpha_glucose', 'alpha_lactose', 'beta_ALLOLACTOSE', 'beta_GALACTOSE', 'beta_glucose', 'beta_lactose' ],
	'loc' : ['cyt', 'cytosk', 'ex', 'mem', 'per', 'wall', 'bnuc', 'cproj', 'imem', 'omem']})
Monomer('prot',
	['name', 'loc', 'dna', 'met', 'prot', 'rna', 'up', 'dw'],
	{ 'name' : [ 'LACY_MONOMER', 'spontaneous' ],
	'loc' : ['cyt', 'cytosk', 'ex', 'mem', 'per', 'wall', 'bnuc', 'cproj', 'imem', 'omem']})
Monomer('cplx',
	['name', 'loc', 'dna', 'met', 'prot', 'rna', 'up', 'dw'],
	{ 'name' : [ 'BETAGALACTOSID_CPLX', 'GALACTOACETYLTRAN_CPLX' ],
	'loc' : ['cyt', 'cytosk', 'ex', 'mem', 'per', 'wall', 'bnuc', 'cproj', 'imem', 'omem']})
Observable('obs_met_ACETYL_COA_cyt', met(name = 'ACETYL_COA', loc = 'cyt'))
Observable('obs_met_CO_A_cyt', met(name = 'CO_A', loc = 'cyt'))
Observable('obs_met_CPD_3561_cyt', met(name = 'CPD_3561', loc = 'cyt'))
Observable('obs_met_CPD_3785_cyt', met(name = 'CPD_3785', loc = 'cyt'))
Observable('obs_met_CPD_3801_cyt', met(name = 'CPD_3801', loc = 'cyt'))
Observable('obs_met_D_ARABINOSE_cyt', met(name = 'D_ARABINOSE', loc = 'cyt'))
Observable('obs_met_Fructofuranose_cyt', met(name = 'Fructofuranose', loc = 'cyt'))
Observable('obs_met_MELIBIOSE_cyt', met(name = 'MELIBIOSE', loc = 'cyt'))
Observable('obs_met_PROTON_cyt', met(name = 'PROTON', loc = 'cyt'))
Observable('obs_met_WATER_cyt', met(name = 'WATER', loc = 'cyt'))
Observable('obs_met__6_Acetyl_beta_D_Galactose_cyt', met(name = '_6_Acetyl_beta_D_Galactose', loc = 'cyt'))
Observable('obs_met_alpha_ALLOLACTOSE_cyt', met(name = 'alpha_ALLOLACTOSE', loc = 'cyt'))
Observable('obs_met_alpha_GALACTOSE_cyt', met(name = 'alpha_GALACTOSE', loc = 'cyt'))
Observable('obs_met_alpha_glucose_cyt', met(name = 'alpha_glucose', loc = 'cyt'))
Observable('obs_met_alpha_lactose_cyt', met(name = 'alpha_lactose', loc = 'cyt'))
Observable('obs_met_beta_ALLOLACTOSE_cyt', met(name = 'beta_ALLOLACTOSE', loc = 'cyt'))
Observable('obs_met_beta_GALACTOSE_cyt', met(name = 'beta_GALACTOSE', loc = 'cyt'))
Observable('obs_met_beta_glucose_cyt', met(name = 'beta_glucose', loc = 'cyt'))
Observable('obs_met_beta_lactose_cyt', met(name = 'beta_lactose', loc = 'cyt'))
Initial(met(name = 'ACETYL_COA', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_ACETYL_COA_cyt', 0))
Initial(met(name = 'CO_A', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_CO_A_cyt', 0))
Initial(met(name = 'CPD_3561', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_CPD_3561_cyt', 0))
Initial(met(name = 'CPD_3785', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_CPD_3785_cyt', 0))
Initial(met(name = 'CPD_3801', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_CPD_3801_cyt', 0))
Initial(met(name = 'D_ARABINOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_D_ARABINOSE_cyt', 0))
Initial(met(name = 'Fructofuranose', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_Fructofuranose_cyt', 0))
Initial(met(name = 'MELIBIOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_MELIBIOSE_cyt', 0))
Initial(met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_PROTON_cyt', 0))
Initial(met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_WATER_cyt', 0))
Initial(met(name = '_6_Acetyl_beta_D_Galactose', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met__6_Acetyl_beta_D_Galactose_cyt', 0))
Initial(met(name = 'alpha_ALLOLACTOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_alpha_ALLOLACTOSE_cyt', 0))
Initial(met(name = 'alpha_GALACTOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_alpha_GALACTOSE_cyt', 0))
Initial(met(name = 'alpha_glucose', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_alpha_glucose_cyt', 0))
Initial(met(name = 'alpha_lactose', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_alpha_lactose_cyt', 0))
Initial(met(name = 'beta_ALLOLACTOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_beta_ALLOLACTOSE_cyt', 0))
Initial(met(name = 'beta_GALACTOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_beta_GALACTOSE_cyt', 0))
Initial(met(name = 'beta_glucose', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_beta_glucose_cyt', 0))
Initial(met(name = 'beta_lactose', loc = 'cyt', dna = None, met = None, prot = None, rna = None), Parameter('t0_met_beta_lactose_cyt', 0))
Initial(prot(name = 'LACY_MONOMER', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter('t0_prot_LACY_MONOMER_cyt', 0))
Initial(prot(name = 'spontaneous', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter('t0_prot_spontaneous_cyt', 0))
Initial(cplx(name = 'BETAGALACTOSID_CPLX', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter('t0_cplx_BETAGALACTOSID_CPLX_cyt', 0))
Initial(cplx(name = 'GALACTOACETYLTRAN_CPLX', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None), Parameter('t0_cplx_GALACTOACETYLTRAN_CPLX_cyt', 0))
Rule('LACTOSE_MUTAROTATION_CYT',
	met(name = 'alpha_lactose', loc = 'cyt', dna = None, met = None, prot = None, rna = None) |
	met(name = 'beta_lactose', loc = 'cyt', dna = None, met = None, prot = None, rna = None),
	Parameter('fwd_LACTOSE_MUTAROTATION_CYT', 1.000000), 
	Parameter('rvs_LACTOSE_MUTAROTATION_CYT', 1.000000))
Rule('GALACTOSE_MUTAROTATION_CYT',
	met(name = 'alpha_GALACTOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) |
	met(name = 'beta_GALACTOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None),
	Parameter('fwd_GALACTOSE_MUTAROTATION_CYT', 1.000000), 
	Parameter('rvs_GALACTOSE_MUTAROTATION_CYT', 1.000000))
Rule('GLUCOSE_MUTAROTATION_CYT',
	met(name = 'alpha_glucose', loc = 'cyt', dna = None, met = None, prot = None, rna = None) |
	met(name = 'beta_glucose', loc = 'cyt', dna = None, met = None, prot = None, rna = None),
	Parameter('fwd_GLUCOSE_MUTAROTATION_CYT', 1.000000), 
	Parameter('rvs_GLUCOSE_MUTAROTATION_CYT', 1.000000))
Rule('TRANS_RXN_24',
	prot(name = 'LACY_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'per', dna = None, met = None, prot = None, rna = None) +
	met(name = 'alpha_lactose', loc = 'per', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'LACY_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'alpha_lactose', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_24', 1.000000), 
	Parameter('rvs_TRANS_RXN_24', 0.000000))
Rule('TRANS_RXN_24_beta',
	prot(name = 'LACY_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'per', dna = None, met = None, prot = None, rna = None) +
	met(name = 'beta_lactose', loc = 'per', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'LACY_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'beta_lactose', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_24_beta', 1.000000), 
	Parameter('rvs_TRANS_RXN_24_beta', 0.000000))
Rule('TRANS_RXN_94',
	prot(name = 'LACY_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'per', dna = None, met = None, prot = None, rna = None) +
	met(name = 'MELIBIOSE', loc = 'per', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'LACY_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'MELIBIOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_94', 1.000000), 
	Parameter('rvs_TRANS_RXN_94', 0.000000))
Rule('RXN0_7215',
	prot(name = 'LACY_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'per', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_3561', loc = 'per', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'LACY_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_3561', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_7215', 1.000000), 
	Parameter('rvs_RXN0_7215', 0.000000))
Rule('RXN0_7217',
	prot(name = 'LACY_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'per', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_3785', loc = 'per', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'LACY_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_3785', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_7217', 1.000000), 
	Parameter('rvs_RXN0_7217', 0.000000))
Rule('RXN_17755',
	prot(name = 'LACY_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'per', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_3801', loc = 'per', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'LACY_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_3801', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN_17755', 1.000000), 
	Parameter('rvs_RXN_17755', 0.000000))
Rule('BETAGALACTOSID_RXN',
	cplx(name = 'BETAGALACTOSID_CPLX', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'beta_lactose', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'BETAGALACTOSID_CPLX', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'beta_GALACTOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'beta_glucose', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_BETAGALACTOSID_RXN', 1.000000), 
	Parameter('rvs_BETAGALACTOSID_RXN', 0.000000))
Rule('BETAGALACTOSID_RXN_alpha',
	cplx(name = 'BETAGALACTOSID_CPLX', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'alpha_lactose', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'BETAGALACTOSID_CPLX', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'alpha_GALACTOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'alpha_glucose', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_BETAGALACTOSID_RXN_alpha', 1.000000), 
	Parameter('rvs_BETAGALACTOSID_RXN_alpha', 0.000000))
Rule('RXN0_5363',
	cplx(name = 'BETAGALACTOSID_CPLX', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'alpha_lactose', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'BETAGALACTOSID_CPLX', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'alpha_ALLOLACTOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_5363', 1.000000), 
	Parameter('rvs_RXN0_5363', 1.000000))
Rule('RXN0_5363_beta',
	cplx(name = 'BETAGALACTOSID_CPLX', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'beta_lactose', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'BETAGALACTOSID_CPLX', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'beta_ALLOLACTOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_5363_beta', 1.000000), 
	Parameter('rvs_RXN0_5363_beta', 1.000000))
Rule('ALLOLACTOSE_DEG_alpha',
	cplx(name = 'BETAGALACTOSID_CPLX', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'alpha_ALLOLACTOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'BETAGALACTOSID_CPLX', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'alpha_GALACTOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'alpha_glucose', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_ALLOLACTOSE_DEG_alpha', 1.000000), 
	Parameter('rvs_ALLOLACTOSE_DEG_alpha', 0.000000))
Rule('ALLOLACTOSE_DEG_beta',
	cplx(name = 'BETAGALACTOSID_CPLX', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'beta_ALLOLACTOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'BETAGALACTOSID_CPLX', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'beta_GALACTOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'beta_glucose', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_ALLOLACTOSE_DEG_beta', 1.000000), 
	Parameter('rvs_ALLOLACTOSE_DEG_beta', 0.000000))
Rule('RXN_17726',
	cplx(name = 'BETAGALACTOSID_CPLX', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_3561', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'BETAGALACTOSID_CPLX', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'beta_GALACTOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Fructofuranose', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN_17726', 1.000000), 
	Parameter('rvs_RXN_17726', 0.000000))
Rule('RXN0_7219',
	cplx(name = 'BETAGALACTOSID_CPLX', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_3785', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'BETAGALACTOSID_CPLX', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'beta_GALACTOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'D_ARABINOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_7219', 1.000000), 
	Parameter('rvs_RXN0_7219', 0.000000))
Rule('GALACTOACETYLTRAN_RXN_galactose',
	cplx(name = 'GALACTOACETYLTRAN_CPLX', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'beta_GALACTOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ACETYL_COA', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'GALACTOACETYLTRAN_CPLX', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = '_6_Acetyl_beta_D_Galactose', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CO_A', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_GALACTOACETYLTRAN_RXN_galactose', 1.000000), 
	Parameter('rvs_GALACTOACETYLTRAN_RXN_galactose', 0.000000))
