Rule('TRANS_RXN_10_alpha_af',
    prot(name = 'araE', loc = 'cyt') +
    met(name = 'PROTON', loc = 'per', prot = None) +
    met(name = 'alpha_L_arabinofuranose', loc = 'per', prot = None) | 
    prot(name = 'araE', loc = 'cyt') +
    met(name = 'PROTON', loc = 'cyt', prot = None) +
    met(name = 'alpha_L_arabinofuranose', loc = 'cyt', prot = None), 
    Parameter('fwd_TRANS_RXN_10_alpha_af', 1), 
    Parameter('rvs_TRANS_RXN_10_alpha_af', 0))

Rule('TRANS_RXN_10_beta_af',
    prot(name = 'araE', loc = 'cyt') +
    met(name = 'PROTON', loc = 'per', prot = None) +
    met(name = 'beta_L_arabinofuranose', loc = 'per', prot = None) | 
    prot(name = 'araE', loc = 'cyt') +
    met(name = 'PROTON', loc = 'cyt', prot = None) +
    met(name = 'beta_L_arabinofuranose', loc = 'cyt', prot = None), 
    Parameter('fwd_TRANS_RXN_10_beta_af', 1), 
    Parameter('rvs_TRANS_RXN_10_beta_af', 0))

Rule('TRANS_RXN_10_alpha_ap',
    prot(name = 'araE', loc = 'cyt') +
    met(name = 'PROTON', loc = 'per', prot = None) +
    met(name = 'alpha_L_arabinopyranose', loc = 'per', prot = None) | 
    prot(name = 'araE', loc = 'cyt') +
    met(name = 'PROTON', loc = 'cyt', prot = None) +
    met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = None), 
    Parameter('fwd_TRANS_RXN_10_alpha_ap', 1), 
    Parameter('rvs_TRANS_RXN_10_alpha_ap', 0))

Rule('TRANS_RXN_10_beta_ap',
    prot(name = 'araE', loc = 'cyt') +
    met(name = 'PROTON', loc = 'per', prot = None) +
    met(name = 'beta_L_arabinopyranose', loc = 'per', prot = None) | 
    prot(name = 'araE', loc = 'cyt') +
    met(name = 'PROTON', loc = 'cyt', prot = None) +
    met(name = 'beta_L_arabinopyranose', loc = 'cyt', prot = None), 
    Parameter('fwd_TRANS_RXN_10_beta_ap', 1), 
    Parameter('rvs_TRANS_RXN_10_beta_ap', 0))

Rule('ABC_2_RXN_alpha_af',
    prot(name = 'araF', loc = 'cyt', up = None, dw = 1) %
    prot(name = 'araH', loc = 'cyt', up = 1, dw = 2) %
    prot(name = 'araH', loc = 'cyt', up = 2, dw = 3) %
    prot(name = 'araG', loc = 'cyt', up = 3, dw = 4) %
    prot(name = 'araG', loc = 'cyt', up = 4, dw = None) +
    met(name = 'WATER', loc = 'cyt', prot = None) +
    met(name = 'ATP', loc = 'cyt', prot = None) +
    met(name = 'alpha_L_arabinofuranose', loc = 'per', prot = None) +
    None | 
    prot(name = 'araF', loc = 'cyt', up = None, dw = 1) %
    prot(name = 'araH', loc = 'cyt', up = 1, dw = 2) %
    prot(name = 'araH', loc = 'cyt', up = 2, dw = 3) %
    prot(name = 'araG', loc = 'cyt', up = 3, dw = 4) %
    prot(name = 'araG', loc = 'cyt', up = 4, dw = None) +
    met(name = 'Pi', loc = 'cyt', prot = None) +
    met(name = 'ADP', loc = 'cyt', prot = None) +
    met(name = 'PROTON', loc = 'cyt', prot = None) +
    met(name = 'alpha_L_arabinofuranose', loc = 'cyt', prot = None), 
    Parameter('fwd_ABC_2_RXN_alpha_af', 1), 
    Parameter('rvs_ABC_2_RXN_alpha_af', 0))

Rule('ABC_2_RXN_beta_af',
    prot(name = 'araF', loc = 'cyt', up = None, dw = 1) %
    prot(name = 'araH', loc = 'cyt', up = 1, dw = 2) %
    prot(name = 'araH', loc = 'cyt', up = 2, dw = 3) %
    prot(name = 'araG', loc = 'cyt', up = 3, dw = 4) %
    prot(name = 'araG', loc = 'cyt', up = 4, dw = None) +
    met(name = 'WATER', loc = 'cyt', prot = None) +
    met(name = 'ATP', loc = 'cyt', prot = None) +
    met(name = 'beta_L_arabinofuranose', loc = 'per', prot = None) +
    None | 
    prot(name = 'araF', loc = 'cyt', up = None, dw = 1) %
    prot(name = 'araH', loc = 'cyt', up = 1, dw = 2) %
    prot(name = 'araH', loc = 'cyt', up = 2, dw = 3) %
    prot(name = 'araG', loc = 'cyt', up = 3, dw = 4) %
    prot(name = 'araG', loc = 'cyt', up = 4, dw = None) +
    met(name = 'Pi', loc = 'cyt', prot = None) +
    met(name = 'ADP', loc = 'cyt', prot = None) +
    met(name = 'PROTON', loc = 'cyt', prot = None) +
    met(name = 'beta_L_arabinofuranose', loc = 'cyt', prot = None), 
    Parameter('fwd_ABC_2_RXN_beta_af', 1), 
    Parameter('rvs_ABC_2_RXN_beta_af', 0))

