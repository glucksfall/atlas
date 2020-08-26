from pysb import *
Model()

Monomer('dna',
	['name', 'type', 'loc', 'dna', 'met', 'prot', 'rna', 'up', 'dw'],
	{ 'name' : ['lacA', 'lacY', 'lacZ', 'rpoA', 'rpoB', 'rpoC', 'rpoD'],
	'type' : ['BS', 'cds', 'pro1', 'pro2', 'pro3', 'pro4', 'rbs', 'ter1', 'ter2'],
	'loc' : ['cyt']})
Monomer('rna',
	['name', 'type', 'loc', 'dna', 'met', 'prot', 'rna', 'up', 'dw'],
	{ 'name' : ['lacA', 'lacY', 'lacZ', 'rpoA', 'rpoB', 'rpoC', 'rpoD'],
	'type' : ['BS', 'cds', 'pro1', 'pro2', 'pro3', 'pro4', 'rbs', 'ter1', 'ter2'],
	'loc' : ['cyt']})
Monomer('prot',
	['name', 'loc', 'dna', 'met', 'prot', 'rna', 'up', 'dw'],
	{ 'name' : ['lacA', 'lacY', 'lacZ', 'rpoA', 'rpoB', 'rpoC', 'rpoD'],
	'loc' : ['cyt', 'mem']})
Monomer('cplx',
	['name', 'loc', 'dna', 'met', 'prot', 'rna'],
	{ 'name' : ['RIBOSOME_CPLX'],
	'loc' : ['cyt']})
Rule('docking_1_lacZ_pro4',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, up = 3, dw = 4) %
	prot(name = 'rpoD', loc = 'cyt', dna = None, met = None, up = 4, dw = None) +
	dna(name = 'lacZ', type = 'pro4', loc = 'cyt', prot = None, up = WILD, dw = WILD) |
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, up = 3, dw = 4) %
	prot(name = 'rpoD', loc = 'cyt', dna = 5, met = None, up = 4, dw = None) %
	dna(name = 'lacZ', type = 'pro4', loc = 'cyt', prot = 5, up = WILD, dw = WILD),
	Parameter('fwd_docking_1_lacZ_pro4', 1.000000),
	Parameter('rvs_docking_1_lacZ_pro4', 1.000000))
Rule('docking_2_lacZ_pro3',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, up = 3, dw = 4) %
	prot(name = 'rpoD', loc = 'cyt', dna = None, met = None, up = 4, dw = None) +
	dna(name = 'lacZ', type = 'pro3', loc = 'cyt', prot = None, up = WILD, dw = WILD) |
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, up = 3, dw = 4) %
	prot(name = 'rpoD', loc = 'cyt', dna = 5, met = None, up = 4, dw = None) %
	dna(name = 'lacZ', type = 'pro3', loc = 'cyt', prot = 5, up = WILD, dw = WILD),
	Parameter('fwd_docking_2_lacZ_pro3', 1.000000),
	Parameter('rvs_docking_2_lacZ_pro3', 1.000000))
Rule('docking_3_lacZ_pro2',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, up = 3, dw = 4) %
	prot(name = 'rpoD', loc = 'cyt', dna = None, met = None, up = 4, dw = None) +
	dna(name = 'lacZ', type = 'pro2', loc = 'cyt', prot = None, up = WILD, dw = WILD) |
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, up = 3, dw = 4) %
	prot(name = 'rpoD', loc = 'cyt', dna = 5, met = None, up = 4, dw = None) %
	dna(name = 'lacZ', type = 'pro2', loc = 'cyt', prot = 5, up = WILD, dw = WILD),
	Parameter('fwd_docking_3_lacZ_pro2', 1.000000),
	Parameter('rvs_docking_3_lacZ_pro2', 1.000000))
