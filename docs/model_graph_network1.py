from pysb import *
Model()

Monomer('dna',
	['name', 'type', 'loc', 'dna', 'met', 'prot', 'rna', 'up', 'dw'],
	{ 'name' : ['lacI_21_1', 'lacI_422_402', 'lacI_72_92', 'lacA', 'lacY', 'lacZ'],
	'type' : ['BS', 'cds', 'pro1', 'pro2', 'pro3', 'pro4', 'rbs', 'ter1', 'ter2'],
	'loc' : ['cyt']})
Monomer('rna',
	['name', 'type', 'loc', 'dna', 'met', 'prot', 'rna', 'up', 'dw'],
	{ 'name' : ['lacI_21_1', 'lacI_422_402', 'lacI_72_92', 'lacA', 'lacY', 'lacZ'],
	'type' : ['BS', 'cds', 'pro1', 'pro2', 'pro3', 'pro4', 'rbs', 'ter1', 'ter2'],
	'loc' : ['cyt']})
Monomer('prot',
	['name', 'loc', 'dna', 'met', 'prot', 'rna', 'up', 'dw'],
	{ 'name' : ['lacA', 'lacY', 'lacZ'],
	'loc' : ['cyt', 'cytosk', 'ex', 'mem', 'per', 'wall', 'bnuc', 'cproj', 'imem', 'omem']})
Monomer('cplx',
	['name', 'loc', 'dna', 'met', 'prot', 'rna'],
	{ 'name' : ['RNAP_CPLX', 'RIBOSOME_CPLX'],
	'loc' : ['cyt']})
Rule('docking_lacZ_pro4',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = None) +
	dna(name = 'lacZ', type = 'pro4', loc = 'cyt', prot = None) |
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'lacZ', type = 'pro4', loc = 'cyt', prot = 1),
	Parameter('fwd_docking_lacZ_pro4', 1.000000),
	Parameter('rvs_docking_lacZ_pro4', 1.000000))
Rule('docking_lacZ_pro3',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = None) +
	dna(name = 'lacZ', type = 'pro3', loc = 'cyt', prot = None) |
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'lacZ', type = 'pro3', loc = 'cyt', prot = 1),
	Parameter('fwd_docking_lacZ_pro3', 1.000000),
	Parameter('rvs_docking_lacZ_pro3', 1.000000))
Rule('docking_lacZ_pro2',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = None) +
	dna(name = 'lacZ', type = 'pro2', loc = 'cyt', prot = None) |
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'lacZ', type = 'pro2', loc = 'cyt', prot = 1),
	Parameter('fwd_docking_lacZ_pro2', 1.000000),
	Parameter('rvs_docking_lacZ_pro2', 1.000000))
Rule('docking_lacZ_pro1',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = None) +
	dna(name = 'lacZ', type = 'pro1', loc = 'cyt', prot = None) |
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'lacZ', type = 'pro1', loc = 'cyt', prot = 1),
	Parameter('fwd_docking_lacZ_pro1', 1.000000),
	Parameter('rvs_docking_lacZ_pro1', 1.000000))
Rule('docking_lacY_pro1',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = None) +
	dna(name = 'lacY', type = 'pro1', loc = 'cyt', prot = None) |
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'lacY', type = 'pro1', loc = 'cyt', prot = 1),
	Parameter('fwd_docking_lacY_pro1', 0.000000),
	Parameter('rvs_docking_lacY_pro1', 0.000000))
Rule('sliding_lacZ_pro4',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'lacZ', type = 'pro4', loc = 'cyt', prot = 1) +
	dna(name = 'lacZ', type = 'pro3', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'lacZ', type = 'pro3', loc = 'cyt', prot = 1) +
	dna(name = 'lacZ', type = 'pro4', loc = 'cyt', prot = None) +
	rna(name = 'lacZ', type = 'pro3', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_lacZ_pro4', 1.000000))
Rule('sliding_lacZ_pro3',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'lacZ', type = 'pro3', loc = 'cyt', prot = 1) +
	dna(name = 'lacZ', type = 'pro2', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'lacZ', type = 'pro2', loc = 'cyt', prot = 1) +
	dna(name = 'lacZ', type = 'pro3', loc = 'cyt', prot = None) +
	rna(name = 'lacZ', type = 'pro2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_lacZ_pro3', 1.000000))
