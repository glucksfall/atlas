from pysb import *
Model()

Monomer('met',
	['name', 'loc', 'dna', 'met', 'prot', 'rna'],
	{ 'name' : [ 'ACETYL_COA', 'ADP', 'ALLOLACTOSE', 'ATP', 'Alpha_lactose', 'Beta_D_Galactosides', 'CO_A', 'CPD_15972', 'CPD_3561', 'CPD_3785', 'CPD_3801', 'D_ARABINOSE', 'Fructofuranose', 'GALACTOSE', 'Glucopyranose', 'L_ARABINOSE', 'MELIBIOSE', 'PROTON', 'Pi', 'WATER', '_6_Acetyl_Beta_D_Galactosides' ],
	'loc' : ['cyt', 'cytosk', 'ex', 'mem', 'per', 'wall', 'bnuc', 'cproj', 'imem', 'omem']})
Monomer('prot',
	['name', 'loc', 'dna', 'met', 'prot', 'rna', 'up', 'dw'],
	{ 'name' : [ 'LACY_MONOMER' ],
	'loc' : ['cyt', 'cytosk', 'ex', 'mem', 'per', 'wall', 'bnuc', 'cproj', 'imem', 'omem']})
Monomer('cplx',
	['name', 'loc', 'dna', 'met', 'prot', 'rna', 'up', 'dw'],
	{ 'name' : [ 'ABC_2_CPLX', 'BETAGALACTOSID_CPLX', 'GALACTOACETYLTRAN_CPLX' ],
	'loc' : ['cyt', 'cytosk', 'ex', 'mem', 'per', 'wall', 'bnuc', 'cproj', 'imem', 'omem']})
Rule('ABC_2_RXN',
	cplx(name = 'ABC_2_CPLX', loc = 'imem') +
	met(name = 'WATER', loc = 'cyt', prot = None) +
	met(name = 'ATP', loc = 'cyt', prot = None) +
	met(name = 'L_ARABINOSE', loc = 'cyt', prot = None) +
	None | 
	cplx(name = 'ABC_2_CPLX', loc = 'imem') +
	met(name = 'Pi', loc = 'cyt', prot = None) +
	met(name = 'ADP', loc = 'cyt', prot = None) +
	met(name = 'PROTON', loc = 'cyt', prot = None) +
	met(name = 'L_ARABINOSE', loc = 'cyt', prot = None), 
	Parameter('fwd_ABC_2_RXN', 1.000000), 
	Parameter('rvs_ABC_2_RXN', 0.000000))
Rule('BETAGALACTOSID_RXN',
	cplx(name = 'BETAGALACTOSID_CPLX', loc = 'cyt') +
	met(name = 'CPD_15972', loc = 'cyt', prot = None) +
	met(name = 'WATER', loc = 'cyt', prot = None) | 
	cplx(name = 'BETAGALACTOSID_CPLX', loc = 'cyt') +
	met(name = 'GALACTOSE', loc = 'cyt', prot = None) +
	met(name = 'Glucopyranose', loc = 'cyt', prot = None), 
	Parameter('fwd_BETAGALACTOSID_RXN', 1.000000), 
	Parameter('rvs_BETAGALACTOSID_RXN', 0.000000))
Rule('RXN0_5363',
	cplx(name = 'BETAGALACTOSID_CPLX', loc = 'cyt') +
	met(name = 'Alpha_lactose', loc = 'cyt', prot = None) | 
	cplx(name = 'BETAGALACTOSID_CPLX', loc = 'cyt') +
	met(name = 'ALLOLACTOSE', loc = 'cyt', prot = None), 
	Parameter('fwd_RXN0_5363', 1.000000), 
	Parameter('rvs_RXN0_5363', 1.000000))
Rule('RXN_17726',
	cplx(name = 'BETAGALACTOSID_CPLX', loc = 'cyt') +
	met(name = 'CPD_3561', loc = 'cyt', prot = None) +
	met(name = 'WATER', loc = 'cyt', prot = None) | 
	cplx(name = 'BETAGALACTOSID_CPLX', loc = 'cyt') +
	met(name = 'GALACTOSE', loc = 'cyt', prot = None) +
	met(name = 'Fructofuranose', loc = 'cyt', prot = None), 
	Parameter('fwd_RXN_17726', 1.000000), 
	Parameter('rvs_RXN_17726', 0.000000))
