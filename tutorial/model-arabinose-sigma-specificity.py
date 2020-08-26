from pysb import *
Model()

Monomer('dna',
	['name', 'type', 'loc', 'dna', 'met', 'prot', 'rna', 'up', 'dw'],
	{ 'name' : ['araA', 'araB', 'araC', 'araC_56_72', 'araD', 'araE', 'araF', 'araG', 'araH', 'rpoA', 'rpoB', 'rpoC', 'rpoD'],
	'type' : ['BS', 'cds', 'pro1', 'rbs', 'ter1'],
	'loc' : ['cyt']})
Monomer('rna',
	['name', 'type', 'loc', 'dna', 'met', 'prot', 'rna', 'up', 'dw'],
	{ 'name' : ['araA', 'araB', 'araC', 'araC_56_72', 'araD', 'araE', 'araF', 'araG', 'araH', 'rpoA', 'rpoB', 'rpoC', 'rpoD'],
	'type' : ['BS', 'cds', 'pro1', 'rbs', 'ter1'],
	'loc' : ['cyt']})
Monomer('prot',
	['name', 'loc', 'dna', 'met', 'prot', 'rna', 'up', 'dw'],
	{ 'name' : ['araA', 'araB', 'araC', 'araC_56_72', 'araD', 'araE', 'araF', 'araG', 'araH', 'rpoA', 'rpoB', 'rpoC', 'rpoD'],
	'loc' : ['cyt', 'mem']})
Monomer('cplx',
	['name', 'loc', 'dna', 'met', 'prot', 'rna'],
	{ 'name' : ['RIBOSOME_CPLX'],
	'loc' : ['cyt']})
Rule('docking_1_araB_pro1',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, up = 3, dw = 4) %
	prot(name = 'rpoD', loc = 'cyt', dna = None, met = None, up = 4, dw = None) +
	dna(name = 'araB', type = 'pro1', loc = 'cyt', prot = None, up = WILD, dw = WILD) |
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, up = 3, dw = 4) %
	prot(name = 'rpoD', loc = 'cyt', dna = 5, met = None, up = 4, dw = None) %
	dna(name = 'araB', type = 'pro1', loc = 'cyt', prot = 5, up = WILD, dw = WILD),
	Parameter('fwd_docking_1_araB_pro1', 1.000000),
	Parameter('rvs_docking_1_araB_pro1', 1.000000))
Rule('docking_2_araC_pro1',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, up = 3, dw = 4) %
	prot(name = 'rpoD', loc = 'cyt', dna = None, met = None, up = 4, dw = None) +
	dna(name = 'araC', type = 'pro1', loc = 'cyt', prot = None, up = WILD, dw = WILD) |
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, up = 3, dw = 4) %
	prot(name = 'rpoD', loc = 'cyt', dna = 5, met = None, up = 4, dw = None) %
	dna(name = 'araC', type = 'pro1', loc = 'cyt', prot = 5, up = WILD, dw = WILD),
	Parameter('fwd_docking_2_araC_pro1', 1.000000),
	Parameter('rvs_docking_2_araC_pro1', 1.000000))
Rule('docking_3_araE_pro1',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, up = 3, dw = 4) %
	prot(name = 'rpoD', loc = 'cyt', dna = None, met = None, up = 4, dw = None) +
	dna(name = 'araE', type = 'pro1', loc = 'cyt', prot = None, up = WILD, dw = WILD) |
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, up = 3, dw = 4) %
	prot(name = 'rpoD', loc = 'cyt', dna = 5, met = None, up = 4, dw = None) %
	dna(name = 'araE', type = 'pro1', loc = 'cyt', prot = 5, up = WILD, dw = WILD),
	Parameter('fwd_docking_3_araE_pro1', 1.000000),
	Parameter('rvs_docking_3_araE_pro1', 1.000000))
Rule('docking_4_araF_pro1',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, up = 3, dw = 4) %
	prot(name = 'rpoD', loc = 'cyt', dna = None, met = None, up = 4, dw = None) +
	dna(name = 'araF', type = 'pro1', loc = 'cyt', prot = None, up = WILD, dw = WILD) |
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, up = 3, dw = 4) %
	prot(name = 'rpoD', loc = 'cyt', dna = 5, met = None, up = 4, dw = None) %
	dna(name = 'araF', type = 'pro1', loc = 'cyt', prot = 5, up = WILD, dw = WILD),
	Parameter('fwd_docking_4_araF_pro1', 1.000000),
	Parameter('rvs_docking_4_araF_pro1', 1.000000))
Rule('sliding_1_araB_pro1_rbs_holoenzyme',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, up = 3, dw = 4) %
	prot(name = 'rpoD', loc = 'cyt', dna = 5, met = None, up = 4, dw = None) %
	dna(name = 'araB', type = 'pro1', loc = 'cyt', prot = 5, up = WILD, dw = WILD) +
	dna(name = 'araB', type = 'rbs', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	None >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araB', type = 'rbs', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'araB', type = 'pro1', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	rna(name = 'araB', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_1_araB_pro1_rbs_holoenzyme', 1.000000))