Rule('sliding_lacZ_pro2',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'lacZ', type = 'pro2', loc = 'cyt', prot = 1) +
	dna(name = 'lacI_72_92', type = 'BS', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'lacI_72_92', type = 'BS', loc = 'cyt', prot = 1) +
	dna(name = 'lacZ', type = 'pro2', loc = 'cyt', prot = None) +
	rna(name = 'lacI_72_92', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_lacZ_pro2', 1.000000))
Rule('sliding_BS_lacI_72_92',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'lacI_72_92', type = 'BS', loc = 'cyt', prot = 1) +
	dna(name = 'lacI_21_1', type = 'BS', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'lacI_21_1', type = 'BS', loc = 'cyt', prot = 1) +
	dna(name = 'lacI_72_92', type = 'BS', loc = 'cyt', prot = None) +
	rna(name = 'lacI_21_1', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_BS_lacI_72_92', 1.000000))
Rule('sliding_BS_lacI_21_1',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'lacI_21_1', type = 'BS', loc = 'cyt', prot = 1) +
	dna(name = 'lacZ', type = 'pro1', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'lacZ', type = 'pro1', loc = 'cyt', prot = 1) +
	dna(name = 'lacI_21_1', type = 'BS', loc = 'cyt', prot = None) +
	rna(name = 'lacZ', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_BS_lacI_21_1', 1.000000))
Rule('sliding_lacZ_pro1',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'lacZ', type = 'pro1', loc = 'cyt', prot = 1) +
	dna(name = 'lacZ', type = 'rbs', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'lacZ', type = 'rbs', loc = 'cyt', prot = 1) +
	dna(name = 'lacZ', type = 'pro1', loc = 'cyt', prot = None) +
	rna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_lacZ_pro1', 1.000000))
Rule('sliding_lacZ_rbs',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'lacZ', type = 'rbs', loc = 'cyt', prot = 1) +
	dna(name = 'lacZ', type = 'cds', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'lacZ', type = 'cds', loc = 'cyt', prot = 1) +
	dna(name = 'lacZ', type = 'rbs', loc = 'cyt', prot = None) +
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_lacZ_rbs', 1.000000))
Rule('sliding_lacZ_cds',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'lacZ', type = 'cds', loc = 'cyt', prot = 1) +
	dna(name = 'lacI_422_402', type = 'BS', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'lacI_422_402', type = 'BS', loc = 'cyt', prot = 1) +
	dna(name = 'lacZ', type = 'cds', loc = 'cyt', prot = None) +
	rna(name = 'lacI_422_402', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_lacZ_cds', 1.000000))
Rule('sliding_BS_lacI_422_402',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'lacI_422_402', type = 'BS', loc = 'cyt', prot = 1) +
	dna(name = 'lacY', type = 'pro1', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'lacY', type = 'pro1', loc = 'cyt', prot = 1) +
	dna(name = 'lacI_422_402', type = 'BS', loc = 'cyt', prot = None) +
	rna(name = 'lacY', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_BS_lacI_422_402', 1.000000))
Rule('sliding_lacY_pro1',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'lacY', type = 'pro1', loc = 'cyt', prot = 1) +
	dna(name = 'lacY', type = 'rbs', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'lacY', type = 'rbs', loc = 'cyt', prot = 1) +
	dna(name = 'lacY', type = 'pro1', loc = 'cyt', prot = None) +
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_lacY_pro1', 1.000000))
Rule('sliding_lacY_rbs',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'lacY', type = 'rbs', loc = 'cyt', prot = 1) +
	dna(name = 'lacY', type = 'cds', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'lacY', type = 'cds', loc = 'cyt', prot = 1) +
	dna(name = 'lacY', type = 'rbs', loc = 'cyt', prot = None) +
	rna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_lacY_rbs', 1.000000))
Rule('sliding_lacY_cds',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'lacY', type = 'cds', loc = 'cyt', prot = 1) +
	dna(name = 'lacA', type = 'rbs', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'lacA', type = 'rbs', loc = 'cyt', prot = 1) +
	dna(name = 'lacY', type = 'cds', loc = 'cyt', prot = None) +
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_lacY_cds', 1.000000))
Rule('sliding_lacA_rbs',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'lacA', type = 'rbs', loc = 'cyt', prot = 1) +
	dna(name = 'lacA', type = 'cds', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'lacA', type = 'cds', loc = 'cyt', prot = 1) +
	dna(name = 'lacA', type = 'rbs', loc = 'cyt', prot = None) +
	rna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_lacA_rbs', 1.000000))
Rule('sliding_lacA_cds',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'lacA', type = 'cds', loc = 'cyt', prot = 1) +
	dna(name = 'lacA', type = 'ter1', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'lacA', type = 'ter1', loc = 'cyt', prot = 1) +
	dna(name = 'lacA', type = 'cds', loc = 'cyt', prot = None) +
	rna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_lacA_cds', 1.000000))
Rule('sliding_lacA_ter1',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'lacA', type = 'ter1', loc = 'cyt', prot = 1) +
	dna(name = 'lacA', type = 'ter2', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'lacA', type = 'ter2', loc = 'cyt', prot = 1) +
	dna(name = 'lacA', type = 'ter1', loc = 'cyt', prot = None) +
	rna(name = 'lacA', type = 'ter2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_lacA_ter1', 1.000000))
Rule('falloff_lacA_ter1',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'lacA', type = 'ter1', loc = 'cyt', prot = 1) >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = None) +
	dna(name = 'lacA', type = 'ter1', loc = 'cyt', prot = None),
	Parameter('fwd_falloff_lacA_ter1', 1.000000))
Rule('falloff_lacA_ter2',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'lacA', type = 'ter2', loc = 'cyt', prot = 1) >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = None) +
	dna(name = 'lacA', type = 'ter2', loc = 'cyt', prot = None),
	Parameter('fwd_falloff_lacA_ter2', 1.000000))
