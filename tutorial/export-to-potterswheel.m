% PottersWheel model definition file
% save as atlas_rbm_construct_model_from_metabolic_network.m
function m = atlas_rbm_construct_model_from_metabolic_network()

m = pwGetEmptyModel();

% meta information
m.ID          = 'atlas_rbm_construct_model_from_metabolic_network';
m.name        = 'atlas_rbm_construct_model_from_metabolic_network';
m.description = '';
m.authors     = {''};
m.dates       = {''};
m.type        = 'PW-1-5';

% dynamic variables
m = pwAddX(m, 's0', 0.000000e+00);
m = pwAddX(m, 's1', 0.000000e+00);
m = pwAddX(m, 's2', 0.000000e+00);
m = pwAddX(m, 's3', 0.000000e+00);
m = pwAddX(m, 's4', 0.000000e+00);
m = pwAddX(m, 's5', 0.000000e+00);
m = pwAddX(m, 's6', 0.000000e+00);
m = pwAddX(m, 's7', 0.000000e+00);
m = pwAddX(m, 's8', 0.000000e+00);
m = pwAddX(m, 's9', 0.000000e+00);
m = pwAddX(m, 's10', 0.000000e+00);
m = pwAddX(m, 's11', 0.000000e+00);
m = pwAddX(m, 's12', 0.000000e+00);
m = pwAddX(m, 's13', 0.000000e+00);
m = pwAddX(m, 's14', 0.000000e+00);
m = pwAddX(m, 's15', 1.000000e+02);
m = pwAddX(m, 's16', 0.000000e+00);
m = pwAddX(m, 's17', 0.000000e+00);
m = pwAddX(m, 's18', 0.000000e+00);
m = pwAddX(m, 's19', 1.000000e+00);
m = pwAddX(m, 's20', 1.000000e+02);
m = pwAddX(m, 's21', 1.000000e+02);
m = pwAddX(m, 's22', 1.000000e+00);
m = pwAddX(m, 's23', 0.000000e+00);
m = pwAddX(m, 's24', 0.000000e+00);
m = pwAddX(m, 's25', 0.000000e+00);
m = pwAddX(m, 's26', 0.000000e+00);

% dynamic parameters
m = pwAddK(m, 't0_met_ACETYL_COA_cyt', 0.000000e+00);
m = pwAddK(m, 't0_met_ALLOLACTOSE_cyt', 0.000000e+00);
m = pwAddK(m, 't0_met_Alpha_lactose_cyt', 0.000000e+00);
m = pwAddK(m, 't0_met_Beta_D_Galactosides_cyt', 0.000000e+00);
m = pwAddK(m, 't0_met_CO_A_cyt', 0.000000e+00);
m = pwAddK(m, 't0_met_CPD_15972_cyt', 0.000000e+00);
m = pwAddK(m, 't0_met_CPD_3561_cyt', 0.000000e+00);
m = pwAddK(m, 't0_met_CPD_3785_cyt', 0.000000e+00);
m = pwAddK(m, 't0_met_CPD_3801_cyt', 0.000000e+00);
m = pwAddK(m, 't0_met_D_ARABINOSE_cyt', 0.000000e+00);
m = pwAddK(m, 't0_met_Fructofuranose_cyt', 0.000000e+00);
m = pwAddK(m, 't0_met_GALACTOSE_cyt', 0.000000e+00);
m = pwAddK(m, 't0_met_Glucopyranose_cyt', 0.000000e+00);
m = pwAddK(m, 't0_met_MELIBIOSE_cyt', 0.000000e+00);
m = pwAddK(m, 't0_met_PROTON_cyt', 0.000000e+00);
m = pwAddK(m, 't0_met_WATER_cyt', 1.000000e+02);
m = pwAddK(m, 't0_met__6_Acetyl_Beta_D_Galactosides_cyt', 0.000000e+00);
m = pwAddK(m, 't0_prot_lacA_cyt', 0.000000e+00);
m = pwAddK(m, 't0_prot_lacY_cyt', 0.000000e+00);
m = pwAddK(m, 't0_prot_lacZ_cyt', 1.000000e+00);
m = pwAddK(m, 'fwd_GALACTOACETYLTRAN_RXN', 1.000000e+00);
m = pwAddK(m, 'rvs_GALACTOACETYLTRAN_RXN', 0.000000e+00);
m = pwAddK(m, 'fwd_TRANS_RXN_24', 1.000000e+00);
m = pwAddK(m, 'rvs_TRANS_RXN_24', 0.000000e+00);
m = pwAddK(m, 'fwd_TRANS_RXN_94', 1.000000e+00);
m = pwAddK(m, 'rvs_TRANS_RXN_94', 0.000000e+00);
m = pwAddK(m, 'fwd_RXN0_7215', 1.000000e+00);
m = pwAddK(m, 'rvs_RXN0_7215', 0.000000e+00);
m = pwAddK(m, 'fwd_RXN0_7217', 1.000000e+00);
m = pwAddK(m, 'rvs_RXN0_7217', 0.000000e+00);
m = pwAddK(m, 'fwd_RXN_17755', 1.000000e+00);
m = pwAddK(m, 'rvs_RXN_17755', 0.000000e+00);
m = pwAddK(m, 'fwd_BETAGALACTOSID_RXN', 1.000000e+00);
m = pwAddK(m, 'rvs_BETAGALACTOSID_RXN', 0.000000e+00);
m = pwAddK(m, 'fwd_RXN0_5363', 1.000000e+00);
m = pwAddK(m, 'rvs_RXN0_5363', 1.000000e+00);
m = pwAddK(m, 'fwd_RXN_17726', 1.000000e+00);
m = pwAddK(m, 'rvs_RXN_17726', 0.000000e+00);
m = pwAddK(m, 'fwd_RXN0_7219', 1.000000e+00);
m = pwAddK(m, 'rvs_RXN0_7219', 0.000000e+00);
m = pwAddK(m, 't0_dna_Alpha_lactose_per', 1.000000e+02);
m = pwAddK(m, 't0_dna_PROTON_per', 1.000000e+02);
m = pwAddK(m, 't0_prot_lacY_imem', 1.000000e+00);