Rule('sliding_2_araC_pro1_72_holoenzyme',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, up = 3, dw = 4) %
	prot(name = 'rpoD', loc = 'cyt', dna = 5, met = None, up = 4, dw = None) %
	dna(name = 'araC', type = 'pro1', loc = 'cyt', prot = 5, up = WILD, dw = WILD) +
	dna(name = 'araC_56_72', type = 'BS', prot = None, up = WILD, dw = WILD) +
	None >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araC_56_72', type = 'BS', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'araC', type = 'pro1', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	rna(name = 'araC_56_72', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_2_araC_pro1_72_holoenzyme', 1.000000))
Rule('sliding_3_araE_pro1_rbs_holoenzyme',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, up = 3, dw = 4) %
	prot(name = 'rpoD', loc = 'cyt', dna = 5, met = None, up = 4, dw = None) %
	dna(name = 'araE', type = 'pro1', loc = 'cyt', prot = 5, up = WILD, dw = WILD) +
	dna(name = 'araE', type = 'rbs', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	None >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araE', type = 'rbs', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'araE', type = 'pro1', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	rna(name = 'araE', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_3_araE_pro1_rbs_holoenzyme', 1.000000))
Rule('sliding_4_araF_pro1_rbs_holoenzyme',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, up = 3, dw = 4) %
	prot(name = 'rpoD', loc = 'cyt', dna = 5, met = None, up = 4, dw = None) %
	dna(name = 'araF', type = 'pro1', loc = 'cyt', prot = 5, up = WILD, dw = WILD) +
	dna(name = 'araF', type = 'rbs', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	None >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araF', type = 'rbs', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'araF', type = 'pro1', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	rna(name = 'araF', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_4_araF_pro1_rbs_holoenzyme', 1.000000))