Rule('dr_lacZ_rbs',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = None) +
	rna(name = 'lacZ', type = 'rbs', loc = 'cyt', prot = None) |
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'lacZ', type = 'rbs', loc = 'cyt', prot = 1),
	Parameter('fwd_dr_lacZ_rbs', 1.000000),
	Parameter('rvs_dr_lacZ_rbs', 1.000000))
Rule('dr_lacY_rbs',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = None) +
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', prot = None) |
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', prot = 1),
	Parameter('fwd_dr_lacY_rbs', 1.000000),
	Parameter('rvs_dr_lacY_rbs', 1.000000))
Rule('dr_lacA_rbs',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = None) +
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', prot = None) |
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', prot = 1),
	Parameter('fwd_dr_lacA_rbs', 1.000000),
	Parameter('rvs_dr_lacA_rbs', 1.000000))
Rule('sr_lacZ_rbs',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'lacZ', type = 'rbs', loc = 'cyt', prot = 1) +
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', prot = 1) +
	rna(name = 'lacZ', type = 'rbs', loc = 'cyt', prot = None) +
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sr_lacZ_rbs', 1.000000))
Rule('sr_lacY_rbs',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', prot = 1) +
	rna(name = 'lacY', type = 'cds', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', prot = 1) +
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', prot = None) +
	prot(name = 'lacY', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sr_lacY_rbs', 1.000000))
Rule('sr_lacA_rbs',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', prot = 1) +
	rna(name = 'lacA', type = 'cds', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', prot = 1) +
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', prot = None) +
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sr_lacA_rbs', 1.000000))
Rule('fr_lacZ_cds',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', prot = 1) >>
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = None) +
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', prot = None),
	Parameter('fwd_fr_lacZ_cds', 1.000000))
Rule('fr_lacY_cds',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', prot = 1) >>
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = None) +
	rna(name = 'lacY', type = 'cds', loc = 'cyt', prot = None),
	Parameter('fwd_fr_lacY_cds', 1.000000))
Rule('fr_lacA_cds',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', prot = 1) >>
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = None) +
	rna(name = 'lacA', type = 'cds', loc = 'cyt', prot = None),
	Parameter('fwd_fr_lacA_cds', 1.000000))
Initial(prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('t0_prot_lacZ_cyt', 0))
Observable('obs_prot_lacZ_cyt',
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Initial(prot(name = 'lacY', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('t0_prot_lacY_cyt', 0))
Observable('obs_prot_lacY_cyt',
	prot(name = 'lacY', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Initial(prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('t0_prot_lacA_cyt', 0))
Observable('obs_prot_lacA_cyt',
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Initial(dna(name = 'lacZ', type = 'pro4', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	dna(name = 'lacZ', type = 'pro3', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	dna(name = 'lacZ', type = 'pro2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	dna(name = 'lacI_72_92', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	dna(name = 'lacI_21_1', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	dna(name = 'lacZ', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	dna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	dna(name = 'lacZ', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = 8) %
	dna(name = 'lacI_422_402', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 8, dw = 9) %
	dna(name = 'lacY', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 9, dw = 10) %
	dna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 10, dw = 11) %
	dna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 11, dw = 12) %
	dna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 12, dw = 13) %
	dna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 13, dw = 14) %
	dna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 14, dw = 15) %
	dna(name = 'lacA', type = 'ter2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 15, dw = None),
	Parameter('t0_dna_lacZlacYlacA', 0))
Observable('obs_dna_lacZlacYlacA',
	dna(name = 'lacZ', type = 'pro4', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	dna(name = 'lacZ', type = 'pro3', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	dna(name = 'lacZ', type = 'pro2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	dna(name = 'lacI_72_92', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	dna(name = 'lacI_21_1', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	dna(name = 'lacZ', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	dna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	dna(name = 'lacZ', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = 8) %
	dna(name = 'lacI_422_402', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 8, dw = 9) %
	dna(name = 'lacY', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 9, dw = 10) %
	dna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 10, dw = 11) %
	dna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 11, dw = 12) %
	dna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 12, dw = 13) %
	dna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 13, dw = 14) %
	dna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 14, dw = 15) %
	dna(name = 'lacA', type = 'ter2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 15, dw = None))
Initial(rna(name = 'lacZ', type = 'pro3', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'lacZ', type = 'pro2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'lacI_72_92', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'lacI_21_1', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'lacZ', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	rna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	rna(name = 'lacI_422_402', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = 8) %
	rna(name = 'lacY', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 8, dw = 9) %
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 9, dw = 10) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 10, dw = 11) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 11, dw = 12) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 12, dw = 13) %
	rna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 13, dw = None),
	Parameter('t0_rna_lacZlacYlacA_form1', 0))
Observable('obs_rna_lacZlacYlacA_form1',
	rna(name = 'lacZ', type = 'pro3', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'lacZ', type = 'pro2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'lacI_72_92', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'lacI_21_1', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'lacZ', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	rna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	rna(name = 'lacI_422_402', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = 8) %
	rna(name = 'lacY', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 8, dw = 9) %
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 9, dw = 10) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 10, dw = 11) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 11, dw = 12) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 12, dw = 13) %
	rna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 13, dw = None))