Rule('docking_4_lacZ_pro1',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, up = 3, dw = 4) %
	prot(name = 'rpoD', loc = 'cyt', dna = None, met = None, up = 4, dw = None) +
	dna(name = 'lacZ', type = 'pro1', loc = 'cyt', prot = None, up = WILD, dw = WILD) |
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, up = 3, dw = 4) %
	prot(name = 'rpoD', loc = 'cyt', dna = 5, met = None, up = 4, dw = None) %
	dna(name = 'lacZ', type = 'pro1', loc = 'cyt', prot = 5, up = WILD, dw = WILD),
	Parameter('fwd_docking_4_lacZ_pro1', 1.000000),
	Parameter('rvs_docking_4_lacZ_pro1', 1.000000))
Rule('docking_5_lacY_pro1',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, up = 3, dw = 4) %
	prot(name = 'rpoD', loc = 'cyt', dna = None, met = None, up = 4, dw = None) +
	dna(name = 'lacY', type = 'pro1', loc = 'cyt', prot = None, up = WILD, dw = WILD) |
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, up = 3, dw = 4) %
	prot(name = 'rpoD', loc = 'cyt', dna = 5, met = None, up = 4, dw = None) %
	dna(name = 'lacY', type = 'pro1', loc = 'cyt', prot = 5, up = WILD, dw = WILD),
	Parameter('fwd_docking_5_lacY_pro1', 1.000000),
	Parameter('rvs_docking_5_lacY_pro1', 1.000000))
