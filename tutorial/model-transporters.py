from pysb import *
Model()

Monomer('met',
	['name', 'loc', 'dna', 'met', 'prot', 'rna'],
	{ 'name' : [ 'ACET', 'ACETYLSERINE', 'ADENINE', 'ADENOSINE', 'ADP', 'AGplus', 'AGMATHINE', 'ALLOSE', 'AMMONIUM', 'AMP', 'ARG', 'ARSENATE', 'ASCORBATE', 'ASN', 'ATP', 'Acceptor', 'Aldehydes', 'Aldonic_Acids', 'Aliphatic_Sulfonates', 'Alkylphosphonates', 'All_Amines', 'Alpha_lactose', 'Amides', 'Amino_Acids', 'Aminoalkylphosphonates', 'Aromatics', 'B_ALANINE', 'BETAINE', 'BIOTIN', 'Bases', 'Beta_Lactams', 'C4_dicarboxylates', 'C55_PP_GLCNAC_MANNACA_FUC4NAC', 'C6', 'CADAVERINE', 'CANAVANINE', 'CARBON_DIOXIDE', 'CARNITINE', 'CDplus2', 'CELLOBIOSE', 'CHITOBIOSE', 'CHLORAMPHENICOL', 'CHOLATE', 'CHOLINE', 'CIT', 'CL_', 'COplus2', 'CO_A', 'COB_I_ALAMIN', 'COBINAMIDE', 'CPD_10247', 'CPD_10269', 'CPD_10774', 'CPD_10797', 'CPD_1142', 'CPD_1162', 'CPD_1181', 'CPD_14545', 'CPD_15189', 'CPD_15417', 'CPD_15554', 'CPD_15867', 'CPD_15979', 'CPD_16009', 'CPD_16619', 'CPD_18254', 'CPD_18346', 'CPD_18499', 'CPD_18500', 'CPD_18501', 'CPD_18719', 'CPD_19953', 'CPD_20888', 'CPD_20890', 'CPD_20894', 'CPD_20921', 'CPD_20940', 'CPD_21015', 'CPD_21025', 'CPD_21070', 'CPD_21777', 'CPD_218', 'CPD_2482', 'CPD_27', 'CPD_3', 'CPD_334', 'CPD_3561', 'CPD_3564', 'CPD_3565', 'CPD_3570', 'CPD_3582', 'CPD_3617', 'CPD_3736', 'CPD_3738', 'CPD_3740', 'CPD_3785', 'CPD_3801', 'CPD_397', 'CPD_4544', 'CPD_497', 'CPD_507', 'CPD_560', 'CPD_611', 'CPD_660', 'CPD_69', 'CPD_7248', 'CPD_7249', 'CPD_763', 'CPD_7970', 'CPD_8876', 'CPD_9245', 'CPD_9247', 'CPD_9288', 'CPD0_1063', 'CPD0_1080', 'CPD0_1081', 'CPD0_1083', 'CPD0_1113', 'CPD0_1123', 'CPD0_1189', 'CPD0_1192', 'CPD0_1193', 'CPD0_1470', 'CPD0_1551', 'CPD0_1564', 'CPD0_1938', 'CPD0_2039', 'CPD0_2241', 'CPD0_2279', 'CPD0_2482', 'CPD0_2485', 'CPD0_2486', 'CPD0_2499', 'CPD0_2640', 'CPD0_441', 'CPD0_621', 'CPD0_881', 'CPD0_882', 'CPD0_889', 'CPD66_39', 'CUplus', 'CUplus2', 'CYS', 'CYSTINE', 'CYTIDINE', 'CYTOSINE', 'D_ALANINE', 'D_ARABINOSE', 'D_Fructopyranose', 'D_GALACTARATE', 'D_GALACTONATE', 'D_GALACTURONATE', 'D_GLUCARATE', 'D_GLUCOSAMINE_6_P', 'D_LACTATE', 'D_Ribopyranose', 'D_SERINE', 'D_SORBITOL_6_P', 'D_TARTRATE', 'D_Xylose', 'D_fructofuranose_1_phosphate', 'D_fructopyranose_1_phosphate', 'D_fructose_1_phosphate', 'D_galactopyranose', 'D_glucopyranose_6_phosphate', 'D_mannopyranose', 'DEOXYADENOSINE', 'DEOXYCHOLATE', 'DEOXYCYTIDINE', 'DEOXYINOSINE', 'DEOXYURIDINE', 'DIACETYLCHITOBIOSE_6_PHOSPHATE', 'DIPEPTIDES', 'Disaccharides', 'Donor_H2', 'Drugs', 'EG11489_MONOMER', 'ENTEROBACTIN', 'Erythromycins', 'F_', 'FAD', 'FEplus2', 'FERRIC_CITRATE_COMPLEX', 'FERRIC_ENTEROBACTIN_COMPLEX', 'FMN', 'FORMATE', 'FRU', 'FRUCTOSELYSINE', 'FRUCTURONATE', 'FUM', 'Ferric_Hydroxamate_Complexes', 'Fructofuranose', 'GALACTITOL', 'GALACTITOL_1_PHOSPHATE', 'GAMMA_BUTYROBETAINE', 'GLN', 'GLT', 'GLUCONATE', 'GLUCOSAMINE', 'GLUCURONATE', 'GLUTATHIONE', 'GLY', 'GLYCERATE', 'GLYCEROL', 'GLYCEROL_3P', 'GLYCOLLATE', 'GUANINE', 'GUANOSINE', 'General_Protein_Substrates', 'Gentamycins', 'Glucopyranose', 'Glucuronides', 'Glycerol_1_phosphate', 'Glycerophosphodiesters', 'Glycosides', 'HIS', 'HOMO_SER', 'HOMOCYSTINE', 'HYDROGEN_MOLECULE', 'HYDROGEN_PEROXIDE', 'HYDROQUINONE_O_BETA_D_GLUCOPYRANOSIDE', 'HYPOXANTHINE', 'Hpr_Histidine', 'Hpr_pi_phospho_L_histidines', 'Hydrophilic_Solute_Or_Ion_LT_600Da', 'Hydroxy_carboxylates', 'ILE', 'INDOLE', 'INOSINE', 'Inositols', 'Ions', 'Kplus', 'L_ALA_GAMMA_D_GLU_DAP', 'L_ALPHA_ALANINE', 'L_ARABINOSE', 'L_ASCORBATE_6_PHOSPHATE', 'L_ASPARTATE', 'L_GLYCERALDEHYDE_3_PHOSPHATE', 'L_Galactose', 'L_IDONATE', 'L_LACTATE', 'L_Methionine_sulfoxides', 'L_ORNITHINE', 'L_fucoses', 'L_rhamnose', 'LEU', 'LIplus', 'LOS', 'LYS', 'Lactones', 'Lipopolysaccharides', 'Long_Chain_Fatty_Acids', 'Lysophosphatidylglycerols', 'MAL', 'MALTOSE', 'MALTOTETRAOSE', 'MALTOTRIOSE', 'MANNITOL', 'MANNITOL_1P', 'MELIBIOSE', 'MESO_DIAMINOPIMELATE', 'MET', 'METHYL_BETA_D_GALACTOSIDE', 'MGplus2', 'MNplus2', 'Macrolide_Antibiotics', 'Medium_chain_fatty_acids', 'Menaquinols', 'Menaquinones', 'Monocarboxylates', 'N_ACETYL_D_GLUCOSAMINE_6_P', 'N_ACETYL_D_MANNOSAMINE_6P', 'N_ACETYLNEURAMINATE', 'N_acetyl_D_glucosamine', 'N_acetyl_D_mannosamine', 'NAplus', 'NACMUR', 'NAD', 'NADH', 'NADP', 'NADPH', 'NIplus2', 'NICOTINAMIDE_RIBOSE', 'NITRATE', 'NITRITE', 'NUCLEOTIDE_SUGARS', 'Nucleosides', 'Nucleotides', 'OLEATE_CPD', 'OLEOYL_COA', 'OLIGOPEPTIDES', 'ORGANOSULFUR', 'OROTATE', 'OXYGEN_MOLECULE', 'Organophosphorus_Compounds', 'PANTOTHENATE', 'PHE', 'PPI', 'PRO', 'PROPIONATE', 'PROTOHEME', 'PROTON', 'PSICOSELYSINE', 'PTSH_MONOMER', 'PTSH_PHOSPHORYLATED', 'PTSI_MONOMER', 'PTSI_PHOSPHORYLATED', 'PUTRESCINE', 'PYRIDOXAL', 'PYRIDOXAMINE', 'PYRIDOXINE', 'PYRUVATE', 'Peptide_Antibiotics', 'Pi', 'Polymyxins', 'Quaternary_Amines', 'S2O3', 'SELENATE', 'SELENITE', 'SER', 'SHIKIMATE', 'SORBITOL', 'SPERMIDINE', 'SUC', 'SULFATE', 'SULFO_CYSTEINE', 'Saturated_Fatty_Acyl_CoA', 'Short_Chain_Alcohols', 'Short_Chain_Carboxylates', 'Sugar', 'Sugar_Phosphate', 'Sugar_alcohols', 'TARTRATE', 'TAURINE', 'THIAMINE', 'THIAMINE_PYROPHOSPHATE', 'THR', 'THYMIDINE', 'THYMINE', 'TREHALOSE', 'TREHALOSE_6P', 'TRIPEPTIDES', 'TRP', 'TYR', 'Trisaccharides', 'UDP', 'UDP_N_ACETYL_D_GLUCOSAMINE', 'URACIL', 'URATE', 'UREA', 'URIDINE', 'Ubiquinols', 'Ubiquinones', 'Unspecified_Ion_Or_Solute', 'VAL', 'WATER', 'XANTHINE', 'XANTHOSINE', 'ZNplus2', '_2_ACYL_GPE', '_2_DEHYDRO_3_DEOXY_D_GLUCONATE', '_2_DEOXY_D_GLUCOSE', '_2_DEOXY_D_GLUCOSE_6_PHOSPHATE', '_2_KETOGLUTARATE', '_2_O_ALPHA_MANNOSYL_D_GLYCERATE', '_3_HYDROXYPHENYL_PROPIONATE', '_3_KETOBUTYRATE', '_3_PHENYLPROPIONATE', '_4_AMINO_BUTYRATE', '_4_hydroxybenzoate', '_5_AMINOPENTANOATE', '_5_DEHYDROGLUCONATE', 'a_lyso_cardiolipin', 'bacitracin', 'cystine', 'dicarboxylate' ],
	'loc' : ['cyt', 'cytosk', 'ex', 'mem', 'per', 'wall', 'bnuc', 'cproj', 'imem', 'omem']})
Monomer('prot',
	['name', 'loc', 'dna', 'met', 'prot', 'rna', 'up', 'dw'],
	{ 'name' : [ 'ABGT_MONOMER', 'AMPG_MONOMER', 'ANSP_MONOMER', 'ARAE_MONOMER', 'AROP_MONOMER', 'B0070_MONOMER', 'B0260_MONOMER', 'B0612_MONOMER', 'B0709_MONOMER', 'B0752_MONOMER', 'B1006_MONOMER', 'B1296_MONOMER', 'B1634_MONOMER', 'B1791_MONOMER', 'B2789_MONOMER', 'B2975_MONOMER', 'B4141_MONOMER', 'BCR_MONOMER', 'BETT_MONOMER', 'BRNQ_MONOMER', 'CADB_MONOMER', 'CHAA_MONOMER', 'CMR_MONOMER', 'CODB_MONOMER', 'CORA_MONOMER', 'CYCA_MONOMER', 'CYNX_MONOMER', 'DCTA_MONOMER', 'DCUA_MONOMER', 'DCUB_MONOMER', 'DCUC_MONOMER', 'DSDX_MONOMER', 'EG10003_MONOMER', 'EG10280_MONOMER', 'EG11035_MONOMER', 'EG11167_MONOMER', 'EG11471_MONOMER', 'EG11486_MONOMER', 'EG11512_MONOMER', 'EG11639_MONOMER', 'EG11671_MONOMER', 'EG11691_MONOMER', 'EG11724_MONOMER', 'EG11902_MONOMER', 'EG11919_MONOMER', 'EG11939_MONOMER', 'EG12134_MONOMER', 'EG12455_MONOMER', 'EG12713_MONOMER', 'EIISGA', 'EMRD_MONOMER', 'EXUT_MONOMER', 'FSR_MONOMER', 'FUCP_MONOMER', 'G6260_MONOMER', 'G6370_MONOMER', 'G6458_MONOMER', 'G6531_MONOMER', 'G6561_MONOMER', 'G6657_MONOMER', 'G6674_MONOMER', 'G6859_MONOMER', 'G6934_MONOMER', 'G6999_MONOMER', 'G7097_MONOMER', 'G7138_MONOMER', 'G7399_MONOMER', 'G7921_MONOMER', 'G7942_MONOMER', 'GABP_MONOMER', 'GALP_MONOMER', 'GLPT_MONOMER', 'GLTP_MONOMER', 'GLTS_MONOMER', 'GNTP_MONOMER', 'HCAT_MONOMER', 'HRSA_MONOMER', 'KDGT_MONOMER', 'KGTP_MONOMER', 'KUP_MONOMER', 'LACY_MONOMER', 'LYSP_MONOMER', 'MALX_MONOMER', 'MELB_MONOMER', 'MGTA_MONOMER', 'MHPT_MONOMER', 'MONOMER0_2797', 'MONOMER0_2798', 'MONOMER0_2799', 'MONOMER0_5', 'MTR_MONOMER', 'NANT_MONOMER', 'NARK_MONOMER', 'NHAB_MONOMER', 'NUPC_MONOMER', 'NUPG_MONOMER', 'PANF_MONOMER', 'PITA_MONOMER', 'PNUC_MONOMER', 'POTE_MONOMER', 'PUTP_MONOMER', 'RFBX_MONOMER', 'RHAT_MONOMER', 'RHTB_MONOMER', 'SDAC_MONOMER', 'SHIA_MONOMER', 'TDCC_MONOMER', 'TEHA_MONOMER', 'UHPT_MONOMER', 'UIDB_MONOMER', 'XAPB_MONOMER', 'XASA_MONOMER', 'XYLE_MONOMER', 'YBDA_MONOMER', 'YCEE_MONOMER', 'YDEA_MONOMER', 'YDHE_MONOMER', 'YEEO_MONOMER', 'YEIM_MONOMER', 'YFEP_MONOMER', 'YGFU_MONOMER', 'YGGA_MONOMER', 'YGJE_MONOMER', 'YGJU_MONOMER', 'YHFM_MONOMER', 'YHHO_MONOMER', 'YICM_MONOMER', 'YIDT_MONOMER', 'YIDY_MONOMER', 'YIHO_MONOMER', 'YJGT_MONOMER', 'YJIO_MONOMER', 'YJIZ_MONOMER' ],
	'loc' : ['cyt', 'cytosk', 'ex', 'mem', 'per', 'wall', 'bnuc', 'cproj', 'imem', 'omem']})
