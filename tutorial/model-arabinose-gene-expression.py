from pysb import *
Model()

Monomer('dna',
	['name', 'type', 'loc', 'dna', 'met', 'prot', 'rna', 'up', 'dw'],
	{ 'name' : ['araA', 'araB', 'araC', 'araC_56_72', 'araD', 'araE', 'araF', 'araG', 'araH'],
	'type' : ['BS', 'cds', 'pro1', 'rbs', 'ter1'],
	'loc' : ['cyt']})
Monomer('rna',
	['name', 'type', 'loc', 'dna', 'met', 'prot', 'rna', 'up', 'dw'],
	{ 'name' : ['araA', 'araB', 'araC', 'araC_56_72', 'araD', 'araE', 'araF', 'araG', 'araH'],
	'type' : ['BS', 'cds', 'pro1', 'rbs', 'ter1'],
	'loc' : ['cyt']})
Monomer('prot',
	['name', 'loc', 'dna', 'met', 'prot', 'rna', 'up', 'dw'],
	{ 'name' : ['araA', 'araB', 'araC', 'araC_56_72', 'araD', 'araE', 'araF', 'araG', 'araH'],
	'loc' : ['cyt', 'mem']})
Monomer('cplx',
	['name', 'loc', 'dna', 'met', 'prot', 'rna'],
	{ 'name' : ['RNAP_CPLX', 'RIBOSOME_CPLX'],
	'loc' : ['cyt']})
Rule('docking_araB_pro1',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = None) +
	dna(name = 'araB', type = 'pro1', loc = 'cyt', prot = None) |
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araB', type = 'pro1', loc = 'cyt', prot = 1),
	Parameter('fwd_docking_araB_pro1', 1.000000),
	Parameter('rvs_docking_araB_pro1', 1.000000))
Rule('docking_araC_pro1',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = None) +
	dna(name = 'araC', type = 'pro1', loc = 'cyt', prot = None) |
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araC', type = 'pro1', loc = 'cyt', prot = 1),
	Parameter('fwd_docking_araC_pro1', 1.000000),
	Parameter('rvs_docking_araC_pro1', 1.000000))
Rule('docking_araE_pro1',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = None) +
	dna(name = 'araE', type = 'pro1', loc = 'cyt', prot = None) |
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araE', type = 'pro1', loc = 'cyt', prot = 1),
	Parameter('fwd_docking_araE_pro1', 1.000000),
	Parameter('rvs_docking_araE_pro1', 1.000000))
Rule('docking_araF_pro1',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = None) +
	dna(name = 'araF', type = 'pro1', loc = 'cyt', prot = None) |
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araF', type = 'pro1', loc = 'cyt', prot = 1),
	Parameter('fwd_docking_araF_pro1', 1.000000),
	Parameter('rvs_docking_araF_pro1', 1.000000))