% ODEs
m = pwAddODE(m, 's0', '__s16*__s17*__s4*rvs_GALACTOACETYLTRAN_RXN + (__s0*__s17*__s3*fwd_GALACTOACETYLTRAN_RXN)*(-1)');
m = pwAddODE(m, 's1', '__s19*__s2*fwd_RXN0_5363 + (__s1*__s19*rvs_RXN0_5363)*(-1)');
m = pwAddODE(m, 's2', '__s1*__s19*rvs_RXN0_5363 + __s20*__s21*__s22*fwd_TRANS_RXN_24 + (__s19*__s2*fwd_RXN0_5363)*(-1) + (__s14*__s2*__s22*rvs_TRANS_RXN_24)*(-1)');
m = pwAddODE(m, 's3', '__s16*__s17*__s4*rvs_GALACTOACETYLTRAN_RXN + (__s0*__s17*__s3*fwd_GALACTOACETYLTRAN_RXN)*(-1)');
m = pwAddODE(m, 's4', '__s0*__s17*__s3*fwd_GALACTOACETYLTRAN_RXN + (__s16*__s17*__s4*rvs_GALACTOACETYLTRAN_RXN)*(-1)');
m = pwAddODE(m, 's5', '__s11*__s12*__s19*rvs_BETAGALACTOSID_RXN + (__s15*__s19*__s5*fwd_BETAGALACTOSID_RXN)*(-1)');
m = pwAddODE(m, 's6', '__s10*__s11*__s19*rvs_RXN_17726 + __s21*__s22*__s24*fwd_RXN0_7215 + (__s14*__s22*__s6*rvs_RXN0_7215)*(-1) + (__s15*__s19*__s6*fwd_RXN_17726)*(-1)');
m = pwAddODE(m, 's7', '__s11*__s19*__s9*rvs_RXN0_7219 + __s21*__s22*__s25*fwd_RXN0_7217 + (__s14*__s22*__s7*rvs_RXN0_7217)*(-1) + (__s15*__s19*__s7*fwd_RXN0_7219)*(-1)');
m = pwAddODE(m, 's8', '__s21*__s22*__s26*fwd_RXN_17755 + (__s14*__s22*__s8*rvs_RXN_17755)*(-1)');
m = pwAddODE(m, 's9', '__s15*__s19*__s7*fwd_RXN0_7219 + (__s11*__s19*__s9*rvs_RXN0_7219)*(-1)');
m = pwAddODE(m, 's10', '__s15*__s19*__s6*fwd_RXN_17726 + (__s10*__s11*__s19*rvs_RXN_17726)*(-1)');
m = pwAddODE(m, 's11', '__s15*__s19*__s5*fwd_BETAGALACTOSID_RXN + __s15*__s19*__s6*fwd_RXN_17726 + __s15*__s19*__s7*fwd_RXN0_7219 + (__s10*__s11*__s19*rvs_RXN_17726)*(-1) + (__s11*__s12*__s19*rvs_BETAGALACTOSID_RXN)*(-1) + (__s11*__s19*__s9*rvs_RXN0_7219)*(-1)');
m = pwAddODE(m, 's12', '__s15*__s19*__s5*fwd_BETAGALACTOSID_RXN + (__s11*__s12*__s19*rvs_BETAGALACTOSID_RXN)*(-1)');
m = pwAddODE(m, 's13', '__s21*__s22*__s23*fwd_TRANS_RXN_94 + (__s13*__s14*__s22*rvs_TRANS_RXN_94)*(-1)');
m = pwAddODE(m, 's14', '__s20*__s21*__s22*fwd_TRANS_RXN_24 + __s21*__s22*__s23*fwd_TRANS_RXN_94 + __s21*__s22*__s24*fwd_RXN0_7215 + __s21*__s22*__s25*fwd_RXN0_7217 + __s21*__s22*__s26*fwd_RXN_17755 + (__s13*__s14*__s22*rvs_TRANS_RXN_94)*(-1) + (__s14*__s2*__s22*rvs_TRANS_RXN_24)*(-1) + (__s14*__s22*__s6*rvs_RXN0_7215)*(-1) + (__s14*__s22*__s7*rvs_RXN0_7217)*(-1) + (__s14*__s22*__s8*rvs_RXN_17755)*(-1)');
m = pwAddODE(m, 's15', '__s10*__s11*__s19*rvs_RXN_17726 + __s11*__s12*__s19*rvs_BETAGALACTOSID_RXN + __s11*__s19*__s9*rvs_RXN0_7219 + (__s15*__s19*__s5*fwd_BETAGALACTOSID_RXN)*(-1) + (__s15*__s19*__s6*fwd_RXN_17726)*(-1) + (__s15*__s19*__s7*fwd_RXN0_7219)*(-1)');
m = pwAddODE(m, 's16', '__s0*__s17*__s3*fwd_GALACTOACETYLTRAN_RXN + (__s16*__s17*__s4*rvs_GALACTOACETYLTRAN_RXN)*(-1)');
m = pwAddODE(m, 's17', '0');
m = pwAddODE(m, 's18', '0');
m = pwAddODE(m, 's19', '0');
m = pwAddODE(m, 's20', '__s14*__s2*__s22*rvs_TRANS_RXN_24 + (__s20*__s21*__s22*fwd_TRANS_RXN_24)*(-1)');
m = pwAddODE(m, 's21', '__s13*__s14*__s22*rvs_TRANS_RXN_94 + __s14*__s2*__s22*rvs_TRANS_RXN_24 + __s14*__s22*__s6*rvs_RXN0_7215 + __s14*__s22*__s7*rvs_RXN0_7217 + __s14*__s22*__s8*rvs_RXN_17755 + (__s20*__s21*__s22*fwd_TRANS_RXN_24)*(-1) + (__s21*__s22*__s23*fwd_TRANS_RXN_94)*(-1) + (__s21*__s22*__s24*fwd_RXN0_7215)*(-1) + (__s21*__s22*__s25*fwd_RXN0_7217)*(-1) + (__s21*__s22*__s26*fwd_RXN_17755)*(-1)');
m = pwAddODE(m, 's22', '0');
m = pwAddODE(m, 's23', '__s13*__s14*__s22*rvs_TRANS_RXN_94 + (__s21*__s22*__s23*fwd_TRANS_RXN_94)*(-1)');
m = pwAddODE(m, 's24', '__s14*__s22*__s6*rvs_RXN0_7215 + (__s21*__s22*__s24*fwd_RXN0_7215)*(-1)');
m = pwAddODE(m, 's25', '__s14*__s22*__s7*rvs_RXN0_7217 + (__s21*__s22*__s25*fwd_RXN0_7217)*(-1)');
m = pwAddODE(m, 's26', '__s14*__s22*__s8*rvs_RXN_17755 + (__s21*__s22*__s26*fwd_RXN_17755)*(-1)');