Monomer('cplx',
	['name', 'loc', 'dna', 'met', 'prot', 'rna', 'up', 'dw'],
	{ 'name' : [ 'ABC_10_CPLX', 'ABC_11_CPLX', 'ABC_12_CPLX', 'ABC_13_CPLX', 'ABC_14_CPLX', 'ABC_15_CPLX', 'ABC_16_CPLX', 'ABC_18_CPLX', 'ABC_19_CPLX', 'ABC_2_CPLX', 'ABC_20_CPLX', 'ABC_22_CPLX', 'ABC_23_CPLX', 'ABC_24_CPLX', 'ABC_26_CPLX', 'ABC_27_CPLX', 'ABC_28_CPLX', 'ABC_29_CPLX', 'ABC_3_CPLX', 'ABC_32_CPLX', 'ABC_33_CPLX', 'ABC_34_CPLX', 'ABC_35_CPLX', 'ABC_40_CPLX', 'ABC_42_CPLX', 'ABC_46_CPLX', 'ABC_49_CPLX', 'ABC_5_CPLX', 'ABC_56_CPLX', 'ABC_57_CPLX', 'ABC_58_CPLX', 'ABC_6_CPLX', 'ABC_63_CPLX', 'ABC_64_CPLX', 'ABC_7_CPLX', 'ABC_8_CPLX', 'ABC_9_CPLX', 'ACYLCOASYN_CPLX', 'APP_UBIOX_CPLX', 'ATPASE_1_CPLX', 'ATPSYN_CPLX', 'CPLX_153', 'CPLX_154', 'CPLX_155', 'CPLX_156', 'CPLX_157', 'CPLX_158', 'CPLX_165', 'CPLX_166', 'CPLX_168', 'CPLX_3945', 'CPLX_7', 'CPLX0_1721', 'CPLX0_1924', 'CPLX0_1941', 'CPLX0_1942', 'CPLX0_1943', 'CPLX0_2121', 'CPLX0_2141', 'CPLX0_231', 'CPLX0_3932', 'CPLX0_3970', 'CPLX0_4', 'CPLX0_7', 'CPLX0_7530', 'CPLX0_7532', 'CPLX0_7533', 'CPLX0_7534', 'CPLX0_7535', 'CPLX0_7626', 'CPLX0_7629', 'CPLX0_7641', 'CPLX0_7642', 'CPLX0_7653', 'CPLX0_7654', 'CPLX0_7655', 'CPLX0_7684', 'CPLX0_7704', 'CPLX0_7720', 'CPLX0_7807', 'CPLX0_7843', 'CPLX0_7906', 'CPLX0_7952', 'CPLX0_7955', 'CPLX0_7961', 'CPLX0_7963', 'CPLX0_7992', 'CPLX0_7994', 'CPLX0_8097', 'CPLX0_8152', 'CPLX0_8167', 'CPLX0_8263', 'CPLX0_8271', 'CPLX0_8541', 'CYT_D_UBIOX_CPLX', 'CYT_O_UBIOX_CPLX', 'FORMATEDEHYDROGN_CPLX', 'METNIQ_METHIONINE_ABC_CPLX', 'NADH_DHI_CPLX', 'NITRATREDUCTA_CPLX', 'PYRNUTRANSHYDROGEN_CPLX', 'TATABCE_CPLX', 'TRANS_200_CPLX', 'TRANS_CPLX_201', 'TRANS_CPLX_202', 'TRANS_CPLX_203', 'YDGEF_CPLX' ],
	'loc' : ['cyt', 'cytosk', 'ex', 'mem', 'per', 'wall', 'bnuc', 'cproj', 'imem', 'omem']})
Rule('ABC_10_RXN',
	cplx(name = 'ABC_10_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'FERRIC_ENTEROBACTIN_COMPLEX', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_10_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'FERRIC_ENTEROBACTIN_COMPLEX', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_ABC_10_RXN', 1.000000), 
	Parameter('rvs_ABC_10_RXN', 0.000000))