Rule('sliding_araB_pro1',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araB', type = 'pro1', loc = 'cyt', prot = 1) +
	dna(name = 'araB', type = 'rbs', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araB', type = 'rbs', loc = 'cyt', prot = 1) +
	dna(name = 'araB', type = 'pro1', loc = 'cyt', prot = None) +
	rna(name = 'araB', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_araB_pro1', 1.000000))
Rule('sliding_araB_rbs',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araB', type = 'rbs', loc = 'cyt', prot = 1) +
	dna(name = 'araB', type = 'cds', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araB', type = 'cds', loc = 'cyt', prot = 1) +
	dna(name = 'araB', type = 'rbs', loc = 'cyt', prot = None) +
	rna(name = 'araB', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_araB_rbs', 1.000000))
Rule('sliding_araB_cds',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araB', type = 'cds', loc = 'cyt', prot = 1) +
	dna(name = 'araA', type = 'rbs', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araA', type = 'rbs', loc = 'cyt', prot = 1) +
	dna(name = 'araB', type = 'cds', loc = 'cyt', prot = None) +
	rna(name = 'araA', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_araB_cds', 1.000000))
Rule('sliding_araA_rbs',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araA', type = 'rbs', loc = 'cyt', prot = 1) +
	dna(name = 'araA', type = 'cds', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araA', type = 'cds', loc = 'cyt', prot = 1) +
	dna(name = 'araA', type = 'rbs', loc = 'cyt', prot = None) +
	rna(name = 'araA', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_araA_rbs', 1.000000))
Rule('sliding_araA_cds',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araA', type = 'cds', loc = 'cyt', prot = 1) +
	dna(name = 'araD', type = 'rbs', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araD', type = 'rbs', loc = 'cyt', prot = 1) +
	dna(name = 'araA', type = 'cds', loc = 'cyt', prot = None) +
	rna(name = 'araD', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_araA_cds', 1.000000))
Rule('sliding_araD_rbs',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araD', type = 'rbs', loc = 'cyt', prot = 1) +
	dna(name = 'araD', type = 'cds', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araD', type = 'cds', loc = 'cyt', prot = 1) +
	dna(name = 'araD', type = 'rbs', loc = 'cyt', prot = None) +
	rna(name = 'araD', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_araD_rbs', 1.000000))
Rule('sliding_araD_cds',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araD', type = 'cds', loc = 'cyt', prot = 1) +
	dna(name = 'araD', type = 'ter1', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araD', type = 'ter1', loc = 'cyt', prot = 1) +
	dna(name = 'araD', type = 'cds', loc = 'cyt', prot = None) +
	rna(name = 'araD', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_araD_cds', 1.000000))
Rule('sliding_araC_pro1',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araC', type = 'pro1', loc = 'cyt', prot = 1) +
	dna(name = 'araC_56_72', type = 'BS', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araC_56_72', type = 'BS', loc = 'cyt', prot = 1) +
	dna(name = 'araC', type = 'pro1', loc = 'cyt', prot = None) +
	rna(name = 'araC_56_72', type = 'BS', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_araC_pro1', 1.000000))
Rule('sliding_BS_araC_56_72',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araC_56_72', type = 'BS', loc = 'cyt', prot = 1) +
	dna(name = 'araC', type = 'rbs', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araC', type = 'rbs', loc = 'cyt', prot = 1) +
	dna(name = 'araC_56_72', type = 'BS', loc = 'cyt', prot = None) +
	rna(name = 'araC', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_BS_araC_56_72', 1.000000))
Rule('sliding_araC_rbs',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araC', type = 'rbs', loc = 'cyt', prot = 1) +
	dna(name = 'araC', type = 'cds', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araC', type = 'cds', loc = 'cyt', prot = 1) +
	dna(name = 'araC', type = 'rbs', loc = 'cyt', prot = None) +
	rna(name = 'araC', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_araC_rbs', 1.000000))
Rule('sliding_araC_cds',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araC', type = 'cds', loc = 'cyt', prot = 1) +
	dna(name = 'araC', type = 'ter1', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araC', type = 'ter1', loc = 'cyt', prot = 1) +
	dna(name = 'araC', type = 'cds', loc = 'cyt', prot = None) +
	rna(name = 'araC', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_araC_cds', 1.000000))
Rule('sliding_araE_pro1',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araE', type = 'pro1', loc = 'cyt', prot = 1) +
	dna(name = 'araE', type = 'rbs', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araE', type = 'rbs', loc = 'cyt', prot = 1) +
	dna(name = 'araE', type = 'pro1', loc = 'cyt', prot = None) +
	rna(name = 'araE', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_araE_pro1', 1.000000))
Rule('sliding_araE_rbs',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araE', type = 'rbs', loc = 'cyt', prot = 1) +
	dna(name = 'araE', type = 'cds', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araE', type = 'cds', loc = 'cyt', prot = 1) +
	dna(name = 'araE', type = 'rbs', loc = 'cyt', prot = None) +
	rna(name = 'araE', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_araE_rbs', 1.000000))
Rule('sliding_araE_cds',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araE', type = 'cds', loc = 'cyt', prot = 1) +
	dna(name = 'araE', type = 'ter1', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araE', type = 'ter1', loc = 'cyt', prot = 1) +
	dna(name = 'araE', type = 'cds', loc = 'cyt', prot = None) +
	rna(name = 'araE', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_araE_cds', 1.000000))
Rule('sliding_araF_pro1',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araF', type = 'pro1', loc = 'cyt', prot = 1) +
	dna(name = 'araF', type = 'rbs', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araF', type = 'rbs', loc = 'cyt', prot = 1) +
	dna(name = 'araF', type = 'pro1', loc = 'cyt', prot = None) +
	rna(name = 'araF', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_araF_pro1', 1.000000))
Rule('sliding_araF_rbs',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araF', type = 'rbs', loc = 'cyt', prot = 1) +
	dna(name = 'araF', type = 'cds', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araF', type = 'cds', loc = 'cyt', prot = 1) +
	dna(name = 'araF', type = 'rbs', loc = 'cyt', prot = None) +
	rna(name = 'araF', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_araF_rbs', 1.000000))
Rule('sliding_araF_cds',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araF', type = 'cds', loc = 'cyt', prot = 1) +
	dna(name = 'araG', type = 'rbs', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araG', type = 'rbs', loc = 'cyt', prot = 1) +
	dna(name = 'araF', type = 'cds', loc = 'cyt', prot = None) +
	rna(name = 'araG', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_araF_cds', 1.000000))
Rule('sliding_araG_rbs',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araG', type = 'rbs', loc = 'cyt', prot = 1) +
	dna(name = 'araG', type = 'cds', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araG', type = 'cds', loc = 'cyt', prot = 1) +
	dna(name = 'araG', type = 'rbs', loc = 'cyt', prot = None) +
	rna(name = 'araG', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_araG_rbs', 1.000000))
Rule('sliding_araG_cds',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araG', type = 'cds', loc = 'cyt', prot = 1) +
	dna(name = 'araH', type = 'rbs', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araH', type = 'rbs', loc = 'cyt', prot = 1) +
	dna(name = 'araG', type = 'cds', loc = 'cyt', prot = None) +
	rna(name = 'araH', type = 'rbs', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_araG_cds', 1.000000))
Rule('sliding_araH_rbs',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araH', type = 'rbs', loc = 'cyt', prot = 1) +
	dna(name = 'araH', type = 'cds', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araH', type = 'cds', loc = 'cyt', prot = 1) +
	dna(name = 'araH', type = 'rbs', loc = 'cyt', prot = None) +
	rna(name = 'araH', type = 'cds', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_araH_rbs', 1.000000))
Rule('sliding_araH_cds',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araH', type = 'cds', loc = 'cyt', prot = 1) +
	dna(name = 'araH', type = 'ter1', loc = 'cyt', prot = None) +
	None >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araH', type = 'ter1', loc = 'cyt', prot = 1) +
	dna(name = 'araH', type = 'cds', loc = 'cyt', prot = None) +
	rna(name = 'araH', type = 'ter1', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None),
	Parameter('fwd_sliding_araH_cds', 1.000000))
Rule('falloff_araH_ter1',
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = 1) %
	dna(name = 'araH', type = 'ter1', loc = 'cyt', prot = 1) >>
	cplx(name = 'RNAP_CPLX', loc = 'cyt', dna = None) +
	dna(name = 'araH', type = 'ter1', loc = 'cyt', prot = None),
	Parameter('fwd_falloff_araH_ter1', 1.000000))
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