Rule('RXN0_7219',
	cplx(name = 'BETAGALACTOSID_CPLX', loc = 'cyt') +
	met(name = 'CPD_3785', loc = 'cyt', prot = None) +
	met(name = 'WATER', loc = 'cyt', prot = None) | 
	cplx(name = 'BETAGALACTOSID_CPLX', loc = 'cyt') +
	met(name = 'GALACTOSE', loc = 'cyt', prot = None) +
	met(name = 'D_ARABINOSE', loc = 'cyt', prot = None), 
	Parameter('fwd_RXN0_7219', 1.000000), 
	Parameter('rvs_RXN0_7219', 0.000000))
Rule('GALACTOACETYLTRAN_RXN',
	cplx(name = 'GALACTOACETYLTRAN_CPLX', loc = 'cyt') +
	met(name = 'Beta_D_Galactosides', loc = 'cyt', prot = None) +
	met(name = 'ACETYL_COA', loc = 'cyt', prot = None) | 
	cplx(name = 'GALACTOACETYLTRAN_CPLX', loc = 'cyt') +
	met(name = '_6_Acetyl_Beta_D_Galactosides', loc = 'cyt', prot = None) +
	met(name = 'CO_A', loc = 'cyt', prot = None), 
	Parameter('fwd_GALACTOACETYLTRAN_RXN', 1.000000), 
	Parameter('rvs_GALACTOACETYLTRAN_RXN', 0.000000))
Rule('TRANS_RXN_24',
	prot(name = 'LACY_MONOMER', loc = 'imem') +
	met(name = 'PROTON', loc = 'cyt', prot = None) +
	met(name = 'Alpha_lactose', loc = 'cyt', prot = None) | 
	prot(name = 'LACY_MONOMER', loc = 'imem') +
	met(name = 'PROTON', loc = 'cyt', prot = None) +
	met(name = 'Alpha_lactose', loc = 'cyt', prot = None), 
	Parameter('fwd_TRANS_RXN_24', 1.000000), 
	Parameter('rvs_TRANS_RXN_24', 1.000000))
Rule('TRANS_RXN_94',
	prot(name = 'LACY_MONOMER', loc = 'imem') +
	met(name = 'PROTON', loc = 'cyt', prot = None) +
	met(name = 'MELIBIOSE', loc = 'cyt', prot = None) | 
	prot(name = 'LACY_MONOMER', loc = 'imem') +
	met(name = 'PROTON', loc = 'cyt', prot = None) +
	met(name = 'MELIBIOSE', loc = 'cyt', prot = None), 
	Parameter('fwd_TRANS_RXN_94', 1.000000), 
	Parameter('rvs_TRANS_RXN_94', 1.000000))
Rule('RXN0_7215',
	prot(name = 'LACY_MONOMER', loc = 'imem') +
	met(name = 'PROTON', loc = 'cyt', prot = None) +
	met(name = 'CPD_3561', loc = 'cyt', prot = None) | 
	prot(name = 'LACY_MONOMER', loc = 'imem') +
	met(name = 'PROTON', loc = 'cyt', prot = None) +
	met(name = 'CPD_3561', loc = 'cyt', prot = None), 
	Parameter('fwd_RXN0_7215', 1.000000), 
	Parameter('rvs_RXN0_7215', 1.000000))
Rule('RXN0_7217',
	prot(name = 'LACY_MONOMER', loc = 'imem') +
	met(name = 'PROTON', loc = 'cyt', prot = None) +
	met(name = 'CPD_3785', loc = 'cyt', prot = None) | 
	prot(name = 'LACY_MONOMER', loc = 'imem') +
	met(name = 'PROTON', loc = 'cyt', prot = None) +
	met(name = 'CPD_3785', loc = 'cyt', prot = None), 
	Parameter('fwd_RXN0_7217', 1.000000), 
	Parameter('rvs_RXN0_7217', 1.000000))
Rule('RXN_17755',
	prot(name = 'LACY_MONOMER', loc = 'imem') +
	met(name = 'PROTON', loc = 'cyt', prot = None) +
	met(name = 'CPD_3801', loc = 'cyt', prot = None) | 
	prot(name = 'LACY_MONOMER', loc = 'imem') +
	met(name = 'PROTON', loc = 'cyt', prot = None) +
	met(name = 'CPD_3801', loc = 'cyt', prot = None), 
	Parameter('fwd_RXN_17755', 1.000000), 
	Parameter('rvs_RXN_17755', 1.000000))