Initial(rna(name = 'lacZ', type = 'pro3', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'lacZ', type = 'pro2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'lacI_72_92', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'lacI_21_1', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'lacZ', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	rna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	rna(name = 'lacI_422_402', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = 8) %
	rna(name = 'lacY', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 8, dw = 9) %
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 9, dw = 10) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 10, dw = 11) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 11, dw = 12) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 12, dw = 13) %
	rna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 13, dw = 14) %
	rna(name = 'lacA', type = 'ter2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 14, dw = None),
	Parameter('t0_rna_lacZlacYlacA_form2', 0))
Observable('obs_rna_lacZlacYlacA_form2',
	rna(name = 'lacZ', type = 'pro3', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'lacZ', type = 'pro2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'lacI_72_92', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'lacI_21_1', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'lacZ', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	rna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	rna(name = 'lacI_422_402', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = 8) %
	rna(name = 'lacY', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 8, dw = 9) %
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 9, dw = 10) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 10, dw = 11) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 11, dw = 12) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 12, dw = 13) %
	rna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 13, dw = 14) %
	rna(name = 'lacA', type = 'ter2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 14, dw = None))
Initial(rna(name = 'lacZ', type = 'pro2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'lacI_72_92', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'lacI_21_1', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'lacZ', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	rna(name = 'lacI_422_402', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	rna(name = 'lacY', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = 8) %
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 8, dw = 9) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 9, dw = 10) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 10, dw = 11) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 11, dw = 12) %
	rna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 12, dw = None),
	Parameter('t0_rna_lacZlacYlacA_form3', 0))