% observables
m = pwAddY(m, 'obs_met_ACETYL_COA_cyt', '1.000000 * s0');
m = pwAddY(m, 'obs_met_ALLOLACTOSE_cyt', '1.000000 * s1');
m = pwAddY(m, 'obs_met_Alpha_lactose_cyt', '1.000000 * s2');
m = pwAddY(m, 'obs_met_Beta_D_Galactosides_cyt', '1.000000 * s3');
m = pwAddY(m, 'obs_met_CO_A_cyt', '1.000000 * s4');
m = pwAddY(m, 'obs_met_CPD_15972_cyt', '1.000000 * s5');
m = pwAddY(m, 'obs_met_CPD_3561_cyt', '1.000000 * s6');
m = pwAddY(m, 'obs_met_CPD_3785_cyt', '1.000000 * s7');
m = pwAddY(m, 'obs_met_CPD_3801_cyt', '1.000000 * s8');
m = pwAddY(m, 'obs_met_D_ARABINOSE_cyt', '1.000000 * s9');
m = pwAddY(m, 'obs_met_Fructofuranose_cyt', '1.000000 * s10');
m = pwAddY(m, 'obs_met_GALACTOSE_cyt', '1.000000 * s11');
m = pwAddY(m, 'obs_met_Glucopyranose_cyt', '1.000000 * s12');
m = pwAddY(m, 'obs_met_MELIBIOSE_cyt', '1.000000 * s13');
m = pwAddY(m, 'obs_met_PROTON_cyt', '1.000000 * s14');
m = pwAddY(m, 'obs_met_WATER_cyt', '1.000000 * s15');
m = pwAddY(m, 'obs_met__6_Acetyl_Beta_D_Galactosides_cyt', '1.000000 * s16');
m = pwAddY(m, 'obs_met_Alpha_lactose_per', '1.000000 * s20');
m = pwAddY(m, 'obs_met_PROTON_per', '1.000000 * s21');
m = pwAddY(m, 'obs_prot_lacY_imem', '1.000000 * s22');

% end of PottersWheel model atlas_rbm_construct_model_from_metabolic_network