Rule('sliding_1_araB_rbs_to_araB_cds',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araB', type = 'rbs', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'araB', type = 'cds', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	None >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araB', type = 'cds', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'araB', type = 'rbs', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	rna(name = 'araB', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_1_araB_rbs_to_araB_cds', 1.000000))
Rule('sliding_2_araB_cds_to_araA_rbs',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araB', type = 'cds', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'araA', type = 'rbs', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	None >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araA', type = 'rbs', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'araB', type = 'cds', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	rna(name = 'araA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_2_araB_cds_to_araA_rbs', 1.000000))
Rule('sliding_3_araA_rbs_to_araA_cds',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araA', type = 'rbs', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'araA', type = 'cds', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	None >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araA', type = 'cds', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'araA', type = 'rbs', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	rna(name = 'araA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_3_araA_rbs_to_araA_cds', 1.000000))
Rule('sliding_4_araA_cds_to_araD_rbs',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araA', type = 'cds', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'araD', type = 'rbs', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	None >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araD', type = 'rbs', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'araA', type = 'cds', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	rna(name = 'araD', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_4_araA_cds_to_araD_rbs', 1.000000))
Rule('sliding_5_araD_rbs_to_araD_cds',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araD', type = 'rbs', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'araD', type = 'cds', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	None >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araD', type = 'cds', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'araD', type = 'rbs', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	rna(name = 'araD', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_5_araD_rbs_to_araD_cds', 1.000000))
Rule('sliding_6_araD_cds_to_araD_ter1',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araD', type = 'cds', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'araD', type = 'ter1', loc = 'cyt', prot = None, up = WILD, dw = WILD) >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araD', type = 'ter1', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'araD', type = 'cds', loc = 'cyt', prot = None, up = WILD, dw = WILD),
	Parameter('fwd_sliding_6_araD_cds_to_araD_ter1', 1.000000))
Rule('sliding_1_BS_araC_56_72_to_araC_rbs',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araC_56_72', type = 'BS', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'araC', type = 'rbs', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	None >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araC', type = 'rbs', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'araC_56_72', type = 'BS', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	rna(name = 'araC', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_1_BS_araC_56_72_to_araC_rbs', 1.000000))
Rule('sliding_2_araC_rbs_to_araC_cds',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araC', type = 'rbs', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'araC', type = 'cds', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	None >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araC', type = 'cds', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'araC', type = 'rbs', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	rna(name = 'araC', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_2_araC_rbs_to_araC_cds', 1.000000))
Rule('sliding_3_araC_cds_to_araC_ter1',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araC', type = 'cds', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'araC', type = 'ter1', loc = 'cyt', prot = None, up = WILD, dw = WILD) >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araC', type = 'ter1', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'araC', type = 'cds', loc = 'cyt', prot = None, up = WILD, dw = WILD),
	Parameter('fwd_sliding_3_araC_cds_to_araC_ter1', 1.000000))
Rule('sliding_1_araE_rbs_to_araE_cds',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araE', type = 'rbs', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'araE', type = 'cds', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	None >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araE', type = 'cds', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'araE', type = 'rbs', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	rna(name = 'araE', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_1_araE_rbs_to_araE_cds', 1.000000))
Rule('sliding_2_araE_cds_to_araE_ter1',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araE', type = 'cds', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'araE', type = 'ter1', loc = 'cyt', prot = None, up = WILD, dw = WILD) >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araE', type = 'ter1', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'araE', type = 'cds', loc = 'cyt', prot = None, up = WILD, dw = WILD),
	Parameter('fwd_sliding_2_araE_cds_to_araE_ter1', 1.000000))
Rule('sliding_1_araF_rbs_to_araF_cds',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araF', type = 'rbs', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'araF', type = 'cds', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	None >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araF', type = 'cds', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'araF', type = 'rbs', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	rna(name = 'araF', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_1_araF_rbs_to_araF_cds', 1.000000))
Rule('sliding_2_araF_cds_to_araG_rbs',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araF', type = 'cds', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'araG', type = 'rbs', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	None >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araG', type = 'rbs', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'araF', type = 'cds', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	rna(name = 'araG', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_2_araF_cds_to_araG_rbs', 1.000000))
Rule('sliding_3_araG_rbs_to_araG_cds',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araG', type = 'rbs', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'araG', type = 'cds', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	None >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araG', type = 'cds', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'araG', type = 'rbs', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	rna(name = 'araG', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_3_araG_rbs_to_araG_cds', 1.000000))
Rule('sliding_4_araG_cds_to_araH_rbs',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araG', type = 'cds', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'araH', type = 'rbs', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	None >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araH', type = 'rbs', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'araG', type = 'cds', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	rna(name = 'araH', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_4_araG_cds_to_araH_rbs', 1.000000))
Rule('sliding_5_araH_rbs_to_araH_cds',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araH', type = 'rbs', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'araH', type = 'cds', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	None >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araH', type = 'cds', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'araH', type = 'rbs', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	rna(name = 'araH', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_5_araH_rbs_to_araH_cds', 1.000000))
Rule('sliding_6_araH_cds_to_araH_ter1',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araH', type = 'cds', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'araH', type = 'ter1', loc = 'cyt', prot = None, up = WILD, dw = WILD) >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araH', type = 'ter1', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'araH', type = 'cds', loc = 'cyt', prot = None, up = WILD, dw = WILD),
	Parameter('fwd_sliding_6_araH_cds_to_araH_ter1', 1.000000))
Rule('sliding_1_rpoA_rbs_to_rpoA_cds',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'rpoA', type = 'rbs', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'rpoA', type = 'cds', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	None >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'rpoA', type = 'cds', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'rpoA', type = 'rbs', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	rna(name = 'rpoA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_1_rpoA_rbs_to_rpoA_cds', 1.000000))
Rule('sliding_2_rpoA_cds_to_rpoA_ter1',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'rpoA', type = 'cds', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'rpoA', type = 'ter1', loc = 'cyt', prot = None, up = WILD, dw = WILD) >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'rpoA', type = 'ter1', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'rpoA', type = 'cds', loc = 'cyt', prot = None, up = WILD, dw = WILD),
	Parameter('fwd_sliding_2_rpoA_cds_to_rpoA_ter1', 1.000000))
Rule('sliding_1_rpoB_rbs_to_rpoB_cds',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'rpoB', type = 'rbs', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'rpoB', type = 'cds', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	None >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'rpoB', type = 'cds', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'rpoB', type = 'rbs', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	rna(name = 'rpoB', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_1_rpoB_rbs_to_rpoB_cds', 1.000000))
Rule('sliding_2_rpoB_cds_to_rpoC_rbs',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'rpoB', type = 'cds', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'rpoC', type = 'rbs', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	None >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'rpoC', type = 'rbs', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'rpoB', type = 'cds', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	rna(name = 'rpoC', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_2_rpoB_cds_to_rpoC_rbs', 1.000000))
Rule('sliding_3_rpoC_rbs_to_rpoC_cds',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'rpoC', type = 'rbs', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'rpoC', type = 'cds', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	None >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'rpoC', type = 'cds', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'rpoC', type = 'rbs', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	rna(name = 'rpoC', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_3_rpoC_rbs_to_rpoC_cds', 1.000000))
Rule('sliding_4_rpoC_cds_to_rpoC_ter1',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'rpoC', type = 'cds', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'rpoC', type = 'ter1', loc = 'cyt', prot = None, up = WILD, dw = WILD) >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'rpoC', type = 'ter1', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'rpoC', type = 'cds', loc = 'cyt', prot = None, up = WILD, dw = WILD),
	Parameter('fwd_sliding_4_rpoC_cds_to_rpoC_ter1', 1.000000))
Rule('sliding_1_rpoD_rbs_to_rpoD_cds',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'rpoD', type = 'rbs', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'rpoD', type = 'cds', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	None >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'rpoD', type = 'cds', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'rpoD', type = 'rbs', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	rna(name = 'rpoD', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_1_rpoD_rbs_to_rpoD_cds', 1.000000))
Rule('sliding_2_rpoD_cds_to_rpoD_ter1',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'rpoD', type = 'cds', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'rpoD', type = 'ter1', loc = 'cyt', prot = None, up = WILD, dw = WILD) >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'rpoD', type = 'ter1', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'rpoD', type = 'cds', loc = 'cyt', prot = None, up = WILD, dw = WILD),
	Parameter('fwd_sliding_2_rpoD_cds_to_rpoD_ter1', 1.000000))
Rule('falloff_from_araD_ter1', 
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araD', type = 'ter1', loc = 'cyt', prot = 4, up = WILD, dw = WILD) >> 
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, up = 3, dw = None) +
	dna(name = 'araD', type = 'ter1', loc = 'cyt', prot = None, up = WILD, dw = WILD), 
	Parameter('fwd_falloff_from_araD_ter1', 1.000000))
Rule('falloff_from_araC_ter1', 
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araC', type = 'ter1', loc = 'cyt', prot = 4, up = WILD, dw = WILD) >> 
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, up = 3, dw = None) +
	dna(name = 'araC', type = 'ter1', loc = 'cyt', prot = None, up = WILD, dw = WILD), 
	Parameter('fwd_falloff_from_araC_ter1', 1.000000))
Rule('falloff_from_araE_ter1', 
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araE', type = 'ter1', loc = 'cyt', prot = 4, up = WILD, dw = WILD) >> 
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, up = 3, dw = None) +
	dna(name = 'araE', type = 'ter1', loc = 'cyt', prot = None, up = WILD, dw = WILD), 
	Parameter('fwd_falloff_from_araE_ter1', 1.000000))
Rule('falloff_from_araH_ter1', 
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'araH', type = 'ter1', loc = 'cyt', prot = 4, up = WILD, dw = WILD) >> 
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, up = 3, dw = None) +
	dna(name = 'araH', type = 'ter1', loc = 'cyt', prot = None, up = WILD, dw = WILD), 
	Parameter('fwd_falloff_from_araH_ter1', 1.000000))
Rule('falloff_from_rpoA_ter1', 
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'rpoA', type = 'ter1', loc = 'cyt', prot = 4, up = WILD, dw = WILD) >> 
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, up = 3, dw = None) +
	dna(name = 'rpoA', type = 'ter1', loc = 'cyt', prot = None, up = WILD, dw = WILD), 
	Parameter('fwd_falloff_from_rpoA_ter1', 1.000000))
Rule('falloff_from_rpoC_ter1', 
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'rpoC', type = 'ter1', loc = 'cyt', prot = 4, up = WILD, dw = WILD) >> 
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, up = 3, dw = None) +
	dna(name = 'rpoC', type = 'ter1', loc = 'cyt', prot = None, up = WILD, dw = WILD), 
	Parameter('fwd_falloff_from_rpoC_ter1', 1.000000))
Rule('falloff_from_rpoD_ter1', 
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'rpoD', type = 'ter1', loc = 'cyt', prot = 4, up = WILD, dw = WILD) >> 
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, up = 3, dw = None) +
	dna(name = 'rpoD', type = 'ter1', loc = 'cyt', prot = None, up = WILD, dw = WILD), 
	Parameter('fwd_falloff_from_rpoD_ter1', 1.000000))
Rule('dr_araB_rbs',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = None) +
	rna(name = 'araB', type = 'rbs', loc = 'cyt', prot = None) |
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'araB', type = 'rbs', loc = 'cyt', prot = 1),
	Parameter('fwd_dr_araB_rbs', 1.000000),
	Parameter('rvs_dr_araB_rbs', 1.000000))
Rule('dr_araA_rbs',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = None) +
	rna(name = 'araA', type = 'rbs', loc = 'cyt', prot = None) |
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'araA', type = 'rbs', loc = 'cyt', prot = 1),
	Parameter('fwd_dr_araA_rbs', 1.000000),
	Parameter('rvs_dr_araA_rbs', 1.000000))
Rule('dr_araD_rbs',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = None) +
	rna(name = 'araD', type = 'rbs', loc = 'cyt', prot = None) |
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'araD', type = 'rbs', loc = 'cyt', prot = 1),
	Parameter('fwd_dr_araD_rbs', 1.000000),
	Parameter('rvs_dr_araD_rbs', 1.000000))
Rule('dr_araC_rbs',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = None) +
	rna(name = 'araC', type = 'rbs', loc = 'cyt', prot = None) |
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'araC', type = 'rbs', loc = 'cyt', prot = 1),
	Parameter('fwd_dr_araC_rbs', 1.000000),
	Parameter('rvs_dr_araC_rbs', 1.000000))
Rule('dr_araE_rbs',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = None) +
	rna(name = 'araE', type = 'rbs', loc = 'cyt', prot = None) |
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'araE', type = 'rbs', loc = 'cyt', prot = 1),
	Parameter('fwd_dr_araE_rbs', 1.000000),
	Parameter('rvs_dr_araE_rbs', 1.000000))