Rule('ABC_11_RXN',
	cplx(name = 'ABC_11_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Ferric_Hydroxamate_Complexes', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'ABC_11_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Ferric_Hydroxamate_Complexes', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_ABC_11_RXN', 1.000000), 
	Parameter('rvs_ABC_11_RXN', 0.000000))
Rule('TRANS_RXN_297',
	cplx(name = 'ABC_11_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_621', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_11_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_621', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_297', 1.000000), 
	Parameter('rvs_TRANS_RXN_297', 0.000000))
Rule('TRANS_RXN_298',
	cplx(name = 'ABC_11_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_2241', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_11_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_2241', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_298', 1.000000), 
	Parameter('rvs_TRANS_RXN_298', 0.000000))
Rule('ABC_12_RXN',
	cplx(name = 'ABC_12_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'GLN', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_12_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'GLN', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_ABC_12_RXN', 1.000000), 
	Parameter('rvs_ABC_12_RXN', 0.000000))
Rule('TRANS_RXN0_222',
	cplx(name = 'ABC_13_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'L_ASPARTATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_13_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'L_ASPARTATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_222', 1.000000), 
	Parameter('rvs_TRANS_RXN0_222', 0.000000))
Rule('ABC_13_RXN',
	cplx(name = 'ABC_13_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'GLT', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_13_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'GLT', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_ABC_13_RXN', 1.000000), 
	Parameter('rvs_ABC_13_RXN', 0.000000))
Rule('ABC_14_RXN',
	cplx(name = 'ABC_14_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'HIS', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_14_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'HIS', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_ABC_14_RXN', 1.000000), 
	Parameter('rvs_ABC_14_RXN', 0.000000))
Rule('ABC_35_RXN',
	cplx(name = 'ABC_15_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'LEU', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_15_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'LEU', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_ABC_35_RXN', 1.000000), 
	Parameter('rvs_ABC_35_RXN', 0.000000))
Rule('ABC_36_RXN',
	cplx(name = 'ABC_15_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'VAL', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_15_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'VAL', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_ABC_36_RXN', 1.000000), 
	Parameter('rvs_ABC_36_RXN', 0.000000))
Rule('ABC_15_RXN',
	cplx(name = 'ABC_15_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ILE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_15_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ILE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_ABC_15_RXN', 1.000000), 
	Parameter('rvs_ABC_15_RXN', 0.000000))
Rule('TRANS_RXN_312',
	cplx(name = 'ABC_15_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PHE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_15_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PHE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_312', 1.000000), 
	Parameter('rvs_TRANS_RXN_312', 0.000000))
Rule('ABC_16_RXN',
	cplx(name = 'ABC_16_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'MALTOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_16_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'MALTOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_ABC_16_RXN', 1.000000), 
	Parameter('rvs_ABC_16_RXN', 0.000000))
Rule('TRANS_RXN0_504',
	cplx(name = 'ABC_16_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'MALTOTETRAOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_16_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'MALTOTETRAOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_504', 1.000000), 
	Parameter('rvs_TRANS_RXN0_504', 0.000000))
Rule('TRANS_RXN0_503',
	cplx(name = 'ABC_16_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'MALTOTRIOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_16_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'MALTOTRIOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_503', 1.000000), 
	Parameter('rvs_TRANS_RXN0_503', 0.000000))
Rule('ABC_18_RXN',
	cplx(name = 'ABC_18_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'D_galactopyranose', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_18_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'D_galactopyranose', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_ABC_18_RXN', 1.000000), 
	Parameter('rvs_ABC_18_RXN', 0.000000))
Rule('TRANS_RXN0_541',
	cplx(name = 'ABC_18_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'METHYL_BETA_D_GALACTOSIDE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_18_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'METHYL_BETA_D_GALACTOSIDE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_541', 1.000000), 
	Parameter('rvs_TRANS_RXN0_541', 0.000000))
Rule('ABC_19_RXN',
	cplx(name = 'ABC_19_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_3', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_19_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_3', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_ABC_19_RXN', 1.000000), 
	Parameter('rvs_ABC_19_RXN', 0.000000))
Rule('ABC_2_RXN',
	cplx(name = 'ABC_2_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'L_ARABINOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_2_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'L_ARABINOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_ABC_2_RXN', 1.000000), 
	Parameter('rvs_ABC_2_RXN', 0.000000))
Rule('ABC_20_RXN',
	cplx(name = 'ABC_20_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NIplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_20_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NIplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_ABC_20_RXN', 1.000000), 
	Parameter('rvs_ABC_20_RXN', 0.000000))
Rule('_3dot6dot3dot23_RXN',
	cplx(name = 'ABC_22_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'OLIGOPEPTIDES', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_22_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'OLIGOPEPTIDES', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd__3dot6dot3dot23_RXN', 1.000000), 
	Parameter('rvs__3dot6dot3dot23_RXN', 0.000000))
Rule('ABC_23_RXN',
	cplx(name = 'ABC_23_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Alkylphosphonates', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_23_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Alkylphosphonates', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_ABC_23_RXN', 1.000000), 
	Parameter('rvs_ABC_23_RXN', 0.000000))
Rule('TRANS_RXN_238',
	cplx(name = 'ABC_23_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Aminoalkylphosphonates', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_23_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Aminoalkylphosphonates', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_238', 1.000000), 
	Parameter('rvs_TRANS_RXN_238', 0.000000))
Rule('ABC_24_RXN',
	cplx(name = 'ABC_24_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'SPERMIDINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_24_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'SPERMIDINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_ABC_24_RXN', 1.000000), 
	Parameter('rvs_ABC_24_RXN', 0.000000))
Rule('ABC_25_RXN',
	cplx(name = 'ABC_24_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PUTRESCINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_24_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PUTRESCINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_ABC_25_RXN', 1.000000), 
	Parameter('rvs_ABC_25_RXN', 0.000000))
Rule('RXN_8638',
	cplx(name = 'ABC_26_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Quaternary_Amines', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_26_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Quaternary_Amines', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN_8638', 1.000000), 
	Parameter('rvs_RXN_8638', 0.000000))
Rule('ABC_26_RXN',
	cplx(name = 'ABC_26_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PRO', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_26_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PRO', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_ABC_26_RXN', 1.000000), 
	Parameter('rvs_ABC_26_RXN', 0.000000))
Rule('ABC_27_RXN',
	cplx(name = 'ABC_27_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'ABC_27_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_ABC_27_RXN', 1.000000), 
	Parameter('rvs_ABC_27_RXN', 0.000000))
Rule('ABC_28_RXN',
	cplx(name = 'ABC_28_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'D_Ribopyranose', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_28_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'D_Ribopyranose', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_ABC_28_RXN', 1.000000), 
	Parameter('rvs_ABC_28_RXN', 0.000000))
Rule('TRANS_RXN_328',
	cplx(name = 'ABC_29_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PUTRESCINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_29_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PUTRESCINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_328', 1.000000), 
	Parameter('rvs_TRANS_RXN_328', 0.000000))
Rule('ABC_37_RXN',
	cplx(name = 'ABC_3_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'L_ORNITHINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_3_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'L_ORNITHINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_ABC_37_RXN', 1.000000), 
	Parameter('rvs_ABC_37_RXN', 0.000000))
Rule('ABC_4_RXN',
	cplx(name = 'ABC_3_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ARG', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_3_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ARG', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_ABC_4_RXN', 1.000000), 
	Parameter('rvs_ABC_4_RXN', 0.000000))
Rule('ABC_3_RXN',
	cplx(name = 'ABC_3_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'LYS', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_3_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'LYS', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_ABC_3_RXN', 1.000000), 
	Parameter('rvs_ABC_3_RXN', 0.000000))
Rule('ABC_32_RXN',
	cplx(name = 'ABC_32_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'THIAMINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_32_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'THIAMINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_ABC_32_RXN', 1.000000), 
	Parameter('rvs_ABC_32_RXN', 0.000000))
Rule('ABC_33_RXN',
	cplx(name = 'ABC_33_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'D_Xylose', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_33_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'D_Xylose', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_ABC_33_RXN', 1.000000), 
	Parameter('rvs_ABC_33_RXN', 0.000000))
Rule('ABC_34_RXN',
	cplx(name = 'ABC_34_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'GLYCEROL_3P', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_34_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'GLYCEROL_3P', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_ABC_34_RXN', 1.000000), 
	Parameter('rvs_ABC_34_RXN', 0.000000))
Rule('TRANS_RXN0_573',
	cplx(name = 'ABC_34_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Glycerophosphodiesters', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_34_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Glycerophosphodiesters', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_573', 1.000000), 
	Parameter('rvs_TRANS_RXN0_573', 0.000000))
Rule('TRANS_RXN0_162',
	cplx(name = 'ABC_35_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTOHEME', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_35_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTOHEME', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_162', 1.000000), 
	Parameter('rvs_TRANS_RXN0_162', 0.000000))
Rule('TRANS_RXN_283',
	cplx(name = 'ABC_40_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'BETAINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_40_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'BETAINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_283', 1.000000), 
	Parameter('rvs_TRANS_RXN_283', 0.000000))
Rule('ABC_42_RXN',
	cplx(name = 'ABC_42_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ALLOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_42_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ALLOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_ABC_42_RXN', 1.000000), 
	Parameter('rvs_ABC_42_RXN', 0.000000))
Rule('TRANS_RXN0_492',
	cplx(name = 'ABC_46_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_2485', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_46_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_2485', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_492', 1.000000), 
	Parameter('rvs_TRANS_RXN0_492', 0.000000))
Rule('TRANS_RXN0_491',
	cplx(name = 'ABC_46_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_2486', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_46_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_2486', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_491', 1.000000), 
	Parameter('rvs_TRANS_RXN0_491', 0.000000))
Rule('RXN0_11',
	cplx(name = 'ABC_49_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'GLUTATHIONE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_49_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'GLUTATHIONE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_11', 1.000000), 
	Parameter('rvs_RXN0_11', 0.000000))
Rule('ABC_5_RXN',
	cplx(name = 'ABC_5_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'COB_I_ALAMIN', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_5_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'COB_I_ALAMIN', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_ABC_5_RXN', 1.000000), 
	Parameter('rvs_ABC_5_RXN', 0.000000))
Rule('TRANS_RXN_296',
	cplx(name = 'ABC_5_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'COBINAMIDE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_5_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'COBINAMIDE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_296', 1.000000), 
	Parameter('rvs_TRANS_RXN_296', 0.000000))
Rule('ABC_56_RXN',
	cplx(name = 'ABC_56_CPLX', loc = 'per', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Aliphatic_Sulfonates', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_56_CPLX', loc = 'per', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Aliphatic_Sulfonates', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_ABC_56_RXN', 1.000000), 
	Parameter('rvs_ABC_56_RXN', 0.000000))
Rule('TRANS_RXN_366',
	cplx(name = 'ABC_57_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_19953', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_57_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_19953', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_366', 1.000000), 
	Parameter('rvs_TRANS_RXN_366', 0.000000))
Rule('TRANS_RXN0_454',
	cplx(name = 'ABC_58_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_10774', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_58_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_10774', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_454', 1.000000), 
	Parameter('rvs_TRANS_RXN0_454', 0.000000))
Rule('RXN0_21',
	cplx(name = 'ABC_6_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'GLUTATHIONE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_6_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'GLUTATHIONE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_21', 1.000000), 
	Parameter('rvs_RXN0_21', 0.000000))
Rule('RXN0_3',
	cplx(name = 'ABC_6_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CYS', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_6_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CYS', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_3', 1.000000), 
	Parameter('rvs_RXN0_3', 0.000000))
Rule('ABC_63_RXN',
	cplx(name = 'ABC_63_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ZNplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_63_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ZNplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_ABC_63_RXN', 1.000000), 
	Parameter('rvs_ABC_63_RXN', 0.000000))
Rule('ABC_64_RXN',
	cplx(name = 'ABC_64_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'TAURINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_64_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'TAURINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_ABC_64_RXN', 1.000000), 
	Parameter('rvs_ABC_64_RXN', 0.000000))
Rule('ABC_7_RXN',
	cplx(name = 'ABC_7_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'S2O3', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_7_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'S2O3', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_ABC_7_RXN', 1.000000), 
	Parameter('rvs_ABC_7_RXN', 0.000000))
Rule('ABC_70_RXN',
	cplx(name = 'ABC_7_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'SULFATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_7_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'SULFATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_ABC_70_RXN', 1.000000), 
	Parameter('rvs_ABC_70_RXN', 0.000000))
Rule('TRANS_RXN0_478',
	cplx(name = 'ABC_7_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'SELENATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_7_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'SELENATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_478', 1.000000), 
	Parameter('rvs_TRANS_RXN0_478', 0.000000))
Rule('TRANS_RXN0_479',
	cplx(name = 'ABC_7_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'SELENITE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_7_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'SELENITE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_479', 1.000000), 
	Parameter('rvs_TRANS_RXN0_479', 0.000000))
Rule('ABC_8_RXN',
	cplx(name = 'ABC_8_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'DIPEPTIDES', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_8_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'DIPEPTIDES', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_ABC_8_RXN', 1.000000), 
	Parameter('rvs_ABC_8_RXN', 0.000000))
Rule('ABC_9_RXN',
	cplx(name = 'ABC_9_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'FERRIC_CITRATE_COMPLEX', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ABC_9_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'FERRIC_CITRATE_COMPLEX', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_ABC_9_RXN', 1.000000), 
	Parameter('rvs_ABC_9_RXN', 0.000000))
Rule('TRANS_RXN0_452',
	prot(name = 'ABGT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD0_889', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'ABGT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD0_889', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_452', 1.000000), 
	Parameter('rvs_TRANS_RXN0_452', 1.000000))
Rule('ACYLCOASYN_RXN',
	cplx(name = 'ACYLCOASYN_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD66_39', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CO_A', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'ACYLCOASYN_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Saturated_Fatty_Acyl_CoA', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PPI', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'AMP', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_ACYLCOASYN_RXN', 1.000000), 
	Parameter('rvs_ACYLCOASYN_RXN', 0.000000))
Rule('TRANS_RXN0_623',
	cplx(name = 'ACYLCOASYN_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD66_39', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CO_A', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'ACYLCOASYN_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Saturated_Fatty_Acyl_CoA', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'AMP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PPI', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_623', 1.000000), 
	Parameter('rvs_TRANS_RXN0_623', 0.000000))
Rule('RXN0_7238',
	cplx(name = 'ACYLCOASYN_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_9247', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CO_A', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'ACYLCOASYN_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_18346', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'AMP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PPI', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_7238', 1.000000), 
	Parameter('rvs_RXN0_7238', 0.000000))
Rule('RXN0_7239',
	cplx(name = 'ACYLCOASYN_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'OLEATE_CPD', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CO_A', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'ACYLCOASYN_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'OLEOYL_COA', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'AMP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PPI', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_7239', 1.000000), 
	Parameter('rvs_RXN0_7239', 0.000000))
Rule('RXN0_7248',
	cplx(name = 'ACYLCOASYN_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_9245', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CO_A', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'ACYLCOASYN_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_10269', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'AMP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PPI', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_7248', 1.000000), 
	Parameter('rvs_RXN0_7248', 0.000000))
Rule('TRANS_RXN0_258',
	prot(name = 'AMPG_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_1081', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'AMPG_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_1081', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_258', 1.000000), 
	Parameter('rvs_TRANS_RXN0_258', 1.000000))
Rule('TRANS_RXN0_226',
	prot(name = 'AMPG_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_1080', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'AMPG_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_1080', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_226', 1.000000), 
	Parameter('rvs_TRANS_RXN0_226', 1.000000))
Rule('TRANS_RXN_262',
	prot(name = 'ANSP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ASN', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'ANSP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ASN', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_262', 1.000000), 
	Parameter('rvs_TRANS_RXN_262', 1.000000))
Rule('RXN0_5266',
	cplx(name = 'APP_UBIOX_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Ubiquinols', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'APP_UBIOX_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Ubiquinones', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_5266', 1.000000), 
	Parameter('rvs_RXN0_5266', 0.000000))
Rule('TRANS_RXN_10',
	prot(name = 'ARAE_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'L_ARABINOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'ARAE_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'L_ARABINOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_10', 1.000000), 
	Parameter('rvs_TRANS_RXN_10', 1.000000))
Rule('TRANS_RXN_76',
	prot(name = 'AROP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'TRP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'AROP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'TRP', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_76', 1.000000), 
	Parameter('rvs_TRANS_RXN_76', 1.000000))
Rule('TRANS_RXN_77',
	prot(name = 'AROP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'TYR', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'AROP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'TYR', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_77', 1.000000), 
	Parameter('rvs_TRANS_RXN_77', 1.000000))
Rule('TRANS_RXN_56',
	prot(name = 'AROP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PHE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'AROP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PHE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_56', 1.000000), 
	Parameter('rvs_TRANS_RXN_56', 1.000000))
Rule('TRANS_RXN_2',
	cplx(name = 'ATPASE_1_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Kplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'ATPASE_1_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Kplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_2', 1.000000), 
	Parameter('rvs_TRANS_RXN_2', 0.000000))
Rule('ATPSYN_RXN',
	cplx(name = 'ATPSYN_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'ATPSYN_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_ATPSYN_RXN', 1.000000), 
	Parameter('rvs_ATPSYN_RXN', 1.000000))
Rule('RXN0_7041',
	cplx(name = 'ATPSYN_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'THIAMINE_PYROPHOSPHATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'ATPSYN_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_611', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_7041', 1.000000), 
	Parameter('rvs_RXN0_7041', 0.000000))
Rule('TRANS_RXN_82',
	prot(name = 'B0070_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Alpha_lactose', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'B0070_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Alpha_lactose', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_82', 1.000000), 
	Parameter('rvs_TRANS_RXN_82', 1.000000))
Rule('TRANS_RXN0_486',
	prot(name = 'B0260_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_397', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'B0260_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_397', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_486', 1.000000), 
	Parameter('rvs_TRANS_RXN0_486', 0.000000))
Rule('TRANS_RXN0_201',
	prot(name = 'B0612_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'SUC', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CIT', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'B0612_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CIT', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'SUC', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_201', 1.000000), 
	Parameter('rvs_TRANS_RXN0_201', 1.000000))
Rule('TRANS_RXN0_288',
	prot(name = 'B0709_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'DIPEPTIDES', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'B0709_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'DIPEPTIDES', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_288', 1.000000), 
	Parameter('rvs_TRANS_RXN0_288', 1.000000))
Rule('TRANS_RXN0_200',
	prot(name = 'B0752_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ZNplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'B0752_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ZNplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_200', 1.000000), 
	Parameter('rvs_TRANS_RXN0_200', 0.000000))
Rule('TRANS_RXN_132',
	prot(name = 'B1006_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'URACIL', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'B1006_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'URACIL', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_132', 1.000000), 
	Parameter('rvs_TRANS_RXN_132', 1.000000))
Rule('TRANS_RXN_362',
	prot(name = 'B1006_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'THYMINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'B1006_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'THYMINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_362', 1.000000), 
	Parameter('rvs_TRANS_RXN_362', 1.000000))
Rule('RXN_5076',
	prot(name = 'B1006_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'XANTHINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'B1006_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'XANTHINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN_5076', 1.000000), 
	Parameter('rvs_RXN_5076', 1.000000))
Rule('TRANS_RXN_69',
	prot(name = 'B1296_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PUTRESCINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'B1296_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PUTRESCINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_69', 1.000000), 
	Parameter('rvs_TRANS_RXN_69', 1.000000))
Rule('TRANS_RXN0_267',
	prot(name = 'B1634_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'TRIPEPTIDES', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'B1634_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'TRIPEPTIDES', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_267', 1.000000), 
	Parameter('rvs_TRANS_RXN0_267', 1.000000))
Rule('TRANS_RXN0_596',
	prot(name = 'B1791_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'Drugs', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'B1791_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'Drugs', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_596', 1.000000), 
	Parameter('rvs_TRANS_RXN0_596', 0.000000))
Rule('TRANS_RXN_273',
	prot(name = 'B1791_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_14545', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'B1791_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_14545', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_273', 1.000000), 
	Parameter('rvs_TRANS_RXN_273', 0.000000))
Rule('TRANS_RXN0_204',
	prot(name = 'B2789_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'D_GLUCARATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'B2789_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'D_GLUCARATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_204', 1.000000), 
	Parameter('rvs_TRANS_RXN0_204', 1.000000))
Rule('TRANS_RXN0_203',
	prot(name = 'B2789_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'D_GALACTARATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'B2789_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'D_GALACTARATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_203', 1.000000), 
	Parameter('rvs_TRANS_RXN0_203', 1.000000))
Rule('TRANS_RXN0_523',
	prot(name = 'B2789_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'GLYCERATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'B2789_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'GLYCERATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_523', 1.000000), 
	Parameter('rvs_TRANS_RXN0_523', 1.000000))
Rule('TRANS_RXN_105',
	prot(name = 'B2975_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'GLYCOLLATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'B2975_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'GLYCOLLATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_105', 1.000000), 
	Parameter('rvs_TRANS_RXN_105', 1.000000))
Rule('TRANS_RXN_104',
	prot(name = 'B2975_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'L_LACTATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'B2975_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'L_LACTATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_104', 1.000000), 
	Parameter('rvs_TRANS_RXN_104', 0.000000))
Rule('TRANS_RXN0_515',
	prot(name = 'B2975_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'D_LACTATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'B2975_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'D_LACTATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_515', 1.000000), 
	Parameter('rvs_TRANS_RXN0_515', 0.000000))
Rule('TRANS_RXN0_622',
	prot(name = 'B2975_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_3564', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'B2975_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_3564', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_622', 1.000000), 
	Parameter('rvs_TRANS_RXN0_622', 1.000000))
Rule('RXN0_7050',
	prot(name = 'B4141_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'MET', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'B4141_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'MET', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_7050', 1.000000), 
	Parameter('rvs_RXN0_7050', 1.000000))
Rule('TRANS_RXN_282',
	prot(name = 'B4141_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'VAL', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'B4141_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'VAL', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_282', 1.000000), 
	Parameter('rvs_TRANS_RXN_282', 1.000000))
Rule('TRANS_RXN_281',
	prot(name = 'B4141_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'ILE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'B4141_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'ILE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_281', 1.000000), 
	Parameter('rvs_TRANS_RXN_281', 1.000000))
Rule('TRANS_RXN0_270',
	prot(name = 'B4141_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'LEU', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'B4141_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'LEU', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_270', 1.000000), 
	Parameter('rvs_TRANS_RXN0_270', 1.000000))
Rule('TRANS_RXN_340',
	prot(name = 'BCR_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_20921', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'BCR_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_20921', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_340', 1.000000), 
	Parameter('rvs_TRANS_RXN_340', 1.000000))
Rule('TRANS_RXN_44',
	prot(name = 'BCR_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Drugs', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'BCR_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Drugs', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_44', 1.000000), 
	Parameter('rvs_TRANS_RXN_44', 1.000000))
Rule('TRANS_RXN_99',
	prot(name = 'BETT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CHOLINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'BETT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CHOLINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_99', 1.000000), 
	Parameter('rvs_TRANS_RXN_99', 1.000000))
Rule('TRANS_RXN_126B',
	prot(name = 'BRNQ_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'LEU', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'BRNQ_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'LEU', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_126B', 1.000000), 
	Parameter('rvs_TRANS_RXN_126B', 1.000000))
Rule('TRANS_RXN_126A',
	prot(name = 'BRNQ_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'VAL', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'BRNQ_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'VAL', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_126A', 1.000000), 
	Parameter('rvs_TRANS_RXN_126A', 1.000000))
Rule('TRANS_RXN_126',
	prot(name = 'BRNQ_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ILE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'BRNQ_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ILE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_126', 1.000000), 
	Parameter('rvs_TRANS_RXN_126', 1.000000))
Rule('TRANS_RXN_68',
	prot(name = 'CADB_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CADAVERINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'LYS', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'CADB_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CADAVERINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'LYS', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_68', 1.000000), 
	Parameter('rvs_TRANS_RXN_68', 1.000000))
Rule('TRANS_RXN0_212',
	prot(name = 'CADB_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CADAVERINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'CADB_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CADAVERINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_212', 1.000000), 
	Parameter('rvs_TRANS_RXN0_212', 1.000000))
Rule('TRANS_RXN_42',
	prot(name = 'CHAA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Kplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'CHAA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Kplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_42', 1.000000), 
	Parameter('rvs_TRANS_RXN_42', 1.000000))
Rule('TRANS_RXN_101',
	prot(name = 'CHAA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'CHAA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_101', 1.000000), 
	Parameter('rvs_TRANS_RXN_101', 0.000000))
Rule('TRANS_RXN_338',
	prot(name = 'CMR_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD0_1938', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'CMR_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD0_1938', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_338', 1.000000), 
	Parameter('rvs_TRANS_RXN_338', 1.000000))
Rule('TRANS_RXN_337',
	prot(name = 'CMR_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_20894', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'CMR_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_20894', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_337', 1.000000), 
	Parameter('rvs_TRANS_RXN_337', 1.000000))
Rule('TRANS_RXN_116',
	prot(name = 'CODB_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CYTOSINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'CODB_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CYTOSINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_116', 1.000000), 
	Parameter('rvs_TRANS_RXN_116', 0.000000))
Rule('TRANS_RXN_141B',
	prot(name = 'CORA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'NIplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'CORA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'NIplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_141B', 1.000000), 
	Parameter('rvs_TRANS_RXN_141B', 0.000000))
Rule('TRANS_RXN_141A',
	prot(name = 'CORA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'COplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'CORA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'COplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_141A', 1.000000), 
	Parameter('rvs_TRANS_RXN_141A', 0.000000))
Rule('TRANS_RXN_141',
	prot(name = 'CORA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'MGplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'CORA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'MGplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_141', 1.000000), 
	Parameter('rvs_TRANS_RXN_141', 0.000000))
Rule('TRANS_RXN_155',
	cplx(name = 'CPLX_153', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSH_PHOSPHORYLATED', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CELLOBIOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX_153', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_507', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSH_MONOMER', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_155', 1.000000), 
	Parameter('rvs_TRANS_RXN_155', 0.000000))
Rule('TRANS_RXN_153A',
	cplx(name = 'CPLX_153', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSH_PHOSPHORYLATED', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_1142', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX_153', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_1181', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSH_MONOMER', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_153A', 1.000000), 
	Parameter('rvs_TRANS_RXN_153A', 0.000000))
Rule('TRANS_RXN_153',
	cplx(name = 'CPLX_153', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'HYDROQUINONE_O_BETA_D_GLUCOPYRANOSIDE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSH_PHOSPHORYLATED', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX_153', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_1162', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSH_MONOMER', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_153', 1.000000), 
	Parameter('rvs_TRANS_RXN_153', 0.000000))
Rule('TRANS_RXN0_518',
	cplx(name = 'CPLX_154', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_3570', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSH_PHOSPHORYLATED', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX_154', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_2499', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSH_MONOMER', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_518', 1.000000), 
	Parameter('rvs_TRANS_RXN0_518', 0.000000))
Rule('TRANS_RXN_157',
	cplx(name = 'CPLX_154', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSH_PHOSPHORYLATED', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Glucopyranose', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX_154', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'D_glucopyranose_6_phosphate', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSH_MONOMER', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_157', 1.000000), 
	Parameter('rvs_TRANS_RXN_157', 0.000000))
Rule('TRANS_RXN_155B',
	cplx(name = 'CPLX_155', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSH_PHOSPHORYLATED', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CHITOBIOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX_155', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'DIACETYLCHITOBIOSE_6_PHOSPHATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSH_MONOMER', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_155B', 1.000000), 
	Parameter('rvs_TRANS_RXN_155B', 0.000000))
Rule('TRANS_RXN_156',
	cplx(name = 'CPLX_156', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSH_PHOSPHORYLATED', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'MANNITOL', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX_156', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'MANNITOL_1P', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSH_MONOMER', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_156', 1.000000), 
	Parameter('rvs_TRANS_RXN_156', 0.000000))
Rule('TRANS_RXN0_583',
	cplx(name = 'CPLX_157', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_3582', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSH_PHOSPHORYLATED', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX_157', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSH_MONOMER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_16619', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_583', 1.000000), 
	Parameter('rvs_TRANS_RXN0_583', 0.000000))
Rule('TRANS_RXN0_582',
	cplx(name = 'CPLX_158', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'FRU', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSI_PHOSPHORYLATED', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX_158', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'D_fructose_1_phosphate', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSI_MONOMER', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_582', 1.000000), 
	Parameter('rvs_TRANS_RXN0_582', 0.000000))
Rule('TRANS_RXN0_618',
	cplx(name = 'CPLX_158', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSI_PHOSPHORYLATED', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'D_Fructopyranose', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX_158', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSI_MONOMER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'D_fructopyranose_1_phosphate', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_618', 1.000000), 
	Parameter('rvs_TRANS_RXN0_618', 0.000000))
Rule('TRANS_RXN_158',
	cplx(name = 'CPLX_158', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Fructofuranose', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSI_PHOSPHORYLATED', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX_158', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'D_fructofuranose_1_phosphate', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSI_MONOMER', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_158', 1.000000), 
	Parameter('rvs_TRANS_RXN_158', 0.000000))
Rule('TRANS_RXN_165',
	cplx(name = 'CPLX_165', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'D_mannopyranose', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSH_PHOSPHORYLATED', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX_165', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_15979', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSH_MONOMER', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_165', 1.000000), 
	Parameter('rvs_TRANS_RXN_165', 0.000000))
Rule('TRANS_RXN0_540',
	cplx(name = 'CPLX_165', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = '_2_DEOXY_D_GLUCOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSH_PHOSPHORYLATED', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX_165', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = '_2_DEOXY_D_GLUCOSE_6_PHOSPHATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSH_MONOMER', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_540', 1.000000), 
	Parameter('rvs_TRANS_RXN0_540', 0.000000))
Rule('TRANS_RXN0_446',
	cplx(name = 'CPLX_165', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'N_acetyl_D_mannosamine', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSH_PHOSPHORYLATED', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX_165', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'N_ACETYL_D_MANNOSAMINE_6P', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSH_MONOMER', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_446', 1.000000), 
	Parameter('rvs_TRANS_RXN0_446', 0.000000))
Rule('TRANS_RXN_167A',
	cplx(name = 'CPLX_165', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSH_PHOSPHORYLATED', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'GLUCOSAMINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX_165', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'D_GLUCOSAMINE_6_P', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSH_MONOMER', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_167A', 1.000000), 
	Parameter('rvs_TRANS_RXN_167A', 0.000000))
Rule('TRANS_RXN_167',
	cplx(name = 'CPLX_165', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSH_PHOSPHORYLATED', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'N_acetyl_D_glucosamine', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX_165', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'N_ACETYL_D_GLUCOSAMINE_6_P', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSH_MONOMER', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_167', 1.000000), 
	Parameter('rvs_TRANS_RXN_167', 0.000000))
Rule('TRANS_RXN_158A',
	cplx(name = 'CPLX_165', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Fructofuranose', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSH_PHOSPHORYLATED', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX_165', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_18719', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSH_MONOMER', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_158A', 1.000000), 
	Parameter('rvs_TRANS_RXN_158A', 0.000000))
Rule('TRANS_RXN_169',
	cplx(name = 'CPLX_166', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSH_PHOSPHORYLATED', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'SORBITOL', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX_166', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'D_SORBITOL_6_P', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSH_MONOMER', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_169', 1.000000), 
	Parameter('rvs_TRANS_RXN_169', 0.000000))
Rule('TRANS_RXN_168',
	cplx(name = 'CPLX_168', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSH_PHOSPHORYLATED', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'TREHALOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX_168', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'TREHALOSE_6P', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSH_MONOMER', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_168', 1.000000), 
	Parameter('rvs_TRANS_RXN_168', 0.000000))
Rule('RXN_5068',
	cplx(name = 'CPLX_3945', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'EG11489_MONOMER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX_3945', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'EG11489_MONOMER', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN_5068', 1.000000), 
	Parameter('rvs_RXN_5068', 0.000000))
Rule('RXN0_7190',
	cplx(name = 'CPLX_7', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_2039', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX_7', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_2039', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_7190', 1.000000), 
	Parameter('rvs_RXN0_7190', 1.000000))
Rule('TRANS_RXN0_264',
	cplx(name = 'CPLX_7', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_763', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX_7', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_763', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_264', 1.000000), 
	Parameter('rvs_TRANS_RXN0_264', 0.000000))
Rule('TRANS_RXN0_280',
	cplx(name = 'CPLX0_1721', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CUplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_1721', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CUplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_280', 1.000000), 
	Parameter('rvs_TRANS_RXN0_280', 0.000000))
Rule('TRANS_RXN_90',
	cplx(name = 'CPLX0_1721', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'AGplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_1721', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'AGplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_90', 1.000000), 
	Parameter('rvs_TRANS_RXN_90', 0.000000))
Rule('RXN0_1565',
	cplx(name = 'CPLX0_1924', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'COB_I_ALAMIN', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_1924', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'COB_I_ALAMIN', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_1565', 1.000000), 
	Parameter('rvs_RXN0_1565', 0.000000))
Rule('TRANS_RXN0_283',
	cplx(name = 'CPLX0_1924', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'COBINAMIDE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_1924', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'COBINAMIDE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_283', 1.000000), 
	Parameter('rvs_TRANS_RXN0_283', 0.000000))
Rule('RXN0_1682',
	cplx(name = 'CPLX0_1941', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'FERRIC_ENTEROBACTIN_COMPLEX', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_1941', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'FERRIC_ENTEROBACTIN_COMPLEX', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_1682', 1.000000), 
	Parameter('rvs_RXN0_1682', 0.000000))
Rule('RXN0_1701',
	cplx(name = 'CPLX0_1942', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_2241', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_1942', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_2241', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_1701', 1.000000), 
	Parameter('rvs_RXN0_1701', 0.000000))
Rule('RXN0_1684',
	cplx(name = 'CPLX0_1943', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'FERRIC_CITRATE_COMPLEX', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_1943', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'FERRIC_CITRATE_COMPLEX', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_1684', 1.000000), 
	Parameter('rvs_RXN0_1684', 0.000000))
Rule('TRANS_RXN_365',
	cplx(name = 'CPLX0_2121', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'DEOXYCHOLATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_2121', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'DEOXYCHOLATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_365', 1.000000), 
	Parameter('rvs_TRANS_RXN_365', 0.000000))
Rule('TRANS_RXN_364',
	cplx(name = 'CPLX0_2121', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_7970', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_2121', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_7970', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_364', 1.000000), 
	Parameter('rvs_TRANS_RXN_364', 0.000000))
Rule('TRANS_RXN_363',
	cplx(name = 'CPLX0_2121', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_21025', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_2121', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_21025', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_363', 1.000000), 
	Parameter('rvs_TRANS_RXN_363', 0.000000))
Rule('TRANS_RXN_352',
	cplx(name = 'CPLX0_2141', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'DEOXYCHOLATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_2141', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'DEOXYCHOLATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_352', 1.000000), 
	Parameter('rvs_TRANS_RXN_352', 0.000000))
Rule('TRANS_RXN_367',
	cplx(name = 'CPLX0_2141', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Erythromycins', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_2141', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Erythromycins', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_367', 1.000000), 
	Parameter('rvs_TRANS_RXN_367', 0.000000))
Rule('TRANS_RXN_354',
	cplx(name = 'CPLX0_2141', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_21070', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_2141', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_21070', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_354', 1.000000), 
	Parameter('rvs_TRANS_RXN_354', 0.000000))
Rule('TRANS_RXN_355',
	cplx(name = 'CPLX0_2141', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_9288', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_2141', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_9288', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_355', 1.000000), 
	Parameter('rvs_TRANS_RXN_355', 0.000000))
Rule('TRANS_RXN_161',
	cplx(name = 'CPLX0_231', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Hpr_pi_phospho_L_histidines', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'GALACTITOL', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_231', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'GALACTITOL_1_PHOSPHATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Hpr_Histidine', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_161', 1.000000), 
	Parameter('rvs_TRANS_RXN_161', 0.000000))
Rule('TRANS_RXN_360',
	cplx(name = 'CPLX0_3932', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Gentamycins', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_3932', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Gentamycins', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_360', 1.000000), 
	Parameter('rvs_TRANS_RXN_360', 0.000000))
Rule('TRANS_RXN0_268',
	cplx(name = 'CPLX0_3970', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'L_ALA_GAMMA_D_GLU_DAP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'CPLX0_3970', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'L_ALA_GAMMA_D_GLU_DAP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_268', 1.000000), 
	Parameter('rvs_TRANS_RXN0_268', 0.000000))
Rule('TRANS_RXN0_233',
	cplx(name = 'CPLX0_4', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = '_4_hydroxybenzoate', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_4', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = '_4_hydroxybenzoate', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_233', 1.000000), 
	Parameter('rvs_TRANS_RXN0_233', 1.000000))
Rule('RXN0_2481',
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Hydrophilic_Solute_Or_Ion_LT_600Da', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Hydrophilic_Solute_Or_Ion_LT_600Da', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_2481', 1.000000), 
	Parameter('rvs_RXN0_2481', 1.000000))
Rule('RXN0_7241',
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Medium_chain_fatty_acids', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Medium_chain_fatty_acids', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_7241', 1.000000), 
	Parameter('rvs_RXN0_7241', 1.000000))
Rule('RXN0_7211',
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Organophosphorus_Compounds', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Organophosphorus_Compounds', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_7211', 1.000000), 
	Parameter('rvs_RXN0_7211', 1.000000))
Rule('RXN0_7210',
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Glycosides', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Glycosides', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_7210', 1.000000), 
	Parameter('rvs_RXN0_7210', 1.000000))
Rule('RXN0_7209',
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Sugar', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Sugar', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_7209', 1.000000), 
	Parameter('rvs_RXN0_7209', 1.000000))
Rule('RXN0_7208',
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Sugar_Phosphate', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Sugar_Phosphate', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_7208', 1.000000), 
	Parameter('rvs_RXN0_7208', 1.000000))
Rule('RXN0_7207',
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Monocarboxylates', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Monocarboxylates', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_7207', 1.000000), 
	Parameter('rvs_RXN0_7207', 1.000000))
Rule('RXN0_7206',
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Aromatics', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Aromatics', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_7206', 1.000000), 
	Parameter('rvs_RXN0_7206', 1.000000))
Rule('RXN0_7204',
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Trisaccharides', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Trisaccharides', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_7204', 1.000000), 
	Parameter('rvs_RXN0_7204', 1.000000))
Rule('RXN0_7203',
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Disaccharides', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Disaccharides', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_7203', 1.000000), 
	Parameter('rvs_RXN0_7203', 1.000000))
Rule('RXN0_7202',
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'OLIGOPEPTIDES', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'OLIGOPEPTIDES', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_7202', 1.000000), 
	Parameter('rvs_RXN0_7202', 1.000000))
Rule('RXN0_7201',
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NUCLEOTIDE_SUGARS', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NUCLEOTIDE_SUGARS', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_7201', 1.000000), 
	Parameter('rvs_RXN0_7201', 1.000000))
Rule('RXN0_7200',
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Nucleotides', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Nucleotides', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_7200', 1.000000), 
	Parameter('rvs_RXN0_7200', 1.000000))
Rule('RXN0_7199',
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Nucleosides', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Nucleosides', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_7199', 1.000000), 
	Parameter('rvs_RXN0_7199', 1.000000))
Rule('RXN0_7247',
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Aldehydes', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Aldehydes', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_7247', 1.000000), 
	Parameter('rvs_RXN0_7247', 1.000000))
Rule('RXN0_7246',
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Lactones', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Lactones', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_7246', 1.000000), 
	Parameter('rvs_RXN0_7246', 1.000000))
Rule('RXN0_7245',
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Amides', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Amides', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_7245', 1.000000), 
	Parameter('rvs_RXN0_7245', 1.000000))
Rule('RXN0_7244',
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'All_Amines', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'All_Amines', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_7244', 1.000000), 
	Parameter('rvs_RXN0_7244', 1.000000))
Rule('RXN0_7243',
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Hydroxy_carboxylates', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Hydroxy_carboxylates', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_7243', 1.000000), 
	Parameter('rvs_RXN0_7243', 1.000000))
Rule('RXN0_7242',
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Aldonic_Acids', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Aldonic_Acids', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_7242', 1.000000), 
	Parameter('rvs_RXN0_7242', 1.000000))
Rule('TRANS_RXN0_615',
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_560', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_560', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_615', 1.000000), 
	Parameter('rvs_TRANS_RXN0_615', 1.000000))
Rule('TRANS_RXN0_614',
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Inositols', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Inositols', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_614', 1.000000), 
	Parameter('rvs_TRANS_RXN0_614', 1.000000))
Rule('TRANS_RXN0_612',
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Amino_Acids', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Amino_Acids', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_612', 1.000000), 
	Parameter('rvs_TRANS_RXN0_612', 1.000000))
Rule('TRANS_RXN0_611',
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Bases', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Bases', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_611', 1.000000), 
	Parameter('rvs_TRANS_RXN0_611', 1.000000))
Rule('TRANS_RXN0_609',
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'dicarboxylate', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'dicarboxylate', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_609', 1.000000), 
	Parameter('rvs_TRANS_RXN0_609', 1.000000))
Rule('TRANS_RXN0_608',
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Sugar_alcohols', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Sugar_alcohols', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_608', 1.000000), 
	Parameter('rvs_TRANS_RXN0_608', 1.000000))
Rule('TRANS_RXN0_607',
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Short_Chain_Alcohols', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Short_Chain_Alcohols', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_607', 1.000000), 
	Parameter('rvs_TRANS_RXN0_607', 1.000000))
Rule('TRANS_RXN0_606',
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Short_Chain_Carboxylates', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Short_Chain_Carboxylates', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_606', 1.000000), 
	Parameter('rvs_TRANS_RXN0_606', 1.000000))
Rule('TRANS_RXN0_604',
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ORGANOSULFUR', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ORGANOSULFUR', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_604', 1.000000), 
	Parameter('rvs_TRANS_RXN0_604', 1.000000))
Rule('TRANS_RXN0_603',
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_603', 1.000000), 
	Parameter('rvs_TRANS_RXN0_603', 1.000000))
Rule('TRANS_RXN0_601',
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Ions', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Ions', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_601', 1.000000), 
	Parameter('rvs_TRANS_RXN0_601', 1.000000))
Rule('TRANS_RXN0_598',
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Glycerol_1_phosphate', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7530', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Glycerol_1_phosphate', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_598', 1.000000), 
	Parameter('rvs_TRANS_RXN0_598', 1.000000))
Rule('TRANS_RXN0_206',
	cplx(name = 'CPLX0_7532', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'AMMONIUM', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7532', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'AMMONIUM', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_206', 1.000000), 
	Parameter('rvs_TRANS_RXN0_206', 0.000000))
Rule('TRANS_RXN0_490',
	cplx(name = 'CPLX0_7533', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'BETAINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7533', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'BETAINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_490', 1.000000), 
	Parameter('rvs_TRANS_RXN0_490', 1.000000))
Rule('TRANS_RXN_380',
	cplx(name = 'CPLX0_7534', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Beta_Lactams', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7534', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Beta_Lactams', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_380', 1.000000), 
	Parameter('rvs_TRANS_RXN_380', 1.000000))
Rule('RXN0_2162',
	cplx(name = 'CPLX0_7535', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'AGMATHINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ARG', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7535', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'AGMATHINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ARG', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_2162', 1.000000), 
	Parameter('rvs_RXN0_2162', 1.000000))
Rule('TRANS_RXN_86',
	cplx(name = 'CPLX0_7626', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Unspecified_Ion_Or_Solute', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7626', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Unspecified_Ion_Or_Solute', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_86', 1.000000), 
	Parameter('rvs_TRANS_RXN_86', 0.000000))
Rule('TRANS_RXN_129',
	cplx(name = 'CPLX0_7629', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7629', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_129', 1.000000), 
	Parameter('rvs_TRANS_RXN_129', 1.000000))
Rule('TRANS_RXN_292',
	cplx(name = 'CPLX0_7629', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'LIplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7629', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'LIplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_292', 1.000000), 
	Parameter('rvs_TRANS_RXN_292', 1.000000))
Rule('TRANS_RXN0_244',
	cplx(name = 'CPLX0_7641', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CDplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7641', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CDplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_244', 1.000000), 
	Parameter('rvs_TRANS_RXN0_244', 0.000000))
Rule('RXN0_6',
	cplx(name = 'CPLX0_7641', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'FEplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7641', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'FEplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_6', 1.000000), 
	Parameter('rvs_RXN0_6', 1.000000))
Rule('TRANS_RXN_29',
	cplx(name = 'CPLX0_7642', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PRO', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7642', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PRO', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_29', 1.000000), 
	Parameter('rvs_TRANS_RXN_29', 1.000000))
Rule('TRANS_RXN_29A',
	cplx(name = 'CPLX0_7642', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'BETAINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7642', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'BETAINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_29A', 1.000000), 
	Parameter('rvs_TRANS_RXN_29A', 1.000000))
Rule('TRANS_RXN_145',
	cplx(name = 'CPLX0_7653', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7653', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_145', 1.000000), 
	Parameter('rvs_TRANS_RXN_145', 1.000000))
Rule('TRANS_RXN_131',
	cplx(name = 'CPLX0_7654', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'GLYCEROL', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7654', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'GLYCEROL', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_131', 1.000000), 
	Parameter('rvs_TRANS_RXN_131', 1.000000))
Rule('RXN0_7189',
	cplx(name = 'CPLX0_7654', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Sugar_alcohols', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7654', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Sugar_alcohols', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_7189', 1.000000), 
	Parameter('rvs_RXN0_7189', 1.000000))
Rule('TRANS_RXN0_536',
	cplx(name = 'CPLX0_7654', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_1551', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7654', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_1551', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_536', 1.000000), 
	Parameter('rvs_TRANS_RXN0_536', 1.000000))
Rule('TRANS_RXN0_537',
	cplx(name = 'CPLX0_7654', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'GLY', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7654', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'GLY', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_537', 1.000000), 
	Parameter('rvs_TRANS_RXN0_537', 1.000000))
Rule('TRANS_RXN0_460',
	cplx(name = 'CPLX0_7654', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'UREA', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7654', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'UREA', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_460', 1.000000), 
	Parameter('rvs_TRANS_RXN0_460', 1.000000))
Rule('TRANS_RXN0_551',
	cplx(name = 'CPLX0_7654', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_763', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7654', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_763', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_551', 1.000000), 
	Parameter('rvs_TRANS_RXN0_551', 1.000000))
Rule('RXN0_7191',
	cplx(name = 'CPLX0_7654', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_2039', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7654', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_2039', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_7191', 1.000000), 
	Parameter('rvs_RXN0_7191', 1.000000))
Rule('RXN0_1741',
	cplx(name = 'CPLX0_7655', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'MALTOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7655', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'MALTOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_1741', 1.000000), 
	Parameter('rvs_RXN0_1741', 0.000000))
Rule('RXN0_1804',
	cplx(name = 'CPLX0_7655', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Unspecified_Ion_Or_Solute', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7655', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Unspecified_Ion_Or_Solute', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_1804', 1.000000), 
	Parameter('rvs_RXN0_1804', 0.000000))
Rule('TRANS_RXN0_269',
	cplx(name = 'CPLX0_7684', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'VAL', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7684', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'VAL', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_269', 1.000000), 
	Parameter('rvs_TRANS_RXN0_269', 1.000000))
Rule('TRANS_RXN_236',
	cplx(name = 'CPLX0_7704', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'LOS', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'CPLX0_7704', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'LOS', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_236', 1.000000), 
	Parameter('rvs_TRANS_RXN_236', 0.000000))
Rule('_3dot6dot3dot39_RXN',
	cplx(name = 'CPLX0_7704', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Lipopolysaccharides', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'CPLX0_7704', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Lipopolysaccharides', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd__3dot6dot3dot39_RXN', 1.000000), 
	Parameter('rvs__3dot6dot3dot39_RXN', 0.000000))
Rule('TRANS_RXN0_276',
	cplx(name = 'CPLX0_7720', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_1189', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7720', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_1189', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_276', 1.000000), 
	Parameter('rvs_TRANS_RXN0_276', 0.000000))
Rule('TRANS_RXN_351',
	cplx(name = 'CPLX0_7807', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_20940', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7807', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_20940', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_351', 1.000000), 
	Parameter('rvs_TRANS_RXN_351', 0.000000))
Rule('TRANS_RXN_1',
	cplx(name = 'CPLX0_7843', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'FORMATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7843', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'FORMATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_1', 1.000000), 
	Parameter('rvs_TRANS_RXN_1', 1.000000))
Rule('TRANS_RXN_381',
	cplx(name = 'CPLX0_7843', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_27', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7843', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_27', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_381', 1.000000), 
	Parameter('rvs_TRANS_RXN_381', 1.000000))
Rule('TRANS_RXN_100',
	cplx(name = 'CPLX0_7906', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'GAMMA_BUTYROBETAINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CARNITINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7906', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'GAMMA_BUTYROBETAINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CARNITINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_100', 1.000000), 
	Parameter('rvs_TRANS_RXN_100', 1.000000))
Rule('RXN0_1702',
	cplx(name = 'CPLX0_7952', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_621', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7952', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_621', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_1702', 1.000000), 
	Parameter('rvs_RXN0_1702', 0.000000))
Rule('RXN0_1981',
	cplx(name = 'CPLX0_7955', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ACET', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7955', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ACET', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_1981', 1.000000), 
	Parameter('rvs_RXN0_1981', 1.000000))
Rule('RXN0_5111',
	cplx(name = 'CPLX0_7955', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'GLYCOLLATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7955', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'GLYCOLLATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_5111', 1.000000), 
	Parameter('rvs_RXN0_5111', 1.000000))
Rule('TRANS_RXN0_576',
	cplx(name = 'CPLX0_7955', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_4544', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7955', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_4544', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_576', 1.000000), 
	Parameter('rvs_TRANS_RXN0_576', 1.000000))
Rule('RXN0_2501',
	cplx(name = 'CPLX0_7961', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CL_', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7961', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CL_', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_2501', 1.000000), 
	Parameter('rvs_RXN0_2501', 1.000000))
Rule('TRANS_RXN0_628',
	cplx(name = 'CPLX0_7963', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Drugs', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7963', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Drugs', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_628', 1.000000), 
	Parameter('rvs_TRANS_RXN0_628', 1.000000))
Rule('TRANS_RXN0_493',
	cplx(name = 'CPLX0_7963', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_20940', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7963', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_20940', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_493', 1.000000), 
	Parameter('rvs_TRANS_RXN0_493', 1.000000))
Rule('TRANS_RXN_344',
	cplx(name = 'CPLX0_7963', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_1938', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7963', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_1938', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_344', 1.000000), 
	Parameter('rvs_TRANS_RXN_344', 1.000000))
Rule('TRANS_RXN0_533',
	cplx(name = 'CPLX0_7963', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CHOLINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7963', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CHOLINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_533', 1.000000), 
	Parameter('rvs_TRANS_RXN0_533', 1.000000))
Rule('TRANS_RXN0_532',
	cplx(name = 'CPLX0_7963', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'BETAINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7963', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'BETAINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_532', 1.000000), 
	Parameter('rvs_TRANS_RXN0_532', 1.000000))
Rule('TRANS_RXN_237',
	cplx(name = 'CPLX0_7992', loc = 'per', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Lipopolysaccharides', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'CPLX0_7992', loc = 'per', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Lipopolysaccharides', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_237', 1.000000), 
	Parameter('rvs_TRANS_RXN_237', 0.000000))
Rule('TRANS_RXN0_549',
	cplx(name = 'CPLX0_7994', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_1192', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7994', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_1192', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_549', 1.000000), 
	Parameter('rvs_TRANS_RXN0_549', 0.000000))
Rule('RXN0_5413',
	cplx(name = 'CPLX0_7994', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'UDP_N_ACETYL_D_GLUCOSAMINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'N_acetyl_D_glucosamine', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7994', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_1192', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'UDP', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_5413', 1.000000), 
	Parameter('rvs_RXN0_5413', 0.000000))
Rule('RXN0_17',
	cplx(name = 'CPLX0_7', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NACMUR', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSH_PHOSPHORYLATED', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_7', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_881', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSH_MONOMER', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_17', 1.000000), 
	Parameter('rvs_RXN0_17', 0.000000))
Rule('TRANS_RXN_205A',
	cplx(name = 'CPLX0_8097', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Peptide_Antibiotics', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_8097', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Peptide_Antibiotics', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_205A', 1.000000), 
	Parameter('rvs_TRANS_RXN_205A', 0.000000))
Rule('TRANS_RXN0_593',
	cplx(name = 'CPLX0_8152', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CYSTINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'CPLX0_8152', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CYSTINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_593', 1.000000), 
	Parameter('rvs_TRANS_RXN0_593', 0.000000))
Rule('TRANS_RXN_291',
	cplx(name = 'CPLX0_8152', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'MESO_DIAMINOPIMELATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'CPLX0_8152', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'MESO_DIAMINOPIMELATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_291', 1.000000), 
	Parameter('rvs_TRANS_RXN_291', 0.000000))
Rule('TRANS_RXN0_508',
	cplx(name = 'CPLX0_8152', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_3740', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'CPLX0_8152', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_3740', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_508', 1.000000), 
	Parameter('rvs_TRANS_RXN0_508', 0.000000))
Rule('TRANS_RXN0_513',
	cplx(name = 'CPLX0_8152', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_3736', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'CPLX0_8152', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_3736', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_513', 1.000000), 
	Parameter('rvs_TRANS_RXN0_513', 0.000000))
Rule('TRANS_RXN_290',
	cplx(name = 'CPLX0_8152', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_1564', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'CPLX0_8152', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_1564', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_290', 1.000000), 
	Parameter('rvs_TRANS_RXN_290', 0.000000))
Rule('TRANS_RXN0_617',
	cplx(name = 'CPLX0_8152', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'HOMOCYSTINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'CPLX0_8152', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'HOMOCYSTINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_617', 1.000000), 
	Parameter('rvs_TRANS_RXN0_617', 0.000000))
Rule('RXN0_5256',
	cplx(name = 'CPLX0_8167', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Menaquinones', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'HYDROGEN_MOLECULE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_8167', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Menaquinols', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None, 
	Parameter('fwd_RXN0_5256', 1.000000), 
	Parameter('rvs_RXN0_5256', 1.000000))
Rule('RXN_16420',
	cplx(name = 'CPLX0_8167', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'HYDROGEN_MOLECULE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_8167', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None, 
	Parameter('fwd_RXN_16420', 1.000000), 
	Parameter('rvs_RXN_16420', 0.000000))
Rule('TRANS_RXN_369',
	cplx(name = 'CPLX0_8263', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_1470', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_8263', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_1470', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_369', 1.000000), 
	Parameter('rvs_TRANS_RXN_369', 1.000000))
Rule('TRANS_RXN_368',
	cplx(name = 'CPLX0_8263', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_20888', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_8263', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_20888', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_368', 1.000000), 
	Parameter('rvs_TRANS_RXN_368', 1.000000))
Rule('TRANS_RXN0_498',
	cplx(name = 'CPLX0_8271', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'F_', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_8271', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'F_', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_498', 1.000000), 
	Parameter('rvs_TRANS_RXN0_498', 1.000000))
Rule('RXN0_1721',
	cplx(name = 'CPLX0_8541', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_2482', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CPLX0_8541', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_2482', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_1721', 1.000000), 
	Parameter('rvs_RXN0_1721', 0.000000))
Rule('TRANS_RXN_62A',
	prot(name = 'CYCA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'D_ALANINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'CYCA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'D_ALANINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_62A', 1.000000), 
	Parameter('rvs_TRANS_RXN_62A', 1.000000))
Rule('RXN0_5130',
	prot(name = 'CYCA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'D_SERINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'CYCA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'D_SERINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_5130', 1.000000), 
	Parameter('rvs_RXN0_5130', 1.000000))
Rule('TRANS_RXN_62B',
	prot(name = 'CYCA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'GLY', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'CYCA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'GLY', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_62B', 1.000000), 
	Parameter('rvs_TRANS_RXN_62B', 1.000000))
Rule('RXN0_5202',
	prot(name = 'CYCA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'L_ALPHA_ALANINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'CYCA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'L_ALPHA_ALANINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_5202', 1.000000), 
	Parameter('rvs_RXN0_5202', 1.000000))
Rule('RXN0_5201',
	prot(name = 'CYCA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'B_ALANINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'CYCA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'B_ALANINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_5201', 1.000000), 
	Parameter('rvs_RXN0_5201', 1.000000))
Rule('RXN0_5203',
	prot(name = 'CYCA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_2482', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'CYCA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_2482', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_5203', 1.000000), 
	Parameter('rvs_RXN0_5203', 1.000000))
Rule('TRANS_RXN_14',
	prot(name = 'CYNX_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_69', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'CYNX_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_69', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_14', 1.000000), 
	Parameter('rvs_TRANS_RXN_14', 0.000000))
Rule('RXN_19778',
	cplx(name = 'CYT_D_UBIOX_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Ubiquinols', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'HYDROGEN_PEROXIDE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CYT_D_UBIOX_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Ubiquinones', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN_19778', 1.000000), 
	Parameter('rvs_RXN_19778', 0.000000))
Rule('RXN_19777',
	cplx(name = 'CYT_D_UBIOX_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_7249', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'HYDROGEN_PEROXIDE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CYT_D_UBIOX_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_7248', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN_19777', 1.000000), 
	Parameter('rvs_RXN_19777', 1.000000))
Rule('RXN0_5268',
	cplx(name = 'CYT_O_UBIOX_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Ubiquinols', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'CYT_O_UBIOX_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Ubiquinones', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_5268', 1.000000), 
	Parameter('rvs_RXN0_5268', 0.000000))
Rule('TRANS_RXN0_517',
	prot(name = 'DCTA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'C4_dicarboxylates', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'DCTA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'C4_dicarboxylates', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_517', 1.000000), 
	Parameter('rvs_TRANS_RXN0_517', 1.000000))
Rule('TRANS_RXN0_451',
	prot(name = 'DCTA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_660', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'DCTA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_660', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_451', 1.000000), 
	Parameter('rvs_TRANS_RXN0_451', 1.000000))
Rule('TRANS_RXN_122A',
	prot(name = 'DCTA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'L_ASPARTATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'DCTA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'L_ASPARTATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_122A', 1.000000), 
	Parameter('rvs_TRANS_RXN_122A', 1.000000))
Rule('TRANS_RXN_121C',
	prot(name = 'DCTA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'OROTATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'DCTA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'OROTATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_121C', 1.000000), 
	Parameter('rvs_TRANS_RXN_121C', 1.000000))
Rule('TRANS_RXN0_553',
	prot(name = 'DCTA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'FUM', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'DCTA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'FUM', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_553', 1.000000), 
	Parameter('rvs_TRANS_RXN0_553', 1.000000))
Rule('TRANS_RXN_121A',
	prot(name = 'DCTA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'MAL', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'DCTA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'MAL', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_121A', 1.000000), 
	Parameter('rvs_TRANS_RXN_121A', 1.000000))
Rule('TRANS_RXN_121',
	prot(name = 'DCTA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'SUC', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'DCTA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'SUC', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_121', 1.000000), 
	Parameter('rvs_TRANS_RXN_121', 1.000000))
Rule('TRANS_RXN_379',
	prot(name = 'DCUA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'L_ASPARTATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'FUM', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'DCUA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'L_ASPARTATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'FUM', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_379', 1.000000), 
	Parameter('rvs_TRANS_RXN_379', 1.000000))
Rule('TRANS_RXN_106',
	prot(name = 'DCUA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'SUC', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'FUM', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'DCUA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'FUM', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'SUC', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_106', 1.000000), 
	Parameter('rvs_TRANS_RXN_106', 1.000000))
Rule('TRANS_RXN_106B',
	prot(name = 'DCUA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'SUC', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'MAL', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'DCUA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'MAL', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'SUC', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_106B', 1.000000), 
	Parameter('rvs_TRANS_RXN_106B', 1.000000))
Rule('TRANS_RXN_106A',
	prot(name = 'DCUA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'SUC', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'L_ASPARTATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'DCUA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'L_ASPARTATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'SUC', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_106A', 1.000000), 
	Parameter('rvs_TRANS_RXN_106A', 1.000000))
Rule('TRANS_RXN_299',
	prot(name = 'DCUA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'FUM', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'DCUA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'FUM', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_299', 1.000000), 
	Parameter('rvs_TRANS_RXN_299', 1.000000))
Rule('TRANS_RXN0_499',
	prot(name = 'DCUB_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'D_TARTRATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'SUC', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'DCUB_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'SUC', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'D_TARTRATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_499', 1.000000), 
	Parameter('rvs_TRANS_RXN0_499', 1.000000))
Rule('TRANS_RXN_300',
	prot(name = 'DCUC_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'SUC', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'DCUC_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'SUC', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_300', 1.000000), 
	Parameter('rvs_TRANS_RXN_300', 1.000000))
Rule('TRANS_RXN0_495',
	prot(name = 'DSDX_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'D_SERINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'DSDX_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'D_SERINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_495', 1.000000), 
	Parameter('rvs_TRANS_RXN0_495', 0.000000))
Rule('TRANS_RXN0_586',
	prot(name = 'EG10003_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'SULFATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'EG10003_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'SULFATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_586', 1.000000), 
	Parameter('rvs_TRANS_RXN0_586', 1.000000))
Rule('RXN0_1802',
	prot(name = 'EG10280_MONOMER', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'Long_Chain_Fatty_Acids', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'EG10280_MONOMER', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'Long_Chain_Fatty_Acids', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_1802', 1.000000), 
	Parameter('rvs_RXN0_1802', 0.000000))
Rule('TRANS_RXN0_468',
	prot(name = 'EG11035_MONOMER', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'Nucleosides', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'EG11035_MONOMER', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'Nucleosides', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_468', 1.000000), 
	Parameter('rvs_TRANS_RXN0_468', 0.000000))
Rule('RXN0_16',
	prot(name = 'EG11167_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'MNplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'EG11167_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'MNplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_16', 1.000000), 
	Parameter('rvs_RXN0_16', 0.000000))
Rule('RXN0_14',
	prot(name = 'EG11167_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CUplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'EG11167_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CUplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_14', 1.000000), 
	Parameter('rvs_RXN0_14', 0.000000))
Rule('RXN0_12',
	prot(name = 'EG11167_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'ZNplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'EG11167_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'ZNplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_12', 1.000000), 
	Parameter('rvs_RXN0_12', 0.000000))
Rule('RXN0_10',
	prot(name = 'EG11167_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CDplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'EG11167_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CDplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_10', 1.000000), 
	Parameter('rvs_RXN0_10', 0.000000))
Rule('TRANS_RXN_8',
	prot(name = 'EG11167_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'FEplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'EG11167_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'FEplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_8', 1.000000), 
	Parameter('rvs_TRANS_RXN_8', 0.000000))
Rule('TRANS_RXN0_240',
	prot(name = 'EG11471_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'BIOTIN', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'EG11471_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'BIOTIN', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_240', 1.000000), 
	Parameter('rvs_TRANS_RXN0_240', 0.000000))
Rule('TRANS_RXN0_279',
	prot(name = 'EG11486_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'C55_PP_GLCNAC_MANNACA_FUC4NAC', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'EG11486_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'C55_PP_GLCNAC_MANNACA_FUC4NAC', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_279', 1.000000), 
	Parameter('rvs_TRANS_RXN0_279', 0.000000))
Rule('TRANS_RXN0_571',
	prot(name = 'EG11512_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'ACET', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'EG11512_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'ACET', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_571', 1.000000), 
	Parameter('rvs_TRANS_RXN0_571', 1.000000))
Rule('RXN0_1924',
	prot(name = 'EG11639_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CYS', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'EG11639_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CYS', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_1924', 1.000000), 
	Parameter('rvs_RXN0_1924', 0.000000))
Rule('RXN0_1923',
	prot(name = 'EG11639_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'ACETYLSERINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'EG11639_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'ACETYLSERINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_1923', 1.000000), 
	Parameter('rvs_RXN0_1923', 0.000000))
Rule('TRANS_RXN0_281',
	prot(name = 'EG11671_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = '_3_KETOBUTYRATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'EG11671_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = '_3_KETOBUTYRATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_281', 1.000000), 
	Parameter('rvs_TRANS_RXN0_281', 0.000000))
Rule('TRANS_RXN0_577',
	prot(name = 'EG11691_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'ADENINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'EG11691_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'ADENINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_577', 1.000000), 
	Parameter('rvs_TRANS_RXN0_577', 0.000000))
Rule('TRANS_RXN0_447',
	prot(name = 'EG11724_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'ADENINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'EG11724_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'ADENINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_447', 1.000000), 
	Parameter('rvs_TRANS_RXN0_447', 1.000000))
Rule('TRANS_RXN_267',
	prot(name = 'EG11902_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'cystine', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'EG11902_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'cystine', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_267', 1.000000), 
	Parameter('rvs_TRANS_RXN_267', 0.000000))
Rule('TRANS_RXN0_470',
	prot(name = 'EG11919_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'EG11919_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_470', 1.000000), 
	Parameter('rvs_TRANS_RXN0_470', 0.000000))
Rule('TRANS_RXN0_562',
	prot(name = 'EG11939_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'HYPOXANTHINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'EG11939_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'HYPOXANTHINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_562', 0.000000), 
	Parameter('rvs_TRANS_RXN0_562', 1.000000))
Rule('TRANS_RXN0_578',
	prot(name = 'EG11939_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'GUANINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'EG11939_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'GUANINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_578', 1.000000), 
	Parameter('rvs_TRANS_RXN0_578', 0.000000))
Rule('TRANS_RXN_242',
	prot(name = 'EG12134_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'HOMO_SER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'EG12134_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'HOMO_SER', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_242', 1.000000), 
	Parameter('rvs_TRANS_RXN_242', 1.000000))
Rule('TRANS_RXN0_0244',
	prot(name = 'EG12134_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'THR', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'EG12134_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'THR', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_0244', 1.000000), 
	Parameter('rvs_TRANS_RXN0_0244', 1.000000))
Rule('TRANS_RXN_294',
	prot(name = 'EG12455_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = '_2_ACYL_GPE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'EG12455_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = '_2_ACYL_GPE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_294', 1.000000), 
	Parameter('rvs_TRANS_RXN_294', 1.000000))
Rule('TRANS_RXN_295',
	prot(name = 'EG12455_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'Lysophosphatidylglycerols', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'EG12455_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'Lysophosphatidylglycerols', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_295', 1.000000), 
	Parameter('rvs_TRANS_RXN_295', 1.000000))
Rule('TRANS_RXN_387',
	prot(name = 'EG12455_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'a_lyso_cardiolipin', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'EG12455_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'a_lyso_cardiolipin', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_387', 1.000000), 
	Parameter('rvs_TRANS_RXN_387', 0.000000))
Rule('TRANS_RXN0_265',
	prot(name = 'EG12713_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'Amino_Acids', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'EG12713_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'Amino_Acids', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_265', 1.000000), 
	Parameter('rvs_TRANS_RXN0_265', 0.000000))
Rule('RXN0_2461',
	prot(name = 'EIISGA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PTSH_PHOSPHORYLATED', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ASCORBATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'EIISGA', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'L_ASCORBATE_6_PHOSPHATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSH_MONOMER', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_2461', 1.000000), 
	Parameter('rvs_RXN0_2461', 0.000000))
Rule('TRANS_RXN_339',
	prot(name = 'EMRD_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_7970', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'EMRD_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_7970', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_339', 1.000000), 
	Parameter('rvs_TRANS_RXN_339', 1.000000))
Rule('TRANS_RXN_123',
	prot(name = 'EXUT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'D_GALACTURONATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'EXUT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'D_GALACTURONATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_123', 1.000000), 
	Parameter('rvs_TRANS_RXN_123', 1.000000))
Rule('TRANS_RXN_35',
	prot(name = 'EXUT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'GLUCURONATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'EXUT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'GLUCURONATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_35', 1.000000), 
	Parameter('rvs_TRANS_RXN_35', 1.000000))
Rule('FORMATEDEHYDROG_RXN',
	cplx(name = 'FORMATEDEHYDROGN_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'FORMATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Menaquinones', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'FORMATEDEHYDROGN_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Menaquinols', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_FORMATEDEHYDROG_RXN', 1.000000), 
	Parameter('rvs_FORMATEDEHYDROG_RXN', 0.000000))
Rule('TRANS_RXN_41',
	prot(name = 'FSR_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD0_441', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'FSR_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD0_441', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_41', 1.000000), 
	Parameter('rvs_TRANS_RXN_41', 1.000000))
Rule('TRANS_RXN_20',
	prot(name = 'FUCP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'L_fucoses', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'FUCP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'L_fucoses', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_20', 1.000000), 
	Parameter('rvs_TRANS_RXN_20', 1.000000))
Rule('RXN0_7221',
	prot(name = 'FUCP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'D_ARABINOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'FUCP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'D_ARABINOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_7221', 1.000000), 
	Parameter('rvs_RXN0_7221', 1.000000))
Rule('RXN0_7222',
	prot(name = 'FUCP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'L_Galactose', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'FUCP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'L_Galactose', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_7222', 1.000000), 
	Parameter('rvs_RXN0_7222', 1.000000))
Rule('TRANS_RXN0_207',
	prot(name = 'G6260_MONOMER', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CUplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	prot(name = 'G6260_MONOMER', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CUplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_207', 1.000000), 
	Parameter('rvs_TRANS_RXN0_207', 0.000000))
Rule('TRANS_RXN0_445',
	prot(name = 'G6370_MONOMER', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CHITOBIOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'G6370_MONOMER', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CHITOBIOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_445', 1.000000), 
	Parameter('rvs_TRANS_RXN0_445', 0.000000))
Rule('TRANS_RXN0_569',
	prot(name = 'G6458_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'LYS', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'G6458_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'LYS', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_569', 1.000000), 
	Parameter('rvs_TRANS_RXN0_569', 0.000000))
Rule('TRANS_RXN0_275',
	prot(name = 'G6531_MONOMER', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD0_1193', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'G6531_MONOMER', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD0_1193', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_275', 1.000000), 
	Parameter('rvs_TRANS_RXN0_275', 0.000000))
Rule('TRANS_RXN0_286',
	prot(name = 'G6561_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'C6', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'G6561_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'C6', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_286', 1.000000), 
	Parameter('rvs_TRANS_RXN0_286', 0.000000))
Rule('RXN0_2542',
	prot(name = 'G6657_MONOMER', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_18254', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'G6657_MONOMER', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_18254', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_2542', 1.000000), 
	Parameter('rvs_RXN0_2542', 0.000000))
Rule('TRANS_RXN_346',
	prot(name = 'G6674_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'ZNplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'G6674_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'ZNplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_346', 1.000000), 
	Parameter('rvs_TRANS_RXN_346', 0.000000))
Rule('TRANS_RXN0_453',
	prot(name = 'G6859_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_10774', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'G6859_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_10774', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_453', 1.000000), 
	Parameter('rvs_TRANS_RXN0_453', 1.000000))
Rule('TRANS_RXN_285',
	prot(name = 'G6934_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CYSTINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'G6934_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CYSTINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_285', 1.000000), 
	Parameter('rvs_TRANS_RXN_285', 1.000000))
Rule('TRANS_RXN_330',
	prot(name = 'G6934_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'SULFO_CYSTEINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'G6934_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'SULFO_CYSTEINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_330', 1.000000), 
	Parameter('rvs_TRANS_RXN_330', 1.000000))
Rule('TRANS_RXN0_616',
	prot(name = 'G6934_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD0_1564', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'G6934_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD0_1564', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_616', 1.000000), 
	Parameter('rvs_TRANS_RXN0_616', 1.000000))
Rule('TRANS_RXN_286',
	prot(name = 'G6934_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'HOMOCYSTINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'G6934_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'HOMOCYSTINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_286', 1.000000), 
	Parameter('rvs_TRANS_RXN_286', 1.000000))
Rule('TRANS_RXN0_487',
	prot(name = 'G6999_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'MNplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'G6999_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'MNplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_487', 1.000000), 
	Parameter('rvs_TRANS_RXN0_487', 0.000000))
Rule('TRANS_RXN_376',
	prot(name = 'G7097_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD0_2640', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'G7097_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD0_2640', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_376', 1.000000), 
	Parameter('rvs_TRANS_RXN_376', 0.000000))
Rule('TRANS_RXN0_585',
	prot(name = 'G7138_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'COplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'G7138_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'COplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_585', 1.000000), 
	Parameter('rvs_TRANS_RXN0_585', 0.000000))
Rule('TRANS_RXN0_584',
	prot(name = 'G7138_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'NIplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'G7138_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'NIplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_584', 1.000000), 
	Parameter('rvs_TRANS_RXN0_584', 0.000000))
Rule('TRANS_RXN0_469',
	prot(name = 'G7399_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'L_ALPHA_ALANINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'G7399_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'L_ALPHA_ALANINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_469', 1.000000), 
	Parameter('rvs_TRANS_RXN0_469', 1.000000))
Rule('RXN_15315',
	prot(name = 'G7921_MONOMER', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD0_1123', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'G7921_MONOMER', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD0_1123', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN_15315', 1.000000), 
	Parameter('rvs_RXN_15315', 0.000000))
Rule('RXN0_0',
	prot(name = 'G7921_MONOMER', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'N_ACETYLNEURAMINATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'G7921_MONOMER', loc = 'omem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'N_ACETYLNEURAMINATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_0', 1.000000), 
	Parameter('rvs_RXN0_0', 0.000000))
Rule('TRANS_RXN_335',
	prot(name = 'G7942_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PYRUVATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'G7942_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PYRUVATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_335', 1.000000), 
	Parameter('rvs_TRANS_RXN_335', 1.000000))
Rule('TRANS_RXN_57',
	prot(name = 'GABP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = '_4_AMINO_BUTYRATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'GABP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = '_4_AMINO_BUTYRATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_57', 1.000000), 
	Parameter('rvs_TRANS_RXN_57', 1.000000))
Rule('TRANS_RXN_384',
	prot(name = 'GABP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = '_5_AMINOPENTANOATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'GABP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = '_5_AMINOPENTANOATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_384', 1.000000), 
	Parameter('rvs_TRANS_RXN_384', 1.000000))
Rule('TRANS_RXN_21',
	prot(name = 'GALP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'D_galactopyranose', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'GALP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'D_galactopyranose', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_21', 1.000000), 
	Parameter('rvs_TRANS_RXN_21', 1.000000))
Rule('RXN0_7077',
	prot(name = 'GALP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Glucopyranose', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'GALP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Glucopyranose', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_7077', 1.000000), 
	Parameter('rvs_RXN0_7077', 0.000000))
Rule('TRANS_RXN_22',
	prot(name = 'GLPT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'GLYCEROL_3P', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'GLPT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'GLYCEROL_3P', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_22', 1.000000), 
	Parameter('rvs_TRANS_RXN_22', 1.000000))
Rule('TRANS_RXN_162',
	prot(name = 'GLTP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'GLT', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'GLTP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'GLT', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_162', 1.000000), 
	Parameter('rvs_TRANS_RXN_162', 1.000000))
Rule('TRANS_RXN_122',
	prot(name = 'GLTS_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'GLT', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'GLTS_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'GLT', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_122', 1.000000), 
	Parameter('rvs_TRANS_RXN_122', 1.000000))
Rule('TRANS_RXN_81',
	prot(name = 'GNTP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'FRUCTURONATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'GNTP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'FRUCTURONATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_81', 1.000000), 
	Parameter('rvs_TRANS_RXN_81', 1.000000))
Rule('TRANS_RXN0_209',
	prot(name = 'GNTP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'GLUCONATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'GNTP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'GLUCONATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_209', 1.000000), 
	Parameter('rvs_TRANS_RXN0_209', 1.000000))
Rule('TRANS_RXN0_282',
	prot(name = 'HCAT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = '_3_PHENYLPROPIONATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'HCAT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = '_3_PHENYLPROPIONATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_282', 1.000000), 
	Parameter('rvs_TRANS_RXN0_282', 0.000000))
Rule('RXN0_2522',
	prot(name = 'HRSA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PTSH_PHOSPHORYLATED', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = '_2_O_ALPHA_MANNOSYL_D_GLYCERATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'HRSA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD0_1063', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PTSH_MONOMER', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_2522', 1.000000), 
	Parameter('rvs_RXN0_2522', 0.000000))
Rule('TRANS_RXN_113',
	prot(name = 'KDGT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = '_2_DEHYDRO_3_DEOXY_D_GLUCONATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'KDGT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = '_2_DEHYDRO_3_DEOXY_D_GLUCONATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_113', 1.000000), 
	Parameter('rvs_TRANS_RXN_113', 1.000000))
Rule('TRANS_RXN_23',
	prot(name = 'KGTP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'KGTP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_23', 1.000000), 
	Parameter('rvs_TRANS_RXN_23', 1.000000))
Rule('TRANS_RXN_3',
	prot(name = 'KUP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Kplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'KUP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Kplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_3', 1.000000), 
	Parameter('rvs_TRANS_RXN_3', 0.000000))
Rule('TRANS_RXN_24',
	prot(name = 'LACY_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Alpha_lactose', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'LACY_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Alpha_lactose', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_24', 1.000000), 
	Parameter('rvs_TRANS_RXN_24', 1.000000))
Rule('TRANS_RXN_94',
	prot(name = 'LACY_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'MELIBIOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'LACY_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'MELIBIOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_94', 1.000000), 
	Parameter('rvs_TRANS_RXN_94', 1.000000))
Rule('RXN0_7215',
	prot(name = 'LACY_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_3561', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'LACY_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_3561', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_7215', 1.000000), 
	Parameter('rvs_RXN0_7215', 1.000000))
Rule('RXN0_7217',
	prot(name = 'LACY_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_3785', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'LACY_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_3785', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_7217', 1.000000), 
	Parameter('rvs_RXN0_7217', 1.000000))
Rule('RXN_17755',
	prot(name = 'LACY_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_3801', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'LACY_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_3801', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN_17755', 1.000000), 
	Parameter('rvs_RXN_17755', 1.000000))
Rule('TRANS_RXN_58',
	prot(name = 'LYSP_MONOMER', loc = 'per', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'LYS', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'LYSP_MONOMER', loc = 'per', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'LYS', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_58', 1.000000), 
	Parameter('rvs_TRANS_RXN_58', 1.000000))
Rule('TRANS_RXN0_575',
	prot(name = 'MALX_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'MALTOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'MALX_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'MALTOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_575', 1.000000), 
	Parameter('rvs_TRANS_RXN0_575', 0.000000))
Rule('TRANS_RXN0_574',
	prot(name = 'MALX_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'Glucopyranose', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'MALX_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'Glucopyranose', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_574', 1.000000), 
	Parameter('rvs_TRANS_RXN0_574', 0.000000))
Rule('TRANS_RXN_94B',
	prot(name = 'MELB_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'LIplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'MELIBIOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'MELB_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'LIplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'MELIBIOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_94B', 1.000000), 
	Parameter('rvs_TRANS_RXN_94B', 1.000000))
Rule('TRANS_RXN_94A',
	prot(name = 'MELB_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'MELIBIOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'MELB_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'MELIBIOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_94A', 1.000000), 
	Parameter('rvs_TRANS_RXN_94A', 1.000000))
Rule('TRANS_RXN0_520',
	prot(name = 'MELB_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'METHYL_BETA_D_GALACTOSIDE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'MELB_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'METHYL_BETA_D_GALACTOSIDE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_520', 1.000000), 
	Parameter('rvs_TRANS_RXN0_520', 1.000000))
Rule('TRANS_RXN0_519',
	prot(name = 'MELB_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_3565', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'MELB_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_3565', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_519', 1.000000), 
	Parameter('rvs_TRANS_RXN0_519', 1.000000))
Rule('RXN0_4522',
	cplx(name = 'METNIQ_METHIONINE_ABC_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'MET', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'METNIQ_METHIONINE_ABC_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'MET', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_4522', 1.000000), 
	Parameter('rvs_RXN0_4522', 0.000000))
Rule('TRANS_RXN0_202',
	cplx(name = 'METNIQ_METHIONINE_ABC_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_218', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'METNIQ_METHIONINE_ABC_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_218', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_202', 1.000000), 
	Parameter('rvs_TRANS_RXN0_202', 0.000000))
Rule('TRANS_RXN0_511',
	cplx(name = 'METNIQ_METHIONINE_ABC_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'L_Methionine_sulfoxides', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'METNIQ_METHIONINE_ABC_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'L_Methionine_sulfoxides', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_511', 1.000000), 
	Parameter('rvs_TRANS_RXN0_511', 0.000000))
Rule('TRANS_RXN0_510',
	cplx(name = 'METNIQ_METHIONINE_ABC_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_3738', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'METNIQ_METHIONINE_ABC_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_3738', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_510', 1.000000), 
	Parameter('rvs_TRANS_RXN0_510', 0.000000))
Rule('TRANS_RXN_383',
	cplx(name = 'METNIQ_METHIONINE_ABC_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_21777', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'METNIQ_METHIONINE_ABC_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_21777', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_383', 1.000000), 
	Parameter('rvs_TRANS_RXN_383', 0.000000))
Rule('TRANS_RXN_250',
	prot(name = 'MGTA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'MGplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	prot(name = 'MGTA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'MGplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_250', 1.000000), 
	Parameter('rvs_TRANS_RXN_250', 0.000000))
Rule('TRANS_RXN0_457',
	prot(name = 'MHPT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_10797', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'MHPT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_10797', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_457', 1.000000), 
	Parameter('rvs_TRANS_RXN0_457', 1.000000))
Rule('TRANS_RXN_61',
	prot(name = 'MHPT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = '_3_HYDROXYPHENYL_PROPIONATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'MHPT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = '_3_HYDROXYPHENYL_PROPIONATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_61', 1.000000), 
	Parameter('rvs_TRANS_RXN_61', 1.000000))
Rule('TRANS_RXN0_205',
	prot(name = 'MONOMER0_2797', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PYRIDOXINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'MONOMER0_2797', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PYRIDOXINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_205', 1.000000), 
	Parameter('rvs_TRANS_RXN0_205', 0.000000))
Rule('TRANS_RXN0_213',
	prot(name = 'MONOMER0_2798', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PYRIDOXAMINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'MONOMER0_2798', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PYRIDOXAMINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_213', 1.000000), 
	Parameter('rvs_TRANS_RXN0_213', 0.000000))
Rule('TRANS_RXN0_214',
	prot(name = 'MONOMER0_2799', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PYRIDOXAL', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'MONOMER0_2799', loc = 'cyt', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PYRIDOXAL', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_214', 1.000000), 
	Parameter('rvs_TRANS_RXN0_214', 0.000000))
Rule('TRANS_RXN0_587',
	prot(name = 'MONOMER0_5', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD0_882', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'MONOMER0_5', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD0_882', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_587', 1.000000), 
	Parameter('rvs_TRANS_RXN0_587', 0.000000))
Rule('TRANS_RXN_142',
	prot(name = 'MTR_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'INDOLE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'MTR_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'INDOLE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_142', 1.000000), 
	Parameter('rvs_TRANS_RXN_142', 1.000000))
Rule('NADH_DEHYDROG_A_RXN',
	cplx(name = 'NADH_DHI_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NADH', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Ubiquinones', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'NADH_DHI_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NAD', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Ubiquinols', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_NADH_DEHYDROG_A_RXN', 1.000000), 
	Parameter('rvs_NADH_DEHYDROG_A_RXN', 1.000000))
Rule('RXN0_5388',
	cplx(name = 'NADH_DHI_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Menaquinones', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NADH', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'NADH_DHI_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Menaquinols', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NAD', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_5388', 1.000000), 
	Parameter('rvs_RXN0_5388', 0.000000))
Rule('TRANS_RXN_25',
	prot(name = 'NANT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'N_ACETYLNEURAMINATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'NANT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'N_ACETYLNEURAMINATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_25', 1.000000), 
	Parameter('rvs_TRANS_RXN_25', 1.000000))
Rule('RXN_15314',
	prot(name = 'NANT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD0_1123', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'NANT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD0_1123', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN_15314', 1.000000), 
	Parameter('rvs_RXN_15314', 1.000000))
Rule('TRANS_RXN_137',
	prot(name = 'NARK_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'NITRITE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'NARK_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'NITRITE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_137', 1.000000), 
	Parameter('rvs_TRANS_RXN_137', 0.000000))
Rule('TRANS_RXN0_239',
	prot(name = 'NARK_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'NITRATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NITRITE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'NARK_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'NITRATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NITRITE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_239', 1.000000), 
	Parameter('rvs_TRANS_RXN0_239', 0.000000))
Rule('TRANS_RXN_130',
	prot(name = 'NHAB_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'NHAB_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_130', 1.000000), 
	Parameter('rvs_TRANS_RXN_130', 1.000000))
Rule('RXN0_3501',
	cplx(name = 'NITRATREDUCTA_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Menaquinols', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NITRATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'NITRATREDUCTA_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Menaquinones', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NITRITE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_3501', 1.000000), 
	Parameter('rvs_RXN0_3501', 0.000000))
Rule('RXN0_7124',
	cplx(name = 'NITRATREDUCTA_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Ubiquinols', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NITRATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'NITRATREDUCTA_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Ubiquinones', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NITRITE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_7124', 1.000000), 
	Parameter('rvs_RXN0_7124', 0.000000))
Rule('RXN_15119',
	cplx(name = 'NITRATREDUCTA_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_4544', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Donor_H2', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'NITRATREDUCTA_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_16009', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Acceptor', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN_15119', 1.000000), 
	Parameter('rvs_RXN_15119', 0.000000))
Rule('TRANS_RXN_108E',
	prot(name = 'NUPC_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'DEOXYINOSINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'NUPC_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'DEOXYINOSINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_108E', 1.000000), 
	Parameter('rvs_TRANS_RXN_108E', 1.000000))
Rule('TRANS_RXN_108G',
	prot(name = 'NUPC_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'INOSINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'NUPC_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'INOSINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_108G', 1.000000), 
	Parameter('rvs_TRANS_RXN_108G', 1.000000))
Rule('TRANS_RXN_108I',
	prot(name = 'NUPC_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'URIDINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'NUPC_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'URIDINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_108I', 1.000000), 
	Parameter('rvs_TRANS_RXN_108I', 1.000000))
Rule('TRANS_RXN_108H',
	prot(name = 'NUPC_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'THYMIDINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'NUPC_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'THYMIDINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_108H', 1.000000), 
	Parameter('rvs_TRANS_RXN_108H', 1.000000))
Rule('TRANS_RXN_108F',
	prot(name = 'NUPC_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'DEOXYURIDINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'NUPC_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'DEOXYURIDINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_108F', 1.000000), 
	Parameter('rvs_TRANS_RXN_108F', 1.000000))
Rule('TRANS_RXN_108D',
	prot(name = 'NUPC_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'DEOXYCYTIDINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'NUPC_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'DEOXYCYTIDINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_108D', 1.000000), 
	Parameter('rvs_TRANS_RXN_108D', 1.000000))
Rule('TRANS_RXN_108C',
	prot(name = 'NUPC_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'DEOXYADENOSINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'NUPC_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'DEOXYADENOSINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_108C', 1.000000), 
	Parameter('rvs_TRANS_RXN_108C', 1.000000))
Rule('TRANS_RXN_108B',
	prot(name = 'NUPC_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CYTIDINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'NUPC_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CYTIDINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_108B', 1.000000), 
	Parameter('rvs_TRANS_RXN_108B', 1.000000))
Rule('TRANS_RXN_108A',
	prot(name = 'NUPC_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADENOSINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'NUPC_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADENOSINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_108A', 1.000000), 
	Parameter('rvs_TRANS_RXN_108A', 1.000000))
Rule('TRANS_RXN_108',
	prot(name = 'NUPG_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Nucleosides', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'NUPG_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Nucleosides', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_108', 1.000000), 
	Parameter('rvs_TRANS_RXN_108', 1.000000))
Rule('TRANS_RXN_117',
	prot(name = 'PANF_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PANTOTHENATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'PANF_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PANTOTHENATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_117', 1.000000), 
	Parameter('rvs_TRANS_RXN_117', 1.000000))
Rule('TRANS_RXN_114',
	prot(name = 'PITA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'PITA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_114', 1.000000), 
	Parameter('rvs_TRANS_RXN_114', 1.000000))
Rule('TRANS_RXN_279',
	prot(name = 'PITA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_18501', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'PITA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_18501', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_279', 1.000000), 
	Parameter('rvs_TRANS_RXN_279', 1.000000))
Rule('TRANS_RXN_278',
	prot(name = 'PITA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_18500', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'PITA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_18500', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_278', 1.000000), 
	Parameter('rvs_TRANS_RXN_278', 1.000000))
Rule('TRANS_RXN_277',
	prot(name = 'PITA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_18499', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'PITA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_18499', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_277', 1.000000), 
	Parameter('rvs_TRANS_RXN_277', 1.000000))
Rule('TRANS_RXN0_550',
	prot(name = 'PITA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'ARSENATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'PITA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ARSENATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_550', 1.000000), 
	Parameter('rvs_TRANS_RXN0_550', 1.000000))
Rule('TRANS_RXN_280',
	prot(name = 'PITA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_4544', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'PITA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_4544', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_280', 1.000000), 
	Parameter('rvs_TRANS_RXN_280', 1.000000))
Rule('TRANS_RXN0_481',
	prot(name = 'PNUC_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'NICOTINAMIDE_RIBOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'PNUC_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'NICOTINAMIDE_RIBOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_481', 1.000000), 
	Parameter('rvs_TRANS_RXN0_481', 0.000000))
Rule('TRANS_RXN0_211',
	prot(name = 'POTE_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PUTRESCINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'L_ORNITHINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'POTE_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PUTRESCINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'L_ORNITHINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_211', 1.000000), 
	Parameter('rvs_TRANS_RXN0_211', 1.000000))
Rule('TRANS_RXN_118',
	prot(name = 'PUTP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PRO', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'PUTP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PRO', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_118', 1.000000), 
	Parameter('rvs_TRANS_RXN_118', 1.000000))
Rule('TRANS_RXN0_505',
	prot(name = 'PUTP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROPIONATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'PUTP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROPIONATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_505', 1.000000), 
	Parameter('rvs_TRANS_RXN0_505', 0.000000))
Rule('TRANS_RXN0_277',
	cplx(name = 'PYRNUTRANSHYDROGEN_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NADPH', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NAD', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'PYRNUTRANSHYDROGEN_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NADH', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_277', 1.000000), 
	Parameter('rvs_TRANS_RXN0_277', 1.000000))
Rule('TRANS_RXN_146',
	prot(name = 'RFBX_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD0_2279', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'RFBX_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD0_2279', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_146', 1.000000), 
	Parameter('rvs_TRANS_RXN_146', 0.000000))
Rule('TRANS_RXN_112',
	prot(name = 'RHAT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'L_rhamnose', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'RHAT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'L_rhamnose', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_112', 1.000000), 
	Parameter('rvs_TRANS_RXN_112', 1.000000))
Rule('TRANS_RXN0_236',
	prot(name = 'RHAT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_15867', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'RHAT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_15867', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_236', 1.000000), 
	Parameter('rvs_TRANS_RXN0_236', 1.000000))
Rule('TRANS_RXN_242A',
	prot(name = 'RHTB_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_15554', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'RHTB_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_15554', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_242A', 1.000000), 
	Parameter('rvs_TRANS_RXN_242A', 1.000000))
Rule('TRANS_RXN_71',
	prot(name = 'SDAC_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'SER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'SDAC_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'SER', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_71', 1.000000), 
	Parameter('rvs_TRANS_RXN_71', 1.000000))
Rule('TRANS_RXN_27',
	prot(name = 'SHIA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'SHIKIMATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'SHIA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'SHIKIMATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_27', 1.000000), 
	Parameter('rvs_TRANS_RXN_27', 1.000000))
Rule('TRANS_RXN0_181',
	cplx(name = 'TATABCE_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'General_Protein_Substrates', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'TATABCE_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'General_Protein_Substrates', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_181', 1.000000), 
	Parameter('rvs_TRANS_RXN0_181', 0.000000))
Rule('TRANS_RXN_72',
	prot(name = 'TDCC_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'THR', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'TDCC_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'THR', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_72', 1.000000), 
	Parameter('rvs_TRANS_RXN_72', 1.000000))
Rule('TRANS_RXN0_539',
	prot(name = 'TEHA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD0_1938', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'TEHA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD0_1938', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_539', 1.000000), 
	Parameter('rvs_TRANS_RXN0_539', 0.000000))
Rule('TRANS_RXN0_224',
	cplx(name = 'TRANS_200_CPLX', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Macrolide_Antibiotics', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'TRANS_200_CPLX', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Macrolide_Antibiotics', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_224', 1.000000), 
	Parameter('rvs_TRANS_RXN0_224', 0.000000))
Rule('TRANS_RXN_377',
	cplx(name = 'TRANS_200_CPLX', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'bacitracin', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'TRANS_200_CPLX', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'bacitracin', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_377', 1.000000), 
	Parameter('rvs_TRANS_RXN_377', 0.000000))
Rule('TRANS_RXN_378',
	cplx(name = 'TRANS_200_CPLX', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Polymyxins', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	cplx(name = 'TRANS_200_CPLX', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Polymyxins', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_378', 1.000000), 
	Parameter('rvs_TRANS_RXN_378', 0.000000))
Rule('TRANS_RXN_359',
	cplx(name = 'TRANS_CPLX_201', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_1938', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'TRANS_CPLX_201', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_1938', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_359', 1.000000), 
	Parameter('rvs_TRANS_RXN_359', 0.000000))
Rule('TRANS_RXN0_592',
	cplx(name = 'TRANS_CPLX_201', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_15189', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'TRANS_CPLX_201', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_15189', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_592', 1.000000), 
	Parameter('rvs_TRANS_RXN0_592', 0.000000))
Rule('TRANS_RXN_356',
	cplx(name = 'TRANS_CPLX_201', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_3617', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'TRANS_CPLX_201', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_3617', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_356', 1.000000), 
	Parameter('rvs_TRANS_RXN_356', 0.000000))
Rule('TRANS_RXN_357',
	cplx(name = 'TRANS_CPLX_201', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ENTEROBACTIN', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'TRANS_CPLX_201', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ENTEROBACTIN', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_357', 1.000000), 
	Parameter('rvs_TRANS_RXN_357', 0.000000))
Rule('TRANS_RXN_353',
	cplx(name = 'TRANS_CPLX_202', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_15417', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'TRANS_CPLX_202', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_15417', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_353', 1.000000), 
	Parameter('rvs_TRANS_RXN_353', 0.000000))
Rule('TRANS_RXN_92',
	cplx(name = 'TRANS_CPLX_202', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_8876', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'TRANS_CPLX_202', loc = 'omem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_8876', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_92', 1.000000), 
	Parameter('rvs_TRANS_RXN_92', 0.000000))
Rule('TRANS_RXN0_235',
	cplx(name = 'TRANS_CPLX_203', loc = 'per', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_334', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'TRANS_CPLX_203', loc = 'per', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_334', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_235', 1.000000), 
	Parameter('rvs_TRANS_RXN0_235', 0.000000))
Rule('TRANS_RXN_33',
	prot(name = 'UHPT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'D_glucopyranose_6_phosphate', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'UHPT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'D_glucopyranose_6_phosphate', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_33', 1.000000), 
	Parameter('rvs_TRANS_RXN_33', 1.000000))
Rule('TRANS_RXN0_502',
	prot(name = 'UHPT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_15979', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'UHPT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_15979', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_502', 1.000000), 
	Parameter('rvs_TRANS_RXN0_502', 1.000000))
Rule('TRANS_RXN0_501',
	prot(name = 'UHPT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_18719', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'UHPT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_18719', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_501', 1.000000), 
	Parameter('rvs_TRANS_RXN0_501', 1.000000))
Rule('TRANS_RXN0_534',
	prot(name = 'UHPT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'L_GLYCERALDEHYDE_3_PHOSPHATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'UHPT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'L_GLYCERALDEHYDE_3_PHOSPHATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_534', 1.000000), 
	Parameter('rvs_TRANS_RXN0_534', 1.000000))
Rule('TRANS_RXN_98',
	prot(name = 'UIDB_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Glucuronides', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'UIDB_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Glucuronides', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_98', 1.000000), 
	Parameter('rvs_TRANS_RXN_98', 1.000000))
Rule('TRANS_RXN_31',
	prot(name = 'XAPB_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'XANTHOSINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'XAPB_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'XANTHOSINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_31', 1.000000), 
	Parameter('rvs_TRANS_RXN_31', 1.000000))
Rule('TRANS_RXN_261',
	prot(name = 'XASA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = '_4_AMINO_BUTYRATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'GLT', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'XASA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'GLT', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = '_4_AMINO_BUTYRATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_261', 1.000000), 
	Parameter('rvs_TRANS_RXN_261', 1.000000))
Rule('TRANS_RXN_30',
	prot(name = 'XYLE_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'D_Xylose', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'XYLE_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'D_Xylose', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_30', 1.000000), 
	Parameter('rvs_TRANS_RXN_30', 1.000000))
Rule('TRANS_RXN0_496',
	prot(name = 'YBDA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'ENTEROBACTIN', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'YBDA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'ENTEROBACTIN', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_496', 1.000000), 
	Parameter('rvs_TRANS_RXN0_496', 1.000000))
Rule('TRANS_RXN_342',
	prot(name = 'YCEE_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD0_1113', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'YCEE_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD0_1113', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_342', 1.000000), 
	Parameter('rvs_TRANS_RXN_342', 1.000000))
Rule('TRANS_RXN0_589',
	prot(name = 'YCEE_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'DEOXYCHOLATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'YCEE_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'DEOXYCHOLATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_589', 1.000000), 
	Parameter('rvs_TRANS_RXN0_589', 1.000000))
Rule('TRANS_RXN_40',
	prot(name = 'YDEA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'L_ARABINOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'YDEA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'L_ARABINOSE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_40', 1.000000), 
	Parameter('rvs_TRANS_RXN_40', 1.000000))
Rule('TRANS_RXN0_266',
	cplx(name = 'YDGEF_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'SPERMIDINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'YDGEF_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'SPERMIDINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_266', 1.000000), 
	Parameter('rvs_TRANS_RXN0_266', 1.000000))
Rule('TRANS_RXN_350',
	cplx(name = 'YDGEF_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_21025', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	cplx(name = 'YDGEF_CPLX', loc = 'imem', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD_21025', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_350', 1.000000), 
	Parameter('rvs_TRANS_RXN_350', 1.000000))
Rule('RXN0_2561',
	prot(name = 'YDHE_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'Drugs', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'YDHE_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'Drugs', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_2561', 1.000000), 
	Parameter('rvs_RXN0_2561', 1.000000))
Rule('TRANS_RXN_347',
	prot(name = 'YDHE_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_21015', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'YDHE_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_21015', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_347', 1.000000), 
	Parameter('rvs_TRANS_RXN_347', 1.000000))
Rule('TRANS_RXN_348',
	prot(name = 'YDHE_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_20890', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'YDHE_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_20890', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_348', 1.000000), 
	Parameter('rvs_TRANS_RXN_348', 1.000000))
Rule('TRANS_RXN_349',
	prot(name = 'YDHE_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'DEOXYCHOLATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'YDHE_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'DEOXYCHOLATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_349', 1.000000), 
	Parameter('rvs_TRANS_RXN_349', 1.000000))
Rule('TRANS_RXN_272',
	prot(name = 'YEEO_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'FAD', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'YEEO_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'FAD', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_272', 1.000000), 
	Parameter('rvs_TRANS_RXN_272', 0.000000))
Rule('TRANS_RXN0_595',
	prot(name = 'YEEO_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'FMN', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'YEEO_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'FMN', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_595', 1.000000), 
	Parameter('rvs_TRANS_RXN0_595', 0.000000))
Rule('TRANS_RXN0_538',
	prot(name = 'YEIM_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_497', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'YEIM_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_497', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_538', 1.000000), 
	Parameter('rvs_TRANS_RXN0_538', 1.000000))
Rule('RXN0_2421',
	prot(name = 'YFEP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'FEplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'YFEP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'FEplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_2421', 1.000000), 
	Parameter('rvs_RXN0_2421', 1.000000))
Rule('TRANS_RXN_241',
	prot(name = 'YFEP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'MNplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'YFEP_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'MNplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_241', 1.000000), 
	Parameter('rvs_TRANS_RXN_241', 1.000000))
Rule('TRANS_RXN0_530',
	prot(name = 'YGFU_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'URATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'YGFU_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'URATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_530', 1.000000), 
	Parameter('rvs_TRANS_RXN0_530', 1.000000))
Rule('RXN66_448',
	prot(name = 'YGGA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'ARG', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'YGGA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'ARG', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN66_448', 0.000000), 
	Parameter('rvs_RXN66_448', 1.000000))
Rule('TRANS_RXN_325',
	prot(name = 'YGGA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CANAVANINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'YGGA_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CANAVANINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_325', 1.000000), 
	Parameter('rvs_TRANS_RXN_325', 0.000000))
Rule('TRANS_RXN_127',
	prot(name = 'YGJE_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'TARTRATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'SUC', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'YGJE_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'TARTRATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'SUC', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_127', 1.000000), 
	Parameter('rvs_TRANS_RXN_127', 1.000000))
Rule('RXN0_4083',
	prot(name = 'YGJU_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'SER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'YGJU_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'NAplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'SER', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_4083', 1.000000), 
	Parameter('rvs_RXN0_4083', 1.000000))
Rule('TRANS_RXN0_418',
	prot(name = 'YHFM_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PSICOSELYSINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'YHFM_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PSICOSELYSINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_418', 1.000000), 
	Parameter('rvs_TRANS_RXN0_418', 0.000000))
Rule('TRANS_RXN0_417',
	prot(name = 'YHFM_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'FRUCTOSELYSINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'YHFM_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'FRUCTOSELYSINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_417', 1.000000), 
	Parameter('rvs_TRANS_RXN0_417', 0.000000))
Rule('RXN0_5205',
	prot(name = 'YHHO_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'ZNplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'WATER', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ATP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	None | 
	prot(name = 'YHHO_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'ZNplus2', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'ADP', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'Pi', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_5205', 1.000000), 
	Parameter('rvs_RXN0_5205', 0.000000))
Rule('RXN0_22',
	prot(name = 'YICM_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'GUANOSINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'YICM_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'GUANOSINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_22', 1.000000), 
	Parameter('rvs_RXN0_22', 1.000000))
Rule('RXN0_18',
	prot(name = 'YICM_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'INOSINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'YICM_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'INOSINE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_RXN0_18', 1.000000), 
	Parameter('rvs_RXN0_18', 1.000000))
Rule('TRANS_RXN_16',
	prot(name = 'YIDT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'D_GALACTONATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'YIDT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'D_GALACTONATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_16', 1.000000), 
	Parameter('rvs_TRANS_RXN_16', 1.000000))
Rule('TRANS_RXN_341',
	prot(name = 'YIDY_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CHLORAMPHENICOL', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'YIDY_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CHLORAMPHENICOL', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_341', 1.000000), 
	Parameter('rvs_TRANS_RXN_341', 1.000000))
Rule('TRANS_RXN0_580',
	prot(name = 'YIHO_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_10247', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'YIHO_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD_10247', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_580', 1.000000), 
	Parameter('rvs_TRANS_RXN0_580', 0.000000))
Rule('TRANS_RXN0_228',
	prot(name = 'YJGT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = '_5_DEHYDROGLUCONATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'YJGT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = '_5_DEHYDROGLUCONATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_228', 1.000000), 
	Parameter('rvs_TRANS_RXN0_228', 1.000000))
Rule('TRANS_RXN_181A',
	prot(name = 'YJGT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'L_IDONATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'YJGT_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'L_IDONATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_181A', 1.000000), 
	Parameter('rvs_TRANS_RXN_181A', 1.000000))
Rule('TRANS_RXN_336',
	prot(name = 'YJIO_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'Kplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'YJIO_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'Kplus', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN_336', 1.000000), 
	Parameter('rvs_TRANS_RXN_336', 1.000000))
Rule('TRANS_RXN0_588',
	prot(name = 'YJIO_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CHOLATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'YJIO_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CHOLATE', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_588', 1.000000), 
	Parameter('rvs_TRANS_RXN0_588', 1.000000))
Rule('TRANS_RXN0_227',
	prot(name = 'YJIZ_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'CPD0_1083', loc = 'cyt', dna = None, met = None, prot = None, rna = None) | 
	prot(name = 'YJIZ_MONOMER', loc = 'imem', dna = None, met = None, prot = None, rna = None, up = None, dw = None) +
	met(name = 'CPD0_1083', loc = 'cyt', dna = None, met = None, prot = None, rna = None) +
	met(name = 'PROTON', loc = 'cyt', dna = None, met = None, prot = None, rna = None), 
	Parameter('fwd_TRANS_RXN0_227', 1.000000), 
	Parameter('rvs_TRANS_RXN0_227', 1.000000))