Rule('ABC_2_RXN_alpha_ap',
    prot(name = 'araF', loc = 'cyt', up = None, dw = 1) %
    prot(name = 'araH', loc = 'cyt', up = 1, dw = 2) %
    prot(name = 'araH', loc = 'cyt', up = 2, dw = 3) %
    prot(name = 'araG', loc = 'cyt', up = 3, dw = 4) %
    prot(name = 'araG', loc = 'cyt', up = 4, dw = None) +
    met(name = 'WATER', loc = 'cyt', prot = None) +
    met(name = 'ATP', loc = 'cyt', prot = None) +
    met(name = 'alpha_L_arabinopyranose', loc = 'per', prot = None) +
    None | 
    prot(name = 'araF', loc = 'cyt', up = None, dw = 1) %
    prot(name = 'araH', loc = 'cyt', up = 1, dw = 2) %
    prot(name = 'araH', loc = 'cyt', up = 2, dw = 3) %
    prot(name = 'araG', loc = 'cyt', up = 3, dw = 4) %
    prot(name = 'araG', loc = 'cyt', up = 4, dw = None) +
    met(name = 'Pi', loc = 'cyt', prot = None) +
    met(name = 'ADP', loc = 'cyt', prot = None) +
    met(name = 'PROTON', loc = 'cyt', prot = None) +
    met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = None), 
    Parameter('fwd_ABC_2_RXN_alpha_ap', 1), 
    Parameter('rvs_ABC_2_RXN_alpha_ap', 0))

Rule('ABC_2_RXN_beta_ap',
    prot(name = 'araF', loc = 'cyt', up = None, dw = 1) %
    prot(name = 'araH', loc = 'cyt', up = 1, dw = 2) %
    prot(name = 'araH', loc = 'cyt', up = 2, dw = 3) %
    prot(name = 'araG', loc = 'cyt', up = 3, dw = 4) %
    prot(name = 'araG', loc = 'cyt', up = 4, dw = None) +
    met(name = 'WATER', loc = 'cyt', prot = None) +
    met(name = 'ATP', loc = 'cyt', prot = None) +
    met(name = 'beta_L_arabinopyranose', loc = 'per', prot = None) +
    None | 
    prot(name = 'araF', loc = 'cyt', up = None, dw = 1) %
    prot(name = 'araH', loc = 'cyt', up = 1, dw = 2) %
    prot(name = 'araH', loc = 'cyt', up = 2, dw = 3) %
    prot(name = 'araG', loc = 'cyt', up = 3, dw = 4) %
    prot(name = 'araG', loc = 'cyt', up = 4, dw = None) +
    met(name = 'Pi', loc = 'cyt', prot = None) +
    met(name = 'ADP', loc = 'cyt', prot = None) +
    met(name = 'PROTON', loc = 'cyt', prot = None) +
    met(name = 'beta_L_arabinopyranose', loc = 'cyt', prot = None), 
    Parameter('fwd_ABC_2_RXN_beta_ap', 1), 
    Parameter('rvs_ABC_2_RXN_beta_ap', 0))

Rule('ARABISOM_RXN_alpha_ap',
    prot(name = 'araA', loc = 'cyt') +
    met(name = 'alpha_L_arabinopyranose', loc = 'cyt', prot = None) | 
    prot(name = 'araA', loc = 'cyt') +
    met(name = 'L_RIBULOSE', loc = 'cyt', prot = None), 
    Parameter('fwd_ARABISOM_RXN_alpha_ap', 1), 
    Parameter('rvs_ARABISOM_RXN_alpha_ap', 0))

Rule('ARABISOM_RXN_beta_ap',
    prot(name = 'araA', loc = 'cyt') +
    met(name = 'beta_L_arabinopyranose', loc = 'cyt', prot = None) | 
    prot(name = 'araA', loc = 'cyt') +
    met(name = 'L_RIBULOSE', loc = 'cyt', prot = None), 
    Parameter('fwd_ARABISOM_RXN_beta_ap', 1), 
    Parameter('rvs_ARABISOM_RXN_beta_ap', 0))

Rule('RXN0_5116',
    prot(name = 'araB', loc = 'cyt') +
    met(name = 'L_RIBULOSE', loc = 'cyt', prot = None) +
    met(name = 'ATP', loc = 'cyt', prot = None) +
    None | 
    prot(name = 'araB', loc = 'cyt') +
    met(name = 'PROTON', loc = 'cyt', prot = None) +
    met(name = 'L_RIBULOSE_5_P', loc = 'cyt', prot = None) +
    met(name = 'ADP', loc = 'cyt', prot = None), 
    Parameter('fwd_RXN0_5116', 1), 
    Parameter('rvs_RXN0_5116', 0))

Rule('RIBULPEPIM_RXN',
    prot(name = 'araD', loc = 'cyt') +
    met(name = 'L_RIBULOSE_5_P', loc = 'cyt', prot = None) | 
    prot(name = 'araD', loc = 'cyt') +
    met(name = 'XYLULOSE_5_PHOSPHATE', loc = 'cyt', prot = None), 
    Parameter('fwd_RIBULPEPIM_RXN', 1), 
    Parameter('rvs_RIBULPEPIM_RXN', 0))