Rule('sliding_1_lacZ_pro4_pro3_holoenzyme',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, up = 3, dw = 4) %
	prot(name = 'rpoD', loc = 'cyt', dna = 5, met = None, up = 4, dw = None) %
	dna(name = 'lacZ', type = 'pro4', loc = 'cyt', prot = 5, up = WILD, dw = WILD) +
	dna(name = 'lacZ', type = 'pro3', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	None >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'lacZ', type = 'pro3', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'lacZ', type = 'pro4', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	rna(name = 'lacZ', type = 'pro3', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_1_lacZ_pro4_pro3_holoenzyme', 1.000000))
Rule('sliding_2_lacZ_pro3_pro2_holoenzyme',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, up = 3, dw = 4) %
	prot(name = 'rpoD', loc = 'cyt', dna = 5, met = None, up = 4, dw = None) %
	dna(name = 'lacZ', type = 'pro3', loc = 'cyt', prot = 5, up = WILD, dw = WILD) +
	dna(name = 'lacZ', type = 'pro2', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	None >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'lacZ', type = 'pro2', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'lacZ', type = 'pro3', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	rna(name = 'lacZ', type = 'pro2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_2_lacZ_pro3_pro2_holoenzyme', 1.000000))
Rule('sliding_3_lacZ_pro2_pro1_holoenzyme',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, up = 3, dw = 4) %
	prot(name = 'rpoD', loc = 'cyt', dna = 5, met = None, up = 4, dw = None) %
	dna(name = 'lacZ', type = 'pro2', loc = 'cyt', prot = 5, up = WILD, dw = WILD) +
	dna(name = 'lacZ', type = 'pro1', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	None >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'lacZ', type = 'pro1', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'lacZ', type = 'pro2', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	rna(name = 'lacZ', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_3_lacZ_pro2_pro1_holoenzyme', 1.000000))
Rule('sliding_4_lacZ_pro1_rbs_holoenzyme',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, up = 3, dw = 4) %
	prot(name = 'rpoD', loc = 'cyt', dna = 5, met = None, up = 4, dw = None) %
	dna(name = 'lacZ', type = 'pro1', loc = 'cyt', prot = 5, up = WILD, dw = WILD) +
	dna(name = 'lacZ', type = 'rbs', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	None >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'lacZ', type = 'rbs', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'lacZ', type = 'pro1', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	rna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_4_lacZ_pro1_rbs_holoenzyme', 1.000000))
Rule('sliding_5_lacY_pro1_rbs_holoenzyme',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, up = 3, dw = 4) %
	prot(name = 'rpoD', loc = 'cyt', dna = 5, met = None, up = 4, dw = None) %
	dna(name = 'lacY', type = 'pro1', loc = 'cyt', prot = 5, up = WILD, dw = WILD) +
	dna(name = 'lacY', type = 'rbs', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	None >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'lacY', type = 'rbs', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'lacY', type = 'pro1', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_5_lacY_pro1_rbs_holoenzyme', 1.000000))
Rule('sliding_1_lacZ_pro3_to_lacZ_pro2',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'lacZ', type = 'pro3', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'lacZ', type = 'pro2', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	None >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'lacZ', type = 'pro2', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'lacZ', type = 'pro3', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	rna(name = 'lacZ', type = 'pro2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_1_lacZ_pro3_to_lacZ_pro2', 1.000000))
Rule('sliding_2_lacZ_pro2_to_lacZ_pro1',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'lacZ', type = 'pro2', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'lacZ', type = 'pro1', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	None >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'lacZ', type = 'pro1', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'lacZ', type = 'pro2', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	rna(name = 'lacZ', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_2_lacZ_pro2_to_lacZ_pro1', 1.000000))
Rule('sliding_3_lacZ_pro1_to_lacZ_rbs',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'lacZ', type = 'pro1', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'lacZ', type = 'rbs', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	None >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'lacZ', type = 'rbs', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'lacZ', type = 'pro1', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	rna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_3_lacZ_pro1_to_lacZ_rbs', 1.000000))
Rule('sliding_4_lacZ_rbs_to_lacZ_cds',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'lacZ', type = 'rbs', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'lacZ', type = 'cds', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	None >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'lacZ', type = 'cds', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'lacZ', type = 'rbs', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_4_lacZ_rbs_to_lacZ_cds', 1.000000))
Rule('sliding_5_lacZ_cds_to_lacY_pro1',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'lacZ', type = 'cds', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'lacY', type = 'pro1', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	None >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'lacY', type = 'pro1', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'lacZ', type = 'cds', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	rna(name = 'lacY', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_5_lacZ_cds_to_lacY_pro1', 1.000000))
Rule('sliding_6_lacY_pro1_to_lacY_rbs',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'lacY', type = 'pro1', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'lacY', type = 'rbs', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	None >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'lacY', type = 'rbs', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'lacY', type = 'pro1', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_6_lacY_pro1_to_lacY_rbs', 1.000000))
Rule('sliding_7_lacY_rbs_to_lacY_cds',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'lacY', type = 'rbs', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'lacY', type = 'cds', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	None >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'lacY', type = 'cds', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'lacY', type = 'rbs', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	rna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_7_lacY_rbs_to_lacY_cds', 1.000000))
Rule('sliding_8_lacY_cds_to_lacA_rbs',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'lacY', type = 'cds', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'lacA', type = 'rbs', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	None >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'lacA', type = 'rbs', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'lacY', type = 'cds', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_8_lacY_cds_to_lacA_rbs', 1.000000))
Rule('sliding_9_lacA_rbs_to_lacA_cds',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'lacA', type = 'rbs', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'lacA', type = 'cds', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	None >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'lacA', type = 'cds', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'lacA', type = 'rbs', loc = 'cyt', prot = None, up = WILD, dw = WILD) +
	rna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_9_lacA_rbs_to_lacA_cds', 1.000000))
Rule('sliding_10_lacA_cds_to_lacA_ter1',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'lacA', type = 'cds', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'lacA', type = 'ter1', loc = 'cyt', prot = None, up = WILD, dw = WILD) >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'lacA', type = 'ter1', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'lacA', type = 'cds', loc = 'cyt', prot = None, up = WILD, dw = WILD),
	Parameter('fwd_sliding_10_lacA_cds_to_lacA_ter1', 1.000000))
Rule('sliding_11_lacA_ter1_to_lacA_ter2',
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'lacA', type = 'ter1', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'lacA', type = 'ter2', loc = 'cyt', prot = None, up = WILD, dw = WILD) >>
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'lacA', type = 'ter2', loc = 'cyt', prot = 4, up = WILD, dw = WILD) +
	dna(name = 'lacA', type = 'ter1', loc = 'cyt', prot = None, up = WILD, dw = WILD),
	Parameter('fwd_sliding_11_lacA_ter1_to_lacA_ter2', 1.000000))
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
Rule('falloff_from_lacA_ter1', 
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'lacA', type = 'ter1', loc = 'cyt', prot = 4, up = WILD, dw = WILD) >> 
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, up = 3, dw = None) +
	dna(name = 'lacA', type = 'ter1', loc = 'cyt', prot = None, up = WILD, dw = WILD), 
	Parameter('fwd_falloff_from_lacA_ter1', 1.000000))
Rule('falloff_from_lacA_ter2', 
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = 4, met = None, up = 3, dw = None) %
	dna(name = 'lacA', type = 'ter2', loc = 'cyt', prot = 4, up = WILD, dw = WILD) >> 
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = None, dw = 1) %
	prot(name = 'rpoA', loc = 'cyt', dna = None, met = None, up = 1, dw = 2) %
	prot(name = 'rpoB', loc = 'cyt', dna = None, met = None, up = 2, dw = 3) %
	prot(name = 'rpoC', loc = 'cyt', dna = None, met = None, up = 3, dw = None) +
	dna(name = 'lacA', type = 'ter2', loc = 'cyt', prot = None, up = WILD, dw = WILD), 
	Parameter('fwd_falloff_from_lacA_ter2', 1.000000))
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
Rule('sr_lacZ_rbs',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'lacZ', type = 'rbs', loc = 'cyt', prot = 1) +
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RIBOSOME_CPLX', rna = 1) %
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', prot = 1) +
	rna(name = 'lacZ', type = 'rbs', loc = 'cyt', prot = None) +
	prot(name = 'lacZ', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sr_lacZ_rbs', 1.000000))
Rule('sr_lacY_rbs',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', prot = 1) +
	rna(name = 'lacY', type = 'cds', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RIBOSOME_CPLX', rna = 1) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', prot = 1) +
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', prot = None) +
	prot(name = 'lacY', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sr_lacY_rbs', 1.000000))
Rule('sr_lacA_rbs',
	cplx(name = 'RIBOSOME_CPLX', loc = 'cyt', rna = 1) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', prot = 1) +
	rna(name = 'lacA', type = 'cds', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RIBOSOME_CPLX', rna = 1) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', prot = 1) +
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', prot = None) +
	prot(name = 'lacA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sr_lacA_rbs', 1.000000))
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
	dna(name = 'lacZ', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	dna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	dna(name = 'lacZ', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	dna(name = 'lacY', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	dna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = 8) %
	dna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 8, dw = 9) %
	dna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 9, dw = 10) %
	dna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 10, dw = 11) %
	dna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 11, dw = 12) %
	dna(name = 'lacA', type = 'ter2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 12, dw = None),
	Parameter('t0_dna_lacZlacYlacA', 0))
Observable('obs_dna_lacZlacYlacA',
	dna(name = 'lacZ', type = 'pro4', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	dna(name = 'lacZ', type = 'pro3', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	dna(name = 'lacZ', type = 'pro2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	dna(name = 'lacZ', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	dna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	dna(name = 'lacZ', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	dna(name = 'lacY', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	dna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = 8) %
	dna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 8, dw = 9) %
	dna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 9, dw = 10) %
	dna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 10, dw = 11) %
	dna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 11, dw = 12) %
	dna(name = 'lacA', type = 'ter2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 12, dw = None))
Initial(rna(name = 'lacZ', type = 'pro3', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'lacZ', type = 'pro2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'lacZ', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	rna(name = 'lacY', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = 8) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 8, dw = 9) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 9, dw = 10) %
	rna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 10, dw = None),
	Parameter('t0_rna_lacZlacYlacA_form1', 0))
Observable('obs_rna_lacZlacYlacA_form1',
	rna(name = 'lacZ', type = 'pro3', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'lacZ', type = 'pro2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'lacZ', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	rna(name = 'lacY', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = 8) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 8, dw = 9) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 9, dw = 10) %
	rna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 10, dw = None))
Initial(rna(name = 'lacZ', type = 'pro3', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'lacZ', type = 'pro2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'lacZ', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	rna(name = 'lacY', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = 8) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 8, dw = 9) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 9, dw = 10) %
	rna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 10, dw = 11) %
	rna(name = 'lacA', type = 'ter2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 11, dw = None),
	Parameter('t0_rna_lacZlacYlacA_form2', 0))
Observable('obs_rna_lacZlacYlacA_form2',
	rna(name = 'lacZ', type = 'pro3', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'lacZ', type = 'pro2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'lacZ', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	rna(name = 'lacY', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = 8) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 8, dw = 9) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 9, dw = 10) %
	rna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 10, dw = 11) %
	rna(name = 'lacA', type = 'ter2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 11, dw = None))
Initial(rna(name = 'lacZ', type = 'pro2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'lacZ', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'lacY', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = 8) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 8, dw = 9) %
	rna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 9, dw = None),
	Parameter('t0_rna_lacZlacYlacA_form3', 0))
Observable('obs_rna_lacZlacYlacA_form3',
	rna(name = 'lacZ', type = 'pro2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'lacZ', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'lacY', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = 8) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 8, dw = 9) %
	rna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 9, dw = None))
Initial(rna(name = 'lacZ', type = 'pro2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'lacZ', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'lacY', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = 8) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 8, dw = 9) %
	rna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 9, dw = 10) %
	rna(name = 'lacA', type = 'ter2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 10, dw = None),
	Parameter('t0_rna_lacZlacYlacA_form4', 0))
Observable('obs_rna_lacZlacYlacA_form4',
	rna(name = 'lacZ', type = 'pro2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'lacZ', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'lacY', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = 8) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 8, dw = 9) %
	rna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 9, dw = 10) %
	rna(name = 'lacA', type = 'ter2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 10, dw = None))
Initial(rna(name = 'lacZ', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'lacY', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = 8) %
	rna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 8, dw = None),
	Parameter('t0_rna_lacZlacYlacA_form5', 0))
Observable('obs_rna_lacZlacYlacA_form5',
	rna(name = 'lacZ', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'lacY', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = 8) %
	rna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 8, dw = None))
Initial(rna(name = 'lacZ', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'lacY', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = 8) %
	rna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 8, dw = 9) %
	rna(name = 'lacA', type = 'ter2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 9, dw = None),
	Parameter('t0_rna_lacZlacYlacA_form6', 0))
Observable('obs_rna_lacZlacYlacA_form6',
	rna(name = 'lacZ', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'lacY', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = 8) %
	rna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 8, dw = 9) %
	rna(name = 'lacA', type = 'ter2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 9, dw = None))
Initial(rna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'lacY', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	rna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = None),
	Parameter('t0_rna_lacZlacYlacA_form7', 0))
Observable('obs_rna_lacZlacYlacA_form7',
	rna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'lacY', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	rna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = None))
Initial(rna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'lacY', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	rna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = 8) %
	rna(name = 'lacA', type = 'ter2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 8, dw = None),
	Parameter('t0_rna_lacZlacYlacA_form8', 0))
Observable('obs_rna_lacZlacYlacA_form8',
	rna(name = 'lacZ', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = 1) %
	rna(name = 'lacZ', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 1, dw = 2) %
	rna(name = 'lacY', type = 'pro1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 2, dw = 3) %
	rna(name = 'lacY', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 3, dw = 4) %
	rna(name = 'lacY', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 4, dw = 5) %
	rna(name = 'lacA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 5, dw = 6) %
	rna(name = 'lacA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 6, dw = 7) %
	rna(name = 'lacA', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 7, dw = 8) %
	rna(name = 'lacA', type = 'ter2', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = 8, dw = None))
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