Observable('obs_rna_lacZlacYlacA_form3',
	rna(name = 'lacZ', type = 'pro2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'lacI_72_92', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'lacI_21_1', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'lacZ', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	rna(name = 'lacI_422_402', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	rna(name = 'lacY', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = 8) %
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 8, dw = 9) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 9, dw = 10) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 10, dw = 11) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 11, dw = 12) %
	rna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 12, dw = None))
Initial(rna(name = 'lacZ', type = 'pro2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'lacI_72_92', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'lacI_21_1', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'lacZ', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	rna(name = 'lacI_422_402', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	rna(name = 'lacY', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = 8) %
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 8, dw = 9) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 9, dw = 10) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 10, dw = 11) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 11, dw = 12) %
	rna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 12, dw = 13) %
	rna(name = 'lacA', type = 'ter2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 13, dw = None),
	Parameter('t0_rna_lacZlacYlacA_form4', 0))
Observable('obs_rna_lacZlacYlacA_form4',
	rna(name = 'lacZ', type = 'pro2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'lacI_72_92', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'lacI_21_1', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'lacZ', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	rna(name = 'lacI_422_402', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	rna(name = 'lacY', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = 8) %
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 8, dw = 9) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 9, dw = 10) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 10, dw = 11) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 11, dw = 12) %
	rna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 12, dw = 13) %
	rna(name = 'lacA', type = 'ter2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 13, dw = None))
Initial(rna(name = 'lacI_72_92', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'lacI_21_1', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'lacZ', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	rna(name = 'lacI_422_402', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	rna(name = 'lacY', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = 8) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 8, dw = 9) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 9, dw = 10) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 10, dw = 11) %
	rna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 11, dw = None),
	Parameter('t0_rna_lacZlacYlacA_form5', 0))
Observable('obs_rna_lacZlacYlacA_form5',
	rna(name = 'lacI_72_92', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'lacI_21_1', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'lacZ', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	rna(name = 'lacI_422_402', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	rna(name = 'lacY', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = 8) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 8, dw = 9) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 9, dw = 10) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 10, dw = 11) %
	rna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 11, dw = None))
Initial(rna(name = 'lacI_72_92', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'lacI_21_1', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'lacZ', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	rna(name = 'lacI_422_402', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	rna(name = 'lacY', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = 8) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 8, dw = 9) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 9, dw = 10) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 10, dw = 11) %
	rna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 11, dw = 12) %
	rna(name = 'lacA', type = 'ter2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 12, dw = None),
	Parameter('t0_rna_lacZlacYlacA_form6', 0))
Observable('obs_rna_lacZlacYlacA_form6',
	rna(name = 'lacI_72_92', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'lacI_21_1', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'lacZ', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	rna(name = 'lacI_422_402', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	rna(name = 'lacY', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = 8) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 8, dw = 9) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 9, dw = 10) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 10, dw = 11) %
	rna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 11, dw = 12) %
	rna(name = 'lacA', type = 'ter2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 12, dw = None))
Initial(rna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'lacI_422_402', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'lacY', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = 8) %
	rna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 8, dw = None),
	Parameter('t0_rna_lacZlacYlacA_form7', 0))
Observable('obs_rna_lacZlacYlacA_form7',
	rna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'lacI_422_402', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'lacY', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = 8) %
	rna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 8, dw = None))
Initial(rna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'lacI_422_402', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'lacY', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = 8) %
	rna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 8, dw = 9) %
	rna(name = 'lacA', type = 'ter2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 9, dw = None),
	Parameter('t0_rna_lacZlacYlacA_form8', 0))
Observable('obs_rna_lacZlacYlacA_form8',
	rna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'lacI_422_402', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'lacY', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = 8) %
	rna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 8, dw = 9) %
	rna(name = 'lacA', type = 'ter2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 9, dw = None))
Initial(rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = None),
	Parameter('t0_rna_lacZlacYlacA_form9', 0))
Observable('obs_rna_lacZlacYlacA_form9',
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = None))
Initial(rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	rna(name = 'lacA', type = 'ter2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = None),
	Parameter('t0_rna_lacZlacYlacA_form10', 0))
Observable('obs_rna_lacZlacYlacA_form10',
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	rna(name = 'lacA', type = 'ter2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = None))