Rule('dr_araF_rbs',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = None) +
	rna(name = 'araF', type = 'rbs', loc = 'cyt', prot = None) |
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'araF', type = 'rbs', loc = 'cyt', prot = 1),
	Parameter('fwd_dr_araF_rbs', 1.000000),
	Parameter('rvs_dr_araF_rbs', 1.000000))
Rule('dr_araG_rbs',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = None) +
	rna(name = 'araG', type = 'rbs', loc = 'cyt', prot = None) |
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'araG', type = 'rbs', loc = 'cyt', prot = 1),
	Parameter('fwd_dr_araG_rbs', 1.000000),
	Parameter('rvs_dr_araG_rbs', 1.000000))
Rule('dr_araH_rbs',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = None) +
	rna(name = 'araH', type = 'rbs', loc = 'cyt', prot = None) |
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'araH', type = 'rbs', loc = 'cyt', prot = 1),
	Parameter('fwd_dr_araH_rbs', 1.000000),
	Parameter('rvs_dr_araH_rbs', 1.000000))
Rule('dr_rpoA_rbs',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = None) +
	rna(name = 'rpoA', type = 'rbs', loc = 'cyt', prot = None) |
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'rpoA', type = 'rbs', loc = 'cyt', prot = 1),
	Parameter('fwd_dr_rpoA_rbs', 1.000000),
	Parameter('rvs_dr_rpoA_rbs', 1.000000))
Rule('dr_rpoB_rbs',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = None) +
	rna(name = 'rpoB', type = 'rbs', loc = 'cyt', prot = None) |
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'rpoB', type = 'rbs', loc = 'cyt', prot = 1),
	Parameter('fwd_dr_rpoB_rbs', 1.000000),
	Parameter('rvs_dr_rpoB_rbs', 1.000000))
Rule('dr_rpoC_rbs',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = None) +
	rna(name = 'rpoC', type = 'rbs', loc = 'cyt', prot = None) |
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'rpoC', type = 'rbs', loc = 'cyt', prot = 1),
	Parameter('fwd_dr_rpoC_rbs', 1.000000),
	Parameter('rvs_dr_rpoC_rbs', 1.000000))
Rule('dr_rpoD_rbs',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = None) +
	rna(name = 'rpoD', type = 'rbs', loc = 'cyt', prot = None) |
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'rpoD', type = 'rbs', loc = 'cyt', prot = 1),
	Parameter('fwd_dr_rpoD_rbs', 1.000000),
	Parameter('rvs_dr_rpoD_rbs', 1.000000))
Rule('sr_araB_rbs',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'araB', type = 'rbs', loc = 'cyt', prot = 1) +
	rna(name = 'araB', type = 'cds', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RIBOSOME_CPLX', rna = 1) %
	rna(name = 'araB', type = 'cds', loc = 'cyt', prot = 1) +
	rna(name = 'araB', type = 'rbs', loc = 'cyt', prot = None) +
	prot(name = 'araB', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sr_araB_rbs', 1.000000))
Rule('sr_araA_rbs',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'araA', type = 'rbs', loc = 'cyt', prot = 1) +
	rna(name = 'araA', type = 'cds', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RIBOSOME_CPLX', rna = 1) %
	rna(name = 'araA', type = 'cds', loc = 'cyt', prot = 1) +
	rna(name = 'araA', type = 'rbs', loc = 'cyt', prot = None) +
	prot(name = 'araA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sr_araA_rbs', 1.000000))
Rule('sr_araD_rbs',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'araD', type = 'rbs', loc = 'cyt', prot = 1) +
	rna(name = 'araD', type = 'cds', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RIBOSOME_CPLX', rna = 1) %
	rna(name = 'araD', type = 'cds', loc = 'cyt', prot = 1) +
	rna(name = 'araD', type = 'rbs', loc = 'cyt', prot = None) +
	prot(name = 'araD', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sr_araD_rbs', 1.000000))
Rule('sr_araC_rbs',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'araC', type = 'rbs', loc = 'cyt', prot = 1) +
	rna(name = 'araC', type = 'cds', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RIBOSOME_CPLX', rna = 1) %
	rna(name = 'araC', type = 'cds', loc = 'cyt', prot = 1) +
	rna(name = 'araC', type = 'rbs', loc = 'cyt', prot = None) +
	prot(name = 'araC', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sr_araC_rbs', 1.000000))
Rule('sr_araE_rbs',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'araE', type = 'rbs', loc = 'cyt', prot = 1) +
	rna(name = 'araE', type = 'cds', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RIBOSOME_CPLX', rna = 1) %
	rna(name = 'araE', type = 'cds', loc = 'cyt', prot = 1) +
	rna(name = 'araE', type = 'rbs', loc = 'cyt', prot = None) +
	prot(name = 'araE', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sr_araE_rbs', 1.000000))
Rule('sr_araF_rbs',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'araF', type = 'rbs', loc = 'cyt', prot = 1) +
	rna(name = 'araF', type = 'cds', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RIBOSOME_CPLX', rna = 1) %
	rna(name = 'araF', type = 'cds', loc = 'cyt', prot = 1) +
	rna(name = 'araF', type = 'rbs', loc = 'cyt', prot = None) +
	prot(name = 'araF', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sr_araF_rbs', 1.000000))
Rule('sr_araG_rbs',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'araG', type = 'rbs', loc = 'cyt', prot = 1) +
	rna(name = 'araG', type = 'cds', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RIBOSOME_CPLX', rna = 1) %
	rna(name = 'araG', type = 'cds', loc = 'cyt', prot = 1) +
	rna(name = 'araG', type = 'rbs', loc = 'cyt', prot = None) +
	prot(name = 'araG', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sr_araG_rbs', 1.000000))
Rule('sr_araH_rbs',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'araH', type = 'rbs', loc = 'cyt', prot = 1) +
	rna(name = 'araH', type = 'cds', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RIBOSOME_CPLX', rna = 1) %
	rna(name = 'araH', type = 'cds', loc = 'cyt', prot = 1) +
	rna(name = 'araH', type = 'rbs', loc = 'cyt', prot = None) +
	prot(name = 'araH', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sr_araH_rbs', 1.000000))
Rule('sr_rpoA_rbs',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'rpoA', type = 'rbs', loc = 'cyt', prot = 1) +
	rna(name = 'rpoA', type = 'cds', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RIBOSOME_CPLX', rna = 1) %
	rna(name = 'rpoA', type = 'cds', loc = 'cyt', prot = 1) +
	rna(name = 'rpoA', type = 'rbs', loc = 'cyt', prot = None) +
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sr_rpoA_rbs', 1.000000))
Rule('sr_rpoB_rbs',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'rpoB', type = 'rbs', loc = 'cyt', prot = 1) +
	rna(name = 'rpoB', type = 'cds', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RIBOSOME_CPLX', rna = 1) %
	rna(name = 'rpoB', type = 'cds', loc = 'cyt', prot = 1) +
	rna(name = 'rpoB', type = 'rbs', loc = 'cyt', prot = None) +
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sr_rpoB_rbs', 1.000000))
Rule('sr_rpoC_rbs',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'rpoC', type = 'rbs', loc = 'cyt', prot = 1) +
	rna(name = 'rpoC', type = 'cds', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RIBOSOME_CPLX', rna = 1) %
	rna(name = 'rpoC', type = 'cds', loc = 'cyt', prot = 1) +
	rna(name = 'rpoC', type = 'rbs', loc = 'cyt', prot = None) +
	prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sr_rpoC_rbs', 1.000000))
Rule('sr_rpoD_rbs',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'rpoD', type = 'rbs', loc = 'cyt', prot = 1) +
	rna(name = 'rpoD', type = 'cds', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RIBOSOME_CPLX', rna = 1) %
	rna(name = 'rpoD', type = 'cds', loc = 'cyt', prot = 1) +
	rna(name = 'rpoD', type = 'rbs', loc = 'cyt', prot = None) +
	prot(name = 'rpoD', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sr_rpoD_rbs', 1.000000))
Rule('fr_araB_cds',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'araB', type = 'cds', loc = 'cyt', prot = 1) >>
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = None) +
	rna(name = 'araB', type = 'cds', loc = 'cyt', prot = None),
	Parameter('fwd_fr_araB_cds', 1.000000))
Rule('fr_araA_cds',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'araA', type = 'cds', loc = 'cyt', prot = 1) >>
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = None) +
	rna(name = 'araA', type = 'cds', loc = 'cyt', prot = None),
	Parameter('fwd_fr_araA_cds', 1.000000))
Rule('fr_araD_cds',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'araD', type = 'cds', loc = 'cyt', prot = 1) >>
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = None) +
	rna(name = 'araD', type = 'cds', loc = 'cyt', prot = None),
	Parameter('fwd_fr_araD_cds', 1.000000))
Rule('fr_araC_cds',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'araC', type = 'cds', loc = 'cyt', prot = 1) >>
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = None) +
	rna(name = 'araC', type = 'cds', loc = 'cyt', prot = None),
	Parameter('fwd_fr_araC_cds', 1.000000))
Rule('fr_araE_cds',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'araE', type = 'cds', loc = 'cyt', prot = 1) >>
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = None) +
	rna(name = 'araE', type = 'cds', loc = 'cyt', prot = None),
	Parameter('fwd_fr_araE_cds', 1.000000))
Rule('fr_araF_cds',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'araF', type = 'cds', loc = 'cyt', prot = 1) >>
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = None) +
	rna(name = 'araF', type = 'cds', loc = 'cyt', prot = None),
	Parameter('fwd_fr_araF_cds', 1.000000))
Rule('fr_araG_cds',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'araG', type = 'cds', loc = 'cyt', prot = 1) >>
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = None) +
	rna(name = 'araG', type = 'cds', loc = 'cyt', prot = None),
	Parameter('fwd_fr_araG_cds', 1.000000))
Rule('fr_araH_cds',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'araH', type = 'cds', loc = 'cyt', prot = 1) >>
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = None) +
	rna(name = 'araH', type = 'cds', loc = 'cyt', prot = None),
	Parameter('fwd_fr_araH_cds', 1.000000))
Rule('fr_rpoA_cds',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'rpoA', type = 'cds', loc = 'cyt', prot = 1) >>
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = None) +
	rna(name = 'rpoA', type = 'cds', loc = 'cyt', prot = None),
	Parameter('fwd_fr_rpoA_cds', 1.000000))
Rule('fr_rpoB_cds',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'rpoB', type = 'cds', loc = 'cyt', prot = 1) >>
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = None) +
	rna(name = 'rpoB', type = 'cds', loc = 'cyt', prot = None),
	Parameter('fwd_fr_rpoB_cds', 1.000000))
Rule('fr_rpoC_cds',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'rpoC', type = 'cds', loc = 'cyt', prot = 1) >>
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = None) +
	rna(name = 'rpoC', type = 'cds', loc = 'cyt', prot = None),
	Parameter('fwd_fr_rpoC_cds', 1.000000))
Rule('fr_rpoD_cds',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'rpoD', type = 'cds', loc = 'cyt', prot = 1) >>
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = None) +
	rna(name = 'rpoD', type = 'cds', loc = 'cyt', prot = None),
	Parameter('fwd_fr_rpoD_cds', 1.000000))
Initial(prot(name = 'araB', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('t0_prot_araB_cyt', 0))
Observable('obs_prot_araB_cyt',
	prot(name = 'araB', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Initial(prot(name = 'araA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('t0_prot_araA_cyt', 0))
Observable('obs_prot_araA_cyt',
	prot(name = 'araA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Initial(prot(name = 'araD', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('t0_prot_araD_cyt', 0))
Observable('obs_prot_araD_cyt',
	prot(name = 'araD', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Initial(dna(name = 'araB', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	dna(name = 'araB', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	dna(name = 'araB', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	dna(name = 'araA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	dna(name = 'araA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	dna(name = 'araD', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	dna(name = 'araD', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	dna(name = 'araD', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = None),
	Parameter('t0_dna_araBaraAaraD', 0))
Observable('obs_dna_araBaraAaraD',
	dna(name = 'araB', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	dna(name = 'araB', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	dna(name = 'araB', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	dna(name = 'araA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	dna(name = 'araA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	dna(name = 'araD', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	dna(name = 'araD', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	dna(name = 'araD', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = None))
Initial(rna(name = 'araB', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'araB', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'araA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'araA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'araD', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	rna(name = 'araD', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	rna(name = 'araD', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = None),
	Parameter('t0_rna_araBaraAaraD_form1', 0))
Observable('obs_rna_araBaraAaraD_form1',
	rna(name = 'araB', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'araB', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'araA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'araA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'araD', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	rna(name = 'araD', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	rna(name = 'araD', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = None))
Initial(prot(name = 'araC', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('t0_prot_araC_cyt', 0))
Observable('obs_prot_araC_cyt',
	prot(name = 'araC', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Initial(dna(name = 'araC', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	dna(name = 'araC_56_72', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	dna(name = 'araC', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	dna(name = 'araC', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	dna(name = 'araC', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = None),
	Parameter('t0_dna_araC', 0))
Observable('obs_dna_araC',
	dna(name = 'araC', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	dna(name = 'araC_56_72', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	dna(name = 'araC', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	dna(name = 'araC', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	dna(name = 'araC', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = None))
Initial(rna(name = 'araC_56_72', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'araC', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'araC', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'araC', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = None),
	Parameter('t0_rna_araC_form1', 0))
Observable('obs_rna_araC_form1',
	rna(name = 'araC_56_72', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'araC', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'araC', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'araC', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = None))
Initial(prot(name = 'araE', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('t0_prot_araE_cyt', 0))
Observable('obs_prot_araE_cyt',
	prot(name = 'araE', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Initial(dna(name = 'araE', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	dna(name = 'araE', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	dna(name = 'araE', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	dna(name = 'araE', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = None),
	Parameter('t0_dna_araE', 0))
Observable('obs_dna_araE',
	dna(name = 'araE', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	dna(name = 'araE', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	dna(name = 'araE', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	dna(name = 'araE', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = None))
Initial(rna(name = 'araE', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'araE', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'araE', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = None),
	Parameter('t0_rna_araE_form1', 0))
Observable('obs_rna_araE_form1',
	rna(name = 'araE', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'araE', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'araE', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = None))
Initial(prot(name = 'araF', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('t0_prot_araF_cyt', 0))
Observable('obs_prot_araF_cyt',
	prot(name = 'araF', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Initial(prot(name = 'araG', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('t0_prot_araG_cyt', 0))
Observable('obs_prot_araG_cyt',
	prot(name = 'araG', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Initial(prot(name = 'araH', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('t0_prot_araH_cyt', 0))
Observable('obs_prot_araH_cyt',
	prot(name = 'araH', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Initial(dna(name = 'araF', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	dna(name = 'araF', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	dna(name = 'araF', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	dna(name = 'araG', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	dna(name = 'araG', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	dna(name = 'araH', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	dna(name = 'araH', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	dna(name = 'araH', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = None),
	Parameter('t0_dna_araFaraGaraH', 0))
Observable('obs_dna_araFaraGaraH',
	dna(name = 'araF', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	dna(name = 'araF', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	dna(name = 'araF', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	dna(name = 'araG', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	dna(name = 'araG', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	dna(name = 'araH', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	dna(name = 'araH', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	dna(name = 'araH', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = None))
Initial(rna(name = 'araF', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'araF', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'araG', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'araG', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'araH', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	rna(name = 'araH', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	rna(name = 'araH', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = None),
	Parameter('t0_rna_araFaraGaraH_form1', 0))
Observable('obs_rna_araFaraGaraH_form1',
	rna(name = 'araF', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'araF', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'araG', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'araG', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'araH', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	rna(name = 'araH', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	rna(name = 'araH', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = None))
Initial(prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('t0_prot_rpoA_cyt', 0))
Observable('obs_prot_rpoA_cyt',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Initial(dna(name = 'rpoA', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	dna(name = 'rpoA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	dna(name = 'rpoA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	dna(name = 'rpoA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = None),
	Parameter('t0_dna_rpoA', 0))
Observable('obs_dna_rpoA',
	dna(name = 'rpoA', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	dna(name = 'rpoA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	dna(name = 'rpoA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	dna(name = 'rpoA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = None))
Initial(rna(name = 'rpoA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'rpoA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'rpoA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = None),
	Parameter('t0_rna_rpoA_form1', 0))
Observable('obs_rna_rpoA_form1',
	rna(name = 'rpoA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'rpoA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'rpoA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = None))
Initial(prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('t0_prot_rpoB_cyt', 0))
Observable('obs_prot_rpoB_cyt',
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Initial(prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('t0_prot_rpoC_cyt', 0))
Observable('obs_prot_rpoC_cyt',
	prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Initial(dna(name = 'rpoB', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	dna(name = 'rpoB', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	dna(name = 'rpoB', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	dna(name = 'rpoC', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	dna(name = 'rpoC', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	dna(name = 'rpoC', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = None),
	Parameter('t0_dna_rpoBrpoC', 0))
Observable('obs_dna_rpoBrpoC',
	dna(name = 'rpoB', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	dna(name = 'rpoB', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	dna(name = 'rpoB', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	dna(name = 'rpoC', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	dna(name = 'rpoC', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	dna(name = 'rpoC', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = None))
Initial(rna(name = 'rpoB', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'rpoB', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'rpoC', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'rpoC', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'rpoC', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = None),
	Parameter('t0_rna_rpoBrpoC_form1', 0))
Observable('obs_rna_rpoBrpoC_form1',
	rna(name = 'rpoB', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'rpoB', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'rpoC', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'rpoC', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'rpoC', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = None))
Initial(prot(name = 'rpoD', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('t0_prot_rpoD_cyt', 0))
Observable('obs_prot_rpoD_cyt',
	prot(name = 'rpoD', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None))
Initial(dna(name = 'rpoD', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	dna(name = 'rpoD', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	dna(name = 'rpoD', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	dna(name = 'rpoD', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = None),
	Parameter('t0_dna_rpoD', 0))
Observable('obs_dna_rpoD',
	dna(name = 'rpoD', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	dna(name = 'rpoD', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	dna(name = 'rpoD', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	dna(name = 'rpoD', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = None))
Initial(rna(name = 'rpoD', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'rpoD', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'rpoD', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = None),
	Parameter('t0_rna_rpoD_form1', 0))
Observable('obs_rna_rpoD_form1',
	rna(name = 'rpoD', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'rpoD', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'rpoD', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = None))
