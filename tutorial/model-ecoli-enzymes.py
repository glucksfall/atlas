from pysb import *
Model()

Monomer('met',
	['name', 'loc', 'dna', 'met', 'prot', 'rna'],
	{ 'name' : [ 'A_5_prime_PP_5_prime_DNA', 'A_5_prime_PP_5_prime_RNA', 'A_DOUBLE_STRANDED_DNA_WITH_A_3_OVERHANG', 'A_REDUCED_TORY_PROTEIN', 'ACEF_LIPOATE', 'ACET', 'ACETALD', 'ACETOACETYL_COA', 'ACETOIN', 'ACETOL', 'ACETYL_ACP', 'ACETYL_COA', 'ACETYL_D_GLUCOSAMINYLDIPHOSPHO_UNDECAPRE', 'ACETYL_GLU', 'ACETYL_P', 'ACETYLSERINE', 'ACP', 'ACRYLYL_COA', 'ACYL_ACP', 'ACYL_COA', 'ACYL_SN_GLYCEROL_3P', 'ADENINE', 'ADENOSINE', 'ADENOSINE5TRIPHOSPHO5ADENOSINE', 'ADENOSINE_DIPHOSPHATE_RIBOSE', 'ADENOSYL_HOMO_CYS', 'ADENOSYL_P4', 'ADENOSYLCOBALAMIN', 'ADENOSYLCOBALAMIN_5_P', 'ADENOSYLCOBINAMIDE', 'ADENOSYLCOBINAMIDE_GDP', 'ADENOSYLCOBINAMIDE_P', 'ADENYLOSUCC', 'ADP', 'ADP_D_GLUCOSE', 'ADP_D_GLYCERO_D_MANNO_HEPTOSE', 'ADP_L_GLYCERO_D_MANNO_HEPTOSE', 'ADP_SUGARS', 'AGMATHINE', 'AICAR', 'ALA_tRNAs', 'ALLANTOATE', 'ALLO_THR', 'ALLOLACTOSE', 'ALPHA_D_GALACTOSE', 'ALPHA_GLUCOSE', 'ALPHA_RIBAZOLE', 'ALPHA_RIBAZOLE_5_P', 'AMINO_ACETONE', 'AMINO_HYDROXYMETHYL_METHYL_PYR_P', 'AMINO_HYDROXYMETHYL_METHYLPYRIMIDINE_PP', 'AMINO_OH_HYDROXYMETHYL_DIHYDROPTERIDINE', 'AMINO_OXOBUT', 'AMINO_RIBOSYLAMINO_1H_3H_PYR_DIONE', 'AMINOMETHYLDIHYDROLIPOYL_GCVH', 'AMMONIA', 'AMMONIUM', 'AMP', 'ANTHRANILATE', 'APO_CITRATE_LYASE', 'APS', 'ARABINOSE_5P', 'ARCB_MONOMER', 'ARG', 'ARG_tRNAs', 'ARSENATE', 'ASN', 'ASN_tRNAs', 'ASP_tRNAs', 'ATP', 'Acceptor', 'Acetate_esters', 'Acetoacetyl_ACPs', 'Acetylated_S18_N_terminal_L_alanine', 'Acetylated_S5_N_terminal_L_alanine', 'Acyl_Phosphates', 'Adenylated_ThiS_Proteins', 'Alcohols', 'Aldehydes', 'Aldonic_Acids', 'Aldoses', 'Aliphatic_Alpha_Omega_Diamines', 'Aliphatic_Amines', 'Aliphatic_N_Acetyl_Diamines', 'Aliphatic_Omega_Amino_Aldehydes', 'Alkanesulfonates', 'Alkyl_Hydro_Peroxides', 'Alkylated_Bases', 'Alkylated_DNAs', 'All_apo_ACPs', 'All_holo_ACPs', 'All_tRNAs', 'Alpha_D_aldose_1_phosphates', 'Alpha_lactose', 'Aminated_Amine_Donors', 'Amino_Acids', 'Amino_Acids_20', 'Aminopeptidase_Substrates', 'Apo_EntB', 'Apo_EntF', 'Aromatic_Amino_Acids', 'Aromatic_Oxoacids', 'Aryl_Amines', 'Aryl_sulfates', 'B_ALANINE', 'B_KETOACYL_ACP', 'B12_Corrinoid_Adenosyltranferase', 'BCCP_L_lysine', 'BCCP_biotin_L_lysine', 'BENZALDEHYDE', 'BETA_D_FRUCTOSE', 'BETAINE', 'BETAINE_ALDEHYDE_HYDRATE', 'BETAINE_ALDEHYDE', 'BIO_5_AMP', 'BIOTIN', 'BISOHMYR_GLC', 'BISOHMYR_GLUCOSAMINYL_1P', 'BR_', 'BROMOACETATE', 'Beta_3_hydroxybutyryl_ACPs', 'Beta_D_Galactosides', 'Beta_D_Glucuronides', 'Beta_D_glucosides', 'Beta_Lactams', 'Beta_hydroxydecanoyl_ACPs', 'Butanoyl_ACPs', 'C_DI_GMP', 'C_terminal_32_aminoacid_Peptides', 'C1', 'C5', 'C55_PP_GLCNAC_MANNACA', 'C55_PP_GLCNAC_MANNACA_FUC4NAC', 'C6', 'CADAVERINE', 'CAMP', 'CARBAMATE', 'CARBAMOYL_P', 'CARBAMYUL_L_ASPARTATE', 'CARBON_DIOXIDE', 'CARBON_MONOXIDE', 'CARBOXYETHYL_3_5_CYCLOHEXADIENE_1_2_DIOL', 'CARBOXYPHENYLAMINO_DEOXYRIBULOSE_P', 'CARDIOLIPIN', 'CARNITINE', 'CDP', 'CDP_2_3_4_Saturated_Diacylglycerols', 'CDPDIACYLGLYCEROL', 'CELLULOSE', 'CGMP', 'CH33ADO', 'CH4', 'CHEY_MONOMER', 'CHITIN', 'CHITOBIOSE', 'CHOLANATE2', 'CHOLATE', 'CHOLINE', 'CHORISMATE', 'CIS_ACONITATE', 'CIS_DELTA3_ENOYL_COA', 'CIT', 'CITRATE_LYASE', 'CL_', 'CMP', 'CMP_KDO', 'CO_A', 'COPROPORPHYRINOGEN_III', 'CPD_10247', 'CPD_10269', 'CPD_10329', 'CPD_10551', 'CPD_10796', 'CPD_10797', 'CPD_108', 'CPD_1086', 'CPD_1091', 'CPD_1093', 'CPD_1106', 'CPD_1136', 'CPD_11592', 'CPD_1162', 'CPD_11653', 'CPD_11770', 'CPD_1181', 'CPD_12115', 'CPD_12255', 'CPD_12274', 'CPD_12279', 'CPD_12284', 'CPD_12365', 'CPD_12366', 'CPD_12367', 'CPD_12427', 'CPD_12575', 'CPD_12587', 'CPD_12773', 'CPD_12797', 'CPD_12991', 'CPD_1301', 'CPD_1302', 'CPD_13025', 'CPD_13034', 'CPD_13043', 'CPD_13059', 'CPD_13118', 'CPD_13314', 'CPD_13315', 'CPD_13357', 'CPD_13469', 'CPD_13575', 'CPD_13851', 'CPD_13852', 'CPD_13853', 'CPD_13927', 'CPD_13930', 'CPD_14101', 'CPD_14133', 'CPD_14332', 'CPD_14443', 'CPD_14447', 'CPD_14553', 'CPD_14736', 'CPD_14762', 'CPD_14925', 'CPD_15016', 'CPD_15158', 'CPD_15237', 'CPD_15238', 'CPD_15242', 'CPD_15244', 'CPD_15317', 'CPD_15373', 'CPD_15382', 'CPD_15384', 'CPD_15390', 'CPD_15391', 'CPD_15392', 'CPD_15393', 'CPD_15403', 'CPD_15435', 'CPD_15436', 'CPD_15530', 'CPD_15633', 'CPD_157', 'CPD_15709', 'CPD_15818', 'CPD_15826', 'CPD_15873', 'CPD_15874', 'CPD_15972', 'CPD_15978', 'CPD_15979', 'CPD_16009', 'CPD_16398', 'CPD_16400', 'CPD_16401', 'CPD_16491', 'CPD_16500', 'CPD_16501', 'CPD_16502', 'CPD_16566', 'CPD_16567', 'CPD_16569', 'CPD_16618', 'CPD_16716', 'CPD_16720', 'CPD_16843', 'CPD_17063', 'CPD_173', 'CPD_17523', 'CPD_17530', 'CPD_17573', 'CPD_17574', 'CPD_1772', 'CPD_17752', 'CPD_17753', 'CPD_17926', 'CPD_17927', 'CPD_17931', 'CPD_17932', 'CPD_17947', 'CPD_17968', 'CPD_17969', 'CPD_17989', 'CPD_18118', 'CPD_18259', 'CPD_18260', 'CPD_18346', 'CPD_18348', 'CPD_18379', 'CPD_1843', 'CPD_18529', 'CPD_18717', 'CPD_18804', 'CPD_18805', 'CPD_18806', 'CPD_18807', 'CPD_18808', 'CPD_18901', 'CPD_18902', 'CPD_18903', 'CPD_19111', 'CPD_19144', 'CPD_19147', 'CPD_19148', 'CPD_19150', 'CPD_19151', 'CPD_19153', 'CPD_19154', 'CPD_19155', 'CPD_19157', 'CPD_19158', 'CPD_19159', 'CPD_19160', 'CPD_19161', 'CPD_19162', 'CPD_19163', 'CPD_19167', 'CPD_19168', 'CPD_19169', 'CPD_19170', 'CPD_19171', 'CPD_19172', 'CPD_19179', 'CPD_19181', 'CPD_19185', 'CPD_19186', 'CPD_19233', 'CPD_19235', 'CPD_19236', 'CPD_19237', 'CPD_19240', 'CPD_19241', 'CPD_19242', 'CPD_19243', 'CPD_19395', 'CPD_194', 'CPD_195', 'CPD_20035', 'CPD_20036', 'CPD_207', 'CPD_20746', 'CPD_20750', 'CPD_20756', 'CPD_20757', 'CPD_20903', 'CPD_20905', 'CPD_20966', 'CPD_20969', 'CPD_21359', 'CPD_21406', 'CPD_21407', 'CPD_21409', 'CPD_21531', 'CPD_225', 'CPD_2343', 'CPD_239', 'CPD_253', 'CPD_264', 'CPD_2961', 'CPD_3', 'CPD_316', 'CPD_330', 'CPD_334', 'CPD_335', 'CPD_343', 'CPD_3462', 'CPD_347', 'CPD_3561', 'CPD_3564', 'CPD_358', 'CPD_37', 'CPD_3705', 'CPD_3706', 'CPD_3707', 'CPD_3708', 'CPD_3709', 'CPD_3710', 'CPD_3711', 'CPD_3713', 'CPD_3721', 'CPD_3723', 'CPD_3724', 'CPD_3725', 'CPD_3728', 'CPD_3734', 'CPD_3745', 'CPD_3766', 'CPD_377', 'CPD_3785', 'CPD_3801', 'CPD_381', 'CPD_389', 'CPD_397', 'CPD_4', 'CPD_421', 'CPD_4211', 'CPD_448', 'CPD_4544', 'CPD_469', 'CPD_476', 'CPD_479', 'CPD_497', 'CPD_520', 'CPD_534', 'CPD_536', 'CPD_548', 'CPD_558', 'CPD_560', 'CPD_564', 'CPD_568', 'CPD_582', 'CPD_5821', 'CPD_602', 'CPD_606', 'CPD_618', 'CPD_622', 'CPD_644', 'CPD_650', 'CPD_653', 'CPD_66', 'CPD_660', 'CPD_6602', 'CPD_67', 'CPD_674', 'CPD_6746', 'CPD_69', 'CPD_6972', 'CPD_6982', 'CPD_7000', 'CPD_702', 'CPD_703', 'CPD_7046', 'CPD_722', 'CPD_7221', 'CPD_7248', 'CPD_7249', 'CPD_763', 'CPD_7670', 'CPD_782', 'CPD_7867', 'CPD_8122', 'CPD_8123', 'CPD_8180', 'CPD_8199', 'CPD_8200', 'CPD_822', 'CPD_8521', 'CPD_8524', 'CPD_8534', 'CPD_8550', 'CPD_8624', 'CPD_8625', 'CPD_8876', 'CPD_8887', 'CPD_8891', 'CPD_8989', 'CPD_8990', 'CPD_9000', 'CPD_9038', 'CPD_9190', 'CPD_9245', 'CPD_9247', 'CPD_9385', 'CPD_9646', 'CPD_9728', 'CPD_9923', 'CPD_9924', 'CPD_9925', 'CPD_9956', 'CPD0_1027', 'CPD0_1032', 'CPD0_1048', 'CPD0_1049', 'CPD0_1063', 'CPD0_1065', 'CPD0_1068', 'CPD0_1074', 'CPD0_1080', 'CPD0_1081', 'CPD0_1082', 'CPD0_1083', 'CPD0_1085', 'CPD0_1090', 'CPD0_1095', 'CPD0_1101', 'CPD0_1107', 'CPD0_1108', 'CPD0_1110', 'CPD0_1112', 'CPD0_1122', 'CPD0_1123', 'CPD0_1133', 'CPD0_1147', 'CPD0_1148', 'CPD0_1151', 'CPD0_1156', 'CPD0_1157', 'CPD0_1158', 'CPD0_1159', 'CPD0_1162', 'CPD0_1163', 'CPD0_1171', 'CPD0_1181', 'CPD0_1182', 'CPD0_1183', 'CPD0_1184', 'CPD0_1185', 'CPD0_1189', 'CPD0_1192', 'CPD0_1193', 'CPD0_1202', 'CPD0_1283', 'CPD0_1442', 'CPD0_1445', 'CPD0_1456', 'CPD0_1699', 'CPD0_1719', 'CPD0_181', 'CPD0_1882', 'CPD0_1885', 'CPD0_1905', 'CPD0_1965', 'CPD0_2015', 'CPD0_2030', 'CPD0_2101', 'CPD0_2167', 'CPD0_2184', 'CPD0_2189', 'CPD0_2190', 'CPD0_2283', 'CPD0_2298', 'CPD0_2331', 'CPD0_2338', 'CPD0_2339', 'CPD0_2340', 'CPD0_2350', 'CPD0_2351', 'CPD0_2352', 'CPD0_2353', 'CPD0_2354', 'CPD0_2362', 'CPD0_2363', 'CPD0_2364', 'CPD0_2370', 'CPD0_2381', 'CPD0_2461', 'CPD0_2463', 'CPD0_2467', 'CPD0_2468', 'CPD0_2471', 'CPD0_2472', 'CPD0_2474', 'CPD0_2479', 'CPD0_2480', 'CPD0_2482', 'CPD0_2483', 'CPD0_2499', 'CPD0_2501', 'CPD0_2511', 'CPD0_2518', 'CPD0_2521', 'CPD0_2552', 'CPD0_2558', 'CPD0_2559', 'CPD0_2582', 'CPD0_2634', 'CPD0_881', 'CPD0_882', 'CPD0_888', 'CPD0_889', 'CPD0_903', 'CPD0_929', 'CPD0_930', 'CPD0_932', 'CPD0_933', 'CPD0_934', 'CPD0_935', 'CPD0_936', 'CPD0_937', 'CPD0_938', 'CPD0_939', 'CPD0_944', 'CPD0_971', 'CPD3O_0', 'CPD66_39', 'CPDMETA_13650', 'CPLX0_1', 'CPLX0_2', 'CPLX0_7748', 'CPLX0_7849', 'CPXR_MONOMER', 'CRplus3', 'CRplus6', 'CREATINE', 'CREATINE_P', 'CROTONOBETAINYL_COA', 'CROTONYL_COA', 'CTP', 'CUplus', 'CUplus2', 'CYS', 'CYS_GLY', 'CYS_tRNAs', 'CYTIDINE', 'CYTOSINE', 'Carboxyadenylated_MPT_synthases', 'Carboxylates', 'Carboxylic_esters', 'Cellodextrins', 'Chap_ADP_apo_SP_Complex', 'Charged_ALA_tRNAs', 'Charged_ARG_tRNAs', 'Charged_ASN_tRNAs', 'Charged_ASP_tRNAs', 'Charged_CYS_tRNAs', 'Charged_GLN_tRNAs', 'Charged_GLT_tRNAs', 'Charged_GLY_tRNAs', 'Charged_HIS_tRNAs', 'Charged_ILE_tRNAs', 'Charged_LEU_tRNAs', 'Charged_LYS_tRNAs', 'Charged_MET_tRNAs', 'Charged_PHE_tRNAs', 'Charged_PRO_tRNAs', 'Charged_SEC_tRNAs', 'Charged_SER_tRNAs', 'Charged_THR_tRNAs', 'Charged_TRP_tRNAs', 'Charged_TYR_tRNAs', 'Charged_VAL_tRNAs', 'Chitodextrins', 'Cis_Delta5_dodecenoyl_ACPs', 'Cis_Delta7_tetradecenoyl_ACPs', 'Cis_delta_3_decenoyl_ACPs', 'Cis_vaccenoyl_ACPs', 'Citrate_Lyase_Citryl_Form', 'Cleaved_DNA', 'Cleaved_Type_IV_Prepillins', 'Cleaved_type_1_transmembrane_domains', 'Crotonyl_ACPs', 'Cyclic_2_3_Ribonucleoside_Monophosphates', 'Cyclic_N6_threonylcarbamoyl_A37_tRNAs', 'Cyclic_Phosphate_Terminated_RNAs', 'Cysteine_Desulfurase_L_cysteine', 'Cytidine_32_tRNAs', 'Cytidine_34_tRNAIle2', 'Cytidine_34_tRNAmet', 'Cytidine_34_tRNAs', 'Cytochromes_C_Oxidized', 'Cytochromes_C_Reduced', 'Cytosine_32_In_tRNAs', 'D_3_HYDROXYACYL_COA', 'D_6_P_GLUCONO_DELTA_LACTONE', 'D_ALA_D_ALA', 'D_ALANINE', 'D_ALLOSE_6_PHOSPHATE', 'D_ALLULOSE_6_PHOSPHATE', 'D_ALPHABETA_D_HEPTOSE_7_PHOSPHATE', 'D_ALTRONATE', 'D_ARABINOSE', 'D_Allopyranose', 'D_Amino_Acids', 'D_BETA_D_HEPTOSE_1_P', 'D_BETA_D_HEPTOSE_17_DIPHOSPHATE', 'D_CYSTEINE', 'D_ERYTHRO_IMIDAZOLE_GLYCEROL_P', 'D_GALACTARATE', 'D_GALACTONATE', 'D_GALACTONO_1_4_LACTONE', 'D_GALACTOSAMINE_6_PHOSPHATE', 'D_GLT', 'D_GLUCARATE', 'D_GLUCOSAMINE_6_P', 'D_Glucopyranuronate', 'D_LACTATE', 'D_MANNONATE', 'D_METHYL_MALONYL_COA', 'D_MYO_INOSITOL_1_MONOPHOSPHATE', 'D_RIBULOSE', 'D_RIBULOSE_1_P', 'D_Ribofuranose', 'D_SEDOHEPTULOSE_1_7_P2', 'D_SEDOHEPTULOSE_7_P', 'D_SERINE', 'D_SORBITOL_6_P', 'D_TAGATURONATE', 'D_TARTRATE', 'D_TYROSINE', 'D_TYROSYL_TRNATYR', 'D_XYLONATE', 'D_XYLULOSE', 'D_Xylopyranose', 'D_aminoacyl_tRNAs', 'D_arabinopyranose', 'D_form_FeS_Cluster_Scaffold_Proteins', 'D_galactopyranose', 'D_glucopyranose_6_phosphate', 'D_glucose_1_phosphates', 'D_mannopyranose', 'DADP', 'DAMP', 'DATP', 'DCDP', 'DCMP', 'DCTP', 'DEAMIDO_NAD', 'DEHYDRO_3_DEOXY_L_RHAMNONATE', 'DEHYDRO_DEOXY_GALACTONATE_PHOSPHATE', 'DEHYDROQUINATE', 'DELTA1_PIPERIDEINE_2_6_DICARBOXYLATE', 'DELTA3_ISOPENTENYL_PP', 'DEOXY_D_RIBOSE_1_PHOSPHATE', 'DEOXY_RIBOSE_5P', 'DEOXYADENOSINE', 'DEOXYCYTIDINE', 'DEOXYGUANOSINE', 'DEOXYINOSINE', 'DEOXYURIDINE', 'DEOXYXYLULOSE_5P', 'DEPHOSPHO_COA', 'DETHIOBIOTIN', 'DGDP', 'DGMP', 'DGTP', 'DHB_Seryl_EntF', 'DI_H_OROTATE', 'DI_H_URACIL', 'DIACETYL', 'DIACETYLCHITOBIOSE_6_PHOSPHATE', 'DIACYLGLYCEROL', 'DIACYLGLYCEROL_PYROPHOSPHATE', 'DIAMINO_OH_PHOSPHORIBOSYLAMINO_PYR', 'DIAMINONONANOATE', 'DIHYDRO_DIOH_BENZOATE', 'DIHYDRO_NEO_PTERIN', 'DIHYDRO_THYMINE', 'DIHYDROFOLATE', 'DIHYDROFOLATE_GLU_N', 'DIHYDROLIPOYL_GCVH', 'DIHYDROMONAPTERIN_TRIPHOSPHATE', 'DIHYDRONEOPTERIN_P', 'DIHYDRONEOPTERIN_P3', 'DIHYDROPTERIN_CH2OH_PP', 'DIHYDROSIROHYDROCHLORIN', 'DIHYDROXY_ACETONE_PHOSPHATE', 'DIHYDROXY_BUTANONE_P', 'DIHYDROXYACETONE', 'DIHYDROXYNAPHTHOATE', 'DIHYDROXYPENTANEDIONE', 'DIMETHYL_D_RIBITYL_LUMAZINE', 'DIMETHYLBENZIMIDAZOLE', 'DIMP', 'DIPEPTIDES', 'DITP', 'DMSO', 'DNA_3_methyladenines', 'DNA_6_O_Methyl_Guanines', 'DNA_Adenines', 'DNA_Cleaved_Recognition_Site', 'DNA_Combined_With_Exogenous_DNA', 'DNA_Containing_N6_Methyladenine', 'DNA_Cytidines', 'DNA_Cytosines', 'DNA_Guanines', 'DNA_Holder', 'DNA_N', 'DNA_Segment_Placeholder', 'DNA_Segment_in_Reverse_Orientations', 'DNA_With_GO', 'DNA_With_GO_A_Mismatch', 'DNA_With_Recognition_Site', 'DNA_containing_a_Apyrimidinic_Sites', 'DNA_containing_aPurinic_Sites', 'DNA_containing_abasic_Sites', 'DNA_containing_diamino_hydro_formamidops', 'DNA_deoxycytidine_dimer', 'DNA_deoxycytidine_thymidine_dimer', 'DNA_thymidine_dimer', 'DNA_thymidines', 'DNA_with_Holiday_Junctions', 'DNA_with_Uracils', 'DPG', 'DTDP_D_GLUCOSE', 'DTDP_DEOH_DEOXY_GLUCOSE', 'DTDP_DEOH_DEOXY_MANNOSE', 'DTDP_RHAMNOSE', 'DUDP', 'DUMP', 'DUTP', 'Damaged_DNA_Pyrimidine', 'Deaminated_Amine_Donors', 'Decanoyl_ACPs', 'Deoxy_Ribonucleoside_3P', 'Deoxy_Ribonucleoside_Diphosphates', 'Deoxy_Ribonucleoside_Monophosphates', 'Deoxy_Ribonucleoside_Triphosphates', 'Deoxy_Ribonucleosides', 'Diacylglycerol_Prolipoproteins', 'Dihydro_Lipoyl_Proteins', 'Dipeptides_With_Asp_At_N_Terminal', 'Dipeptides_With_Proline_Carboxy', 'Diribonucleotide', 'Disulfide_Isomerase_with_Disulfide_Bond', 'Dodec_2_enoyl_ACPs', 'Dodecanoyl_ACPs', 'Donor_H2', 'Double_Stranded_DNA_with_terminal_PO4s', 'Double_Stranded_DNAs', 'E_', 'E2O_MONOMER', 'E2P_MONOMER', 'EF_P_L_lysine', 'EF_P_lysyl_hydroxylysine', 'EG10443_MONOMER', 'EG10544_MONOMER', 'EG10823_MONOMER', 'EG10873_MONOMER', 'EG11171_MONOMER', 'ENOL_OXALOACETATE', 'ENTB_CPLX', 'ENTEROBACTIN', 'ERYTHRONATE_4P', 'ERYTHROSE_4P', 'ETF_Oxidized', 'ETF_Reduced', 'ETHANOL_AMINE', 'ETHYL_2_METHYLACETOACETATE', 'ETHYL_2R_METHYL_3S_HYDROXYBUTANOATE', 'ETOH', 'ETR_Quinols', 'ETR_Quinones', 'Elongation_tRNAMet', 'Elongator_tRNAMet_acetylcytidine', 'Enoylglutaryl_ACP_methyl_esters', 'Enoylpimeloyl_ACP_methyl_esters', 'Exoaminopeptidase_Substrates', 'FAD', 'FADH2', 'FARNESYL_PP', 'FEplus2', 'FEplus3', 'FERRIC_ENTEROBACTIN_COMPLEX', 'FMN', 'FMNH2', 'FORMALDEHYDE', 'FORMATE', 'FORMYL_COA', 'FORMYL_L_METHIONYL_PEPTIDE', 'FORMYL_THF_GLU_N', 'FRU1P', 'FRUCTOSE_16_DIPHOSPHATE', 'FRUCTOSE_6P', 'FRUCTOSELYSINE', 'FRUCTOSELYSINE_6_PHOSPHATE', 'FRUCTURONATE', 'FUCULOSE_1P', 'FUM', 'Fatty_Acids', 'Fe3_siderophores', 'Fe4S4_Cluster_Protein', 'FeS_Cluster_Chaperones_ATP', 'Flavodoxins_Semiquinones', 'Fructofuranose', 'G3P', 'GALACTITOL_1_PHOSPHATE', 'GALACTOSE', 'GALACTOSE_1P', 'GAMMA_BUTYROBETAINE', 'GAMMA_BUTYROBETAINYL_COA', 'GAMMA_GLUTAMYL_GAMMA_AMINOBUTYRALDEH', 'GAMMA_GLUTAMYL_PUTRESCINE', 'GAP', 'GDP', 'GDP_4_DEHYDRO_6_DEOXY_D_MANNOSE', 'GDP_D_GLUCOSE', 'GDP_MANNOSE', 'GDP_TP', 'GERANYL_PP', 'GLC', 'GLC_1_P', 'GLC_6_P', 'GLC_D_LACTONE', 'GLN', 'GLN_tRNAs', 'GLT', 'GLT_tRNAs', 'GLUCONATE', 'GLUCOSAMINE', 'GLUCOSAMINE_1P', 'GLUTAMATE_1_SEMIALDEHYDE', 'GLUTATHIONE', 'GLUTATHIONYLSPERMIDINE', 'GLY', 'GLY_tRNAs', 'GLYCERALD', 'GLYCERATE', 'GLYCEROL', 'GLYCEROL_3P', 'GLYCEROPHOSPHOGLYCEROL', 'GLYCOL', 'GLYCOLALDEHYDE', 'GLYCOLLATE', 'GLYCYLGLYCINE', 'GLYOX', 'GMP', 'GMP_LYSINE_PHOSPHORAMIDATE', 'GTP', 'GUANINE', 'GUANOSINE', 'GUANOSINE_5DP_3DP', 'Gcv_H', 'General_Protein_Substrates', 'GlcNAc_1_6_anhydro_MurNAc_pentapeptide', 'Gln_B', 'Glucopyranose', 'Glucosyl_Lipopolysaccharides', 'Glutamine_synthetase_Tyr', 'Glutamine_synthetase_adenylyl_Tyr', 'Glutaryl_ACP_methyl_esters', 'Glycerol_1_phosphate', 'Glycerophosphodiesters', 'Glycogens', 'Guanine34_in_tRNAs', 'Guanine37_in_tRNA', 'Guanine46_in_tRNA', 'HCN', 'HCO3', 'HEME_D', 'HEPTA_ACYLATED_LIPID_A', 'HEPTOSYL_KDO2_LIPID_IVA', 'HIPA_P', 'HIS', 'HIS_tRNAs', 'HISTIDINAL', 'HISTIDINOL', 'HMP', 'HOLO_CITRATE_LYASE', 'HOMO_CYS', 'HOMO_SER', 'HS', 'HSCN', 'HYDROGEN_MOLECULE', 'HYDROGEN_PEROXIDE', 'HYDROQUINONE', 'HYDROXY_METHYL_BUTENYL_DIP', 'HYDROXYLAMINE', 'HYDROXYMETHYLBILANE', 'HYDROXYPROPANAL', 'HYPOXANTHINE', 'Heme_b', 'Hex_2_enoyl_ACPs', 'Hexanoyl_ACPs', 'Holo_EntB', 'Holo_EntF', 'HypE_Proteins', 'HypE_S_carboxamide', 'HypE_S_cyanate', 'IDP', 'ILE', 'ILE_tRNAs', 'IMIDAZOLE_ACETOL_P', 'IMINOASPARTATE', 'IMP', 'INDOLE', 'INDOLE_3_GLYCEROL_P', 'INOSINE', 'IS30_Insertion_Sequences', 'IS30_with_Integrated_Transposon', 'ISOBUTANOL', 'ISOCHORISMATE', 'ISOVALERYL_COA', 'ITP', 'Initiation_tRNAmet', 'Iron_Sulfur_Cluster_Scaffold_Proteins', 'Iso_Cit', 'KDO', 'KDO_8P', 'KDO_LIPID_IVA', 'KDO2_LAUROYL_LIPID_IVA', 'KDO2_LIPID_A', 'KDO2_LIPID_IVA', 'KDO2_PALMITOLEOYL_LIPID_IVA', 'KETOBUTFORMLY_INACT_MONOMER', 'KETOBUTFORMLY_MONOMER', 'L_1_GLYCERO_PHOSPHORYLCHOLINE', 'L_1_GLYCEROPHOSPHORYLETHANOL_AMINE', 'L_1_PHOSPHATIDYL_ETHANOLAMINE', 'L_1_PHOSPHATIDYL_GLYCEROL', 'L_1_PHOSPHATIDYL_GLYCEROL_P', 'L_1_PHOSPHATIDYL_SERINE', 'L_3_HYDROXYACYL_COA', 'L_ALA_GAMMA_D_GLU_DAP', 'L_ALLO_THREONINE', 'L_ALPHA_ALANINE', 'L_ARA4N_MODIFIED_KDO2_LIPID_A', 'L_ARGININO_SUCCINATE', 'L_ASCORBATE_6_PHOSPHATE', 'L_ASPARTATE', 'L_ASPARTATE_SEMIALDEHYDE', 'L_BETA_ASPARTYL_P', 'L_CARNITINYL_COA', 'L_CITRULLINE', 'L_CYSTATHIONINE', 'L_Cysteine_Desulfurase_persulfide', 'L_Cysteine_Desulfurases', 'L_DELTA1_PYRROLINE_5_CARBOXYLATE', 'L_DI_GMP', 'L_DIHYDROXY_PHENYLALANINE', 'L_FUCULOSE', 'L_GAMMA_GLUTAMYLCYSTEINE', 'L_GLUTAMATE_5_P', 'L_GLUTAMATE_GAMMA_SEMIALDEHYDE', 'L_GLYCERALDEHYDE', 'L_GLYCERALDEHYDE_3_PHOSPHATE', 'L_HISTIDINOL_P', 'L_IDONATE', 'L_LACTATE', 'L_LYXOSE', 'L_ORNITHINE', 'L_PANTOATE', 'L_PHOSPHATIDATE', 'L_RHAMNONATE', 'L_RIBULOSE', 'L_RIBULOSE_5_P', 'L_SELENOCYSTEINE', 'L_THREONINE_O_3_PHOSPHATE', 'L_XYLULOSE', 'L_XYLULOSE_5_P', 'L_arabinopyranose', 'L_leucyl_L_arginyl_Protein', 'L_leucyl_L_lysyl_Protein', 'L_methionyl_tRNAfmet', 'L_phenylalanyl_L_arginyl_Protein', 'L_phenylalanyl_L_lysyl_Protein', 'L_seryl_SEC_tRNAs', 'LACTALD', 'LEU', 'LEU_tRNAs', 'LIPID_IV_A', 'LIPOIC_ACID', 'LIPOYL_ACP', 'LIPOYL_AMP', 'LL_DIAMINOPIMELATE', 'LYS', 'LYS_tRNAs', 'Leader_Sequences', 'Light', 'Lipopolysaccharides', 'Lipoprotein_signal_peptide', 'Lipoyl_ACPs', 'Lipoyl_Protein_L_Lysine', 'Lipoyl_Protein_N6_lipoyllysine', 'Long_Chain_Polyphosphate', 'Lysidine_tRNA_Ile2', 'Lysophospholipids', 'MAL', 'MALONATE_S_ALD', 'MALONYL_ACP', 'MALONYL_COA', 'MALTOHEXAOSE', 'MALTOPENTAOSE', 'MALTOSE', 'MALTOTETRAOSE', 'MANNITOL', 'MANNITOL_1P', 'MANNOSE', 'MANNOSE_1P', 'MDO_D_Glucoses', 'MELIBIOSE', 'MENADIOL', 'MESO_DIAMINOPIMELATE', 'MET', 'METHIONYL_PEPTIDE', 'METHYL_GLYOXAL', 'METHYL_MALONYL_COA', 'METHYLENE_THF_GLU_N', 'METOH', 'MI_HEXAKISPHOSPHATE', 'MI_PENTAKISPHOSPHATE', 'MONOMER0_2811', 'MONOMER0_4152', 'MONOMER0_4170', 'MONOMER0_4342', 'MONOMER0_4438', 'MONOMETHYL_ESTER_OF_TRANS_ACONITATE', 'MPT_Synthase_small_subunits', 'MUTATED_TRNA', 'MYO_INOSITOL', 'Malonyl_acp_methyl_ester', 'Mannose_6_phosphate', 'Menaquinols', 'Menaquinones', 'Methylated_Ribosomal_Protein_L11s', 'Mnm5Se2U_containing_tRNAs', 'Modified_Bases', 'Myristoyl_ACPs', 'N_23_DIHYDROXYBENZOYL_L_SERINE', 'N_5_PHOSPHORIBOSYL_ANTHRANILATE', 'N_ACETYL_9_O_ACETYLNEURAMINATE', 'N_ACETYL_D_GLUCOSAMINE', 'N_ACETYL_D_GLUCOSAMINE_1_P', 'N_ACETYL_D_GLUCOSAMINE_6_P', 'N_ACETYL_D_MANNOSAMINE', 'N_ACETYL_D_MANNOSAMINE_6P', 'N_ACETYL_GLUTAMYL_P', 'N_ACETYLNEURAMINATE', 'N_ALPHA_ACETYLORNITHINE', 'N_Acetoxy_Arylamines', 'N_Acetyl_beta_D_Hexosaminides', 'N_ETHYLMALEIMIDE', 'N_Hydroxy_Arylamines', 'N_METHYLTRYPTOPHAN', 'N_SUCCINYL_2_AMINO_6_KETOPIMELATE', 'N_SUCCINYLLL_2_6_DIAMINOPIMELATE', 'N_Substituted_Amino_Acids', 'N_Substituted_Aminoacyl_tRNA', 'N_acetyl_D_glucosamine', 'N_acetyl_D_mannosamine', 'N_acetyl_beta_D_hexosamines', 'N_acetylarylamines', 'N_formyl_L_methionyl_tRNAfmet', 'N2_SUCCINYLGLUTAMATE', 'N2_SUCCINYLORNITHINE', 'N5_Formyl_THF_Glu_N', 'N6_L_threonylcarbamoyladenine37_tRNAs', 'N6_met_threonylcarbamoyl_A37_tRNAs', 'NAD', 'NAD_P_OR_NOP', 'NADH', 'NADH_P_OR_NOP', 'NADP', 'NADPH', 'NARL_MONOMER', 'NAcMur_Peptide_NAcGlc_Undecaprenols', 'NAcMur_Peptide_Undecaprenols', 'NIACINAMIDE', 'NIACINE', 'NICOTINAMIDE_NUCLEOTIDE', 'NICOTINAMIDE_RIBOSE', 'NICOTINATE_NUCLEOTIDE', 'NITRATE', 'NITRIC_OXIDE', 'NITRITE', 'NMNH', 'Negatively_super_coiled_DNAs', 'Nitroaromatic_Ox_Compounds', 'Nitroaromatic_Red_Compounds', 'Non_Glucosylated_Glucose_Acceptors', 'Nonmethylated_Ribosomal_Protein_L11s', 'Nucleoside_3_5_bisphosphate', 'Nucleoside_Diphosphates', 'Nucleoside_Monophosphates', 'Nucleoside_Triphosphates', 'Nucleosides', 'O_PHOSPHO_L_HOMOSERINE', 'O_SUCCINYL_L_HOMOSERINE', 'O_SUCCINYLBENZOATE', 'OCTAPRENYL_DIPHOSPHATE', 'OCTAPRENYL_METHOXY_BENZOQUINONE', 'OCTAPRENYL_METHYL_METHOXY_BENZQ', 'OCTAPRENYL_METHYL_OH_METHOXY_BENZQ', 'OH_ACYL_ACP', 'OH_MYRISTOYL', 'OH_PYR', 'OLEATE_CPD', 'OLEOYL_COA', 'OLIGOPEPTIDES', 'OROTATE', 'OROTIDINE_5_PHOSPHATE', 'OXALACETIC_ACID', 'OXALATE', 'OXALYL_COA', 'OXIDIZED_GLUTATHIONE', 'OXYGEN_MOLECULE', 'Octanoyl_ACPs', 'Octanoylated_domains', 'Oligonucleotides', 'Orthophosphoric_Monoesters', 'Ox_Glutaredoxins', 'Ox_Hybrid_Cluster_Proteins', 'Ox_Thioredoxin', 'Oxidized_2Fe_2S_Ferredoxins', 'Oxidized_Disulfide_Carrier_Proteins', 'Oxidized_Flavoproteins', 'Oxidized_NapC_proteins', 'Oxidized_NrdH_Proteins', 'Oxidized_ferredoxins', 'Oxidized_flavodoxins', 'Oxidized_hydrogenase_3', 'Oxo_glutarate_dehydro_suc_DH_lipoyl', 'Oxo_glutarate_dehydrogenase_DH_lipoyl', 'Oxo_glutarate_dehydrogenase_lipoyl', 'P_AMINO_BENZOATE', 'P_BENZOQUINONE', 'P_HYDROXY_PHENYLPYRUVATE', 'P_NITROPHENOL', 'P_RIBOSYL_4_SUCCCARB_AMINOIMIDAZOLE', 'P3I', 'PANTETHEINE_P', 'PANTOTHENATE', 'PANTOYL_LACTONE', 'PAPS', 'PHE', 'PHE_tRNAs', 'PHENYL_PYRUVATE', 'PHENYLACETALDEHYDE', 'PHENYLACETATE', 'PHENYLETHYLAMINE', 'PHENYLHYDANTOIN', 'PHOSPHATIDYLETHANOLAMINE_KDO2', 'PHOSPHO_ARCB717', 'PHOSPHO_CHEY', 'PHOSPHO_ENOL_PYRUVATE', 'PHOSPHO_NARL', 'PHOSPHORIBOSYL_AMP', 'PHOSPHORIBOSYL_ATP', 'PHOSPHORIBOSYL_CARBOXY_AMINOIMIDAZOLE', 'PHOSPHORIBOSYL_FORMAMIDO_CARBOXAMIDE', 'PHOSPHORIBOSYL_FORMIMINO_AICAR_P', 'PHOSPHORIBULOSYL_FORMIMINO_AICAR_P', 'PHOSPHORYL_CHOLINE', 'PHOSPHORYL_ETHANOLAMINE', 'PORPHOBILINOGEN', 'PPI', 'PRECURSOR_Z', 'PRENOL', 'PREPHENATE', 'PRO', 'PRO_tRNAs', 'PROPANE_1_2_DIOL', 'PROPIONATE', 'PROPIONYL_COA', 'PROPIONYL_P', 'PROT_CYS', 'PROTEIN_L_BETA_ISOASPARTATES', 'PROTEIN_L_BETA_ISOSPARTATE_METHYL_ESTERS', 'PROTEIN_LIPOYLLYSINE', 'PROTEIN_N_UBIQUITYL_LYSINE', 'PROTEIN_PII2', 'PROTOHEME', 'PROTON', 'PROTOPORPHYRINOGEN', 'PROTOPORPHYRIN_IX', 'PRPP', 'PSEUDOURIDINE_5_P', 'PSICOSELYSINE', 'PUTRESCINE', 'PYRAZINAMIDE', 'PYRAZINOIC_ACID', 'PYRIDOXAL', 'PYRIDOXAL_PHOSPHATE', 'PYRIDOXAMINE', 'PYRIDOXAMINE_5P', 'PYRIDOXINE', 'PYRIDOXINE_5P', 'PYRUVATE', 'PYRUVFORMLY_CPLX', 'PYRUVFORMLY_INACTIVE_CPLX', 'Palmitoleoyl_ACPs', 'Palmitoyl_ACPs', 'PepB_Aminopeptidase_Substrates', 'Peptide_Holder_Alternative', 'Peptide_with_N_terminal_Alanine', 'Peptides_holder', 'Peptides_with_Leader_Sequence', 'Peptidoglycan_dimer', 'Peptidoglycans', 'Peptidyl_Dipeptidase_Dcp_Substrates', 'Persulfurated_L_cysteine_desulfurases', 'Phenols', 'Phosphoglycerides', 'Phospholipid_Cyclopropane_Fatty_Acids', 'Phospholipid_Olefinic_Fatty_Acids', 'Pi', 'Pimeloyl_ACP_methyl_esters', 'Pimeloyl_ACPs', 'Poly_Hydroxybutyrate', 'Pre_crRNAs', 'Pre_tRNA_3_prime_half_molecules', 'Pre_tRNA_5_prime_half_molecules', 'Precursor_of_hydrogenase_3', 'Primary_Alcohols', 'Primary_Amines', 'Prolipoprotein_Cysteines', 'Protein_Arginine_Aminocarbinol', 'Protein_Cysteine_Hemithioacetal', 'Protein_Disulfides', 'Protein_Dithiols', 'Protein_L_Arginines', 'Protein_L_glutamine', 'Protein_L_lysine', 'Protein_L_methionine', 'Protein_L_methionine_R_S_oxides', 'Protein_L_methionine_S_S_oxides', 'Protein_L_serine_or_L_threonine', 'Protein_Lysine_Aminocarbinol', 'Protein_N_terminal_L_Arginine', 'Protein_N_terminal_L_Lysine', 'Protein_Ox_Disulfides', 'Protein_Red_Disulfides', 'Protein_S_methyl_L_cysteine', 'Protein_Ser_or_Thr_phosphate', 'Protein_Tyrosines', 'Protein_With_N_Terminal_Met', 'Protein_With_N_Terminal_Pro', 'Protein_With_N_Terminal_X_Pro', 'Protein_alpha_L_Glutamates', 'Protein_tyrosine_phosphates', 'Proteins_with_N_terminal_L_arginine', 'Proteins_with_correct_disulfides', 'Proteins_with_incorrect_disulfides', 'Purine_Bases', 'Purine_Ribonucleosides', 'Pyrimidine_Bases', 'Pyrimidine_Nucleosides', 'Pyrimidine_ribonucleotides', 'Pyruvate_dehydrogenase_acetylDHlipoyl', 'Pyruvate_dehydrogenase_dihydrolipoate', 'Pyruvate_dehydrogenase_lipoate', 'QUINATE', 'QUINOLINATE', 'Quinones', 'R_2_HYDROXYGLUTARATE', 'R_3_Hydroxypalmitoyl_ACPs', 'R_3_hydroxy_cis_vaccenoyl_ACPs', 'R_3_hydroxydodecanoyl_ACPs', 'R_3_hydroxyhexanoyl_ACPs', 'R_3_hydroxymyristoyl_ACPs', 'R_4_PHOSPHOPANTOTHENOYL_L_CYSTEINE', 'REDUCED_MENAQUINONE', 'RHAMNOSE', 'RHAMNULOSE_1P', 'RIBOFLAVIN', 'RIBOSE_15_BISPHOSPHATE', 'RIBOSE_1P', 'RIBOSE_5P', 'RIBULOSE_5P', 'RNA_DNA_hybrids', 'RNA_Holder', 'RNASE_E_DEGRADATION_SUBSTRATE_MRNA', 'RNASE_E_MRNA_PROCESSING_SUBSTRATE', 'RNASE_E_PROCESSING_PRODUCT_MRNA', 'RNASE_G_DEGRADATION_SUBSTRATE_MRNA', 'RNASE_II_DEGRADATION_SUBSTRATE_MRNA', 'RNASE_II_POLY_A_SUBSTRATE_MRNA', 'RNASE_II_SUBSTRATE_WITH_NO_POLY_A_TAIL', 'RNASE_III_MRNA_PROCESSING_SUBSTRATE', 'RNASE_III_PROCESSING_PRODUCT_MRNA', 'RNASE_R_DEGRADATION_SUBSTRATE_RNA', 'Red_Glutaredoxins', 'Red_Hybrid_Cluster_Proteins', 'Red_Thioredoxin', 'Reduced_2Fe_2S_Ferredoxins', 'Reduced_Disulfide_Carrier_Proteins', 'Reduced_Disulfide_Isomerases', 'Reduced_Flavoproteins', 'Reduced_NapC_proteins', 'Reduced_NrdH_Proteins', 'Reduced_ferredoxins', 'Reduced_flavodoxins', 'Reduced_hydrogenase_3', 'Relaxed_DNAs', 'Release_factor_L_glutamine', 'Release_factor_N5_Methyl_L_glutamine', 'Resolution_of_Recombinational_Junction', 'Ribonuc_tri_P_reductases_active', 'Ribonuc_tri_P_reductases_inactive', 'Ribonucleoside_Diphosphates', 'Ribonucleoside_Monophosphates', 'Ribonucleoside_Triphosphates', 'Ribonucleosides', 'Ribosomal_protein_L3_L_glutamine', 'Ribosomal_protein_L3_N5M_L_glutamine', 'Ribosomal_protein_S12_3_methylthio_Asp89', 'Ribosomal_protein_S12_Asp89', 'S_24_DINITROPHENYLGLUTATHIONE', 'S_3_HYDROXYBUTANOYL_COA', 'S_ADENOSYL_4_METHYLTHIO_2_OXOBUTANOATE', 'S_ADENOSYLMETHIONINAMINE', 'S_ADENOSYLMETHIONINE', 'S_ALLANTOIN', 'S_CARBOXYMETHYL_D_CYSTEINE', 'S_CD_Apo_SP_Complex', 'S_HYDROXYMETHYLGLUTATHIONE', 'S_LACTOYL_GLUTATHIONE', 'S_METHYLGLUTATHIONE', 'S18_N_terminal_L_alanine', 'S2O3', 'S5_N_terminal_L_alanine', 'SE_2', 'SELENATE', 'SELENITE', 'SEPO3', 'SER', 'SER_tRNAs', 'SHIKIMATE', 'SHIKIMATE_5P', 'SIROHEME', 'SIROHYDROCHLORIN', 'SN_GLYCEROL_1_PHOSPHATE', 'SO3', 'SORBITOL', 'SPERMIDINE', 'SS_Oligodeoxyribonucleotides', 'SS_Oligoribonucleotides', 'SUC', 'SUC_COA', 'SUCB_LIPOATE', 'SUCC_S_ALD', 'SULFATE', 'SULFO_CYSTEINE', 'SULFOQUINOVOSYLDIACYLGLYCEROL', 'SUPER_OXIDE', 'Saturated_Fatty_Acyl_ACPs', 'Saturated_Fatty_Acyl_CoA', 'Semiquinones', 'Seryl_EntF', 'Siderophore', 'Single_Stranded_DNAs', 'Stabilized_RecA_Filament_DNA_Complex', 'Sugar', 'Sugar_Phosphate', 'Sulfur_Carrier_Proteins_ThiI', 'Sulfurated_Sulfur_Acceptors', 'Sulfurylated_ThiI', 'Supercoiled_Duplex_DNAs', 'T2_C4_DECADIENYL_COA', 'T2_DECENOYL_COA', 'TAGATOSE_1_6_DIPHOSPHATE', 'TAGATOSE_6_PHOSPHATE', 'TAP_GLN', 'TAP_GLU', 'TAP_GLUME', 'TAR_GLN', 'TAR_GLU', 'TAR_GLUME', 'TARTRATE', 'TARTRONATE_S_ALD', 'TAURINE', 'TDP', 'TDP_D_FUCOSAMINE', 'TDP_FUC4NAC', 'THF_GLU_N', 'THIAMINE', 'THIAMINE_P', 'THIAMINE_PYROPHOSPHATE', 'THIOGLYCOLATE', 'THR', 'THR_tRNAs', 'THREO_DS_ISO_CITRATE', 'THYMIDINE', 'THYMINE', 'THZ', 'THZ_P', 'TMP', 'TRANS_23_DEHYDROADIPYL_COA', 'TRANS_D2_ENOYL_ACP', 'TRANS_D2_ENOYL_COA', 'TREHALOSE', 'TREHALOSE_6P', 'TRG_GLN', 'TRG_GLU', 'TRG_GLUME', 'TRIMETHYLAMINE', 'TRIMETHYLAMINE_N_O', 'TRIPEPTIDES', 'TRP', 'TRP_tRNAs', 'TSR_GLN', 'TSR_GLU', 'TSR_GLUME', 'TTP', 'TYR', 'TYR_tRNAs', 'Tetradec_2_enoyl_ACPs', 'Thi_S', 'Thiocarboxyadenylated_ThiS_Proteins', 'Thiocarboxylated_MPT_synthases', 'Trans_D2_cis_D7_tetradecenoyl_ACPs', 'Trans_D2_decenoyl_ACPs', 'Trans_D3_cis_D5_dodecenoyl_ACPs', 'Trans_D3_cis_D9_hexadecenoyl_ACPs', 'TusA_L_cysteine', 'TusA_Persulfides', 'TusD_L_cysteine', 'TusD_Persulfides', 'TusE_L_cysteine', 'TusE_S_sulfanylcysteine', 'Type_1_transmemberane_domains', 'UBIQUINONE_8', 'UDP', 'UDP_4_AMINO_4_DEOXY_L_ARABINOSE', 'UDP_AA_GLUTAMATE', 'UDP_AAGM_DIAMINOHEPTANEDIOATE', 'UDP_ACETYL_CARBOXYVINYL_GLUCOSAMINE', 'UDP_D_GALACTO_14_FURANOSE', 'UDP_GLUCURONATE', 'UDP_L_ARA4_FORMYL_N', 'UDP_MANNAC', 'UDP_MANNACA', 'UDP_MURNAC_TETRAPEPTIDE', 'UDP_N_ACETYL_D_GLUCOSAMINE', 'UDP_N_ACETYLMURAMATE', 'UDP_OHMYR_ACETYLGLUCOSAMINE', 'UDP_OHMYR_GLUCOSAMINE', 'UDP_sugar', 'UMP', 'UNDECAPRENYL_DIPHOSPHATE', 'URACIL', 'URATE', 'UREA', 'URIDINE', 'URIDYLYL_PII2', 'URIDYLYL_PROTEIN_PII', 'UROPORPHYRINOGEN_III', 'UTP', 'Ubiquinols', 'Ubiquinones', 'Ubiquitin_C_Terminal_Glycine', 'Unstable_RecA_Filament_DNA_Complex', 'Unsulfurated_Sulfur_Acceptors', 'Unwound_RNA', 'Uracil_54_in_tRNA', 'Uracil_tRNAs', 'Uridine32_in_tRNA', 'VAL', 'VAL_tRNAs', 'Val_tRNA1_Adenine37', 'Val_tRNA1_N6_MeAdenine37', 'WATER', 'Wound_RNA', 'XANTHINE', 'XANTHOSINE', 'XANTHOSINE_5_PHOSPHATE', 'XDP', 'XTP', 'XYLOSE', 'XYLULOSE_5_PHOSPHATE', 'Xylans', 'YHAV_DEGRADATION_SUBSTRATE_MRNA', '_1_2_Diglycerides', '_1_4_alpha_D_Glucan', '_1_AMINO_PROPAN_2_OL', '_1_AMINO_PROPAN_2_ONE_3_PHOSPHATE', '_1_CHLORO_24_DINITROBENZENE', '_1_KETO_2_METHYLVALERATE', '_1_Lyso_phospholipids', '_1_PALMITOYLGLYCEROL_3_PHOSPHATE', '_11_DEOXYCORTICOSTERONE', '_16S_rRNA_2_O_methylcytidine1402', '_16S_rRNA_5_O_methylcytosine1407', '_16S_rRNA_5_O_methylcytosine967', '_16S_rRNA_N2_methylguanine1207', '_16S_rRNA_N2_methylguanine966', '_16S_rRNA_N2methylguanine1516', '_16S_rRNA_N3_methyluracil1498', '_16S_rRNA_N4_methylcytidine1402', '_16S_rRNA_N6_dimethyladenine1518_1519', '_16S_rRNA_N7_methylguanine527', '_16S_rRNA_adenine1518_adenine1519', '_16S_rRNA_cytidine1402', '_16S_rRNA_cytosine1407', '_16S_rRNA_cytosine967', '_16S_rRNA_guanine_1207', '_16S_rRNA_guanine_527', '_16S_rRNA_guanine_966', '_16S_rRNA_guanine1516', '_16S_rRNA_pseudouridine516', '_16S_rRNA_uracil1498', '_16S_rRNA_uridine516', '_1iNisup6sup_ethenoadenine_in_DNA', '_2_3_4_Saturated_L_Phosphatidates', '_2_3_DIHYDROXYBENZOATE', '_2_3_DIHYDROXYPHENYL_PROPIONATE', '_2_3_dihydroxypropane_1_sulfonate', '_2_5_TRIPHOSPHORIBOSYL_3_DEPHOSPHO_', '_2_ACETO_2_HYDROXY_BUTYRATE', '_2_ACETO_LACTATE', '_2_ACYL_GPE', '_2_AMINOMALONATE_SEMIALDEHYDE', '_2_Acylglycero_Phosphocholines', '_2_Aminobutyrate', '_2_C_METHYL_D_ERYTHRITOL_4_PHOSPHATE', '_2_CARBOXYMUCONATE', '_2_D_THREO_HYDROXY_3_CARBOXY_ISOCAPROATE', '_2_DEHYDRO_3_DEOXY_D_GALACTONATE', '_2_DEHYDRO_3_DEOXY_D_GLUCONATE', '_2_DEHYDROPANTOATE', '_2_DEHYDROPANTOYL_LACTONE', '_2_DEOXY_D_GLUCOSE', '_2_DEOXY_D_GLUCOSE_6_PHOSPHATE', '_2_DH_3_DO_D_ARABINONATE', '_2_HYDROXYGLUTARIC_ACID', '_2_Hexadecenoyl_ACPs', '_2_KETO_3_DEOXY_6_P_GLUCONATE', '_2_KETO_3_METHYL_VALERATE', '_2_KETO_GLUTARAMATE', '_2_KETO_ISOVALERATE', '_2_KETOGLUTARATE', '_2_LYSOPHOSPHATIDYLETHANOLAMINES', '_2_Lysophosphatidylcholines', '_2_MERCAPTOETHANOL', '_2_O_Methylcytidine_32_tRNAs', '_2_O_Methylcytidine_34_tRNAs', '_2_O_Methylguanosine18', '_2_O_Methyluridine32_tRNA', '_2_OCTAPRENYL_6_HYDROXYPHENOL', '_2_OCTAPRENYL_6_METHOXYPHENOL', '_2_OCTAPRENYLPHENOL', '_2_OXOBUTANOATE', '_2_Octenoyl_ACPs', '_2_Oxo_carboxylates', '_2_PG', '_2_PHOSPHO_4_CYTIDINE_5_DIPHOSPHO_2_C_MET', '_2_PROTOCATECHUOYLPHLOROGLUCINOLCARBOXYLA', '_2_Prime_Phosphate_Terminated_RNAs', '_2_Thiocytosine_32_In_tRNAs', '_23_Diaminopropanoate', '_23DHB_EntB', '_23S_RRNA_N2_METHYLGUANINE2445', '_23S_rRNA_2_O_methylcytidine2498', '_23S_rRNA_2_O_methylguanosine2251', '_23S_rRNA_2_O_methyluridine2552', '_23S_rRNA_2_methyladenine2503', '_23S_rRNA_5_methylcytosine1962', '_23S_rRNA_5_methyluracil1939', '_23S_rRNA_5_methyluracil747', '_23S_rRNA_N1_methylguanine745', '_23S_rRNA_N2_methylguanine1835', '_23S_rRNA_N3_methylpseudouridine1915', '_23S_rRNA_N6_m_adenine1618', '_23S_rRNA_N6_methyladenine_2030', '_23S_rRNA_N7_methylguanine_2069', '_23S_rRNA_adenine_1618', '_23S_rRNA_adenine_2030', '_23S_rRNA_adenine_2503', '_23S_rRNA_cytidine_2498', '_23S_rRNA_cytosine_1962', '_23S_rRNA_guanine_1835', '_23S_rRNA_guanine_2069', '_23S_rRNA_guanine_2445', '_23S_rRNA_guanine_2551', '_23S_rRNA_guanine_745', '_23S_rRNA_pseudouridine1911_1915_1917', '_23S_rRNA_pseudouridine1915', '_23S_rRNA_pseudouridine2457', '_23S_rRNA_pseudouridine2604', '_23S_rRNA_pseudouridine2605', '_23S_rRNA_pseudouridine746', '_23S_rRNA_pseudouridine955_2504_2580', '_23S_rRNA_uracil_1939', '_23S_rRNA_uracil_747', '_23S_rRNA_uridine_2552', '_23S_rRNA_uridine1911_1915_1917', '_23S_rRNA_uridine2457', '_23S_rRNA_uridine2604', '_23S_rRNA_uridine2605', '_23S_rRNA_uridine746', '_23S_rRNA_uridine955_2504_2580', '_23S_rRNAs', '_25_DIDEHYDRO_D_GLUCONATE', '_2C_METH_D_ERYTHRITOL_CYCLODIPHOSPHATE', '_2K_4CH3_PENTANOATE', '_3_5_ADP', '_3_BETA_D_GLUCOSYLGLUCOSE', '_3_CARBOXY_3_HYDROXY_ISOCAPROATE', '_3_CHLORO_D_ALANINE', '_3_DEHYDRO_SHIKIMATE', '_3_DEOXY_D_ARABINO_HEPTULOSONATE_7_P', '_3_ENOLPYRUVYL_SHIKIMATE_5P', '_3_HYDROXY_PROPIONATE', '_3_HYDROXYADIPYL_COA', '_3_HYDROXYBENZOATE', '_3_HYDROXYPHENYL_PROPIONATE', '_3_Hydroxy_Terminated_DNAs', '_3_Hydroxy_octanoyl_ACPs', '_3_Hydroxyglutaryl_ACP_methyl_ester', '_3_KETO_ADIPYL_COA', '_3_KETO_L_GULONATE', '_3_KETOACYL_COA', '_3_KETOBUTYRATE', '_3_Ketoglutaryl_ACP_methyl_ester', '_3_Ketopimeloyl_ACP_methyl_esters', '_3_MERCAPTO_PYRUVATE', '_3_METHYL_CROTONYL_COA', '_3_Methyl_Adenines', '_3_OCTAPRENYL_4_HYDROXYBENZOATE', '_3_Oxo_octanoyl_ACPs', '_3_P_HYDROXYPYRUVATE', '_3_P_SERINE', '_3_PHENYLPROPIONATE', '_3_Phosphomonucleotides', '_3_Prime_Phosphate_Terminated_RNAs', '_3_SULFINOALANINE', '_3_hydroxy_cis_D7_tetraecenoyl_ACPs', '_3_hydroxy_cis_D9_hexaecenoyl_ACPs', '_3_hydroxypimeloyl_ACP_methyl_esters', '_3_oxo_cis_D7_tetradecenoyl_ACPs', '_3_oxo_cis_D9_hexadecenoyl_ACPs', '_3_oxo_cis_vaccenoyl_ACPs', '_3_oxo_decanoyl_ACPs', '_3_oxo_dodecanoyl_ACPs', '_3_oxo_hexanoyl_ACPs', '_3_oxo_myristoyl_ACPs', '_3_oxo_palmitoyl_ACPs', '_3_terminal_unsaturated_sugars', '_34_DIHYDROXYPHENYLACETYL_COA', '_34_DIHYDROXYPHENYLPYRUVATE', '_3OH_4P_OH_ALPHA_KETOBUTYRATE', '_4_AMINO_4_DEOXYCHORISMATE', '_4_AMINO_BUTYRALDEHYDE', '_4_AMINO_BUTYRATE', '_4_CYTIDINE_5_DIPHOSPHO_2_C', '_4_HYDROXY_2_KETOVALERATE', '_4_HYDROXY_BUTYRATE', '_4_NITROANILINE', '_4_P_PANTOTHENATE', '_4_PHOSPHONOOXY_THREONINE', '_4_hydroxybenzoate', '_5_10_METHENYL_THF_GLU_N', '_5_AMINO_LEVULINATE', '_5_BETA_L_THREO_PENTAPYRANOSYL_4_ULOSE_', '_5_CarboxyMeAmMe_2_O_MeU34_tRNALeu', '_5_DEHYDROGLUCONATE', '_5_HYDROXY_CTP', '_5_HYDROXYISOURATE', '_5_HYDROXYU34_TRNA', '_5_KETO_4_DEOXY_D_GLUCARATE', '_5_L_GLUTAMYL_AMINO_ACID', '_5_L_GLUTAMYL_PEPTIDE', '_5_METHYL_THF_GLU_N', '_5_METHYLTHIOADENOSINE', '_5_Methylcytosine_DNA', '_5_OXOPROLINE', '_5_P_BETA_D_RIBOSYL_AMINE', '_5_P_RIBOSYL_N_FORMYLGLYCINEAMIDE', '_5_PHOSPHO_RIBOSYL_GLYCINEAMIDE', '_5_PHOSPHORIBOSYL_5_AMINOIMIDAZOLE', '_5_PHOSPHORIBOSYL_N_FORMYLGLYCINEAMIDINE', '_5_Phospho_DNA', '_5_Phospho_RNA', '_5_Phospho_terminated_DNAs', '_5_Phosphomononucleotides', '_5_carbo_me_ami_me_ur_34_tRNALeu', '_5_methoxycarbonylmethoxyU34_tRNA', '_5_oxyacetylU34_tRNA', '_5_phosphooligonucleotides', '_50S_Ribo_protein_L16_Hydroxylarginine', '_50S_Ribosomal_subunit_protein_L16_Arg', '_5678_TETRAHYDROPTERIDINE', '_5Prime_OH_Terminated_RNAs', '_5S_rRNAs', '_6_Acetyl_Beta_D_Galactosides', '_6_Dimethylallyladenosine37_tRNAs', '_67_DIHYDROPTERIDINE', '_7_8_DIHYDROPTEROATE', '_7_AMINOMETHYL_7_DEAZAGUANINE', '_7_CYANO_7_DEAZAGUANINE', '_7_METHYLGUANOSINE_5_PHOSPHATE', '_8_AMINO_7_OXONONANOATE', '_9S_RRNA', 'a_double_stranded_DNA_with_a_blunt_end', 'a_mature_triacylated_lipoprotein', 'a_precursor_of_large_subunit_of_hydrogen', 'a_reduced_NrfB_protein', 'a_reduced_TorC_protein', 'a_thymine_in_DNA', 'alpha_N_Peptidyl_LGlutamate', 'an_Nsup1sup_methyladenine_in_DNA', 'an_Nsup3sup_methylcytosine_in_DNA', 'an_iNisup1sup_ethyladenine_in_DNA', 'an_oxidized_NrfB_protein', 'an_oxidized_TorC_protein', 'an_oxidized_TorY_protein', 'b_Hydroxy_cis_D5_dodecenoyl_ACPs', 'b_Keto_cis_D5_dodecenoyl_ACPs', 'biotin_L_lysine_in_BCCP_dimers', 'carboxybiotin_L_lysine_in_BCCP_dimers', 'cis_vaccen_2_enoyl_ACPs', 'crRNAs', 'isocitrate_dehydrogenase', 'ligated_tRNAs_with_2prime_5prime_linkage', 'mRNA_Fragments', 'mRNAs', 'mRNAs_with_5_diphosphate', 'mRNAs_with_5_monophosphate', 'mRNAs_with_5_triphosphate', 'mature_tRNA', 'mcmo5U34m_tRNA', 'phosphoethanolamine_cellulose', 'protein_L_glutamate_O4_methyl_ester', 'rRNA_fragments', 'signal_peptide', 'ssDNA_RNA_primer_hybrid', 'ssRNA_with_3phosphate', 'ssRNA_with_5OH', 'ssRNAs', 'tRNA_2_thiouridine34', 'tRNA_2methyladenine_37', 'tRNA_4_thiouridine', 'tRNA_Adenosines_37', 'tRNA_Arg_adenosine34', 'tRNA_Arg_inosine34', 'tRNA_Containing_5AminoMe_2_ThioUrdines', 'tRNA_Containing_5MeAminoMe_2_ThioU', 'tRNA_Containing_N1_Methylguanine_37', 'tRNA_Containing_N7_Methylguanine_46', 'tRNA_Dihydrouridines', 'tRNA_Sec', 'tRNA_adenine_37', 'tRNA_containing_5_CarbMeAminome_2_ThioU', 'tRNA_containing_5_CarbMeAminome_uridine', 'tRNA_containing_5Me_uridine54', 'tRNA_fragment', 'tRNA_guanosine18', 'tRNA_precursors', 'tRNA_pseudouridine_38_40', 'tRNA_pseudouridine13', 'tRNA_pseudouridine32', 'tRNA_pseudouridine35', 'tRNA_pseudouridine55', 'tRNA_pseudouridine65', 'tRNA_uridine_38_40', 'tRNA_uridine13', 'tRNA_uridine34', 'tRNA_uridine35', 'tRNA_uridine55', 'tRNA_uridine65', 'tRNA_uridines', 'tRNA_with_7_aminomethyl_7_deazaguanine', 'tRNAs', 'tRNAs_Asp_with_queuosine', 'tRNAs_containing_epoxy_quenosine', 'tRNAs_with_CCA', 'tRNAs_with_glutamylated_queuosine', 'tRNAs_with_queuine', 'type_IV_prepillin' ],
	'loc' : ['cyt', 'cytosk', 'ex', 'mem', 'per', 'wall', 'bnuc', 'cproj', 'imem', 'omem', 'pmem'],
	'strain' : ['ecoli']})
Monomer('prot',
	['name', 'loc', 'dna', 'met', 'prot', 'rna', 'up', 'dw'],
	{ 'name' : [ 'AAS_MONOMER', 'ACECOATRANS_MONOMER', 'ACETATEKINA_MONOMER', 'ACS_MONOMER', 'ACYLCOADEHYDROG_MONOMER', 'ADENODEAMIN_MONOMER', 'ADENYL_KIN_MONOMER', 'ADENYLATECYC_MONOMER', 'ALDHDEHYDROG_MONOMER', 'ALDOSE1EPIM_MONOMER', 'ALPHA_AMYL_CYTO_MONOMER', 'ALPHA_AMYL_PERI_MONOMER', 'ALTRO_OXIDOREDUCT_MONOMER', 'ALTRODEHYDRAT_MONOMER', 'AMYLOMALT_MONOMER', 'ANTHRANSYNCOMPII_MONOMER', 'ARGS_MONOMER', 'ARGSUCCINLYA_MONOMER', 'ARGSUCCTRAN_MONOMER', 'AROA_MONOMER', 'AROB_MONOMER', 'AROE_MONOMER', 'AROK_MONOMER', 'ARYLSULFAT_MONOMER', 'BIOTINLIG_MONOMER', 'BTUE_MONOMER', 'CAIC_MONOMER', 'CARDIOLIPSYN_MONOMER', 'CARNRACE_MONOMER', 'CDPDIGLYPYPHOSPHA_MONOMER', 'CDPDIGLYSYN_MONOMER', 'CHD_MONOMER', 'CHER_MONOMER', 'CHORPYRLY_MONOMER', 'CITC_MONOMER', 'CITRATE_SI_SYNTHASE', 'CMPKI_MONOMER', 'COBALADENOSYLTRANS_MONOMER', 'COBS_MONOMER', 'CPDB_MONOMER', 'CPM_KDOSYNTH_MONOMER', 'CROBETREDUCT_MONOMER', 'CYSS_MONOMER', 'CYTOCHROMEC552_MONOMER', 'DALADALALIGA_MONOMER', 'DEHYDDEOXGALACTKIN_MONOMER', 'DEHYDDEOXPHOSGALACT_ALDOL_MONOMER', 'DEHYDROPANTLACRED_MONOMER', 'DEOXYGLUCONOKIN_MONOMER', 'DEOXYRIBOSE_P_ALD_MONOMER', 'DIENOYLCOAREDUCT_MONOMER', 'DIHYDROFOLATEREDUCT_MONOMER', 'DIHYDRONEOPTERIN_MONO_P_DEPHOS_MONOMER', 'DIHYDROOROTOX_MONOMER', 'DLACTDEHYDROGFAD_MONOMER', 'DMK_MONOMER', 'DSBBPROT_MONOMER', 'DSBD_MONOMER', 'DSERDEAM_MONOMER', 'DTDPDEHYDRHAMEPIM_MONOMER', 'DTDPDEHYRHAMREDUCT_MONOMER', 'E1O', 'E2O', 'E2P_MONOMER', 'EG10037_MONOMER', 'EG10041_MONOMER', 'EG10043_MONOMER', 'EG10048_MONOMER', 'EG10085_MONOMER', 'EG10114_MONOMER', 'EG10119_MONOMER', 'EG10122_MONOMER', 'EG10124_MONOMER', 'EG10136_MONOMER', 'EG10168_MONOMER', 'EG10204_MONOMER', 'EG10211_MONOMER', 'EG10212_MONOMER', 'EG10239_MONOMER', 'EG10243_MONOMER', 'EG10246_MONOMER', 'EG10299_MONOMER', 'EG10329_MONOMER', 'EG10343_MONOMER', 'EG10370_MONOMER', 'EG10376_MONOMER', 'EG10381_MONOMER', 'EG10397_MONOMER', 'EG10443_MONOMER', 'EG10456_MONOMER', 'EG10487_MONOMER', 'EG10488_MONOMER', 'EG10523_MONOMER', 'EG10530_MONOMER', 'EG10534_MONOMER', 'EG10548_MONOMER', 'EG10570_MONOMER', 'EG10573_MONOMER', 'EG10595_MONOMER', 'EG10626_MONOMER', 'EG10627_MONOMER', 'EG10651_MONOMER', 'EG10662_MONOMER', 'EG10668_MONOMER', 'EG10673_MONOMER', 'EG10689_MONOMER', 'EG10690_MONOMER', 'EG10696_MONOMER', 'EG10719_MONOMER', 'EG10722_MONOMER', 'EG10723_MONOMER', 'EG10724_MONOMER', 'EG10736_MONOMER', 'EG10737_MONOMER', 'EG10739_MONOMER', 'EG10746_MONOMER', 'EG10760_MONOMER', 'EG10785_MONOMER', 'EG10786_MONOMER', 'EG10812_MONOMER', 'EG10829_MONOMER', 'EG10850_MONOMER', 'EG10851_MONOMER', 'EG10853_MONOMER', 'EG10856_MONOMER', 'EG10858_MONOMER', 'EG10860_MONOMER', 'EG10863_MONOMER', 'EG10926_MONOMER', 'EG10967_MONOMER', 'EG10983_MONOMER', 'EG10986_MONOMER', 'EG11004_MONOMER', 'EG11013_MONOMER', 'EG11022_MONOMER', 'EG11058_MONOMER', 'EG11073_MONOMER', 'EG11082_MONOMER', 'EG11095_MONOMER', 'EG11112_MONOMER', 'EG11118_MONOMER', 'EG11121_MONOMER', 'EG11158_MONOMER', 'EG11162_MONOMER', 'EG11166_MONOMER', 'EG11177_MONOMER', 'EG11189_MONOMER', 'EG11202_MONOMER', 'EG11222_MONOMER', 'EG11237_MONOMER', 'EG11247_MONOMER', 'EG11253_MONOMER', 'EG11259_MONOMER', 'EG11266_MONOMER', 'EG11268_MONOMER', 'EG11288_MONOMER', 'EG11292_MONOMER', 'EG11309_MONOMER', 'EG11311_MONOMER', 'EG11333_MONOMER', 'EG11336_MONOMER', 'EG11339_MONOMER', 'EG11340_MONOMER', 'EG11341_MONOMER', 'EG11344_MONOMER', 'EG11350_MONOMER', 'EG11351_MONOMER', 'EG11352_MONOMER', 'EG11353_MONOMER', 'EG11359_MONOMER', 'EG11362_MONOMER', 'EG11371_MONOMER', 'EG11423_MONOMER', 'EG11424_MONOMER', 'EG11425_MONOMER', 'EG11426_MONOMER', 'EG11433_MONOMER', 'EG11437_MONOMER', 'EG11438_MONOMER', 'EG11440_MONOMER', 'EG11441_MONOMER', 'EG11494_MONOMER', 'EG11497_MONOMER', 'EG11503_MONOMER', 'EG11507_MONOMER', 'EG11538_MONOMER', 'EG11551_MONOMER', 'EG11579_MONOMER', 'EG11581_MONOMER', 'EG11591_MONOMER', 'EG11595_MONOMER', 'EG11600_MONOMER', 'EG11613_MONOMER', 'EG11620_MONOMER', 'EG11646_MONOMER', 'EG11665_MONOMER', 'EG11736_MONOMER', 'EG11750_MONOMER', 'EG11758_MONOMER', 'EG11768_MONOMER', 'EG11779_MONOMER', 'EG11794_MONOMER', 'EG11796_MONOMER', 'EG11822_MONOMER', 'EG11826_MONOMER', 'EG11829_MONOMER', 'EG11831_MONOMER', 'EG11843_MONOMER', 'EG11846_MONOMER', 'EG11848_MONOMER', 'EG11850_MONOMER', 'EG11914_MONOMER', 'EG11915_MONOMER', 'EG11920_MONOMER', 'EG11921_MONOMER', 'EG11955_MONOMER', 'EG11956_MONOMER', 'EG11957_MONOMER', 'EG11983_MONOMER', 'EG12013_MONOMER', 'EG12019_MONOMER', 'EG12044_MONOMER', 'EG12069_MONOMER', 'EG12096_MONOMER', 'EG12097_MONOMER', 'EG12098_MONOMER', 'EG12128_MONOMER', 'EG12130_MONOMER', 'EG12159_MONOMER', 'EG12163_MONOMER', 'EG12167_MONOMER', 'EG12198_MONOMER', 'EG12207_MONOMER', 'EG12210_MONOMER', 'EG12216_MONOMER', 'EG12221_MONOMER', 'EG12233_MONOMER', 'EG12234_MONOMER', 'EG12237_MONOMER', 'EG12244_MONOMER', 'EG12258_MONOMER', 'EG12265_MONOMER', 'EG12267_MONOMER', 'EG12286_MONOMER', 'EG12287_MONOMER', 'EG12293_MONOMER', 'EG12312_MONOMER', 'EG12318_MONOMER', 'EG12330_MONOMER', 'EG12384_MONOMER', 'EG12387_MONOMER', 'EG12394_MONOMER', 'EG12401_MONOMER', 'EG12403_MONOMER', 'EG12424_MONOMER', 'EG12433_MONOMER', 'EG12436_MONOMER', 'EG12438_MONOMER', 'EG12440_MONOMER', 'EG12449_MONOMER', 'EG12450_MONOMER', 'EG12609_MONOMER', 'EG12666_MONOMER', 'EG12693_MONOMER', 'EG12712_MONOMER', 'EG12717_MONOMER', 'EG12876_MONOMER', 'EG13236_MONOMER', 'ENTC_MONOMER', 'ENTD_MONOMER', 'ENTF_PANT', 'FGAMSYN_MONOMER', 'FLAVONADPREDUCT_MONOMER', 'FMNREDUCT_MONOMER', 'FOLC_MONOMER', 'FORMATEDEHYDROGH_MONOMER', 'FPPSYN_MONOMER', 'FRUCBISALD_CLASSII', 'FUCULOKIN_MONOMER', 'FUMARASE_A', 'FUMARASE_B', 'FUMARATE_REDUCTASE', 'G495_MONOMER', 'G6096_MONOMER', 'G6103_MONOMER', 'G6131_MONOMER', 'G6141_MONOMER', 'G6190_MONOMER', 'G6199_MONOMER', 'G6236_MONOMER', 'G6244_MONOMER', 'G6245_MONOMER', 'G6246_MONOMER', 'G6275_MONOMER', 'G6284_MONOMER', 'G6310_MONOMER', 'G6329_MONOMER', 'G6339_MONOMER', 'G6340_MONOMER', 'G6364_MONOMER', 'G6406_MONOMER', 'G6416_MONOMER', 'G6418_MONOMER', 'G6422_MONOMER', 'G6435_MONOMER', 'G6437_MONOMER', 'G6438_MONOMER', 'G6449_MONOMER', 'G6456_MONOMER', 'G6457_MONOMER', 'G6468_MONOMER', 'G6488_MONOMER', 'G6502_MONOMER', 'G6503_MONOMER', 'G6520_MONOMER', 'G6521_MONOMER', 'G6522_MONOMER', 'G6523_MONOMER', 'G6530_MONOMER', 'G6551_MONOMER', 'G6567_MONOMER', 'G6576_MONOMER', 'G6577_MONOMER', 'G6580_MONOMER', 'G6581_MONOMER', 'G6621_MONOMER', 'G6634_MONOMER', 'G6646_MONOMER', 'G6647_MONOMER', 'G6654_MONOMER', 'G6655_MONOMER', 'G6661_MONOMER', 'G6701_MONOMER', 'G6708_MONOMER', 'G6714_MONOMER', 'G6715_MONOMER', 'G6716_MONOMER', 'G6718_MONOMER', 'G6719_MONOMER', 'G6782_MONOMER', 'G6798_MONOMER', 'G6805_MONOMER', 'G6806_MONOMER', 'G6862_MONOMER', 'G6880_MONOMER', 'G6886_MONOMER', 'G6890_MONOMER', 'G6932_MONOMER', 'G6952_MONOMER', 'G6954_MONOMER', 'G6958_MONOMER', 'G6986_MONOMER', 'G6991_MONOMER', 'G7008_MONOMER', 'G7011_MONOMER', 'G7022_MONOMER', 'G7063_MONOMER', 'G7098_MONOMER', 'G7123_MONOMER', 'G7146_MONOMER', 'G7164_MONOMER', 'G7166_MONOMER', 'G7167_MONOMER', 'G7169_MONOMER', 'G7170_MONOMER', 'G7176_MONOMER', 'G7187_MONOMER', 'G7193_MONOMER', 'G7199_MONOMER', 'G7201_MONOMER', 'G7211_MONOMER', 'G7212_MONOMER', 'G7220_MONOMER', 'G7221_MONOMER', 'G7247_MONOMER', 'G7297_MONOMER', 'G7324_MONOMER', 'G7408_MONOMER', 'G7414_MONOMER', 'G7422_MONOMER', 'G7449_MONOMER', 'G7458_MONOMER', 'G7459_MONOMER', 'G7496_MONOMER', 'G7502_MONOMER', 'G7517_MONOMER', 'G7558_MONOMER', 'G7579_MONOMER', 'G7593_MONOMER', 'G7599_MONOMER', 'G7603_MONOMER', 'G7629_MONOMER', 'G7634_MONOMER', 'G7698_MONOMER', 'G7726_MONOMER', 'G7742_MONOMER', 'G7750_MONOMER', 'G7751_MONOMER', 'G7756_MONOMER', 'G7800_MONOMER', 'G7836_MONOMER', 'G7843_MONOMER', 'G7868_MONOMER', 'G7919_MONOMER', 'G7945_MONOMER', 'G7950_MONOMER', 'GALACTARDEHYDRA_MONOMER', 'GALACTOKIN_MONOMER', 'GALACTONATE_DEHYDRATASE_MONOMER', 'GALPMUT_MONOMER', 'GART_MONOMER', 'GARTRANSFORMYL2_MONOMER', 'GCVT_MONOMER', 'GKI_MONOMER', 'GLND_MONOMER', 'GLNE_MONOMER', 'GLNS_MONOMER', 'GLU6PDEHYDROG_MONOMER', 'GLUCARDEHYDRA_MONOMER', 'GLUCDEHYDROG_MONOMER', 'GLUCOKIN_MONOMER', 'GLUCONOKINI_MONOMER', 'GLUCONOLACT_MONOMER', 'GLUCONREDUCT_MONOMER', 'GLURS_MONOMER', 'GLUTAMINESYN_OLIGOMER', 'GLUTCYSLIG_MONOMER', 'GLUTRACE_MONOMER', 'GLYCEROL_3_P_ACYLTRANSFER_MONOMER', 'GLYCOGEN_BRANCH_MONOMER', 'GLYCOGENSYN_MONOMER', 'GLYCPDIESTER_CYTO_MONOMER', 'GLYCRIBONUCSYN_MONOMER', 'GRXB_MONOMER', 'GUANYLCYC_MONOMER', 'H2NEOPTERINP3PYROPHOSPHOHYDRO_MONOMER', 'H2PTERIDINEPYROPHOSPHOKIN_MONOMER', 'HEMEOSYN_MONOMER', 'HEMN_MONOMER', 'HISTCYCLOPRATPPHOS', 'HOMOCYSMET_MONOMER', 'HOMOCYSMETB12_MONOMER', 'HYDGLUTSYN_MONOMER', 'IDONDEHYD_MONOMER', 'ILES_MONOMER', 'IPPISOM_MONOMER', 'ISOCIT_LYASE', 'KDOTRANS_MONOMER', 'KDUD_MONOMER', 'KETOBUTFORMLY_MONOMER', 'L_ASPARTATE_OXID_MONOMER', 'L_LACTDEHYDROGFMN_MONOMER', 'LAUROYLACYLTRAN_MONOMER', 'LEUS_MONOMER', 'MALATE_DEHASE', 'MALATE_SYNTHASE', 'MALONYL_COA_ACP_TRANSACYL_MONOMER', 'MANNKIN_MONOMER', 'MANNONDEHYDRAT_MONOMER', 'MANNONOXIDOREDUCT_MONOMER', 'MANNPDEHYDROG_MONOMER', 'MANNPGUANYLTRANGDP_MONOMER', 'MANNPISOM_MONOMER', 'METHYLGLYREDUCT_MONOMER', 'METHYLMALONYL_COA_EPIM_MONOMER', 'MHPELY_MONOMER', 'MHPHYDROXY_MONOMER', 'MMUM_MONOMER', 'MONOMER0_1041', 'MONOMER0_148', 'MONOMER0_149', 'MONOMER0_2838', 'MONOMER0_702', 'N_ACETYLGLUTPREDUCT_MONOMER', 'NACGLCTRANS_MONOMER', 'NADH_DHII_MONOMER', 'NADNUCLEOSID_MONOMER', 'NANE_MONOMER', 'NANK_MONOMER', 'NAPC_MONOMER', 'NICONUCADENYLYLTRAN_MONOMER', 'NICOTINAMID_MONOMER', 'NICOTINATEPRIBOSYLTRANS_MONOMER', 'NMNNUCLEOSID_MONOMER', 'O_SUCCINYLBENZOATE_COA_SYN_MONOMER', 'OCTAPRENYL_METHOXYPHENOL_OH_MONOMER', 'OCTAPRENYL_METHYL_METHOXY_BENZOQ_OH_MON', 'OHMETHYLBILANESYN_MONOMER', 'PALMITOTRANS_MONOMER', 'PD00230', 'PEPCARBOXYKIN_MONOMER', 'PFLACTENZ_MONOMER', 'PGK', 'PGLUCONDEHYDRAT_MONOMER', 'PGLYCEROLTRANSI_MONOMER', 'PGMI_MONOMER', 'PGPPHOSPHAB_MONOMER', 'PHENPRODIOLDEHYDROG_MONOMER', 'PHOSGLUCOSAMINEMUT_MONOMER', 'PHOSGLYCMUTASE', 'PHOSMANMUT_MONOMER', 'PHOSNACMURPENTATRANS_MONOMER', 'PHOSPHAGLYPSYN_MONOMER', 'PHOSPHO_CHEB', 'PHOSPHOGLUCMUT_MONOMER', 'PPENTOMUT_MONOMER', 'PRAI_IGPS', 'PRIBFAICARPISOM_MONOMER', 'PROPIONYL_COA_CARBOXY_MONOMER', 'PRPPSYN_MONOMER', 'PYRDAMPTRANS_MONOMER', 'PYROXALTRANSAM_MONOMER', 'PYRUFLAVREDUCT_MONOMER', 'RECBCD', 'RED_GLUTAREDOXIN', 'RELA_MONOMER', 'RHAMNULOKIN_MONOMER', 'RIBAZOLEPHOSPHAT_MONOMER', 'RIBF_MONOMER', 'RIBULP3EPIM_MONOMER', 'SARCOX_MONOMER', 'SPOT_MONOMER', 'SUCCCOASYN', 'SUCCGLUALDDEHYD_MONOMER', 'SUCCGLUDESUCC_MONOMER', 'TDPFUCACTRANS_MONOMER', 'TETRAACYLDISACC4KIN_MONOMER', 'THI_P_KIN_MONOMER', 'THIC_MONOMER', 'THIE_MONOMER', 'THIF_MONOMER', 'THIG_MONOMER', 'THIH_MONOMER', 'THII_MONOMER', 'THIKIN_MONOMER', 'THRESYN_MONOMER', 'TORA_MONOMER', 'TPI', 'TRANSALDOLA_MONOMER', 'TRE6PHYDRO_MONOMER', 'TREHALACYTO_MONOMER', 'TREHALOSE6PSYN_MONOMER', 'TREHALOSEPHOSPHASYN_MONOMER', 'TRYPSYN', 'TRYPSYN_APROTEIN', 'TSA_REDUCT_MONOMER', 'UBIX_MONOMER', 'UDK_MONOMER', 'UDP_NACMURALA_GLU_LIG_MONOMER', 'UDP_NACMURALGLDAPAALIG_MONOMER', 'UDP_NACMURALGLDAPLIG_MONOMER', 'UDPACYLGLCNACDEACETYL_MONOMER', 'UDPMANACATRANS_MONOMER', 'UDPNACETYLGLUCOSAMENOLPYRTRANS_MONOMER', 'UDPNACETYLMURAMATEDEHYDROG_MONOMER', 'UROGENDECARBOX_MONOMER', 'UROGENIIISYN_MONOMER', 'USHA_MONOMER', 'UXAC_MONOMER', 'VALINE_PYRUVATE_AMINOTRANSFER_MONOMER', 'VALS_MONOMER', 'YDCS_MONOMER', '_1_PFK', '_2_DEHYDROPANTOATE_REDUCT_MONOMER', '_2_ISOPROPYLMALATESYN_MONOMER', '_2_OCTAPRENYL_METHOXY_BENZOQ_METH_MONOMER', '_4OHBENZOATE_OCTAPRENYLTRANSFER_MONOMER', '_6PFK_1_CPX', '_6PFK_2_CPX', '_6PGLUCONOLACT_MONOMER' ],
	'loc' : ['cyt', 'cytosk', 'ex', 'mem', 'per', 'wall', 'bnuc', 'cproj', 'imem', 'omem', 'pmem'],
	'strain' : ['ecoli']})
Monomer('cplx',
	['name', 'loc', 'dna', 'met', 'prot', 'rna', 'up', 'dw'],
	{ 'name' : [ 'ACECITLY_CPLX', 'ACETOACETYL_COA_TRANSFER_CPLX', 'ACETOLACTSYNI_CPLX', 'ACETYL_COA_ACETYLTRANSFER_CPLX', 'ACETYL_COA_CARBOXYLTRANSFER_CPLX', 'ACETYLGLUTKIN_CPLX', 'ACETYLORNDEACET_CPLX', 'ACETYLORNTRANSAM_CPLX', 'ACNEULY_CPLX', 'ACSERLYA_CPLX', 'ACSERLYB_CPLX', 'ACYLCOASYN_CPLX', 'ADCLY_CPLX', 'ADENPRIBOSYLTRAN_CPLX', 'ADENYLOSUCCINATE_SYN_DIMER', 'ADENYLYLSULFKIN_CPLX', 'ADHC_CPLX', 'ADHE_CPLX', 'AERGLYC3PDEHYDROG_CPLX', 'AGMATIN_CPLX', 'AICARTRANSIMPCYCLO_CPLX', 'AIRS_CPLX', 'AKBLIG_CPLX', 'ALAS_CPLX', 'ALD_CPLX', 'ALKAPHOSPHA_CPLX', 'ALPHAGALACTOSID_CPLX', 'AMINEOXID_CPLX', 'AMP_NUCLEOSID_CPLX', 'ANGLYC3PDEHYDROG_CPLX', 'ANSA_CPLX', 'ANTHRANSYN_CPLX', 'APHA_CPLX', 'APORNAP_CPLX', 'APP_UBIOX_CPLX', 'ARABISOM_CPLX', 'ARGDECARBOXBIO_CPLX', 'AROC_CPLX', 'AROD_CPLX', 'AROF_CPLX', 'ASNS_CPLX', 'ASNSYNA_CPLX', 'ASNSYNB_CPLX', 'ASP_SEMIALDEHYDE_DEHYDROGENASE_CPLX', 'ASPAMINOTRANS_DIMER', 'ASPARTASE_CPLX', 'ASPCARBTRANS_CPLX', 'ASPKINIHOMOSERDEHYDROGI_CPLX', 'ASPS_CPLX', 'BADH_CPLX', 'BETAGALACTOSID_CPLX', 'BIOTIN_CARBOXYL_CPLX', 'BIOTIN_SYN_CPLX', 'BRANCHED_CHAINAMINOTRANSFER_CPLX', 'CARBODEHYDRAT_CPLX', 'CARBPSYN_CPLX', 'CARNDEHYDRA_CPLX', 'CFA_CPLX', 'CHEZ_CPLX', 'CHORISMUTPREPHENDEHYDRAT_CPLX', 'CHORISMUTPREPHENDEHYDROG_CPLX', 'COADTRI_CPLX', 'COBU_CPLX', 'CPLX_171', 'CPLX_3942', 'CPLX_3946', 'CPLX_64', 'CPLX_722', 'CPLX_7524', 'CPLX_8331', 'CPLX_8401', 'CPLX0_1021', 'CPLX0_1101', 'CPLX0_1121', 'CPLX0_1141', 'CPLX0_1142', 'CPLX0_1163', 'CPLX0_1221', 'CPLX0_1261', 'CPLX0_1262', 'CPLX0_1382', 'CPLX0_1401', 'CPLX0_1421', 'CPLX0_1541', 'CPLX0_1581', 'CPLX0_1601', 'CPLX0_1621', 'CPLX0_1683', 'CPLX0_1762', 'CPLX0_1821', 'CPLX0_1962', 'CPLX0_201', 'CPLX0_2061', 'CPLX0_224', 'CPLX0_225', 'CPLX0_227', 'CPLX0_229', 'CPLX0_230', 'CPLX0_234', 'CPLX0_235', 'CPLX0_236', 'CPLX0_237', 'CPLX0_238', 'CPLX0_240', 'CPLX0_2401', 'CPLX0_242', 'CPLX0_2425', 'CPLX0_244', 'CPLX0_245', 'CPLX0_246', 'CPLX0_248', 'CPLX0_250', 'CPLX0_2502', 'CPLX0_251', 'CPLX0_252', 'CPLX0_253', 'CPLX0_254', 'CPLX0_255', 'CPLX0_263', 'CPLX0_2661', 'CPLX0_2881', 'CPLX0_2901', 'CPLX0_2921', 'CPLX0_2941', 'CPLX0_2982', 'CPLX0_3001', 'CPLX0_301', 'CPLX0_3041', 'CPLX0_3061', 'CPLX0_3081', 'CPLX0_3101', 'CPLX0_3121', 'CPLX0_3161', 'CPLX0_3181', 'CPLX0_3201', 'CPLX0_321', 'CPLX0_322', 'CPLX0_3241', 'CPLX0_3281', 'CPLX0_341', 'CPLX0_3461', 'CPLX0_3482', 'CPLX0_3501', 'CPLX0_3521', 'CPLX0_3541', 'CPLX0_3581', 'CPLX0_3601', 'CPLX0_3602', 'CPLX0_3621', 'CPLX0_3661', 'CPLX0_3681', 'CPLX0_3721', 'CPLX0_3741', 'CPLX0_3841', 'CPLX0_3861', 'CPLX0_3881', 'CPLX0_3901', 'CPLX0_3924', 'CPLX0_3925', 'CPLX0_3927', 'CPLX0_3931', 'CPLX0_3936', 'CPLX0_3941', 'CPLX0_3943', 'CPLX0_3948', 'CPLX0_3950', 'CPLX0_3951', 'CPLX0_3952', 'CPLX0_3954', 'CPLX0_3957', 'CPLX0_3958', 'CPLX0_3961', 'CPLX0_3969', 'CPLX0_3971', 'CPLX0_682', 'CPLX0_721', 'CPLX0_7415', 'CPLX0_7420', 'CPLX0_7421', 'CPLX0_7423', 'CPLX0_7426', 'CPLX0_743', 'CPLX0_7458', 'CPLX0_7462', 'CPLX0_7465', 'CPLX0_7466', 'CPLX0_7525', 'CPLX0_7564', 'CPLX0_7609', 'CPLX0_761', 'CPLX0_7614', 'CPLX0_7615', 'CPLX0_7616', 'CPLX0_7622', 'CPLX0_7625', 'CPLX0_7630', 'CPLX0_7631', 'CPLX0_7633', 'CPLX0_7643', 'CPLX0_7645', 'CPLX0_7646', 'CPLX0_7647', 'CPLX0_7649', 'CPLX0_7652', 'CPLX0_7658', 'CPLX0_7659', 'CPLX0_7660', 'CPLX0_7662', 'CPLX0_7667', 'CPLX0_7683', 'CPLX0_7685', 'CPLX0_7688', 'CPLX0_7691', 'CPLX0_7692', 'CPLX0_7693', 'CPLX0_7709', 'CPLX0_7712', 'CPLX0_7718', 'CPLX0_7719', 'CPLX0_7722', 'CPLX0_7723', 'CPLX0_7725', 'CPLX0_7726', 'CPLX0_7727', 'CPLX0_7728', 'CPLX0_7732', 'CPLX0_7741', 'CPLX0_7744', 'CPLX0_7747', 'CPLX0_7755', 'CPLX0_7758', 'CPLX0_7760', 'CPLX0_7761', 'CPLX0_7766', 'CPLX0_7788', 'CPLX0_7794', 'CPLX0_7802', 'CPLX0_7805', 'CPLX0_7806', 'CPLX0_7808', 'CPLX0_7810', 'CPLX0_7811', 'CPLX0_782', 'CPLX0_7820', 'CPLX0_7826', 'CPLX0_7841', 'CPLX0_7844', 'CPLX0_7847', 'CPLX0_7848', 'CPLX0_7877', 'CPLX0_7878', 'CPLX0_7882', 'CPLX0_7885', 'CPLX0_7887', 'CPLX0_7904', 'CPLX0_7912', 'CPLX0_7913', 'CPLX0_7927', 'CPLX0_7932', 'CPLX0_7936', 'CPLX0_7940', 'CPLX0_7944', 'CPLX0_7946', 'CPLX0_7947', 'CPLX0_7950', 'CPLX0_7951', 'CPLX0_7957', 'CPLX0_7958', 'CPLX0_7959', 'CPLX0_7960', 'CPLX0_7962', 'CPLX0_7974', 'CPLX0_7975', 'CPLX0_7977', 'CPLX0_7979', 'CPLX0_7984', 'CPLX0_7989', 'CPLX0_7990', 'CPLX0_7993', 'CPLX0_7994', 'CPLX0_7997', 'CPLX0_8005', 'CPLX0_8006', 'CPLX0_8008', 'CPLX0_8010', 'CPLX0_8011', 'CPLX0_8012', 'CPLX0_8013', 'CPLX0_8014', 'CPLX0_8015', 'CPLX0_8016', 'CPLX0_8031', 'CPLX0_8032', 'CPLX0_8033', 'CPLX0_8045', 'CPLX0_8092', 'CPLX0_8095', 'CPLX0_8098', 'CPLX0_8106', 'CPLX0_8109', 'CPLX0_8112', 'CPLX0_8121', 'CPLX0_8122', 'CPLX0_8123', 'CPLX0_8124', 'CPLX0_8125', 'CPLX0_8127', 'CPLX0_8128', 'CPLX0_8156', 'CPLX0_8158', 'CPLX0_8159', 'CPLX0_8160', 'CPLX0_8163', 'CPLX0_8164', 'CPLX0_8167', 'CPLX0_8176', 'CPLX0_8182', 'CPLX0_8183', 'CPLX0_8186', 'CPLX0_8189', 'CPLX0_8190', 'CPLX0_8191', 'CPLX0_8205', 'CPLX0_821', 'CPLX0_8211', 'CPLX0_8212', 'CPLX0_8213', 'CPLX0_8214', 'CPLX0_8217', 'CPLX0_8228', 'CPLX0_8231', 'CPLX0_8232', 'CPLX0_8233', 'CPLX0_8238', 'CPLX0_8249', 'CPLX0_8251', 'CPLX0_8252', 'CPLX0_8254', 'CPLX0_8260', 'CPLX0_8261', 'CPLX0_8262', 'CPLX0_8270', 'CPLX0_861', 'CPLX0_901', 'CPLXECOLI_7943', 'CTPSYN_CPLX', 'CYANLY_CPLX', 'CYT_D_UBIOX_CPLX', 'CYT_O_UBIOX_CPLX', 'CYTIDEAM_CPLX', 'DALADEHYDROG_CPLX', 'DAPASYN_CPLX', 'DCTP_DEAM_CPLX', 'DCYSDESULF_CPLX', 'DEOA_CPLX', 'DEOD_CPLX', 'DETHIOBIOTIN_SYN_CPLX', 'DGTPTRIPHYDRO_CPLX', 'DHHB_METHYLTRANSFER_CPLX', 'DHPDIOXYGEN_CPLX', 'DIACYLGLYKIN_CPLX', 'DIAMINOPIMDECARB_CPLX', 'DIHYDRODIPICSYN_CPLX', 'DIHYDROOROT_CPLX', 'DIHYDROPICRED_CPLX', 'DIHYDROPTERIREDUCT_CPLX', 'DIHYDROXYACIDDEHYDRAT_CPLX', 'DIMESULFREDUCT_CPLX', 'DIOHBUTANONEPSYN_CPLX', 'DMBPPRIBOSYLTRANS_CPLX', 'DSBC_CPLX', 'DTDPGLUCDEHYDRAT_CPLX', 'DUTP_PYROP_CPLX', 'DXPREDISOM_CPLX', 'E1P_CPLX', 'E3_CPLX', 'ENOLASE_CPLX', 'ENTA_CPLX', 'ENTB_CPLX', 'ENTE_CPLX', 'ENTMULTI_CPLX', 'ERYTH4PDEHYDROG_CPLX', 'ETHAMLY_CPLX', 'FABA_CPLX', 'FABB_CPLX', 'FABZ_CPLX', 'FADA_CPLX', 'FADB_CPLX', 'FHLMULTI_CPLX', 'FOLD_CPLX', 'FOLE_CPLX', 'FOLXTET_CPLX', 'FORMATEDEHYDROGN_CPLX', 'FORMYLTHFDEFORMYL_CPLX', 'GALACTOACETYLTRAN_CPLX', 'GALACTURIDYLYLTRANS_CPLX', 'GAPDH_A_CPLX', 'GCVMULTI_CPLX', 'GCVP_CPLX', 'GDHA_CPLX', 'GDPMANDEHYDRA_CPLX', 'GLUC1PADENYLTRANS_CPLX', 'GLUCOSAMINE_6_P_DEAMIN_CPLX', 'GLUCOSE_1_PHOSPHAT_CPLX', 'GLUTAMATESYN_CPLX', 'GLUTAMIDOTRANS_CPLX', 'GLUTATHIONE_REDUCT_NADPH_CPLX', 'GLUTATHIONE_SYN_CPLX', 'GLUTDECARBOXA_CPLX', 'GLUTKIN_CPLX', 'GLUTSEMIALDEHYDROG_CPLX', 'GLYC3PDEHYDROGBIOSYN_CPLX', 'GLYCDEH_CPLX', 'GLYCEROL_KIN_CPLX', 'GLYCOPHOSPHORYL_CPLX', 'GLYOCARBOLIG_CPLX', 'GLYOHMETRANS_CPLX', 'GLYOXI_CPLX', 'GLYS_CPLX', 'GMP_REDUCT_CPLX', 'GMP_SYN_CPLX', 'GPT_CPLX', 'GSAAMINOTRANS_CPLX', 'GSP_CPLX', 'GTP_CYCLOHYDRO_II_CPLX', 'GUANYL_KIN_CPLX', 'H2PTEROATESYNTH_CPLX', 'HCAMULTI_CPLX', 'HISS_CPLX', 'HISTDEHYD_CPLX', 'HISTPHOSTRANS_CPLX', 'HMP_P_KIN_CPLX', 'HOMOSERKIN_CPLX', 'HOMSUCTRAN_CPLX', 'HYDROG3_CPLX', 'HYDROPEROXIDI_CPLX', 'HYDROPEROXIDII_CPLX', 'IMIDHISTID_CPLX', 'IMP_DEHYDROG_CPLX', 'ISOCITHASE_CPLX', 'KDO_8PPHOSPHAT_CPLX', 'KDO_8PSYNTH_CPLX', 'KDPGALDOL_4OH2OXOGLUTARALDOL_CPLX', 'L_GLN_FRUCT_6_P_AMINOTRANS_CPLX', 'LACTALDREDUCT_CPLX', 'LDC2_CPLX', 'LTAA_CPLX', 'LTARTDEHYDRA_CPLX', 'LUMAZINESYN_CPLX', 'LYSS_CPLX', 'LYSU_CPLX', 'LYXK_CPLX', 'MALDEXPHOSPHORYL_CPLX', 'MALIC_NAD_CPLX', 'MALIC_NADP_CPLX', 'MALTACETYLTRAN_CPLX', 'MENE_CPLX', 'METG_CPLX', 'METHGLYSYN_CPLX', 'METHYLENETHFREDUCT_CPLX', 'MUTHLS_CPLX', 'N_ACETYLTRANSFER_CPLX', 'NAD_SYNTH_CPLX', 'NADH_DHI_CPLX', 'NAG1P_URIDYLTRANS_CPLX', 'NAG6PDEACET_CPLX', 'NAP_CPLX', 'NARX_CPLX', 'NITRATREDUCTA_CPLX', 'NITRITREDUCT_CPLX', 'NQOR_CPLX', 'NUCLEOSIDE_DIP_KIN_CPLX', 'O_SUCCHOMOSERLYASE_CPLX', 'ORNCARBAMTRANSFERF_CPLX', 'ORNDECARBOX_BIO_CPLX', 'OROPRIBTRANS_CPLX', 'OROTPDECARB_CPLX', 'PABASYN_CPLX', 'PANTOATE_BETA_ALANINE_LIG_CPLX', 'PANTOTHENATE_KIN_CPLX', 'PAPSSULFOTRANS_CPLX', 'PDXH_CPLX', 'PDXK_CPLX', 'PEPCARBOX_CPLX', 'PEPSYNTH_CPLX', 'PGLYCDEHYDROG_CPLX', 'PHENDEHYD_CPLX', 'PHES_CPLX', 'PHOSACETYLTRANS_CPLX', 'PHOSPHASERDECARB_DIMER', 'PHOSPHASERSYN_CPLX', 'PKI_COMPLEX', 'PORPHOBILSYNTH_CPLX', 'PPK_CPLX', 'PPPGPPHYDRO_CPLX', 'PPX_CPLX', 'PROS_CPLX', 'PRPPAMIDOTRANS_CPLX', 'PSERTRANSAM_CPLX', 'PURE_CPLX', 'PURK_CPLX', 'PUTA_CPLX', 'PYRROLINECARBREDUCT_CPLX', 'PYRUVATEDEH_CPLX', 'PYRUVOXID_CPLX', 'QOR_CPLX', 'QUINOPRIBOTRANS_CPLX', 'RECFOR_CPLX', 'RHAMNULPALDOL_CPLX', 'RIB5PISOMA_CPLX', 'RIB5PISOMB_CPLX', 'RIBONUCLEOSIDE_DIP_REDUCTI_CPLX', 'RIBONUCLEOSIDE_DIP_REDUCTII_CPLX', 'RIBONUCLEOSIDE_TRIP_REDUCT_CPLX', 'RIBULOKIN_CPLX', 'RUVABC_CPLX', 'S_ADENMETSYN_CPLX', 'SAICARSYN_CPLX', 'SAMDECARB_CPLX', 'SERS_CPLX', 'SIROHEMESYN_CPLX', 'SORB6PDEHYDROG_CPLX', 'SPERMACTRAN_CPLX', 'SPERMIDINESYN_CPLX', 'SUCCORNTRANSAM_CPLX', 'SULFATE_ADENYLYLTRANS_CPLX', 'SULFITE_REDUCT_CPLX', 'THIOESTERII_CPLX', 'THIOREDOXIN_REDUCT_NADPH_CPLX', 'THREDEHYDCAT_CPLX', 'THRS_CPLX', 'THYMIDYLATESYN_CPLX', 'TMAOREDUCTI_CPLX', 'TRANSENOYLCOARED_CPLX', 'TRPS_CPLX', 'TRYPTOPHAN_CPLX', 'TYRB_DIMER', 'TYRS_CPLX', 'UDHA_CPLX', 'UDPGLUCEPIM_CPLX', 'UDPNACETYLGLUCOSAMACYLTRANS_CPLX', 'UMPKI_CPLX', 'UPPSYN_CPLX', 'URACIL_PRIBOSYLTRANS_CPLX', 'UVRABC_CPLX', 'XANTHOSINEPHOSPHORY_CPLX', 'XYLISOM_CPLX', '_2OXOGLUTARATEDEH_CPLX', '_3_ISOPROPYLMALDEHYDROG_CPLX', '_3_ISOPROPYLMALISOM_CPLX', '_3_METHYL_2_OXOBUT_OHCH3XFER_CPLX', '_3_OXOACYL_ACP_SYNTHII_CPLX', '_6PGLUCONDEHYDROG_CPLX', '_7_ALPHA_HYDROXYSTEROID_DEH_CPLX', '_7KAPSYN_CPLX' ],
	'loc' : ['cyt', 'cytosk', 'ex', 'mem', 'per', 'wall', 'bnuc', 'cproj', 'imem', 'omem', 'pmem'],
	'strain' : ['ecoli']})
Rule('_1PFRUCTPHOSN_RXN',
	prot(name = '_1_PFK', loc = 'cyt') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FRU1P', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = '_1_PFK', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FRUCTOSE_16_DIPHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__1PFRUCTPHOSN_RXN', 1.000000), 
	Parameter('rvs__1PFRUCTPHOSN_RXN', 0.000000))
Rule('_2_DEHYDROPANTOATE_REDUCT_RXN',
	prot(name = '_2_DEHYDROPANTOATE_REDUCT_MONOMER', loc = 'cyt') +
	met(name = 'L_PANTOATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = '_2_DEHYDROPANTOATE_REDUCT_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_DEHYDROPANTOATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__2_DEHYDROPANTOATE_REDUCT_RXN', 0.000000), 
	Parameter('rvs__2_DEHYDROPANTOATE_REDUCT_RXN', 1.000000))
Rule('_2_ISOPROPYLMALATESYN_RXN',
	prot(name = '_2_ISOPROPYLMALATESYN_MONOMER', loc = 'cyt') +
	met(name = '_2_KETO_ISOVALERATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = '_2_ISOPROPYLMALATESYN_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_3_CARBOXY_3_HYDROXY_ISOCAPROATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__2_ISOPROPYLMALATESYN_RXN', 1.000000), 
	Parameter('rvs__2_ISOPROPYLMALATESYN_RXN', 0.000000))
Rule('ADOMET_DMK_METHYLTRANSFER_RXN',
	prot(name = '_2_OCTAPRENYL_METHOXY_BENZOQ_METH_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_12115', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = '_2_OCTAPRENYL_METHOXY_BENZOQ_METH_MONOMER', loc = 'cyt') +
	met(name = 'REDUCED_MENAQUINONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ADOMET_DMK_METHYLTRANSFER_RXN', 1.000000), 
	Parameter('rvs_ADOMET_DMK_METHYLTRANSFER_RXN', 0.000000))
Rule('_2_OCTAPRENYL_METHOXY_BENZOQ_METH_RXN',
	prot(name = '_2_OCTAPRENYL_METHOXY_BENZOQ_METH_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OCTAPRENYL_METHOXY_BENZOQUINONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = '_2_OCTAPRENYL_METHOXY_BENZOQ_METH_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OCTAPRENYL_METHYL_METHOXY_BENZQ', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__2_OCTAPRENYL_METHOXY_BENZOQ_METH_RXN', 1.000000), 
	Parameter('rvs__2_OCTAPRENYL_METHOXY_BENZOQ_METH_RXN', 0.000000))
Rule('_2OXOGLUTARATEDEH_RXN',
	cplx(name = '_2OXOGLUTARATEDEH_CPLX', loc = 'cyt') +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = '_2OXOGLUTARATEDEH_CPLX', loc = 'cyt') +
	met(name = 'SUC_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__2OXOGLUTARATEDEH_RXN', 1.000000), 
	Parameter('rvs__2OXOGLUTARATEDEH_RXN', 0.000000))
Rule('RXN_13158',
	cplx(name = '_3_ISOPROPYLMALDEHYDROG_CPLX', loc = 'cyt') +
	met(name = '_2_D_THREO_HYDROXY_3_CARBOXY_ISOCAPROATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = '_3_ISOPROPYLMALDEHYDROG_CPLX', loc = 'cyt') +
	met(name = '_2K_4CH3_PENTANOATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_13158', 1.000000), 
	Parameter('rvs_RXN_13158', 0.000000))
Rule('RXN_13163',
	cplx(name = '_3_ISOPROPYLMALISOM_CPLX', loc = 'cyt') +
	met(name = '_2_D_THREO_HYDROXY_3_CARBOXY_ISOCAPROATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = '_3_ISOPROPYLMALISOM_CPLX', loc = 'cyt') +
	met(name = '_3_CARBOXY_3_HYDROXY_ISOCAPROATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_13163', 1.000000), 
	Parameter('rvs_RXN_13163', 1.000000))
Rule('_3_CH3_2_OXOBUTANOATE_OH_CH3_XFER_RXN',
	cplx(name = '_3_METHYL_2_OXOBUT_OHCH3XFER_CPLX', loc = 'cyt') +
	met(name = 'METHYLENE_THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_KETO_ISOVALERATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = '_3_METHYL_2_OXOBUT_OHCH3XFER_CPLX', loc = 'cyt') +
	met(name = '_2_DEHYDROPANTOATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd__3_CH3_2_OXOBUTANOATE_OH_CH3_XFER_RXN', 1.000000), 
	Parameter('rvs__3_CH3_2_OXOBUTANOATE_OH_CH3_XFER_RXN', 1.000000))
Rule('_2dot3dot1dot179_RXN',
	cplx(name = '_3_OXOACYL_ACP_SYNTHII_CPLX', loc = 'cyt') +
	met(name = 'Palmitoleoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MALONYL_ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = '_3_OXOACYL_ACP_SYNTHII_CPLX', loc = 'cyt') +
	met(name = '_3_oxo_cis_vaccenoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__2dot3dot1dot179_RXN', 1.000000), 
	Parameter('rvs__2dot3dot1dot179_RXN', 0.000000))
Rule('_3_OXOACYL_ACP_SYNTH_BASE_RXN',
	cplx(name = '_3_OXOACYL_ACP_SYNTHII_CPLX', loc = 'cyt') +
	met(name = 'MALONYL_ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETYL_ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = '_3_OXOACYL_ACP_SYNTHII_CPLX', loc = 'cyt') +
	met(name = 'ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Acetoacetyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3_OXOACYL_ACP_SYNTH_BASE_RXN', 1.000000), 
	Parameter('rvs__3_OXOACYL_ACP_SYNTH_BASE_RXN', 0.000000))
Rule('_3_OXOACYL_ACP_SYNTH_RXN',
	cplx(name = '_3_OXOACYL_ACP_SYNTHII_CPLX', loc = 'cyt') +
	met(name = 'MALONYL_ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Saturated_Fatty_Acyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = '_3_OXOACYL_ACP_SYNTHII_CPLX', loc = 'cyt') +
	met(name = 'ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'B_KETOACYL_ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3_OXOACYL_ACP_SYNTH_RXN', 1.000000), 
	Parameter('rvs__3_OXOACYL_ACP_SYNTH_RXN', 0.000000))
Rule('_4OHBENZOATE_OCTAPRENYLTRANSFER_RXN',
	prot(name = '_4OHBENZOATE_OCTAPRENYLTRANSFER_MONOMER', loc = 'imem') +
	met(name = 'OCTAPRENYL_DIPHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_4_hydroxybenzoate', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = '_4OHBENZOATE_OCTAPRENYLTRANSFER_MONOMER', loc = 'imem') +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_3_OCTAPRENYL_4_HYDROXYBENZOATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__4OHBENZOATE_OCTAPRENYLTRANSFER_RXN', 1.000000), 
	Parameter('rvs__4OHBENZOATE_OCTAPRENYLTRANSFER_RXN', 0.000000))
Rule('RXN0_6541',
	prot(name = '_6PFK_1_CPX', loc = 'cyt') +
	met(name = 'D_SEDOHEPTULOSE_7_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = '_6PFK_1_CPX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_SEDOHEPTULOSE_1_7_P2', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6541', 1.000000), 
	Parameter('rvs_RXN0_6541', 0.000000))
Rule('_6PFRUCTPHOS_RXN',
	prot(name = '_6PFK_1_CPX', loc = 'cyt') +
	met(name = 'FRUCTOSE_6P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = '_6PFK_1_CPX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FRUCTOSE_16_DIPHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__6PFRUCTPHOS_RXN', 1.000000), 
	Parameter('rvs__6PFRUCTPHOS_RXN', 0.000000))
Rule('TAGAKIN_RXN',
	prot(name = '_6PFK_2_CPX', loc = 'cyt') +
	met(name = 'TAGATOSE_6_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = '_6PFK_2_CPX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TAGATOSE_1_6_DIPHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_TAGAKIN_RXN', 1.000000), 
	Parameter('rvs_TAGAKIN_RXN', 0.000000))
Rule('RXN_9952',
	cplx(name = '_6PGLUCONDEHYDROG_CPLX', loc = 'cyt') +
	met(name = 'CPD_2961', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = '_6PGLUCONDEHYDROG_CPLX', loc = 'cyt') +
	met(name = 'RIBULOSE_5P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_9952', 1.000000), 
	Parameter('rvs_RXN_9952', 0.000000))
Rule('_6PGLUCONOLACT_RXN',
	prot(name = '_6PGLUCONOLACT_MONOMER', loc = 'cyt') +
	met(name = 'D_6_P_GLUCONO_DELTA_LACTONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = '_6PGLUCONOLACT_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_2961', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__6PGLUCONOLACT_RXN', 1.000000), 
	Parameter('rvs__6PGLUCONOLACT_RXN', 0.000000))
Rule('_7_ALPHA_HYDROXYSTEROID_DEH_RXN',
	cplx(name = '_7_ALPHA_HYDROXYSTEROID_DEH_CPLX', loc = 'cyt') +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CHOLATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = '_7_ALPHA_HYDROXYSTEROID_DEH_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CHOLANATE2', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__7_ALPHA_HYDROXYSTEROID_DEH_RXN', 1.000000), 
	Parameter('rvs__7_ALPHA_HYDROXYSTEROID_DEH_RXN', 0.000000))
Rule('RXN_11484',
	cplx(name = '_7KAPSYN_CPLX', loc = 'cyt') +
	met(name = 'Pimeloyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_ALPHA_ALANINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = '_7KAPSYN_CPLX', loc = 'cyt') +
	met(name = '_8_AMINO_7_OXONONANOATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11484', 1.000000), 
	Parameter('rvs_RXN_11484', 0.000000))
Rule('_7KAPSYN_RXN',
	cplx(name = '_7KAPSYN_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_ALPHA_ALANINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_558', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = '_7KAPSYN_CPLX', loc = 'cyt') +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_8_AMINO_7_OXONONANOATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__7KAPSYN_RXN', 1.000000), 
	Parameter('rvs__7KAPSYN_RXN', 0.000000))
Rule('RXN_5741',
	prot(name = 'AAS_MONOMER', loc = 'imem') +
	met(name = 'CPD_195', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'AAS_MONOMER', loc = 'imem') +
	met(name = 'Octanoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_5741', 1.000000), 
	Parameter('rvs_RXN_5741', 0.000000))
Rule('ACYLGPEACYLTRANS_RXN',
	prot(name = 'AAS_MONOMER', loc = 'imem') +
	met(name = 'ACYL_ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_ACYL_GPE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'AAS_MONOMER', loc = 'imem') +
	met(name = 'ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_1_PHOSPHATIDYL_ETHANOLAMINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ACYLGPEACYLTRANS_RXN', 1.000000), 
	Parameter('rvs_ACYLGPEACYLTRANS_RXN', 1.000000))
Rule('RXN0_5513',
	prot(name = 'AAS_MONOMER', loc = 'imem') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD66_39', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'AAS_MONOMER', loc = 'imem') +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Saturated_Fatty_Acyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5513', 1.000000), 
	Parameter('rvs_RXN0_5513', 0.000000))
Rule('CITLY_RXN',
	cplx(name = 'ACECITLY_CPLX', loc = 'cyt') +
	met(name = 'CIT', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'ACECITLY_CPLX', loc = 'cyt') +
	met(name = 'ACET', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXALACETIC_ACID', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_CITLY_RXN', 1.000000), 
	Parameter('rvs_CITLY_RXN', 0.000000))
Rule('CITTRANS_RXN',
	cplx(name = 'ACECITLY_CPLX', loc = 'cyt') +
	met(name = 'CIT', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CITRATE_LYASE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ACECITLY_CPLX', loc = 'cyt') +
	met(name = 'Citrate_Lyase_Citryl_Form', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACET', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_CITTRANS_RXN', 1.000000), 
	Parameter('rvs_CITTRANS_RXN', 0.000000))
Rule('CITRYLY_RXN',
	cplx(name = 'ACECITLY_CPLX', loc = 'cyt') +
	met(name = 'Citrate_Lyase_Citryl_Form', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	cplx(name = 'ACECITLY_CPLX', loc = 'cyt') +
	met(name = 'OXALACETIC_ACID', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CITRATE_LYASE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_CITRYLY_RXN', 1.000000), 
	Parameter('rvs_CITRYLY_RXN', 0.000000))
Rule('ACECOATRANS_RXN',
	prot(name = 'ACECOATRANS_MONOMER', loc = 'cyt') +
	met(name = 'Saturated_Fatty_Acyl_CoA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACET', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'ACECOATRANS_MONOMER', loc = 'cyt') +
	met(name = 'CPD66_39', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ACECOATRANS_RXN', 1.000000), 
	Parameter('rvs_ACECOATRANS_RXN', 0.000000))
Rule('ACETATEKIN_RXN',
	prot(name = 'ACETATEKINA_MONOMER', loc = 'cyt') +
	met(name = 'ACET', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'ACETATEKINA_MONOMER', loc = 'cyt') +
	met(name = 'ACETYL_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ACETATEKIN_RXN', 1.000000), 
	Parameter('rvs_ACETATEKIN_RXN', 1.000000))
Rule('PROPKIN_RXN',
	prot(name = 'ACETATEKINA_MONOMER', loc = 'cyt') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROPIONATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'ACETATEKINA_MONOMER', loc = 'cyt') +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROPIONYL_P', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PROPKIN_RXN', 1.000000), 
	Parameter('rvs_PROPKIN_RXN', 1.000000))
Rule('ACETOACETYL_COA_TRANSFER_RXN',
	cplx(name = 'ACETOACETYL_COA_TRANSFER_CPLX', loc = 'cyt') +
	met(name = '_3_KETOBUTYRATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ACETOACETYL_COA_TRANSFER_CPLX', loc = 'cyt') +
	met(name = 'ACETOACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACET', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ACETOACETYL_COA_TRANSFER_RXN', 1.000000), 
	Parameter('rvs_ACETOACETYL_COA_TRANSFER_RXN', 1.000000))
Rule('ACETOOHBUTSYN_RXN',
	cplx(name = 'ACETOLACTSYNI_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_OXOBUTANOATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ACETOLACTSYNI_CPLX', loc = 'cyt') +
	met(name = '_2_ACETO_2_HYDROXY_BUTYRATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_ACETOOHBUTSYN_RXN', 1.000000), 
	Parameter('rvs_ACETOOHBUTSYN_RXN', 0.000000))
Rule('ACETOLACTSYN_RXN',
	cplx(name = 'ACETOLACTSYNI_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ACETOLACTSYNI_CPLX', loc = 'cyt') +
	met(name = '_2_ACETO_LACTATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ACETOLACTSYN_RXN', 1.000000), 
	Parameter('rvs_ACETOLACTSYN_RXN', 0.000000))
Rule('ACETYL_COA_ACETYLTRANSFER_RXN',
	cplx(name = 'ACETYL_COA_ACETYLTRANSFER_CPLX', loc = 'cyt') +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'ACETYL_COA_ACETYLTRANSFER_CPLX', loc = 'cyt') +
	met(name = 'ACETOACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ACETYL_COA_ACETYLTRANSFER_RXN', 1.000000), 
	Parameter('rvs_ACETYL_COA_ACETYLTRANSFER_RXN', 1.000000))
Rule('RXN0_5055',
	cplx(name = 'ACETYL_COA_CARBOXYLTRANSFER_CPLX', loc = 'cyt') +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'carboxybiotin_L_lysine_in_BCCP_dimers', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ACETYL_COA_CARBOXYLTRANSFER_CPLX', loc = 'cyt') +
	met(name = 'MALONYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'biotin_L_lysine_in_BCCP_dimers', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5055', 1.000000), 
	Parameter('rvs_RXN0_5055', 0.000000))
Rule('ACETYLGLUTKIN_RXN',
	cplx(name = 'ACETYLGLUTKIN_CPLX', loc = 'cyt') +
	met(name = 'ACETYL_GLU', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ACETYLGLUTKIN_CPLX', loc = 'cyt') +
	met(name = 'N_ACETYL_GLUTAMYL_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ACETYLGLUTKIN_RXN', 1.000000), 
	Parameter('rvs_ACETYLGLUTKIN_RXN', 0.000000))
Rule('ACETYLORNDEACET_RXN',
	cplx(name = 'ACETYLORNDEACET_CPLX', loc = 'cyt') +
	met(name = 'N_ALPHA_ACETYLORNITHINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ACETYLORNDEACET_CPLX', loc = 'cyt') +
	met(name = 'L_ORNITHINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACET', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ACETYLORNDEACET_RXN', 1.000000), 
	Parameter('rvs_ACETYLORNDEACET_RXN', 0.000000))
Rule('ACETYLORNTRANSAM_RXN',
	cplx(name = 'ACETYLORNTRANSAM_CPLX', loc = 'cyt') +
	met(name = 'N_ALPHA_ACETYLORNITHINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ACETYLORNTRANSAM_CPLX', loc = 'cyt') +
	met(name = 'CPD_469', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ACETYLORNTRANSAM_RXN', 0.000000), 
	Parameter('rvs_ACETYLORNTRANSAM_RXN', 1.000000))
Rule('SUCCINYLDIAMINOPIMTRANS_RXN',
	cplx(name = 'ACETYLORNTRANSAM_CPLX', loc = 'cyt') +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'N_SUCCINYLLL_2_6_DIAMINOPIMELATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ACETYLORNTRANSAM_CPLX', loc = 'cyt') +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'N_SUCCINYL_2_AMINO_6_KETOPIMELATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_SUCCINYLDIAMINOPIMTRANS_RXN', 1.000000), 
	Parameter('rvs_SUCCINYLDIAMINOPIMTRANS_RXN', 1.000000))
Rule('RXN_15313',
	cplx(name = 'ACNEULY_CPLX', loc = 'cyt') +
	met(name = 'CPD0_1123', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'ACNEULY_CPLX', loc = 'cyt') +
	met(name = 'N_ACETYL_D_MANNOSAMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_15313', 1.000000), 
	Parameter('rvs_RXN_15313', 0.000000))
Rule('ACNEULY_RXN',
	cplx(name = 'ACNEULY_CPLX', loc = 'cyt') +
	met(name = 'N_ACETYLNEURAMINATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'ACNEULY_CPLX', loc = 'cyt') +
	met(name = 'N_acetyl_D_mannosamine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ACNEULY_RXN', 1.000000), 
	Parameter('rvs_ACNEULY_RXN', 1.000000))
Rule('ACETATE__COA_LIGASE_RXN',
	prot(name = 'ACS_MONOMER', loc = 'cyt') +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACET', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'ACS_MONOMER', loc = 'cyt') +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ACETATE__COA_LIGASE_RXN', 1.000000), 
	Parameter('rvs_ACETATE__COA_LIGASE_RXN', 0.000000))
Rule('PROPIONATE__COA_LIGASE_RXN',
	prot(name = 'ACS_MONOMER', loc = 'cyt') +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROPIONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'ACS_MONOMER', loc = 'cyt') +
	met(name = 'PROPIONYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PROPIONATE__COA_LIGASE_RXN', 1.000000), 
	Parameter('rvs_PROPIONATE__COA_LIGASE_RXN', 0.000000))
Rule('ACSERLY_RXN',
	cplx(name = 'ACSERLYA_CPLX', loc = 'cyt') +
	met(name = 'ACETYLSERINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HS', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'ACSERLYA_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACET', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ACSERLY_RXN', 1.000000), 
	Parameter('rvs_ACSERLY_RXN', 1.000000))
Rule('LCYSDESULF_RXN',
	cplx(name = 'ACSERLYA_CPLX', loc = 'cyt') +
	met(name = 'CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'ACSERLYA_CPLX', loc = 'cyt') +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HS', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_LCYSDESULF_RXN', 1.000000), 
	Parameter('rvs_LCYSDESULF_RXN', 0.000000))
Rule('SULFOCYS_RXN',
	cplx(name = 'ACSERLYB_CPLX', loc = 'cyt') +
	met(name = 'ACETYLSERINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'S2O3', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'ACSERLYB_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SULFO_CYSTEINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACET', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_SULFOCYS_RXN', 1.000000), 
	Parameter('rvs_SULFOCYS_RXN', 1.000000))
Rule('ACYLCOADEHYDROG_RXN',
	prot(name = 'ACYLCOADEHYDROG_MONOMER', loc = 'imem') +
	met(name = 'Saturated_Fatty_Acyl_CoA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ETF_Oxidized', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'ACYLCOADEHYDROG_MONOMER', loc = 'imem') +
	met(name = 'TRANS_D2_ENOYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ETF_Reduced', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_ACYLCOADEHYDROG_RXN', 1.000000), 
	Parameter('rvs_ACYLCOADEHYDROG_RXN', 0.000000))
Rule('RXN_17775',
	prot(name = 'ACYLCOADEHYDROG_MONOMER', loc = 'imem') +
	met(name = 'OLEOYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ETF_Oxidized', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'ACYLCOADEHYDROG_MONOMER', loc = 'imem') +
	met(name = 'CPD_19172', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ETF_Reduced', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_17775', 1.000000), 
	Parameter('rvs_RXN_17775', 0.000000))
Rule('RXN_17779',
	prot(name = 'ACYLCOADEHYDROG_MONOMER', loc = 'imem') +
	met(name = 'CPD_19144', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ETF_Oxidized', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'ACYLCOADEHYDROG_MONOMER', loc = 'imem') +
	met(name = 'CPD_19170', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ETF_Reduced', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_17779', 1.000000), 
	Parameter('rvs_RXN_17779', 0.000000))
Rule('RXN_17783',
	prot(name = 'ACYLCOADEHYDROG_MONOMER', loc = 'imem') +
	met(name = 'CPD_15436', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ETF_Oxidized', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'ACYLCOADEHYDROG_MONOMER', loc = 'imem') +
	met(name = 'CPD0_1162', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ETF_Reduced', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_17783', 1.000000), 
	Parameter('rvs_RXN_17783', 0.000000))
Rule('RXN_17784',
	prot(name = 'ACYLCOADEHYDROG_MONOMER', loc = 'imem') +
	met(name = 'ETF_Oxidized', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_18346', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'ACYLCOADEHYDROG_MONOMER', loc = 'imem') +
	met(name = 'CPD_19163', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ETF_Reduced', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_17784', 1.000000), 
	Parameter('rvs_RXN_17784', 0.000000))
Rule('RXN_17788',
	prot(name = 'ACYLCOADEHYDROG_MONOMER', loc = 'imem') +
	met(name = 'ETF_Oxidized', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_10269', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'ACYLCOADEHYDROG_MONOMER', loc = 'imem') +
	met(name = 'CPD_19162', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ETF_Reduced', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_17788', 1.000000), 
	Parameter('rvs_RXN_17788', 0.000000))
Rule('RXN_17792',
	prot(name = 'ACYLCOADEHYDROG_MONOMER', loc = 'imem') +
	met(name = 'CPD_19147', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ETF_Oxidized', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'ACYLCOADEHYDROG_MONOMER', loc = 'imem') +
	met(name = 'CPD_19161', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ETF_Reduced', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_17792', 1.000000), 
	Parameter('rvs_RXN_17792', 0.000000))
Rule('RXN_17796',
	prot(name = 'ACYLCOADEHYDROG_MONOMER', loc = 'imem') +
	met(name = 'CPD_19148', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ETF_Oxidized', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'ACYLCOADEHYDROG_MONOMER', loc = 'imem') +
	met(name = 'CPD_19150', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ETF_Reduced', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_17796', 1.000000), 
	Parameter('rvs_RXN_17796', 0.000000))
Rule('ACYLCOASYN_RXN',
	cplx(name = 'ACYLCOASYN_CPLX', loc = 'cyt') +
	met(name = 'CPD66_39', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ACYLCOASYN_CPLX', loc = 'cyt') +
	met(name = 'Saturated_Fatty_Acyl_CoA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ACYLCOASYN_RXN', 1.000000), 
	Parameter('rvs_ACYLCOASYN_RXN', 0.000000))
Rule('TRANS_RXN0_623',
	cplx(name = 'ACYLCOASYN_CPLX', loc = 'cyt') +
	met(name = 'CPD66_39', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ACYLCOASYN_CPLX', loc = 'cyt') +
	met(name = 'Saturated_Fatty_Acyl_CoA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_TRANS_RXN0_623', 1.000000), 
	Parameter('rvs_TRANS_RXN0_623', 0.000000))
Rule('RXN0_7238',
	cplx(name = 'ACYLCOASYN_CPLX', loc = 'cyt') +
	met(name = 'CPD_9247', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ACYLCOASYN_CPLX', loc = 'cyt') +
	met(name = 'CPD_18346', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7238', 1.000000), 
	Parameter('rvs_RXN0_7238', 0.000000))
Rule('RXN0_7239',
	cplx(name = 'ACYLCOASYN_CPLX', loc = 'cyt') +
	met(name = 'OLEATE_CPD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ACYLCOASYN_CPLX', loc = 'cyt') +
	met(name = 'OLEOYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7239', 1.000000), 
	Parameter('rvs_RXN0_7239', 0.000000))
Rule('RXN0_7248',
	cplx(name = 'ACYLCOASYN_CPLX', loc = 'cyt') +
	met(name = 'CPD_9245', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ACYLCOASYN_CPLX', loc = 'cyt') +
	met(name = 'CPD_10269', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7248', 1.000000), 
	Parameter('rvs_RXN0_7248', 0.000000))
Rule('ADCLY_RXN',
	cplx(name = 'ADCLY_CPLX', loc = 'cyt') +
	met(name = '_4_AMINO_4_DEOXYCHORISMATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	cplx(name = 'ADCLY_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'P_AMINO_BENZOATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ADCLY_RXN', 1.000000), 
	Parameter('rvs_ADCLY_RXN', 0.000000))
Rule('ADDALT_RXN',
	prot(name = 'ADENODEAMIN_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DEOXYADENOSINE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'ADENODEAMIN_MONOMER', loc = 'cyt') +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DEOXYINOSINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_ADDALT_RXN', 1.000000), 
	Parameter('rvs_ADDALT_RXN', 0.000000))
Rule('ADENODEAMIN_RXN',
	prot(name = 'ADENODEAMIN_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSINE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'ADENODEAMIN_MONOMER', loc = 'cyt') +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'INOSINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_ADENODEAMIN_RXN', 1.000000), 
	Parameter('rvs_ADENODEAMIN_RXN', 0.000000))
Rule('ADENPRIBOSYLTRAN_RXN',
	cplx(name = 'ADENPRIBOSYLTRAN_CPLX', loc = 'cyt') +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ADENPRIBOSYLTRAN_CPLX', loc = 'cyt') +
	met(name = 'PRPP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ADENPRIBOSYLTRAN_RXN', 0.000000), 
	Parameter('rvs_ADENPRIBOSYLTRAN_RXN', 1.000000))
Rule('ADENYL_KIN_RXN',
	prot(name = 'ADENYL_KIN_MONOMER', loc = 'cyt') +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'ADENYL_KIN_MONOMER', loc = 'cyt') +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_ADENYL_KIN_RXN', 1.000000), 
	Parameter('rvs_ADENYL_KIN_RXN', 1.000000))
Rule('UDPKIN_RXN',
	prot(name = 'ADENYL_KIN_MONOMER', loc = 'cyt') +
	met(name = 'UDP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'ADENYL_KIN_MONOMER', loc = 'cyt') +
	met(name = 'UTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_UDPKIN_RXN', 1.000000), 
	Parameter('rvs_UDPKIN_RXN', 0.000000))
Rule('CDPKIN_RXN',
	prot(name = 'ADENYL_KIN_MONOMER', loc = 'cyt') +
	met(name = 'CDP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'ADENYL_KIN_MONOMER', loc = 'cyt') +
	met(name = 'CTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_CDPKIN_RXN', 1.000000), 
	Parameter('rvs_CDPKIN_RXN', 0.000000))
Rule('GDPKIN_RXN',
	prot(name = 'ADENYL_KIN_MONOMER', loc = 'cyt') +
	met(name = 'GDP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'ADENYL_KIN_MONOMER', loc = 'cyt') +
	met(name = 'GTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GDPKIN_RXN', 1.000000), 
	Parameter('rvs_GDPKIN_RXN', 0.000000))
Rule('DGDPKIN_RXN',
	prot(name = 'ADENYL_KIN_MONOMER', loc = 'cyt') +
	met(name = 'DGDP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'ADENYL_KIN_MONOMER', loc = 'cyt') +
	met(name = 'DGTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DGDPKIN_RXN', 1.000000), 
	Parameter('rvs_DGDPKIN_RXN', 0.000000))
Rule('DCDPKIN_RXN',
	prot(name = 'ADENYL_KIN_MONOMER', loc = 'cyt') +
	met(name = 'DCDP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'ADENYL_KIN_MONOMER', loc = 'cyt') +
	met(name = 'DCTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DCDPKIN_RXN', 1.000000), 
	Parameter('rvs_DCDPKIN_RXN', 0.000000))
Rule('DTDPKIN_RXN',
	prot(name = 'ADENYL_KIN_MONOMER', loc = 'cyt') +
	met(name = 'TDP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'ADENYL_KIN_MONOMER', loc = 'cyt') +
	met(name = 'TTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DTDPKIN_RXN', 1.000000), 
	Parameter('rvs_DTDPKIN_RXN', 0.000000))
Rule('RXN_14074',
	prot(name = 'ADENYL_KIN_MONOMER', loc = 'cyt') +
	met(name = 'GTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'ADENYL_KIN_MONOMER', loc = 'cyt') +
	met(name = 'GDP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14074', 1.000000), 
	Parameter('rvs_RXN_14074', 0.000000))
Rule('ADENYLATECYC_RXN',
	prot(name = 'ADENYLATECYC_MONOMER', loc = 'cyt') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'ADENYLATECYC_MONOMER', loc = 'cyt') +
	met(name = 'CAMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ADENYLATECYC_RXN', 1.000000), 
	Parameter('rvs_ADENYLATECYC_RXN', 0.000000))
Rule('ADENYLOSUCCINATE_SYNTHASE_RXN',
	cplx(name = 'ADENYLOSUCCINATE_SYN_DIMER', loc = 'cyt') +
	met(name = 'L_ASPARTATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'IMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'ADENYLOSUCCINATE_SYN_DIMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENYLOSUCC', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GDP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ADENYLOSUCCINATE_SYNTHASE_RXN', 1.000000), 
	Parameter('rvs_ADENYLOSUCCINATE_SYNTHASE_RXN', 0.000000))
Rule('ADENYLYLSULFKIN_RXN',
	cplx(name = 'ADENYLYLSULFKIN_CPLX', loc = 'cyt') +
	met(name = 'APS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'ADENYLYLSULFKIN_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PAPS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ADENYLYLSULFKIN_RXN', 1.000000), 
	Parameter('rvs_ADENYLYLSULFKIN_RXN', 1.000000))
Rule('RXN_2962',
	cplx(name = 'ADHC_CPLX', loc = 'cyt') +
	met(name = 'NAD_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'S_HYDROXYMETHYLGLUTATHIONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'ADHC_CPLX', loc = 'cyt') +
	met(name = 'NADH_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_548', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_2962', 1.000000), 
	Parameter('rvs_RXN_2962', 0.000000))
Rule('ACETALD_DEHYDROG_RXN',
	cplx(name = 'ADHE_CPLX', loc = 'cyt') +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETALD', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ADHE_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ACETALD_DEHYDROG_RXN', 1.000000), 
	Parameter('rvs_ACETALD_DEHYDROG_RXN', 1.000000))
Rule('RXN0_5260',
	cplx(name = 'AERGLYC3PDEHYDROG_CPLX', loc = 'imem') +
	met(name = 'Ubiquinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLYCEROL_3P', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'AERGLYC3PDEHYDROG_CPLX', loc = 'imem') +
	met(name = 'Ubiquinols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DIHYDROXY_ACETONE_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5260', 1.000000), 
	Parameter('rvs_RXN0_5260', 0.000000))
Rule('AGMATIN_RXN',
	cplx(name = 'AGMATIN_CPLX', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AGMATHINE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'AGMATIN_CPLX', loc = 'cyt') +
	met(name = 'UREA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PUTRESCINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_AGMATIN_RXN', 1.000000), 
	Parameter('rvs_AGMATIN_RXN', 0.000000))
Rule('AICARTRANSFORM_RXN',
	cplx(name = 'AICARTRANSIMPCYCLO_CPLX', loc = 'cyt') +
	met(name = 'FORMYL_THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AICAR', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'AICARTRANSIMPCYCLO_CPLX', loc = 'cyt') +
	met(name = 'THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PHOSPHORIBOSYL_FORMAMIDO_CARBOXAMIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_AICARTRANSFORM_RXN', 1.000000), 
	Parameter('rvs_AICARTRANSFORM_RXN', 1.000000))
Rule('IMPCYCLOHYDROLASE_RXN',
	cplx(name = 'AICARTRANSIMPCYCLO_CPLX', loc = 'cyt') +
	met(name = 'IMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'AICARTRANSIMPCYCLO_CPLX', loc = 'cyt') +
	met(name = 'PHOSPHORIBOSYL_FORMAMIDO_CARBOXAMIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_IMPCYCLOHYDROLASE_RXN', 1.000000), 
	Parameter('rvs_IMPCYCLOHYDROLASE_RXN', 1.000000))
Rule('AIRS_RXN',
	cplx(name = 'AIRS_CPLX', loc = 'cyt') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_5_PHOSPHORIBOSYL_N_FORMYLGLYCINEAMIDINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	cplx(name = 'AIRS_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_5_PHOSPHORIBOSYL_5_AMINOIMIDAZOLE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_AIRS_RXN', 1.000000), 
	Parameter('rvs_AIRS_RXN', 0.000000))
Rule('AKBLIG_RXN',
	cplx(name = 'AKBLIG_CPLX', loc = 'cyt') +
	met(name = 'GLY', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'AKBLIG_CPLX', loc = 'cyt') +
	met(name = 'AMINO_OXOBUT', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_AKBLIG_RXN', 1.000000), 
	Parameter('rvs_AKBLIG_RXN', 1.000000))
Rule('ALANINE__TRNA_LIGASE_RXN',
	cplx(name = 'ALAS_CPLX', loc = 'cyt') +
	met(name = 'ALA_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_ALPHA_ALANINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALAS_CPLX', loc = 'cyt') +
	met(name = 'Charged_ALA_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ALANINE__TRNA_LIGASE_RXN', 1.000000), 
	Parameter('rvs_ALANINE__TRNA_LIGASE_RXN', 0.000000))
Rule('LACTALDDEHYDROG_RXN',
	cplx(name = 'ALD_CPLX', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'LACTALD', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALD_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_LACTATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_LACTALDDEHYDROG_RXN', 1.000000), 
	Parameter('rvs_LACTALDDEHYDROG_RXN', 0.000000))
Rule('GLYCOLALD_DEHYDROG_RXN',
	cplx(name = 'ALD_CPLX', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLYCOLALDEHYDE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALD_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLYCOLLATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLYCOLALD_DEHYDROG_RXN', 1.000000), 
	Parameter('rvs_GLYCOLALD_DEHYDROG_RXN', 0.000000))
Rule('AMINOBUTDEHYDROG_RXN',
	prot(name = 'ALDHDEHYDROG_MONOMER', loc = 'cyt') +
	met(name = '_4_AMINO_BUTYRALDEHYDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'ALDHDEHYDROG_MONOMER', loc = 'cyt') +
	met(name = '_4_AMINO_BUTYRATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_AMINOBUTDEHYDROG_RXN', 1.000000), 
	Parameter('rvs_AMINOBUTDEHYDROG_RXN', 0.000000))
Rule('SUCCINATE_SEMIALDEHYDE_DEHYDROGENASE_RXN',
	prot(name = 'ALDHDEHYDROG_MONOMER', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SUCC_S_ALD', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'ALDHDEHYDROG_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SUC', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_SUCCINATE_SEMIALDEHYDE_DEHYDROGENASE_RXN', 1.000000), 
	Parameter('rvs_SUCCINATE_SEMIALDEHYDE_DEHYDROGENASE_RXN', 0.000000))
Rule('RXN0_5455',
	prot(name = 'ALDHDEHYDROG_MONOMER', loc = 'cyt') +
	met(name = 'HYDROXYPROPANAL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'ALDHDEHYDROG_MONOMER', loc = 'cyt') +
	met(name = '_3_HYDROXY_PROPIONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5455', 1.000000), 
	Parameter('rvs_RXN0_5455', 0.000000))
Rule('RXN0_3922',
	prot(name = 'ALDHDEHYDROG_MONOMER', loc = 'cyt') +
	met(name = 'GAMMA_GLUTAMYL_GAMMA_AMINOBUTYRALDEH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'ALDHDEHYDROG_MONOMER', loc = 'cyt') +
	met(name = 'CPD_9000', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_3922', 1.000000), 
	Parameter('rvs_RXN0_3922', 0.000000))
Rule('ALDOSE1EPIM_RXN',
	prot(name = 'ALDOSE1EPIM_MONOMER', loc = 'cyt') +
	met(name = 'GALACTOSE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'ALDOSE1EPIM_MONOMER', loc = 'cyt') +
	met(name = 'ALPHA_D_GALACTOSE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ALDOSE1EPIM_RXN', 1.000000), 
	Parameter('rvs_ALDOSE1EPIM_RXN', 1.000000))
Rule('ALKAPHOSPHA_RXN',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'Orthophosphoric_Monoesters', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'Alcohols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ALKAPHOSPHA_RXN', 1.000000), 
	Parameter('rvs_ALKAPHOSPHA_RXN', 0.000000))
Rule('RXN_7948',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'PHOSPHORYL_ETHANOLAMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'ETHANOL_AMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_7948', 1.000000), 
	Parameter('rvs_RXN_7948', 0.000000))
Rule('RXN_5647',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'PHOSPHORYL_CHOLINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'CHOLINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_5647', 1.000000), 
	Parameter('rvs_RXN_5647', 0.000000))
Rule('RXN_14514',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'CPD_3721', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'CPD_239', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14514', 1.000000), 
	Parameter('rvs_RXN_14514', 0.000000))
Rule('_4_NITROPHENYLPHOSPHATASE_RXN',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'CPD_194', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'P_NITROPHENOL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__4_NITROPHENYLPHOSPHATASE_RXN', 1.000000), 
	Parameter('rvs__4_NITROPHENYLPHOSPHATASE_RXN', 0.000000))
Rule('_3dot1dot3dot74_RXN',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'PYRIDOXAL_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'PYRIDOXAL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3dot1dot3dot74_RXN', 1.000000), 
	Parameter('rvs__3dot1dot3dot74_RXN', 0.000000))
Rule('RXN_14181',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'PYRIDOXINE_5P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'PYRIDOXINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14181', 1.000000), 
	Parameter('rvs_RXN_14181', 0.000000))
Rule('RXN_7607',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'IMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'INOSINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_7607', 1.000000), 
	Parameter('rvs_RXN_7607', 0.000000))
Rule('RXN_14025',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'UMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'URIDINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14025', 1.000000), 
	Parameter('rvs_RXN_14025', 0.000000))
Rule('RXN_14115',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'CPD_3724', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'URIDINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14115', 1.000000), 
	Parameter('rvs_RXN_14115', 0.000000))
Rule('RXN_14510',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'CPD_3723', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'URIDINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14510', 1.000000), 
	Parameter('rvs_RXN_14510', 0.000000))
Rule('RXN0_5292',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'DCMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'DEOXYCYTIDINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5292', 1.000000), 
	Parameter('rvs_RXN0_5292', 0.000000))
Rule('RXN_14026',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'CMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'CYTIDINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14026', 1.000000), 
	Parameter('rvs_RXN_14026', 0.000000))
Rule('RXN_14090',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'CPD_3711', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'CYTIDINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14090', 1.000000), 
	Parameter('rvs_RXN_14090', 0.000000))
Rule('RXN_14511',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'CPD_3710', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'CYTIDINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14511', 1.000000), 
	Parameter('rvs_RXN_14511', 0.000000))
Rule('RXN_14512',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'CPD_13025', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'GUANOSINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14512', 1.000000), 
	Parameter('rvs_RXN_14512', 0.000000))
Rule('RXN_14142',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'DGMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'DEOXYGUANOSINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14142', 1.000000), 
	Parameter('rvs_RXN_14142', 0.000000))
Rule('RXN_14513',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'CPD_3705', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14513', 1.000000), 
	Parameter('rvs_RXN_14513', 0.000000))
Rule('RXN_14126',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'CPD_3706', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'ADENOSINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14126', 1.000000), 
	Parameter('rvs_RXN_14126', 0.000000))
Rule('RXN_14161',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'DAMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'DEOXYADENOSINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14161', 1.000000), 
	Parameter('rvs_RXN_14161', 0.000000))
Rule('AMP_DEPHOSPHORYLATION_RXN',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'ADENOSINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_AMP_DEPHOSPHORYLATION_RXN', 1.000000), 
	Parameter('rvs_AMP_DEPHOSPHORYLATION_RXN', 0.000000))
Rule('PHOSPHOENOLPYRUVATE_PHOSPHATASE_RXN',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PHOSPHO_ENOL_PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PHOSPHOENOLPYRUVATE_PHOSPHATASE_RXN', 1.000000), 
	Parameter('rvs_PHOSPHOENOLPYRUVATE_PHOSPHATASE_RXN', 0.000000))
Rule('HISTIDPHOS_RXN',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'L_HISTIDINOL_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'HISTIDINOL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_HISTIDPHOS_RXN', 1.000000), 
	Parameter('rvs_HISTIDPHOS_RXN', 0.000000))
Rule('RXN0_5187',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'FMN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'RIBOFLAVIN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5187', 1.000000), 
	Parameter('rvs_RXN0_5187', 0.000000))
Rule('RXN_5822',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_5822', 1.000000), 
	Parameter('rvs_RXN_5822', 0.000000))
Rule('F16BDEPHOS_RXN',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'FRUCTOSE_16_DIPHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'FRUCTOSE_6P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_F16BDEPHOS_RXN', 1.000000), 
	Parameter('rvs_F16BDEPHOS_RXN', 0.000000))
Rule('PHOSPHOGLYCERATE_PHOSPHATASE_RXN',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_PG', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'GLYCERATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PHOSPHOGLYCERATE_PHOSPHATASE_RXN', 1.000000), 
	Parameter('rvs_PHOSPHOGLYCERATE_PHOSPHATASE_RXN', 0.000000))
Rule('GLYCEROL_2_PHOSPHATASE_RXN',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_536', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLYCEROL', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLYCEROL_2_PHOSPHATASE_RXN', 1.000000), 
	Parameter('rvs_GLYCEROL_2_PHOSPHATASE_RXN', 0.000000))
Rule('RXN_14509',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'RIBOSE_5P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'CPD_15818', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14509', 1.000000), 
	Parameter('rvs_RXN_14509', 0.000000))
Rule('RXN_14505',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'L_THREONINE_O_3_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'THR', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14505', 1.000000), 
	Parameter('rvs_RXN_14505', 0.000000))
Rule('RXN0_5114',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = '_3_P_SERINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'SER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5114', 1.000000), 
	Parameter('rvs_RXN0_5114', 0.000000))
Rule('TRIPHOSPHATASE_RXN',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'P3I', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_TRIPHOSPHATASE_RXN', 1.000000), 
	Parameter('rvs_TRIPHOSPHATASE_RXN', 0.000000))
Rule('INORGPYROPHOSPHAT_RXN',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_INORGPYROPHOSPHAT_RXN', 1.000000), 
	Parameter('rvs_INORGPYROPHOSPHAT_RXN', 0.000000))
Rule('RXN_17330',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'D_glucose_1_phosphates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'Glucopyranose', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17330', 1.000000), 
	Parameter('rvs_RXN_17330', 0.000000))
Rule('RXN66_526',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'D_glucopyranose_6_phosphate', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'Glucopyranose', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN66_526', 1.000000), 
	Parameter('rvs_RXN66_526', 0.000000))
Rule('SUGAR_PHOSPHATASE_RXN',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Sugar_Phosphate', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'Sugar', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_SUGAR_PHOSPHATASE_RXN', 1.000000), 
	Parameter('rvs_SUGAR_PHOSPHATASE_RXN', 0.000000))
Rule('RXN_17724',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'Mannose_6_phosphate', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'MANNOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17724', 1.000000), 
	Parameter('rvs_RXN_17724', 0.000000))
Rule('RXN_17725',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'MANNOSE_1P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'MANNOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17725', 1.000000), 
	Parameter('rvs_RXN_17725', 0.000000))
Rule('RXN_17745',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'D_GLUCOSAMINE_6_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'GLUCOSAMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17745', 1.000000), 
	Parameter('rvs_RXN_17745', 0.000000))
Rule('_3_PHOSPHOGLYCERATE_PHOSPHATASE_RXN',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'G3P', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'GLYCERATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3_PHOSPHOGLYCERATE_PHOSPHATASE_RXN', 1.000000), 
	Parameter('rvs__3_PHOSPHOGLYCERATE_PHOSPHATASE_RXN', 0.000000))
Rule('GPH_RXN',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_67', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'GLYCOLLATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GPH_RXN', 1.000000), 
	Parameter('rvs_GPH_RXN', 0.000000))
Rule('_3dot1dot3dot68_RXN',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_DEOXY_D_GLUCOSE_6_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = '_2_DEOXY_D_GLUCOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3dot1dot3dot68_RXN', 1.000000), 
	Parameter('rvs__3dot1dot3dot68_RXN', 0.000000))
Rule('PHOSPHOAMIDASE_RXN',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CREATINE_P', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CREATINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PHOSPHOAMIDASE_RXN', 1.000000), 
	Parameter('rvs_PHOSPHOAMIDASE_RXN', 0.000000))
Rule('RXN0_5185',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'CPD_2961', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'GLUCONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5185', 1.000000), 
	Parameter('rvs_RXN0_5185', 0.000000))
Rule('RXN0_7249',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'DIHYDROXY_ACETONE_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'DIHYDROXYACETONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7249', 1.000000), 
	Parameter('rvs_RXN0_7249', 0.000000))
Rule('RXN0_7250',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'GAP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'GLYCERALD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7250', 1.000000), 
	Parameter('rvs_RXN0_7250', 0.000000))
Rule('RXN0_7251',
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'L_GLYCERALDEHYDE_3_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALKAPHOSPHA_CPLX', loc = 'per') +
	met(name = 'L_GLYCERALDEHYDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7251', 1.000000), 
	Parameter('rvs_RXN0_7251', 0.000000))
Rule('ALPHA_AMYL_RXN',
	prot(name = 'ALPHA_AMYL_CYTO_MONOMER', loc = 'cyt') +
	met(name = '_1_4_alpha_D_Glucan', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'ALPHA_AMYL_CYTO_MONOMER', loc = 'cyt') +
	met(name = '_1_4_alpha_D_Glucan', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_ALPHA_AMYL_RXN', 1.000000), 
	Parameter('rvs_ALPHA_AMYL_RXN', 0.000000))
Rule('RXN0_5181',
	prot(name = 'ALPHA_AMYL_PERI_MONOMER', loc = 'per') +
	met(name = '_1_4_alpha_D_Glucan', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'ALPHA_AMYL_PERI_MONOMER', loc = 'per') +
	met(name = '_1_4_alpha_D_Glucan', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MALTOHEXAOSE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5181', 1.000000), 
	Parameter('rvs_RXN0_5181', 0.000000))
Rule('ALPHAGALACTOSID_RXN',
	cplx(name = 'ALPHAGALACTOSID_CPLX', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MELIBIOSE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALPHAGALACTOSID_CPLX', loc = 'cyt') +
	met(name = 'D_galactopyranose', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Glucopyranose', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ALPHAGALACTOSID_RXN', 1.000000), 
	Parameter('rvs_ALPHAGALACTOSID_RXN', 0.000000))
Rule('RXN_17754',
	cplx(name = 'ALPHAGALACTOSID_CPLX', loc = 'cyt') +
	met(name = 'CPD_3801', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ALPHAGALACTOSID_CPLX', loc = 'cyt') +
	met(name = 'ALPHA_D_GALACTOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLUCONATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17754', 1.000000), 
	Parameter('rvs_RXN_17754', 0.000000))
Rule('ALTRO_OXIDOREDUCT_RXN',
	prot(name = 'ALTRO_OXIDOREDUCT_MONOMER', loc = 'cyt') +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_ALTRONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'ALTRO_OXIDOREDUCT_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_TAGATURONATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ALTRO_OXIDOREDUCT_RXN', 1.000000), 
	Parameter('rvs_ALTRO_OXIDOREDUCT_RXN', 1.000000))
Rule('ALTRODEHYDRAT_RXN',
	prot(name = 'ALTRODEHYDRAT_MONOMER', loc = 'cyt') +
	met(name = 'D_ALTRONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'ALTRODEHYDRAT_MONOMER', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_DEHYDRO_3_DEOXY_D_GLUCONATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ALTRODEHYDRAT_RXN', 1.000000), 
	Parameter('rvs_ALTRODEHYDRAT_RXN', 0.000000))
Rule('RXN_9597',
	cplx(name = 'AMINEOXID_CPLX', loc = 'per') +
	met(name = 'Primary_Amines', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'AMINEOXID_CPLX', loc = 'per') +
	met(name = 'Aldehydes', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HYDROGEN_PEROXIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_9597', 1.000000), 
	Parameter('rvs_RXN_9597', 0.000000))
Rule('AMINEPHEN_RXN',
	cplx(name = 'AMINEOXID_CPLX', loc = 'per') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PHENYLETHYLAMINE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'AMINEOXID_CPLX', loc = 'per') +
	met(name = 'PHENYLACETALDEHYDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HYDROGEN_PEROXIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_AMINEPHEN_RXN', 1.000000), 
	Parameter('rvs_AMINEPHEN_RXN', 0.000000))
Rule('AMACETOXID_RXN',
	cplx(name = 'AMINEOXID_CPLX', loc = 'per') +
	met(name = 'AMINO_ACETONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'AMINEOXID_CPLX', loc = 'per') +
	met(name = 'METHYL_GLYOXAL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HYDROGEN_PEROXIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_AMACETOXID_RXN', 1.000000), 
	Parameter('rvs_AMACETOXID_RXN', 0.000000))
Rule('AMINEOXID_RXN',
	cplx(name = 'AMINEOXID_CPLX', loc = 'per') +
	met(name = 'Aliphatic_Amines', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'AMINEOXID_CPLX', loc = 'per') +
	met(name = 'Aldehydes', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HYDROGEN_PEROXIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_AMINEOXID_RXN', 1.000000), 
	Parameter('rvs_AMINEOXID_RXN', 0.000000))
Rule('AMP_NUCLEOSID_RXN',
	cplx(name = 'AMP_NUCLEOSID_CPLX', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'AMP_NUCLEOSID_CPLX', loc = 'cyt') +
	met(name = 'CPD_15317', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_AMP_NUCLEOSID_RXN', 1.000000), 
	Parameter('rvs_AMP_NUCLEOSID_RXN', 0.000000))
Rule('RXN_14261',
	prot(name = 'AMYLOMALT_MONOMER', loc = 'cyt') +
	met(name = 'MALTOHEXAOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Glucopyranose', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'AMYLOMALT_MONOMER', loc = 'cyt') +
	met(name = 'MALTOPENTAOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MALTOSE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14261', 1.000000), 
	Parameter('rvs_RXN_14261', 1.000000))
Rule('RXN_14260',
	prot(name = 'AMYLOMALT_MONOMER', loc = 'cyt') +
	met(name = 'MALTOPENTAOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Glucopyranose', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'AMYLOMALT_MONOMER', loc = 'cyt') +
	met(name = 'MALTOTETRAOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MALTOSE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14260', 1.000000), 
	Parameter('rvs_RXN_14260', 1.000000))
Rule('RXN_15740',
	cplx(name = 'ANGLYC3PDEHYDROG_CPLX', loc = 'cyt') +
	met(name = 'Menaquinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLYCEROL_3P', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ANGLYC3PDEHYDROG_CPLX', loc = 'cyt') +
	met(name = 'Menaquinols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DIHYDROXY_ACETONE_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_15740', 1.000000), 
	Parameter('rvs_RXN_15740', 0.000000))
Rule('ASPARAGHYD_RXN',
	cplx(name = 'ANSA_CPLX', loc = 'cyt') +
	met(name = 'ASN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ANSA_CPLX', loc = 'cyt') +
	met(name = 'L_ASPARTATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ASPARAGHYD_RXN', 1.000000), 
	Parameter('rvs_ASPARAGHYD_RXN', 0.000000))
Rule('ANTHRANSYN_RXN',
	cplx(name = 'ANTHRANSYN_CPLX', loc = 'cyt') +
	met(name = 'CHORISMATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLN', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	cplx(name = 'ANTHRANSYN_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ANTHRANILATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ANTHRANSYN_RXN', 1.000000), 
	Parameter('rvs_ANTHRANSYN_RXN', 0.000000))
Rule('PRTRANS_RXN',
	prot(name = 'ANTHRANSYNCOMPII_MONOMER', loc = 'cyt') +
	met(name = 'N_5_PHOSPHORIBOSYL_ANTHRANILATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'ANTHRANSYNCOMPII_MONOMER', loc = 'cyt') +
	met(name = 'ANTHRANILATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PRPP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PRTRANS_RXN', 0.000000), 
	Parameter('rvs_PRTRANS_RXN', 1.000000))
Rule('ACID_PHOSPHATASE_RXN',
	cplx(name = 'APHA_CPLX', loc = 'per') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Orthophosphoric_Monoesters', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'APHA_CPLX', loc = 'per') +
	met(name = 'Alcohols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ACID_PHOSPHATASE_RXN', 1.000000), 
	Parameter('rvs_ACID_PHOSPHATASE_RXN', 0.000000))
Rule('RXN_14473',
	cplx(name = 'APHA_CPLX', loc = 'per') +
	met(name = 'Nucleoside_Monophosphates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'APHA_CPLX', loc = 'per') +
	met(name = 'Nucleosides', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14473', 1.000000), 
	Parameter('rvs_RXN_14473', 0.000000))
Rule('_5_NUCLEOTID_RXN',
	cplx(name = 'APHA_CPLX', loc = 'per') +
	met(name = 'Ribonucleoside_Monophosphates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'APHA_CPLX', loc = 'per') +
	met(name = 'Ribonucleosides', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__5_NUCLEOTID_RXN', 1.000000), 
	Parameter('rvs__5_NUCLEOTID_RXN', 0.000000))
Rule('_3_NUCLEOTID_RXN',
	cplx(name = 'APHA_CPLX', loc = 'per') +
	met(name = '_3_Phosphomonucleotides', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'APHA_CPLX', loc = 'per') +
	met(name = 'Ribonucleosides', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3_NUCLEOTID_RXN', 1.000000), 
	Parameter('rvs__3_NUCLEOTID_RXN', 0.000000))
Rule('RXN0_3741',
	cplx(name = 'APHA_CPLX', loc = 'per') +
	met(name = 'Deoxy_Ribonucleoside_Monophosphates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'APHA_CPLX', loc = 'per') +
	met(name = 'Deoxy_Ribonucleosides', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_3741', 1.000000), 
	Parameter('rvs_RXN0_3741', 0.000000))
Rule('DEOXYNUCLEOTIDE_3_PHOSPHATASE_RXN',
	cplx(name = 'APHA_CPLX', loc = 'per') +
	met(name = 'Deoxy_Ribonucleoside_3P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'APHA_CPLX', loc = 'per') +
	met(name = 'Deoxy_Ribonucleosides', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DEOXYNUCLEOTIDE_3_PHOSPHATASE_RXN', 1.000000), 
	Parameter('rvs_DEOXYNUCLEOTIDE_3_PHOSPHATASE_RXN', 0.000000))
Rule('RXN_14522',
	cplx(name = 'APHA_CPLX', loc = 'per') +
	met(name = 'CPD_15392', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'APHA_CPLX', loc = 'per') +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DEOXYCYTIDINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14522', 1.000000), 
	Parameter('rvs_RXN_14522', 0.000000))
Rule('RXN_14525',
	cplx(name = 'APHA_CPLX', loc = 'per') +
	met(name = 'CPD_15390', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'APHA_CPLX', loc = 'per') +
	met(name = 'DEOXYGUANOSINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14525', 1.000000), 
	Parameter('rvs_RXN_14525', 0.000000))
Rule('RXN_14523',
	cplx(name = 'APHA_CPLX', loc = 'per') +
	met(name = 'CPD_15393', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'APHA_CPLX', loc = 'per') +
	met(name = 'DEOXYURIDINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14523', 1.000000), 
	Parameter('rvs_RXN_14523', 0.000000))
Rule('RXN_14524',
	cplx(name = 'APHA_CPLX', loc = 'per') +
	met(name = 'CPD_15391', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'APHA_CPLX', loc = 'per') +
	met(name = 'DEOXYADENOSINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14524', 1.000000), 
	Parameter('rvs_RXN_14524', 0.000000))
Rule('RXN_14534',
	cplx(name = 'APHA_CPLX', loc = 'per') +
	met(name = 'CPD_3728', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'APHA_CPLX', loc = 'per') +
	met(name = 'TYR', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14534', 1.000000), 
	Parameter('rvs_RXN_14534', 0.000000))
Rule('DNA_DIRECTED_RNA_POLYMERASE_RXN',
	cplx(name = 'APORNAP_CPLX', loc = 'cyt') +
	met(name = 'Nucleoside_Triphosphates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'RNA_Holder', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'APORNAP_CPLX', loc = 'cyt') +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'RNA_Holder', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DNA_DIRECTED_RNA_POLYMERASE_RXN', 1.000000), 
	Parameter('rvs_DNA_DIRECTED_RNA_POLYMERASE_RXN', 0.000000))
Rule('RXN0_5266',
	cplx(name = 'APP_UBIOX_CPLX', loc = 'imem') +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Ubiquinols', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'APP_UBIOX_CPLX', loc = 'imem') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Ubiquinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5266', 1.000000), 
	Parameter('rvs_RXN0_5266', 0.000000))
Rule('ARABISOM_RXN',
	cplx(name = 'ARABISOM_CPLX', loc = 'cyt') +
	met(name = 'L_arabinopyranose', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ARABISOM_CPLX', loc = 'cyt') +
	met(name = 'L_RIBULOSE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ARABISOM_RXN', 1.000000), 
	Parameter('rvs_ARABISOM_RXN', 1.000000))
Rule('ARGDECARBOX_RXN',
	cplx(name = 'ARGDECARBOXBIO_CPLX', loc = 'per') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ARG', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ARGDECARBOXBIO_CPLX', loc = 'per') +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AGMATHINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ARGDECARBOX_RXN', 1.000000), 
	Parameter('rvs_ARGDECARBOX_RXN', 0.000000))
Rule('ARGININE__TRNA_LIGASE_RXN',
	prot(name = 'ARGS_MONOMER', loc = 'cyt') +
	met(name = 'ARG_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ARG', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'ARGS_MONOMER', loc = 'cyt') +
	met(name = 'Charged_ARG_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ARGININE__TRNA_LIGASE_RXN', 1.000000), 
	Parameter('rvs_ARGININE__TRNA_LIGASE_RXN', 0.000000))
Rule('ARGSUCCINLYA_RXN',
	prot(name = 'ARGSUCCINLYA_MONOMER', loc = 'cyt') +
	met(name = 'L_ARGININO_SUCCINATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'ARGSUCCINLYA_MONOMER', loc = 'cyt') +
	met(name = 'ARG', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FUM', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ARGSUCCINLYA_RXN', 1.000000), 
	Parameter('rvs_ARGSUCCINLYA_RXN', 1.000000))
Rule('ARGININE_N_SUCCINYLTRANSFERASE_RXN',
	prot(name = 'ARGSUCCTRAN_MONOMER', loc = 'cyt') +
	met(name = 'ARG', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SUC_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'ARGSUCCTRAN_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_421', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ARGININE_N_SUCCINYLTRANSFERASE_RXN', 1.000000), 
	Parameter('rvs_ARGININE_N_SUCCINYLTRANSFERASE_RXN', 0.000000))
Rule('_2dot5dot1dot19_RXN',
	prot(name = 'AROA_MONOMER', loc = 'cyt') +
	met(name = 'SHIKIMATE_5P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PHOSPHO_ENOL_PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'AROA_MONOMER', loc = 'cyt') +
	met(name = '_3_ENOLPYRUVYL_SHIKIMATE_5P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__2dot5dot1dot19_RXN', 1.000000), 
	Parameter('rvs__2dot5dot1dot19_RXN', 1.000000))
Rule('_3_DEHYDROQUINATE_SYNTHASE_RXN',
	prot(name = 'AROB_MONOMER', loc = 'cyt') +
	met(name = '_3_DEOXY_D_ARABINO_HEPTULOSONATE_7_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'AROB_MONOMER', loc = 'cyt') +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DEHYDROQUINATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3_DEHYDROQUINATE_SYNTHASE_RXN', 1.000000), 
	Parameter('rvs__3_DEHYDROQUINATE_SYNTHASE_RXN', 0.000000))
Rule('CHORISMATE_SYNTHASE_RXN',
	cplx(name = 'AROC_CPLX', loc = 'cyt') +
	met(name = '_3_ENOLPYRUVYL_SHIKIMATE_5P', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'AROC_CPLX', loc = 'cyt') +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CHORISMATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_CHORISMATE_SYNTHASE_RXN', 1.000000), 
	Parameter('rvs_CHORISMATE_SYNTHASE_RXN', 0.000000))
Rule('_3_DEHYDROQUINATE_DEHYDRATASE_RXN',
	cplx(name = 'AROD_CPLX', loc = 'cyt') +
	met(name = 'DEHYDROQUINATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'AROD_CPLX', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_3_DEHYDRO_SHIKIMATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3_DEHYDROQUINATE_DEHYDRATASE_RXN', 1.000000), 
	Parameter('rvs__3_DEHYDROQUINATE_DEHYDRATASE_RXN', 1.000000))
Rule('SHIKIMATE_5_DEHYDROGENASE_RXN',
	prot(name = 'AROE_MONOMER', loc = 'cyt') +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SHIKIMATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'AROE_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_3_DEHYDRO_SHIKIMATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_SHIKIMATE_5_DEHYDROGENASE_RXN', 0.000000), 
	Parameter('rvs_SHIKIMATE_5_DEHYDROGENASE_RXN', 1.000000))
Rule('DAHPSYN_RXN',
	cplx(name = 'AROF_CPLX', loc = 'cyt') +
	met(name = 'PHOSPHO_ENOL_PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ERYTHROSE_4P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'AROF_CPLX', loc = 'cyt') +
	met(name = '_3_DEOXY_D_ARABINO_HEPTULOSONATE_7_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_DAHPSYN_RXN', 1.000000), 
	Parameter('rvs_DAHPSYN_RXN', 0.000000))
Rule('SHIKIMATE_KINASE_RXN',
	prot(name = 'AROK_MONOMER', loc = 'cyt') +
	met(name = 'SHIKIMATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'AROK_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SHIKIMATE_5P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_SHIKIMATE_KINASE_RXN', 1.000000), 
	Parameter('rvs_SHIKIMATE_KINASE_RXN', 0.000000))
Rule('ARYLSULFAT_RXN',
	prot(name = 'ARYLSULFAT_MONOMER', loc = 'per') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Aryl_sulfates', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'ARYLSULFAT_MONOMER', loc = 'per') +
	met(name = 'Phenols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SULFATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ARYLSULFAT_RXN', 1.000000), 
	Parameter('rvs_ARYLSULFAT_RXN', 0.000000))
Rule('ASPARAGINE__TRNA_LIGASE_RXN',
	cplx(name = 'ASNS_CPLX', loc = 'cyt') +
	met(name = 'ASN_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ASN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ASNS_CPLX', loc = 'cyt') +
	met(name = 'Charged_ASN_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ASPARAGINE__TRNA_LIGASE_RXN', 1.000000), 
	Parameter('rvs_ASPARAGINE__TRNA_LIGASE_RXN', 0.000000))
Rule('ASNSYNA_RXN',
	cplx(name = 'ASNSYNA_CPLX', loc = 'cyt') +
	met(name = 'L_ASPARTATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'ASNSYNA_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ASN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ASNSYNA_RXN', 1.000000), 
	Parameter('rvs_ASNSYNA_RXN', 0.000000))
Rule('ASNSYNB_RXN',
	cplx(name = 'ASNSYNB_CPLX', loc = 'cyt') +
	met(name = 'GLN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_ASPARTATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'ASNSYNB_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ASN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ASNSYNB_RXN', 1.000000), 
	Parameter('rvs_ASNSYNB_RXN', 0.000000))
Rule('GLUTAMIN_RXN',
	cplx(name = 'ASNSYNB_CPLX', loc = 'cyt') +
	met(name = 'GLN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ASNSYNB_CPLX', loc = 'cyt') +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLUTAMIN_RXN', 1.000000), 
	Parameter('rvs_GLUTAMIN_RXN', 0.000000))
Rule('ASPARTATE_SEMIALDEHYDE_DEHYDROGENASE_RXN',
	cplx(name = 'ASP_SEMIALDEHYDE_DEHYDROGENASE_CPLX', loc = 'cyt') +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_ASPARTATE_SEMIALDEHYDE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ASP_SEMIALDEHYDE_DEHYDROGENASE_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_BETA_ASPARTYL_P', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ASPARTATE_SEMIALDEHYDE_DEHYDROGENASE_RXN', 1.000000), 
	Parameter('rvs_ASPARTATE_SEMIALDEHYDE_DEHYDROGENASE_RXN', 1.000000))
Rule('ASPAMINOTRANS_RXN',
	cplx(name = 'ASPAMINOTRANS_DIMER', loc = 'cyt') +
	met(name = 'L_ASPARTATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ASPAMINOTRANS_DIMER', loc = 'cyt') +
	met(name = 'OXALACETIC_ACID', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ASPAMINOTRANS_RXN', 1.000000), 
	Parameter('rvs_ASPAMINOTRANS_RXN', 1.000000))
Rule('RXN_10814',
	cplx(name = 'ASPAMINOTRANS_DIMER', loc = 'cyt') +
	met(name = 'PHE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ASPAMINOTRANS_DIMER', loc = 'cyt') +
	met(name = 'PHENYL_PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_10814', 1.000000), 
	Parameter('rvs_RXN_10814', 1.000000))
Rule('TYROSINE_AMINOTRANSFERASE_RXN',
	cplx(name = 'ASPAMINOTRANS_DIMER', loc = 'cyt') +
	met(name = 'TYR', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ASPAMINOTRANS_DIMER', loc = 'cyt') +
	met(name = 'P_HYDROXY_PHENYLPYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_TYROSINE_AMINOTRANSFERASE_RXN', 1.000000), 
	Parameter('rvs_TYROSINE_AMINOTRANSFERASE_RXN', 1.000000))
Rule('_2dot6dot1dot7_RXN',
	cplx(name = 'ASPAMINOTRANS_DIMER', loc = 'cyt') +
	met(name = 'CPD_14736', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ASPAMINOTRANS_DIMER', loc = 'cyt') +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_476', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__2dot6dot1dot7_RXN', 1.000000), 
	Parameter('rvs__2dot6dot1dot7_RXN', 1.000000))
Rule('CYSTEINE_AMINOTRANSFERASE_RXN',
	cplx(name = 'ASPAMINOTRANS_DIMER', loc = 'cyt') +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CYS', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ASPAMINOTRANS_DIMER', loc = 'cyt') +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_3_MERCAPTO_PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_CYSTEINE_AMINOTRANSFERASE_RXN', 1.000000), 
	Parameter('rvs_CYSTEINE_AMINOTRANSFERASE_RXN', 1.000000))
Rule('ASPARTASE_RXN',
	cplx(name = 'ASPARTASE_CPLX', loc = 'cyt') +
	met(name = 'L_ASPARTATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'ASPARTASE_CPLX', loc = 'cyt') +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FUM', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ASPARTASE_RXN', 1.000000), 
	Parameter('rvs_ASPARTASE_RXN', 1.000000))
Rule('ASPCARBTRANS_RXN',
	cplx(name = 'ASPCARBTRANS_CPLX', loc = 'cyt') +
	met(name = 'L_ASPARTATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBAMOYL_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'ASPCARBTRANS_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBAMYUL_L_ASPARTATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ASPCARBTRANS_RXN', 1.000000), 
	Parameter('rvs_ASPCARBTRANS_RXN', 0.000000))
Rule('ASPARTATEKIN_RXN',
	cplx(name = 'ASPKINIHOMOSERDEHYDROGI_CPLX', loc = 'cyt') +
	met(name = 'L_ASPARTATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ASPKINIHOMOSERDEHYDROGI_CPLX', loc = 'cyt') +
	met(name = 'L_BETA_ASPARTYL_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ASPARTATEKIN_RXN', 1.000000), 
	Parameter('rvs_ASPARTATEKIN_RXN', 0.000000))
Rule('HOMOSERDEHYDROG_RXN',
	cplx(name = 'ASPKINIHOMOSERDEHYDROGI_CPLX', loc = 'cyt') +
	met(name = 'NAD_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HOMO_SER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'ASPKINIHOMOSERDEHYDROGI_CPLX', loc = 'cyt') +
	met(name = 'NADH_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_ASPARTATE_SEMIALDEHYDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_HOMOSERDEHYDROG_RXN', 0.000000), 
	Parameter('rvs_HOMOSERDEHYDROG_RXN', 1.000000))
Rule('ASPARTATE__TRNA_LIGASE_RXN',
	cplx(name = 'ASPS_CPLX', loc = 'cyt') +
	met(name = 'ASP_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_ASPARTATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ASPS_CPLX', loc = 'cyt') +
	met(name = 'Charged_ASP_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ASPARTATE__TRNA_LIGASE_RXN', 1.000000), 
	Parameter('rvs_ASPARTATE__TRNA_LIGASE_RXN', 0.000000))
Rule('BADH_RXN',
	cplx(name = 'BADH_CPLX', loc = 'cyt') +
	met(name = 'BETAINE_ALDEHYDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'BADH_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'BETAINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_BADH_RXN', 1.000000), 
	Parameter('rvs_BADH_RXN', 0.000000))
Rule('BETAGALACTOSID_RXN',
	cplx(name = 'BETAGALACTOSID_CPLX', loc = 'cyt') +
	met(name = 'CPD_15972', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'BETAGALACTOSID_CPLX', loc = 'cyt') +
	met(name = 'GALACTOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Glucopyranose', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_BETAGALACTOSID_RXN', 1.000000), 
	Parameter('rvs_BETAGALACTOSID_RXN', 0.000000))
Rule('RXN0_5363',
	cplx(name = 'BETAGALACTOSID_CPLX', loc = 'cyt') +
	met(name = 'Alpha_lactose', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'BETAGALACTOSID_CPLX', loc = 'cyt') +
	met(name = 'ALLOLACTOSE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5363', 1.000000), 
	Parameter('rvs_RXN0_5363', 1.000000))
Rule('RXN_17726',
	cplx(name = 'BETAGALACTOSID_CPLX', loc = 'cyt') +
	met(name = 'CPD_3561', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'BETAGALACTOSID_CPLX', loc = 'cyt') +
	met(name = 'GALACTOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Fructofuranose', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17726', 1.000000), 
	Parameter('rvs_RXN_17726', 0.000000))
Rule('RXN0_7219',
	cplx(name = 'BETAGALACTOSID_CPLX', loc = 'cyt') +
	met(name = 'CPD_3785', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'BETAGALACTOSID_CPLX', loc = 'cyt') +
	met(name = 'GALACTOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_ARABINOSE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7219', 1.000000), 
	Parameter('rvs_RXN0_7219', 0.000000))
Rule('BIOTIN_CARBOXYL_RXN',
	cplx(name = 'BIOTIN_CARBOXYL_CPLX', loc = 'cyt') +
	met(name = 'biotin_L_lysine_in_BCCP_dimers', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HCO3', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'BIOTIN_CARBOXYL_CPLX', loc = 'cyt') +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'carboxybiotin_L_lysine_in_BCCP_dimers', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_BIOTIN_CARBOXYL_RXN', 1.000000), 
	Parameter('rvs_BIOTIN_CARBOXYL_RXN', 0.000000))
Rule('_2dot8dot1dot6_RXN',
	cplx(name = 'BIOTIN_SYN_CPLX', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Sulfurated_Sulfur_Acceptors', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DETHIOBIOTIN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Reduced_2Fe_2S_Ferredoxins', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'BIOTIN_SYN_CPLX', loc = 'cyt') +
	met(name = 'Unsulfurated_Sulfur_Acceptors', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'BIOTIN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CH33ADO', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MET', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Oxidized_2Fe_2S_Ferredoxins', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__2dot8dot1dot6_RXN', 1.000000), 
	Parameter('rvs__2dot8dot1dot6_RXN', 0.000000))
Rule('RXN0_7192',
	prot(name = 'BIOTINLIG_MONOMER', loc = 'cyt') +
	met(name = 'BIOTIN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'BIOTINLIG_MONOMER', loc = 'cyt') +
	met(name = 'BIO_5_AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_7192', 1.000000), 
	Parameter('rvs_RXN0_7192', 0.000000))
Rule('BIOTINLIG_RXN',
	prot(name = 'BIOTINLIG_MONOMER', loc = 'cyt') +
	met(name = 'BCCP_L_lysine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'BIOTIN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'BIOTINLIG_MONOMER', loc = 'cyt') +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'BCCP_biotin_L_lysine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_BIOTINLIG_RXN', 1.000000), 
	Parameter('rvs_BIOTINLIG_RXN', 0.000000))
Rule('BRANCHED_CHAINAMINOTRANSFERVAL_RXN',
	cplx(name = 'BRANCHED_CHAINAMINOTRANSFER_CPLX', loc = 'cyt') +
	met(name = 'VAL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'BRANCHED_CHAINAMINOTRANSFER_CPLX', loc = 'cyt') +
	met(name = '_2_KETO_ISOVALERATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_BRANCHED_CHAINAMINOTRANSFERVAL_RXN', 1.000000), 
	Parameter('rvs_BRANCHED_CHAINAMINOTRANSFERVAL_RXN', 1.000000))
Rule('BRANCHED_CHAINAMINOTRANSFERILEU_RXN',
	cplx(name = 'BRANCHED_CHAINAMINOTRANSFER_CPLX', loc = 'cyt') +
	met(name = 'ILE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'BRANCHED_CHAINAMINOTRANSFER_CPLX', loc = 'cyt') +
	met(name = '_2_KETO_3_METHYL_VALERATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_BRANCHED_CHAINAMINOTRANSFERILEU_RXN', 1.000000), 
	Parameter('rvs_BRANCHED_CHAINAMINOTRANSFERILEU_RXN', 1.000000))
Rule('BRANCHED_CHAINAMINOTRANSFERLEU_RXN',
	cplx(name = 'BRANCHED_CHAINAMINOTRANSFER_CPLX', loc = 'cyt') +
	met(name = 'LEU', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'BRANCHED_CHAINAMINOTRANSFER_CPLX', loc = 'cyt') +
	met(name = '_2K_4CH3_PENTANOATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_BRANCHED_CHAINAMINOTRANSFERLEU_RXN', 1.000000), 
	Parameter('rvs_BRANCHED_CHAINAMINOTRANSFERLEU_RXN', 1.000000))
Rule('GLUTATHIONE_PEROXIDASE_RXN',
	prot(name = 'BTUE_MONOMER', loc = 'per') +
	met(name = 'HYDROGEN_PEROXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLUTATHIONE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'BTUE_MONOMER', loc = 'per') +
	met(name = 'OXIDIZED_GLUTATHIONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLUTATHIONE_PEROXIDASE_RXN', 1.000000), 
	Parameter('rvs_GLUTATHIONE_PEROXIDASE_RXN', 0.000000))
Rule('RXN0_267',
	prot(name = 'BTUE_MONOMER', loc = 'per') +
	met(name = 'Red_Thioredoxin', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HYDROGEN_PEROXIDE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'BTUE_MONOMER', loc = 'per') +
	met(name = 'Ox_Thioredoxin', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_267', 1.000000), 
	Parameter('rvs_RXN0_267', 0.000000))
Rule('LCARNCOALIG_RXN',
	prot(name = 'CAIC_MONOMER', loc = 'cyt') +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARNITINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'CAIC_MONOMER', loc = 'cyt') +
	met(name = 'L_CARNITINYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_LCARNCOALIG_RXN', 1.000000), 
	Parameter('rvs_LCARNCOALIG_RXN', 0.000000))
Rule('RXN0_5224',
	cplx(name = 'CARBODEHYDRAT_CPLX', loc = 'cyt') +
	met(name = 'HCO3', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CARBODEHYDRAT_CPLX', loc = 'cyt') +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5224', 1.000000), 
	Parameter('rvs_RXN0_5224', 1.000000))
Rule('CARBPSYN_RXN',
	cplx(name = 'CARBPSYN_CPLX', loc = 'cyt') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HCO3', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CARBPSYN_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBAMOYL_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_CARBPSYN_RXN', 1.000000), 
	Parameter('rvs_CARBPSYN_RXN', 0.000000))
Rule('CARDIOLIPSYN_RXN',
	prot(name = 'CARDIOLIPSYN_MONOMER', loc = 'imem') +
	met(name = 'L_1_PHOSPHATIDYL_GLYCEROL', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'CARDIOLIPSYN_MONOMER', loc = 'imem') +
	met(name = 'CARDIOLIPIN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLYCEROL', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_CARDIOLIPSYN_RXN', 1.000000), 
	Parameter('rvs_CARDIOLIPSYN_RXN', 0.000000))
Rule('RXN0_3601',
	cplx(name = 'CARNDEHYDRA_CPLX', loc = 'cyt') +
	met(name = 'CARNITINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GAMMA_BUTYROBETAINYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CARNDEHYDRA_CPLX', loc = 'cyt') +
	met(name = 'L_CARNITINYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GAMMA_BUTYROBETAINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_3601', 1.000000), 
	Parameter('rvs_RXN0_3601', 0.000000))
Rule('CARNDETRU_RXN',
	prot(name = 'CARNRACE_MONOMER', loc = 'cyt') +
	met(name = 'L_CARNITINYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'CARNRACE_MONOMER', loc = 'cyt') +
	met(name = 'CROTONOBETAINYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_CARNDETRU_RXN', 1.000000), 
	Parameter('rvs_CARNDETRU_RXN', 1.000000))
Rule('CDPDIGLYPYPHOSPHA_RXN',
	prot(name = 'CDPDIGLYPYPHOSPHA_MONOMER', loc = 'imem') +
	met(name = 'CDPDIACYLGLYCEROL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'CDPDIGLYPYPHOSPHA_MONOMER', loc = 'imem') +
	met(name = 'L_PHOSPHATIDATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_CDPDIGLYPYPHOSPHA_RXN', 1.000000), 
	Parameter('rvs_CDPDIGLYPYPHOSPHA_RXN', 0.000000))
Rule('CDPDIGLYSYN_RXN',
	prot(name = 'CDPDIGLYSYN_MONOMER', loc = 'imem') +
	met(name = 'CTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_PHOSPHATIDATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'CDPDIGLYSYN_MONOMER', loc = 'imem') +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CDPDIACYLGLYCEROL', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_CDPDIGLYSYN_RXN', 1.000000), 
	Parameter('rvs_CDPDIGLYSYN_RXN', 0.000000))
Rule('RXN0_5515',
	prot(name = 'CDPDIGLYSYN_MONOMER', loc = 'imem') +
	met(name = 'CTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_3_4_Saturated_L_Phosphatidates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'CDPDIGLYSYN_MONOMER', loc = 'imem') +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CDP_2_3_4_Saturated_Diacylglycerols', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_5515', 1.000000), 
	Parameter('rvs_RXN0_5515', 0.000000))
Rule('_2dot1dot1dot79_RXN',
	cplx(name = 'CFA_CPLX', loc = 'imem') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Phospholipid_Olefinic_Fatty_Acids', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CFA_CPLX', loc = 'imem') +
	met(name = 'Phospholipid_Cyclopropane_Fatty_Acids', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__2dot1dot1dot79_RXN', 1.000000), 
	Parameter('rvs__2dot1dot1dot79_RXN', 0.000000))
Rule('CHD_RXN',
	prot(name = 'CHD_MONOMER', loc = 'cyt') +
	met(name = 'CHOLINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Acceptor', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'CHD_MONOMER', loc = 'cyt') +
	met(name = 'BETAINE_ALDEHYDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Donor_H2', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_CHD_RXN', 1.000000), 
	Parameter('rvs_CHD_RXN', 1.000000))
Rule('RXN0_7230',
	prot(name = 'CHD_MONOMER', loc = 'cyt') +
	met(name = 'ETR_Quinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CHOLINE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'CHD_MONOMER', loc = 'cyt') +
	met(name = 'ETR_Quinols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'BETAINE_ALDEHYDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7230', 1.000000), 
	Parameter('rvs_RXN0_7230', 0.000000))
Rule('RXN0_7231',
	prot(name = 'CHD_MONOMER', loc = 'cyt') +
	met(name = 'ETR_Quinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'BETAINE_ALDEHYDE_HYDRATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'CHD_MONOMER', loc = 'cyt') +
	met(name = 'ETR_Quinols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'BETAINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7231', 1.000000), 
	Parameter('rvs_RXN0_7231', 0.000000))
Rule('CHER_RXN',
	prot(name = 'CHER_MONOMER', loc = 'imem') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Protein_alpha_L_Glutamates', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'CHER_MONOMER', loc = 'imem') +
	met(name = 'protein_L_glutamate_O4_methyl_ester', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_CHER_RXN', 1.000000), 
	Parameter('rvs_CHER_RXN', 0.000000))
Rule('CHERTSRM_RXN',
	prot(name = 'CHER_MONOMER', loc = 'imem') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TSR_GLU', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'CHER_MONOMER', loc = 'imem') +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TSR_GLUME', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_CHERTSRM_RXN', 1.000000), 
	Parameter('rvs_CHERTSRM_RXN', 0.000000))
Rule('CHERTRGM_RXN',
	prot(name = 'CHER_MONOMER', loc = 'imem') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TRG_GLU', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'CHER_MONOMER', loc = 'imem') +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TRG_GLUME', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_CHERTRGM_RXN', 1.000000), 
	Parameter('rvs_CHERTRGM_RXN', 0.000000))
Rule('CHERTARM_RXN',
	prot(name = 'CHER_MONOMER', loc = 'imem') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TAR_GLU', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'CHER_MONOMER', loc = 'imem') +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TAR_GLUME', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_CHERTARM_RXN', 1.000000), 
	Parameter('rvs_CHERTARM_RXN', 0.000000))
Rule('CHERTAPM_RXN',
	prot(name = 'CHER_MONOMER', loc = 'imem') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TAP_GLU', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'CHER_MONOMER', loc = 'imem') +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TAP_GLUME', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_CHERTAPM_RXN', 1.000000), 
	Parameter('rvs_CHERTAPM_RXN', 0.000000))
Rule('RXN_19922',
	prot(name = 'CHER_MONOMER', loc = 'imem') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLUTATHIONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'CHER_MONOMER', loc = 'imem') +
	met(name = 'S_METHYLGLUTATHIONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_19922', 1.000000), 
	Parameter('rvs_RXN_19922', 0.000000))
Rule('CHEYDEPHOS_RXN',
	cplx(name = 'CHEZ_CPLX', loc = 'imem') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PHOSPHO_CHEY', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CHEZ_CPLX', loc = 'imem') +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CHEY_MONOMER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_CHEYDEPHOS_RXN', 1.000000), 
	Parameter('rvs_CHEYDEPHOS_RXN', 0.000000))
Rule('CHORISMATEMUT_RXN',
	cplx(name = 'CHORISMUTPREPHENDEHYDRAT_CPLX', loc = 'cyt') +
	met(name = 'CHORISMATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CHORISMUTPREPHENDEHYDRAT_CPLX', loc = 'cyt') +
	met(name = 'PREPHENATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_CHORISMATEMUT_RXN', 1.000000), 
	Parameter('rvs_CHORISMATEMUT_RXN', 0.000000))
Rule('PREPHENATEDEHYDRAT_RXN',
	cplx(name = 'CHORISMUTPREPHENDEHYDRAT_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PREPHENATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CHORISMUTPREPHENDEHYDRAT_CPLX', loc = 'cyt') +
	met(name = 'PHENYL_PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PREPHENATEDEHYDRAT_RXN', 1.000000), 
	Parameter('rvs_PREPHENATEDEHYDRAT_RXN', 0.000000))
Rule('PREPHENATEDEHYDROG_RXN',
	cplx(name = 'CHORISMUTPREPHENDEHYDROG_CPLX', loc = 'cyt') +
	met(name = 'PREPHENATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CHORISMUTPREPHENDEHYDROG_CPLX', loc = 'cyt') +
	met(name = 'P_HYDROXY_PHENYLPYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PREPHENATEDEHYDROG_RXN', 1.000000), 
	Parameter('rvs_PREPHENATEDEHYDROG_RXN', 0.000000))
Rule('CHORPYRLY_RXN',
	prot(name = 'CHORPYRLY_MONOMER', loc = 'cyt') +
	met(name = 'CHORISMATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'CHORPYRLY_MONOMER', loc = 'cyt') +
	met(name = '_4_hydroxybenzoate', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_CHORPYRLY_RXN', 1.000000), 
	Parameter('rvs_CHORPYRLY_RXN', 0.000000))
Rule('CITC_RXN',
	prot(name = 'CITC_MONOMER', loc = 'cyt') +
	met(name = 'HOLO_CITRATE_LYASE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACET', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'CITC_MONOMER', loc = 'cyt') +
	met(name = 'CITRATE_LYASE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_CITC_RXN', 1.000000), 
	Parameter('rvs_CITC_RXN', 0.000000))
Rule('CITSYN_RXN',
	prot(name = 'CITRATE_SI_SYNTHASE', loc = 'cyt') +
	met(name = 'OXALACETIC_ACID', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'CITRATE_SI_SYNTHASE', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CIT', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_CITSYN_RXN', 1.000000), 
	Parameter('rvs_CITSYN_RXN', 0.000000))
Rule('RXN_11832',
	prot(name = 'CMPKI_MONOMER', loc = 'cyt') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CMP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'CMPKI_MONOMER', loc = 'cyt') +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CDP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11832', 1.000000), 
	Parameter('rvs_RXN_11832', 1.000000))
Rule('RXN_7913',
	prot(name = 'CMPKI_MONOMER', loc = 'cyt') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DCMP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'CMPKI_MONOMER', loc = 'cyt') +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DCDP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_7913', 1.000000), 
	Parameter('rvs_RXN_7913', 0.000000))
Rule('PANTEPADENYLYLTRAN_RXN',
	cplx(name = 'COADTRI_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PANTETHEINE_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'COADTRI_CPLX', loc = 'cyt') +
	met(name = 'DEPHOSPHO_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_PANTEPADENYLYLTRAN_RXN', 1.000000), 
	Parameter('rvs_PANTEPADENYLYLTRAN_RXN', 0.000000))
Rule('BTUR2_RXN',
	prot(name = 'COBALADENOSYLTRANS_MONOMER', loc = 'cyt') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_20903', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Reduced_Flavoproteins', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'COBALADENOSYLTRANS_MONOMER', loc = 'cyt') +
	met(name = 'ADENOSYLCOBINAMIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'P3I', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Oxidized_Flavoproteins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_BTUR2_RXN', 1.000000), 
	Parameter('rvs_BTUR2_RXN', 0.000000))
Rule('COBALADENOSYLTRANS_RXN',
	prot(name = 'COBALADENOSYLTRANS_MONOMER', loc = 'cyt') +
	met(name = 'CPD_20905', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'COBALADENOSYLTRANS_MONOMER', loc = 'cyt') +
	met(name = 'B12_Corrinoid_Adenosyltranferase', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'P3I', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_COBALADENOSYLTRANS_RXN', 1.000000), 
	Parameter('rvs_COBALADENOSYLTRANS_RXN', 0.000000))
Rule('COBALAMIN5PSYN_RXN',
	prot(name = 'COBS_MONOMER', loc = 'imem') +
	met(name = 'ADENOSYLCOBINAMIDE_GDP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ALPHA_RIBAZOLE_5_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'COBS_MONOMER', loc = 'imem') +
	met(name = 'ADENOSYLCOBALAMIN_5_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_COBALAMIN5PSYN_RXN', 1.000000), 
	Parameter('rvs_COBALAMIN5PSYN_RXN', 0.000000))
Rule('COBINPGUANYLYLTRANS_RXN',
	cplx(name = 'COBU_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYLCOBINAMIDE_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GTP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'COBU_CPLX', loc = 'cyt') +
	met(name = 'ADENOSYLCOBINAMIDE_GDP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_COBINPGUANYLYLTRANS_RXN', 1.000000), 
	Parameter('rvs_COBINPGUANYLYLTRANS_RXN', 0.000000))
Rule('COBINAMIDEKIN_RXN',
	cplx(name = 'COBU_CPLX', loc = 'cyt') +
	met(name = 'ADENOSYLCOBINAMIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'COBU_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYLCOBINAMIDE_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_COBINAMIDEKIN_RXN', 1.000000), 
	Parameter('rvs_COBINAMIDEKIN_RXN', 0.000000))
Rule('CYCPHOSDIESTER_RXN',
	prot(name = 'CPDB_MONOMER', loc = 'per') +
	met(name = 'Cyclic_2_3_Ribonucleoside_Monophosphates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'CPDB_MONOMER', loc = 'per') +
	met(name = '_3_Phosphomonucleotides', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_CYCPHOSDIESTER_RXN', 1.000000), 
	Parameter('rvs_CYCPHOSDIESTER_RXN', 0.000000))
Rule('RXN_14124',
	prot(name = 'CPDB_MONOMER', loc = 'per') +
	met(name = 'CPD_3708', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'CPDB_MONOMER', loc = 'per') +
	met(name = 'GUANOSINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14124', 1.000000), 
	Parameter('rvs_RXN_14124', 0.000000))
Rule('RXN_14113',
	prot(name = 'CPDB_MONOMER', loc = 'per') +
	met(name = 'CPD_3707', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'CPDB_MONOMER', loc = 'per') +
	met(name = 'CPD_3706', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14113', 1.000000), 
	Parameter('rvs_RXN_14113', 0.000000))
Rule('RXN_14112',
	prot(name = 'CPDB_MONOMER', loc = 'per') +
	met(name = 'CPD_3713', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'CPDB_MONOMER', loc = 'per') +
	met(name = 'CPD_3711', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14112', 1.000000), 
	Parameter('rvs_RXN_14112', 0.000000))
Rule('RXN_14091',
	prot(name = 'CPDB_MONOMER', loc = 'per') +
	met(name = 'CPD_3725', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'CPDB_MONOMER', loc = 'per') +
	met(name = 'CPD_3724', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14091', 1.000000), 
	Parameter('rvs_RXN_14091', 0.000000))
Rule('RXN_14064',
	prot(name = 'CPDB_MONOMER', loc = 'per') +
	met(name = 'CPD_3709', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'CPDB_MONOMER', loc = 'per') +
	met(name = 'CPD_3708', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14064', 1.000000), 
	Parameter('rvs_RXN_14064', 0.000000))
Rule('RXN0_305',
	cplx(name = 'CPLX_171', loc = 'cyt') +
	met(name = 'OH_PYR', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX_171', loc = 'cyt') +
	met(name = 'TARTRONATE_S_ALD', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_305', 1.000000), 
	Parameter('rvs_RXN0_305', 1.000000))
Rule('RXN_18709',
	cplx(name = 'CPLX_3942', loc = 'cyt') +
	met(name = 'TusA_Persulfides', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TusD_L_cysteine', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX_3942', loc = 'cyt') +
	met(name = 'TusA_L_cysteine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TusD_Persulfides', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_18709', 1.000000), 
	Parameter('rvs_RXN_18709', 0.000000))
Rule('_3dot1dot11dot6_RXN',
	cplx(name = 'CPLX_3946', loc = 'cyt') +
	met(name = 'Single_Stranded_DNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX_3946', loc = 'cyt') +
	met(name = 'Ribonucleoside_Monophosphates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SS_Oligodeoxyribonucleotides', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3dot1dot11dot6_RXN', 1.000000), 
	Parameter('rvs__3dot1dot11dot6_RXN', 0.000000))
Rule('ALLANTOINASE_RXN',
	cplx(name = 'CPLX_64', loc = 'cyt') +
	met(name = 'S_ALLANTOIN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX_64', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ALLANTOATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ALLANTOINASE_RXN', 1.000000), 
	Parameter('rvs_ALLANTOINASE_RXN', 0.000000))
Rule('RXN0_5462',
	cplx(name = 'CPLX_722', loc = 'per') +
	met(name = 'GTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX_722', loc = 'per') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GDP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5462', 1.000000), 
	Parameter('rvs_RXN0_5462', 0.000000))
Rule('RXN_10940',
	cplx(name = 'CPLX_722', loc = 'per') +
	met(name = 'MI_HEXAKISPHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX_722', loc = 'per') +
	met(name = 'MI_PENTAKISPHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_10940', 1.000000), 
	Parameter('rvs_RXN_10940', 0.000000))
Rule('RXN_17495',
	cplx(name = 'CPLX_722', loc = 'per') +
	met(name = 'MI_PENTAKISPHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX_722', loc = 'per') +
	met(name = 'CPD_18901', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17495', 1.000000), 
	Parameter('rvs_RXN_17495', 0.000000))
Rule('RXN_17489',
	cplx(name = 'CPLX_722', loc = 'per') +
	met(name = 'CPD_18901', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX_722', loc = 'per') +
	met(name = 'CPD_18902', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17489', 1.000000), 
	Parameter('rvs_RXN_17489', 0.000000))
Rule('RXN_17490',
	cplx(name = 'CPLX_722', loc = 'per') +
	met(name = 'CPD_18902', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX_722', loc = 'per') +
	met(name = 'CPD_18903', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17490', 1.000000), 
	Parameter('rvs_RXN_17490', 0.000000))
Rule('RXN_17493',
	cplx(name = 'CPLX_722', loc = 'per') +
	met(name = 'CPD_18903', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX_722', loc = 'per') +
	met(name = 'CPD_6746', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17493', 1.000000), 
	Parameter('rvs_RXN_17493', 0.000000))
Rule('ALLANTOATE_DEIMINASE_RXN',
	cplx(name = 'CPLX_7524', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ALLANTOATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX_7524', loc = 'cyt') +
	met(name = 'CPD0_2298', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ALLANTOATE_DEIMINASE_RXN', 1.000000), 
	Parameter('rvs_ALLANTOATE_DEIMINASE_RXN', 0.000000))
Rule('RXN_17809',
	cplx(name = 'CPLX_8331', loc = 'cyt') +
	met(name = 'CPD_19179', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX_8331', loc = 'cyt') +
	met(name = 'PRECURSOR_Z', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17809', 1.000000), 
	Parameter('rvs_RXN_17809', 0.000000))
Rule('_5dot3dot1dot17_RXN',
	cplx(name = 'CPLX_8401', loc = 'cyt') +
	met(name = 'CPD_37', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX_8401', loc = 'cyt') +
	met(name = 'CPD_343', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__5dot3dot1dot17_RXN', 1.000000), 
	Parameter('rvs__5dot3dot1dot17_RXN', 1.000000))
Rule('METHYLISOCITRATE_LYASE_RXN',
	cplx(name = 'CPLX0_1021', loc = 'cyt') +
	met(name = 'CPD_618', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_1021', loc = 'cyt') +
	met(name = 'SUC', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_METHYLISOCITRATE_LYASE_RXN', 1.000000), 
	Parameter('rvs_METHYLISOCITRATE_LYASE_RXN', 1.000000))
Rule('RXN0_1321',
	cplx(name = 'CPLX0_1101', loc = 'cyt') +
	met(name = 'Guanine34_in_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_7_AMINOMETHYL_7_DEAZAGUANINE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_1101', loc = 'cyt') +
	met(name = 'tRNA_with_7_aminomethyl_7_deazaguanine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GUANINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_1321', 1.000000), 
	Parameter('rvs_RXN0_1321', 0.000000))
Rule('RXN_11588',
	cplx(name = 'CPLX0_1121', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_23S_rRNA_guanine_2551', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_1121', loc = 'cyt') +
	met(name = '_23S_rRNA_2_O_methylguanosine2251', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11588', 1.000000), 
	Parameter('rvs_RXN_11588', 0.000000))
Rule('_2dot9dot1dot1_RXN',
	cplx(name = 'CPLX0_1141', loc = 'cyt') +
	met(name = 'SEPO3', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_seryl_SEC_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_1141', loc = 'cyt') +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Charged_SEC_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__2dot9dot1dot1_RXN', 1.000000), 
	Parameter('rvs__2dot9dot1dot1_RXN', 0.000000))
Rule('RXN0_1382',
	cplx(name = 'CPLX0_1142', loc = 'cyt') +
	met(name = 'FORMYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXALATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_1142', loc = 'cyt') +
	met(name = 'FORMATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXALYL_COA', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_1382', 1.000000), 
	Parameter('rvs_RXN0_1382', 1.000000))
Rule('RXN0_5103',
	cplx(name = 'CPLX0_1163', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'General_Protein_Substrates', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_1163', loc = 'cyt') +
	met(name = 'Peptides_holder', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_5103', 1.000000), 
	Parameter('rvs_RXN0_5103', 0.000000))
Rule('ADPSUGPPHOSPHAT_RXN',
	cplx(name = 'CPLX0_1221', loc = 'cyt') +
	met(name = 'ADP_SUGARS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_1221', loc = 'cyt') +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Alpha_D_aldose_1_phosphates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ADPSUGPPHOSPHAT_RXN', 1.000000), 
	Parameter('rvs_ADPSUGPPHOSPHAT_RXN', 0.000000))
Rule('_1TRANSKETO_RXN',
	cplx(name = 'CPLX0_1261', loc = 'cyt') +
	met(name = 'D_SEDOHEPTULOSE_7_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GAP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_1261', loc = 'cyt') +
	met(name = 'RIBOSE_5P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'XYLULOSE_5_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__1TRANSKETO_RXN', 1.000000), 
	Parameter('rvs__1TRANSKETO_RXN', 1.000000))
Rule('_2TRANSKETO_RXN',
	cplx(name = 'CPLX0_1261', loc = 'cyt') +
	met(name = 'ERYTHROSE_4P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'XYLULOSE_5_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_1261', loc = 'cyt') +
	met(name = 'FRUCTOSE_6P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GAP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__2TRANSKETO_RXN', 1.000000), 
	Parameter('rvs__2TRANSKETO_RXN', 1.000000))
Rule('DARAB5PISOM_RXN',
	cplx(name = 'CPLX0_1262', loc = 'cyt') +
	met(name = 'ARABINOSE_5P', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_1262', loc = 'cyt') +
	met(name = 'RIBULOSE_5P', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DARAB5PISOM_RXN', 1.000000), 
	Parameter('rvs_DARAB5PISOM_RXN', 1.000000))
Rule('RXN0_6480',
	cplx(name = 'CPLX0_1382', loc = 'cyt') +
	met(name = 'CPD0_2354', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_1382', loc = 'cyt') +
	met(name = 'tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'tRNA_fragment', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6480', 1.000000), 
	Parameter('rvs_RXN0_6480', 0.000000))
Rule('_3dot1dot26dot5_RXN',
	cplx(name = 'CPLX0_1382', loc = 'cyt') +
	met(name = 'CPD0_2352', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_1382', loc = 'cyt') +
	met(name = 'CPD0_2353', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'tRNA_fragment', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3dot1dot26dot5_RXN', 1.000000), 
	Parameter('rvs__3dot1dot26dot5_RXN', 0.000000))
Rule('_4dot3dot1dot15_RXN',
	cplx(name = 'CPLX0_1401', loc = 'cyt') +
	met(name = '_23_Diaminopropanoate', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_1401', loc = 'cyt') +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__4dot3dot1dot15_RXN', 1.000000), 
	Parameter('rvs__4dot3dot1dot15_RXN', 0.000000))
Rule('RXN0_1483',
	cplx(name = 'CPLX0_1421', loc = 'cyt') +
	met(name = 'FEplus2', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_1421', loc = 'cyt') +
	met(name = 'FEplus3', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_1483', 1.000000), 
	Parameter('rvs_RXN0_1483', 0.000000))
Rule('ADENOSYLHOMOCYSTEINE_NUCLEOSIDASE_RXN',
	cplx(name = 'CPLX0_1541', loc = 'cyt') +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_1541', loc = 'cyt') +
	met(name = 'CPD_564', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ADENOSYLHOMOCYSTEINE_NUCLEOSIDASE_RXN', 1.000000), 
	Parameter('rvs_ADENOSYLHOMOCYSTEINE_NUCLEOSIDASE_RXN', 0.000000))
Rule('METHYLTHIOADENOSINE_NUCLEOSIDASE_RXN',
	cplx(name = 'CPLX0_1541', loc = 'cyt') +
	met(name = '_5_METHYLTHIOADENOSINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_1541', loc = 'cyt') +
	met(name = 'CPD_560', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_METHYLTHIOADENOSINE_NUCLEOSIDASE_RXN', 1.000000), 
	Parameter('rvs_METHYLTHIOADENOSINE_NUCLEOSIDASE_RXN', 0.000000))
Rule('RXN0_6550',
	cplx(name = 'CPLX0_1541', loc = 'cyt') +
	met(name = 'CH33ADO', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_1541', loc = 'cyt') +
	met(name = 'CPD0_2167', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6550', 1.000000), 
	Parameter('rvs_RXN0_6550', 0.000000))
Rule('RXN0_1842',
	cplx(name = 'CPLX0_1581', loc = 'omem') +
	met(name = 'CPD_17523', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_1283', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_1581', loc = 'omem') +
	met(name = 'HEPTA_ACYLATED_LIPID_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_Acylglycero_Phosphocholines', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_1842', 1.000000), 
	Parameter('rvs_RXN0_1842', 0.000000))
Rule('RXN0_2101',
	cplx(name = 'CPLX0_1601', loc = 'per') +
	met(name = 'SELENITE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Acceptor', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_1601', loc = 'per') +
	met(name = 'SELENATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Donor_H2', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_2101', 0.000000), 
	Parameter('rvs_RXN0_2101', 1.000000))
Rule('RXN0_6523',
	cplx(name = 'CPLX0_1621', loc = 'cyt') +
	met(name = 'RNASE_G_DEGRADATION_SUBSTRATE_MRNA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_1621', loc = 'cyt') +
	met(name = 'mRNA_Fragments', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_6523', 1.000000), 
	Parameter('rvs_RXN0_6523', 0.000000))
Rule('ADENINE_DEAMINASE_RXN',
	cplx(name = 'CPLX0_1683', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENINE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_1683', loc = 'cyt') +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HYPOXANTHINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_ADENINE_DEAMINASE_RXN', 1.000000), 
	Parameter('rvs_ADENINE_DEAMINASE_RXN', 0.000000))
Rule('CATAL_RXN',
	cplx(name = 'CPLX0_1683', loc = 'cyt') +
	met(name = 'HYDROGEN_PEROXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_1683', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_CATAL_RXN', 1.000000), 
	Parameter('rvs_CATAL_RXN', 0.000000))
Rule('RXN0_2042',
	cplx(name = 'CPLX0_1762', loc = 'cyt') +
	met(name = 'CPD_207', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_1762', loc = 'cyt') +
	met(name = 'CPD0_2362', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_2042', 1.000000), 
	Parameter('rvs_RXN0_2042', 0.000000))
Rule('_3dot1dot13dot3_RXN',
	cplx(name = 'CPLX0_1821', loc = 'cyt') +
	met(name = 'Oligonucleotides', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_1821', loc = 'cyt') +
	met(name = 'Nucleoside_Monophosphates', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd__3dot1dot13dot3_RXN', 1.000000), 
	Parameter('rvs__3dot1dot13dot3_RXN', 0.000000))
Rule('RXN0_2201',
	cplx(name = 'CPLX0_1962', loc = 'cyt') +
	met(name = 'SER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_1962', loc = 'cyt') +
	met(name = '_2_AMINOMALONATE_SEMIALDEHYDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_2201', 1.000000), 
	Parameter('rvs_RXN0_2201', 0.000000))
Rule('RXN_16000',
	cplx(name = 'CPLX0_1962', loc = 'cyt') +
	met(name = 'L_ALLO_THREONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_1962', loc = 'cyt') +
	met(name = 'AMINO_OXOBUT', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_16000', 1.000000), 
	Parameter('rvs_RXN_16000', 0.000000))
Rule('RXN_8974',
	cplx(name = 'CPLX0_1962', loc = 'cyt') +
	met(name = '_3_HYDROXY_PROPIONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_1962', loc = 'cyt') +
	met(name = 'MALONATE_S_ALD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_8974', 0.000000), 
	Parameter('rvs_RXN_8974', 1.000000))
Rule('RXN0_313',
	cplx(name = 'CPLX0_201', loc = 'cyt') +
	met(name = 'FRUCTOSE_6P', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_201', loc = 'cyt') +
	met(name = 'DIHYDROXYACETONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GAP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_313', 1.000000), 
	Parameter('rvs_RXN0_313', 1.000000))
Rule('RXN0_703',
	cplx(name = 'CPLX0_2061', loc = 'cyt') +
	met(name = '_3_KETO_L_GULONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_2061', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_334', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_703', 0.000000), 
	Parameter('rvs_RXN0_703', 1.000000))
Rule('RXN_12444',
	cplx(name = 'CPLX0_224', loc = 'cyt') +
	met(name = 'FMNH2', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_224', loc = 'cyt') +
	met(name = 'FMN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_12444', 0.000000), 
	Parameter('rvs_RXN_12444', 1.000000))
Rule('RXN0_280',
	cplx(name = 'CPLX0_225', loc = 'cyt') +
	met(name = 'Alkanesulfonates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FMNH2', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	cplx(name = 'CPLX0_225', loc = 'cyt') +
	met(name = 'Aldehydes', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SO3', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FMN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_280', 1.000000), 
	Parameter('rvs_RXN0_280', 0.000000))
Rule('RXN_13418',
	cplx(name = 'CPLX0_225', loc = 'cyt') +
	met(name = 'CPD_3745', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FMNH2', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	cplx(name = 'CPLX0_225', loc = 'cyt') +
	met(name = 'GLYCOLALDEHYDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SO3', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FMN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_13418', 1.000000), 
	Parameter('rvs_RXN_13418', 0.000000))
Rule('RXN0_299',
	cplx(name = 'CPLX0_227', loc = 'cyt') +
	met(name = 'TAURINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	cplx(name = 'CPLX0_227', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_1772', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SO3', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SUC', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_299', 1.000000), 
	Parameter('rvs_RXN0_299', 0.000000))
Rule('RNTRACTIV_RXN',
	cplx(name = 'CPLX0_229', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Ribonuc_tri_P_reductases_inactive', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Reduced_flavodoxins', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	cplx(name = 'CPLX0_229', loc = 'cyt') +
	met(name = 'Ribonuc_tri_P_reductases_active', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CH33ADO', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MET', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Flavodoxins_Semiquinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RNTRACTIV_RXN', 1.000000), 
	Parameter('rvs_RNTRACTIV_RXN', 0.000000))
Rule('PHOSICITDEHASE_RXN',
	cplx(name = 'CPLX0_230', loc = 'cyt') +
	met(name = 'isocitrate_dehydrogenase', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_230', loc = 'cyt') +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Iso_Cit', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PHOSICITDEHASE_RXN', 1.000000), 
	Parameter('rvs_PHOSICITDEHASE_RXN', 1.000000))
Rule('DEPHOSICITDEHASE_RXN',
	cplx(name = 'CPLX0_230', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Iso_Cit', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_230', loc = 'cyt') +
	met(name = 'isocitrate_dehydrogenase', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DEPHOSICITDEHASE_RXN', 1.000000), 
	Parameter('rvs_DEPHOSICITDEHASE_RXN', 0.000000))
Rule('_2dot7dot7dot60_RXN',
	cplx(name = 'CPLX0_234', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_C_METHYL_D_ERYTHRITOL_4_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CTP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_234', loc = 'cyt') +
	met(name = '_4_CYTIDINE_5_DIPHOSPHO_2_C', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd__2dot7dot7dot60_RXN', 1.000000), 
	Parameter('rvs__2dot7dot7dot60_RXN', 0.000000))
Rule('GLYOXYLATE_REDUCTASE_NADPplus_RXN',
	cplx(name = 'CPLX0_235', loc = 'cyt') +
	met(name = 'GLYCOLLATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_235', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLYOX', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLYOXYLATE_REDUCTASE_NADPplus_RXN', 0.000000), 
	Parameter('rvs_GLYOXYLATE_REDUCTASE_NADPplus_RXN', 1.000000))
Rule('RXN0_300',
	cplx(name = 'CPLX0_235', loc = 'cyt') +
	met(name = 'GLYCERATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_235', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OH_PYR', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_300', 0.000000), 
	Parameter('rvs_RXN0_300', 1.000000))
Rule('_1dot1dot1dot215_RXN',
	cplx(name = 'CPLX0_235', loc = 'cyt') +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLUCONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_235', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_377', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__1dot1dot1dot215_RXN', 0.000000), 
	Parameter('rvs__1dot1dot1dot215_RXN', 1.000000))
Rule('RXN0_7021',
	cplx(name = 'CPLX0_235', loc = 'cyt') +
	met(name = 'L_IDONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_235', loc = 'cyt') +
	met(name = 'CPD_13059', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7021', 0.000000), 
	Parameter('rvs_RXN0_7021', 1.000000))
Rule('YIAE1_RXN',
	cplx(name = 'CPLX0_235', loc = 'cyt') +
	met(name = '_5_DEHYDROGLUCONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_235', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_25_DIDEHYDRO_D_GLUCONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_YIAE1_RXN', 0.000000), 
	Parameter('rvs_YIAE1_RXN', 1.000000))
Rule('ARYLAMINE_N_ACETYLTRANSFERASE_RXN',
	cplx(name = 'CPLX0_236', loc = 'cyt') +
	met(name = 'Aryl_Amines', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_236', loc = 'cyt') +
	met(name = 'N_acetylarylamines', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ARYLAMINE_N_ACETYLTRANSFERASE_RXN', 1.000000), 
	Parameter('rvs_ARYLAMINE_N_ACETYLTRANSFERASE_RXN', 0.000000))
Rule('_2dot3dot1dot118_RXN',
	cplx(name = 'CPLX0_236', loc = 'cyt') +
	met(name = 'N_Hydroxy_Arylamines', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_236', loc = 'cyt') +
	met(name = 'N_Acetoxy_Arylamines', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__2dot3dot1dot118_RXN', 1.000000), 
	Parameter('rvs__2dot3dot1dot118_RXN', 0.000000))
Rule('SERINE_O_ACETTRAN_RXN',
	cplx(name = 'CPLX0_237', loc = 'cyt') +
	met(name = 'SER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_237', loc = 'cyt') +
	met(name = 'ACETYLSERINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_SERINE_O_ACETTRAN_RXN', 1.000000), 
	Parameter('rvs_SERINE_O_ACETTRAN_RXN', 0.000000))
Rule('ARGSUCCINSYN_RXN',
	cplx(name = 'CPLX0_238', loc = 'cyt') +
	met(name = 'L_ASPARTATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_CITRULLINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_238', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_ARGININO_SUCCINATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ARGSUCCINSYN_RXN', 1.000000), 
	Parameter('rvs_ARGSUCCINSYN_RXN', 0.000000))
Rule('RXN0_2382',
	cplx(name = 'CPLX0_2401', loc = 'cyt') +
	met(name = 'INDOLE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_2401', loc = 'cyt') +
	met(name = 'TRP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_2382', 1.000000), 
	Parameter('rvs_RXN0_2382', 0.000000))
Rule('TAGAALDOL_RXN',
	cplx(name = 'CPLX0_240', loc = 'cyt') +
	met(name = 'TAGATOSE_1_6_DIPHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_240', loc = 'cyt') +
	met(name = 'DIHYDROXY_ACETONE_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GAP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_TAGAALDOL_RXN', 1.000000), 
	Parameter('rvs_TAGAALDOL_RXN', 0.000000))
Rule('_5dot99dot1dot3_RXN',
	cplx(name = 'CPLX0_2425', loc = 'cyt') +
	met(name = 'Double_Stranded_DNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_2425', loc = 'cyt') +
	met(name = 'Negatively_super_coiled_DNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__5dot99dot1dot3_RXN', 1.000000), 
	Parameter('rvs__5dot99dot1dot3_RXN', 0.000000))
Rule('RXN0_6385',
	cplx(name = 'CPLX0_242', loc = 'cyt') +
	met(name = 'Red_Thioredoxin', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'S2O3', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	cplx(name = 'CPLX0_242', loc = 'cyt') +
	met(name = 'Ox_Thioredoxin', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SO3', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6385', 1.000000), 
	Parameter('rvs_RXN0_6385', 0.000000))
Rule('THIOSULFATE_SULFURTRANSFERASE_RXN',
	cplx(name = 'CPLX0_242', loc = 'cyt') +
	met(name = 'S2O3', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HCN', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_242', loc = 'cyt') +
	met(name = 'HSCN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SO3', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_THIOSULFATE_SULFURTRANSFERASE_RXN', 1.000000), 
	Parameter('rvs_THIOSULFATE_SULFURTRANSFERASE_RXN', 0.000000))
Rule('R303_RXN',
	cplx(name = 'CPLX0_244', loc = 'cyt') +
	met(name = 'Nitroaromatic_Ox_Compounds', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_244', loc = 'cyt') +
	met(name = 'Nitroaromatic_Red_Compounds', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_R303_RXN', 1.000000), 
	Parameter('rvs_R303_RXN', 0.000000))
Rule('R4_RXN',
	cplx(name = 'CPLX0_245', loc = 'cyt') +
	met(name = 'Alcohols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_245', loc = 'cyt') +
	met(name = 'Alkyl_Hydro_Peroxides', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_R4_RXN', 0.000000), 
	Parameter('rvs_R4_RXN', 1.000000))
Rule('RXN_12588',
	cplx(name = 'CPLX0_246', loc = 'cyt') +
	met(name = 'CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Unsulfurated_Sulfur_Acceptors', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_246', loc = 'cyt') +
	met(name = 'L_ALPHA_ALANINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Sulfurated_Sulfur_Acceptors', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_12588', 1.000000), 
	Parameter('rvs_RXN_12588', 0.000000))
Rule('RXN0_279',
	cplx(name = 'CPLX0_246', loc = 'cyt') +
	met(name = '_3_SULFINOALANINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_246', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_ALPHA_ALANINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SO3', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_279', 1.000000), 
	Parameter('rvs_RXN0_279', 0.000000))
Rule('SELENOCYSTEINE_LYASE_RXN',
	cplx(name = 'CPLX0_246', loc = 'cyt') +
	met(name = 'Donor_H2', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_SELENOCYSTEINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	cplx(name = 'CPLX0_246', loc = 'cyt') +
	met(name = 'L_ALPHA_ALANINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SE_2', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Acceptor', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_SELENOCYSTEINE_LYASE_RXN', 1.000000), 
	Parameter('rvs_SELENOCYSTEINE_LYASE_RXN', 0.000000))
Rule('RXN_15881',
	cplx(name = 'CPLX0_248', loc = 'cyt') +
	met(name = 'L_Cysteine_Desulfurases', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CYS', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_248', loc = 'cyt') +
	met(name = 'Persulfurated_L_cysteine_desulfurases', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_ALPHA_ALANINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_15881', 1.000000), 
	Parameter('rvs_RXN_15881', 0.000000))
Rule('RXN_12587',
	cplx(name = 'CPLX0_248', loc = 'cyt') +
	met(name = 'L_Cysteine_Desulfurase_persulfide', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Unsulfurated_Sulfur_Acceptors', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_248', loc = 'cyt') +
	met(name = 'Cysteine_Desulfurase_L_cysteine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Sulfurated_Sulfur_Acceptors', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_12587', 1.000000), 
	Parameter('rvs_RXN_12587', 1.000000))
Rule('RXN_14382',
	cplx(name = 'CPLX0_248', loc = 'cyt') +
	met(name = 'L_Cysteine_Desulfurase_persulfide', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Sulfur_Carrier_Proteins_ThiI', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_248', loc = 'cyt') +
	met(name = 'Cysteine_Desulfurase_L_cysteine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Sulfurylated_ThiI', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14382', 1.000000), 
	Parameter('rvs_RXN_14382', 0.000000))
Rule('RXN0_308',
	cplx(name = 'CPLX0_248', loc = 'cyt') +
	met(name = 'Cysteine_Desulfurase_L_cysteine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CYS', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_248', loc = 'cyt') +
	met(name = 'L_Cysteine_Desulfurase_persulfide', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_ALPHA_ALANINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_308', 1.000000), 
	Parameter('rvs_RXN0_308', 0.000000))
Rule('RXN_8342',
	cplx(name = 'CPLX0_2502', loc = 'cyt') +
	met(name = 'PRECURSOR_Z', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Thiocarboxylated_MPT_synthases', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_2502', loc = 'cyt') +
	met(name = 'CPD_4', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MPT_Synthase_small_subunits', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_8342', 1.000000), 
	Parameter('rvs_RXN_8342', 0.000000))
Rule('MVHMETH_RXN',
	cplx(name = 'CPLX0_250', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'E_', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_250', loc = 'cyt') +
	met(name = 'HYDROGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_MVHMETH_RXN', 1.000000), 
	Parameter('rvs_MVHMETH_RXN', 0.000000))
Rule('_2_METHYLCITRATE_SYNTHASE_RXN',
	cplx(name = 'CPLX0_251', loc = 'cyt') +
	met(name = 'OXALACETIC_ACID', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROPIONYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_251', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_622', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__2_METHYLCITRATE_SYNTHASE_RXN', 1.000000), 
	Parameter('rvs__2_METHYLCITRATE_SYNTHASE_RXN', 0.000000))
Rule('_2dot3dot1dot180_RXN',
	cplx(name = 'CPLX0_252', loc = 'cyt') +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MALONYL_ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_252', loc = 'cyt') +
	met(name = 'Acetoacetyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__2dot3dot1dot180_RXN', 1.000000), 
	Parameter('rvs__2dot3dot1dot180_RXN', 0.000000))
Rule('ACP_S_ACETYLTRANSFER_RXN',
	cplx(name = 'CPLX0_252', loc = 'cyt') +
	met(name = 'ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_252', loc = 'cyt') +
	met(name = 'ACETYL_ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ACP_S_ACETYLTRANSFER_RXN', 1.000000), 
	Parameter('rvs_ACP_S_ACETYLTRANSFER_RXN', 1.000000))
Rule('RXN0_271',
	cplx(name = 'CPLX0_253', loc = 'cyt') +
	met(name = 'ETR_Quinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_253', loc = 'cyt') +
	met(name = 'ETR_Quinols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_271', 1.000000), 
	Parameter('rvs_RXN0_271', 0.000000))
Rule('RXN0_310',
	cplx(name = 'CPLX0_254', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'METHYL_MALONYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_254', loc = 'cyt') +
	met(name = 'PROPIONYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_310', 1.000000), 
	Parameter('rvs_RXN0_310', 0.000000))
Rule('RXN0_275',
	cplx(name = 'CPLX0_255', loc = 'cyt') +
	met(name = 'PHENYLHYDANTOIN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_255', loc = 'cyt') +
	met(name = 'CPD_8524', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_275', 1.000000), 
	Parameter('rvs_RXN0_275', 0.000000))
Rule('RXN0_3241',
	cplx(name = 'CPLX0_263', loc = 'cyt') +
	met(name = 'CPD_12991', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_263', loc = 'cyt') +
	met(name = 'L_ASPARTATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Amino_Acids_20', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_3241', 1.000000), 
	Parameter('rvs_RXN0_3241', 0.000000))
Rule('RXN0_2941',
	cplx(name = 'CPLX0_2661', loc = 'cyt') +
	met(name = 'DNA_With_Recognition_Site', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_2661', loc = 'cyt') +
	met(name = 'Cleaved_DNA', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_2941', 1.000000), 
	Parameter('rvs_RXN0_2941', 0.000000))
Rule('_3dot4dot21dot53_RXN',
	cplx(name = 'CPLX0_2881', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'General_Protein_Substrates', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_2881', loc = 'cyt') +
	met(name = 'Peptides_holder', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd__3dot4dot21dot53_RXN', 1.000000), 
	Parameter('rvs__3dot4dot21dot53_RXN', 0.000000))
Rule('ASPDECARBOX_RXN',
	cplx(name = 'CPLX0_2901', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_ASPARTATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_2901', loc = 'cyt') +
	met(name = 'B_ALANINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ASPDECARBOX_RXN', 1.000000), 
	Parameter('rvs_ASPDECARBOX_RXN', 0.000000))
Rule('_3dot4dot21dot107_RXN',
	cplx(name = 'CPLX0_2921', loc = 'imem') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'General_Protein_Substrates', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_2921', loc = 'imem') +
	met(name = 'Peptides_holder', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd__3dot4dot21dot107_RXN', 1.000000), 
	Parameter('rvs__3dot4dot21dot107_RXN', 0.000000))
Rule('RXN0_3201',
	cplx(name = 'CPLX0_2941', loc = 'imem') +
	met(name = 'Lipoprotein_signal_peptide', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_2941', loc = 'imem') +
	met(name = 'Peptides_holder', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_3201', 1.000000), 
	Parameter('rvs_RXN0_3201', 0.000000))
Rule('RXN0_3221',
	cplx(name = 'CPLX0_2982', loc = 'imem') +
	met(name = 'General_Protein_Substrates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_2982', loc = 'imem') +
	met(name = 'Peptides_holder', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_3221', 1.000000), 
	Parameter('rvs_RXN0_3221', 0.000000))
Rule('RXN0_6981',
	cplx(name = 'CPLX0_3001', loc = 'cyt') +
	met(name = 'CPD0_1445', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3001', loc = 'cyt') +
	met(name = 'L_ALPHA_ALANINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6981', 1.000000), 
	Parameter('rvs_RXN0_6981', 0.000000))
Rule('_3dot4dot13dot18_RXN',
	cplx(name = 'CPLX0_3001', loc = 'cyt') +
	met(name = 'DIPEPTIDES', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3001', loc = 'cyt') +
	met(name = 'Amino_Acids_20', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd__3dot4dot13dot18_RXN', 1.000000), 
	Parameter('rvs__3dot4dot13dot18_RXN', 0.000000))
Rule('RXN_6622',
	cplx(name = 'CPLX0_3001', loc = 'cyt') +
	met(name = 'CYS_GLY', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3001', loc = 'cyt') +
	met(name = 'CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLY', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_6622', 1.000000), 
	Parameter('rvs_RXN_6622', 0.000000))
Rule('_3_OCTAPRENYL_4_OHBENZOATE_DECARBOX_RXN',
	cplx(name = 'CPLX0_301', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_3_OCTAPRENYL_4_HYDROXYBENZOATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_301', loc = 'cyt') +
	met(name = '_2_OCTAPRENYLPHENOL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3_OCTAPRENYL_4_OHBENZOATE_DECARBOX_RXN', 1.000000), 
	Parameter('rvs__3_OCTAPRENYL_4_OHBENZOATE_DECARBOX_RXN', 0.000000))
Rule('_3dot4dot11dot4_RXN',
	cplx(name = 'CPLX0_3041', loc = 'cyt') +
	met(name = 'TRIPEPTIDES', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3041', loc = 'cyt') +
	met(name = 'DIPEPTIDES', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Amino_Acids_20', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3dot4dot11dot4_RXN', 1.000000), 
	Parameter('rvs__3dot4dot11dot4_RXN', 0.000000))
Rule('_3dot4dot11dot1_RXN',
	cplx(name = 'CPLX0_3061', loc = 'cyt') +
	met(name = 'Protein_With_N_Terminal_X_Pro', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_3061', loc = 'cyt') +
	met(name = 'Amino_Acids_20', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Protein_With_N_Terminal_Pro', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3dot4dot11dot1_RXN', 1.000000), 
	Parameter('rvs__3dot4dot11dot1_RXN', 0.000000))
Rule('_3dot4dot11dot9_RXN',
	cplx(name = 'CPLX0_3081', loc = 'cyt') +
	met(name = 'Peptides_holder', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3081', loc = 'cyt') +
	met(name = 'Amino_Acids_20', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Peptides_holder', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3dot4dot11dot9_RXN', 1.000000), 
	Parameter('rvs__3dot4dot11dot9_RXN', 0.000000))
Rule('_3dot4dot21dot92_RXN',
	cplx(name = 'CPLX0_3101', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'General_Protein_Substrates', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3101', loc = 'cyt') +
	met(name = 'Peptides_holder', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd__3dot4dot21dot92_RXN', 1.000000), 
	Parameter('rvs__3dot4dot21dot92_RXN', 0.000000))
Rule('NQOR_RXN',
	cplx(name = 'CPLX0_3121', loc = 'cyt') +
	met(name = 'ETR_Quinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3121', loc = 'cyt') +
	met(name = 'ETR_Quinols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_NQOR_RXN', 1.000000), 
	Parameter('rvs_NQOR_RXN', 0.000000))
Rule('RXN0_3381',
	cplx(name = 'CPLX0_3121', loc = 'cyt') +
	met(name = 'CRplus6', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_3121', loc = 'cyt') +
	met(name = 'CRplus3', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SUPER_OXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_3381', 1.000000), 
	Parameter('rvs_RXN0_3381', 0.000000))
Rule('SUCCDIAMINOPIMDESUCC_RXN',
	cplx(name = 'CPLX0_3161', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'N_SUCCINYLLL_2_6_DIAMINOPIMELATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3161', loc = 'cyt') +
	met(name = 'LL_DIAMINOPIMELATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SUC', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_SUCCDIAMINOPIMDESUCC_RXN', 1.000000), 
	Parameter('rvs_SUCCDIAMINOPIMDESUCC_RXN', 0.000000))
Rule('TETHYDPICSUCC_RXN',
	cplx(name = 'CPLX0_3181', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DELTA1_PIPERIDEINE_2_6_DICARBOXYLATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SUC_COA', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3181', loc = 'cyt') +
	met(name = 'N_SUCCINYL_2_AMINO_6_KETOPIMELATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_TETHYDPICSUCC_RXN', 1.000000), 
	Parameter('rvs_TETHYDPICSUCC_RXN', 0.000000))
Rule('RXN0_5407',
	cplx(name = 'CPLX0_3201', loc = 'per') +
	met(name = 'CPD0_1185', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3201', loc = 'per') +
	met(name = 'CPD0_1184', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_1183', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_5407', 1.000000), 
	Parameter('rvs_RXN0_5407', 0.000000))
Rule('RXN0_3461',
	cplx(name = 'CPLX0_3201', loc = 'per') +
	met(name = 'CPD0_1181', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3201', loc = 'per') +
	met(name = 'CPD0_1183', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_1182', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_3461', 1.000000), 
	Parameter('rvs_RXN0_3461', 0.000000))
Rule('PDXJ_RXN',
	cplx(name = 'CPLX0_321', loc = 'cyt') +
	met(name = '_1_AMINO_PROPAN_2_ONE_3_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DEOXYXYLULOSE_5P', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	cplx(name = 'CPLX0_321', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRIDOXINE_5P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PDXJ_RXN', 1.000000), 
	Parameter('rvs_PDXJ_RXN', 0.000000))
Rule('GUANOSINEKIN_RXN',
	cplx(name = 'CPLX0_322', loc = 'cyt') +
	met(name = 'GUANOSINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_322', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GUANOSINEKIN_RXN', 1.000000), 
	Parameter('rvs_GUANOSINEKIN_RXN', 0.000000))
Rule('INOSINEKIN_RXN',
	cplx(name = 'CPLX0_322', loc = 'cyt') +
	met(name = 'INOSINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_322', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'IMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_INOSINEKIN_RXN', 1.000000), 
	Parameter('rvs_INOSINEKIN_RXN', 0.000000))
Rule('RXN_18584',
	cplx(name = 'CPLX0_3241', loc = 'imem') +
	met(name = 'Ubiquinols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Oxidized_NapC_proteins', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_3241', loc = 'imem') +
	met(name = 'Ubiquinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Reduced_NapC_proteins', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_18584', 1.000000), 
	Parameter('rvs_RXN_18584', 0.000000))
Rule('_3dot1dot26dot3_RXN',
	cplx(name = 'CPLX0_3281', loc = 'cyt') +
	met(name = 'RNASE_III_MRNA_PROCESSING_SUBSTRATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3281', loc = 'cyt') +
	met(name = 'RNASE_III_PROCESSING_PRODUCT_MRNA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'mRNA_Fragments', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3dot1dot26dot3_RXN', 1.000000), 
	Parameter('rvs__3dot1dot26dot3_RXN', 0.000000))
Rule('P_PANTOCYSLIG_RXN',
	cplx(name = 'CPLX0_341', loc = 'cyt') +
	met(name = '_4_P_PANTOTHENATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_341', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'R_4_PHOSPHOPANTOTHENOYL_L_CYSTEINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_P_PANTOCYSLIG_RXN', 1.000000), 
	Parameter('rvs_P_PANTOCYSLIG_RXN', 0.000000))
Rule('P_PANTOCYSDECARB_RXN',
	cplx(name = 'CPLX0_341', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'R_4_PHOSPHOPANTOTHENOYL_L_CYSTEINE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_341', loc = 'cyt') +
	met(name = 'PANTETHEINE_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_P_PANTOCYSDECARB_RXN', 1.000000), 
	Parameter('rvs_P_PANTOCYSDECARB_RXN', 0.000000))
Rule('RXN0_6522',
	cplx(name = 'CPLX0_3461', loc = 'imem') +
	met(name = '_9S_RRNA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3461', loc = 'imem') +
	met(name = '_5S_rRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'rRNA_fragments', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6522', 1.000000), 
	Parameter('rvs_RXN0_6522', 0.000000))
Rule('RXN0_6521',
	cplx(name = 'CPLX0_3461', loc = 'imem') +
	met(name = 'RNASE_E_MRNA_PROCESSING_SUBSTRATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3461', loc = 'imem') +
	met(name = 'RNASE_E_PROCESSING_PRODUCT_MRNA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'mRNA_Fragments', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6521', 1.000000), 
	Parameter('rvs_RXN0_6521', 0.000000))
Rule('RXN0_6485',
	cplx(name = 'CPLX0_3461', loc = 'imem') +
	met(name = 'CPD0_2350', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3461', loc = 'imem') +
	met(name = 'CPD0_2352', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_2350', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6485', 1.000000), 
	Parameter('rvs_RXN0_6485', 0.000000))
Rule('RXN0_6478',
	cplx(name = 'CPLX0_3461', loc = 'imem') +
	met(name = 'CPD0_2350', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3461', loc = 'imem') +
	met(name = 'CPD0_2351', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_2350', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6478', 1.000000), 
	Parameter('rvs_RXN0_6478', 0.000000))
Rule('_3dot1dot26dot12_RXN',
	cplx(name = 'CPLX0_3461', loc = 'imem') +
	met(name = 'RNASE_E_DEGRADATION_SUBSTRATE_MRNA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3461', loc = 'imem') +
	met(name = 'mRNA_Fragments', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd__3dot1dot26dot12_RXN', 1.000000), 
	Parameter('rvs__3dot1dot26dot12_RXN', 0.000000))
Rule('RXN0_3962',
	cplx(name = 'CPLX0_3482', loc = 'cyt') +
	met(name = 'ACETALD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3482', loc = 'cyt') +
	met(name = 'ACET', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_3962', 1.000000), 
	Parameter('rvs_RXN0_3962', 0.000000))
Rule('RXN0_4022',
	cplx(name = 'CPLX0_3501', loc = 'cyt') +
	met(name = '_7_AMINOMETHYL_7_DEAZAGUANINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_3501', loc = 'cyt') +
	met(name = '_7_CYANO_7_DEAZAGUANINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_4022', 0.000000), 
	Parameter('rvs_RXN0_4022', 1.000000))
Rule('RXN0_6479',
	cplx(name = 'CPLX0_3521', loc = 'cyt') +
	met(name = 'CPD0_2351', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3521', loc = 'cyt') +
	met(name = 'CPD0_2352', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Nucleoside_Monophosphates', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6479', 1.000000), 
	Parameter('rvs_RXN0_6479', 0.000000))
Rule('_2dot7dot7dot8_RXN',
	cplx(name = 'CPLX0_3521', loc = 'cyt') +
	met(name = 'ssRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3521', loc = 'cyt') +
	met(name = 'ssRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Nucleoside_Diphosphates', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__2dot7dot7dot8_RXN', 1.000000), 
	Parameter('rvs__2dot7dot7dot8_RXN', 1.000000))
Rule('RXN_11109',
	cplx(name = 'CPLX0_3541', loc = 'cyt') +
	met(name = 'Wound_RNA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_3541', loc = 'cyt') +
	met(name = 'Unwound_RNA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11109', 1.000000), 
	Parameter('rvs_RXN_11109', 0.000000))
Rule('RXN_15041',
	cplx(name = 'CPLX0_3581', loc = 'cyt') +
	met(name = 'D_aminoacyl_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_3581', loc = 'cyt') +
	met(name = 'D_Amino_Acids', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_15041', 1.000000), 
	Parameter('rvs_RXN_15041', 0.000000))
Rule('RXN0_1882',
	cplx(name = 'CPLX0_3581', loc = 'cyt') +
	met(name = 'D_TYROSYL_TRNATYR', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3581', loc = 'cyt') +
	met(name = 'TYR_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_TYROSINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_1882', 1.000000), 
	Parameter('rvs_RXN0_1882', 0.000000))
Rule('_3dot1dot26dot11_RXN',
	cplx(name = 'CPLX0_3601', loc = 'cyt') +
	met(name = 'tRNA_precursors', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3601', loc = 'cyt') +
	met(name = 'mature_tRNA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SS_Oligoribonucleotides', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3dot1dot26dot11_RXN', 1.000000), 
	Parameter('rvs__3dot1dot26dot11_RXN', 0.000000))
Rule('RXN0_6525',
	cplx(name = 'CPLX0_3601', loc = 'cyt') +
	met(name = 'MUTATED_TRNA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3601', loc = 'cyt') +
	met(name = 'Nucleoside_Monophosphates', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_6525', 1.000000), 
	Parameter('rvs_RXN0_6525', 0.000000))
Rule('RXN0_4222',
	cplx(name = 'CPLX0_3601', loc = 'cyt') +
	met(name = 'CPD0_2351', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3601', loc = 'cyt') +
	met(name = 'CPD0_2354', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Ribonucleoside_Monophosphates', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_4222', 1.000000), 
	Parameter('rvs_RXN0_4222', 0.000000))
Rule('RXN0_6484',
	cplx(name = 'CPLX0_3602', loc = 'cyt') +
	met(name = 'CPD0_2353', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_3602', loc = 'cyt') +
	met(name = 'tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Nucleoside_Monophosphates', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6484', 1.000000), 
	Parameter('rvs_RXN0_6484', 0.000000))
Rule('RXN0_6483',
	cplx(name = 'CPLX0_3602', loc = 'cyt') +
	met(name = 'CPD0_2352', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_3602', loc = 'cyt') +
	met(name = 'CPD0_2354', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Ribonucleoside_Monophosphates', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6483', 1.000000), 
	Parameter('rvs_RXN0_6483', 0.000000))
Rule('RXN0_4223',
	cplx(name = 'CPLX0_3602', loc = 'cyt') +
	met(name = 'RNA_Holder', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3602', loc = 'cyt') +
	met(name = 'Nucleoside_Monophosphates', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_4223', 1.000000), 
	Parameter('rvs_RXN0_4223', 0.000000))
Rule('RXN0_4261',
	cplx(name = 'CPLX0_3621', loc = 'cyt') +
	met(name = 'Supercoiled_Duplex_DNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3621', loc = 'cyt') +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Single_Stranded_DNAs', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_4261', 1.000000), 
	Parameter('rvs_RXN0_4261', 0.000000))
Rule('RXN0_4342',
	cplx(name = 'CPLX0_3661', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_BETA_D_HEPTOSE_1_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3661', loc = 'cyt') +
	met(name = 'ADP_D_GLYCERO_D_MANNO_HEPTOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_4342', 1.000000), 
	Parameter('rvs_RXN0_4342', 0.000000))
Rule('RXN0_4341',
	cplx(name = 'CPLX0_3661', loc = 'cyt') +
	met(name = 'D_ALPHABETA_D_HEPTOSE_7_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_3661', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_BETA_D_HEPTOSE_17_DIPHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_4341', 1.000000), 
	Parameter('rvs_RXN0_4341', 0.000000))
Rule('_5dot1dot3dot20_RXN',
	cplx(name = 'CPLX0_3681', loc = 'cyt') +
	met(name = 'ADP_D_GLYCERO_D_MANNO_HEPTOSE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3681', loc = 'cyt') +
	met(name = 'ADP_L_GLYCERO_D_MANNO_HEPTOSE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__5dot1dot3dot20_RXN', 1.000000), 
	Parameter('rvs__5dot1dot3dot20_RXN', 0.000000))
Rule('RXN0_7309',
	cplx(name = 'CPLX0_3721', loc = 'cyt') +
	met(name = 'CPD_4211', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_3721', loc = 'cyt') +
	met(name = 'CPD_14332', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7309', 1.000000), 
	Parameter('rvs_RXN0_7309', 0.000000))
Rule('RXN0_1441',
	cplx(name = 'CPLX0_3721', loc = 'cyt') +
	met(name = 'ADENOSINE_DIPHOSPHATE_RIBOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_3721', loc = 'cyt') +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_15317', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_1441', 1.000000), 
	Parameter('rvs_RXN0_1441', 0.000000))
Rule('GLUTRNAREDUCT_RXN',
	cplx(name = 'CPLX0_3741', loc = 'cyt') +
	met(name = 'GLUTAMATE_1_SEMIALDEHYDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3741', loc = 'cyt') +
	met(name = 'Charged_GLT_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLUTRNAREDUCT_RXN', 0.000000), 
	Parameter('rvs_GLUTRNAREDUCT_RXN', 1.000000))
Rule('_2dot7dot1dot148_RXN',
	cplx(name = 'CPLX0_3841', loc = 'cyt') +
	met(name = '_4_CYTIDINE_5_DIPHOSPHO_2_C', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_3841', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_PHOSPHO_4_CYTIDINE_5_DIPHOSPHO_2_C_MET', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__2dot7dot1dot148_RXN', 1.000000), 
	Parameter('rvs__2dot7dot1dot148_RXN', 0.000000))
Rule('RXN0_4841',
	cplx(name = 'CPLX0_3861', loc = 'cyt') +
	met(name = 'FRUCTOSELYSINE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3861', loc = 'cyt') +
	met(name = 'PSICOSELYSINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_4841', 1.000000), 
	Parameter('rvs_RXN0_4841', 1.000000))
Rule('_1dot1dot1dot271_RXN',
	cplx(name = 'CPLX0_3881', loc = 'cyt') +
	met(name = 'CPD_13118', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_3881', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GDP_4_DEHYDRO_6_DEOXY_D_MANNOSE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__1dot1dot1dot271_RXN', 0.000000), 
	Parameter('rvs__1dot1dot1dot271_RXN', 1.000000))
Rule('RXN0_5001',
	cplx(name = 'CPLX0_3901', loc = 'cyt') +
	met(name = 'Xylans', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3901', loc = 'cyt') +
	met(name = 'XYLOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_5001', 1.000000), 
	Parameter('rvs_RXN0_5001', 0.000000))
Rule('RXN_12402',
	cplx(name = 'CPLX0_3901', loc = 'cyt') +
	met(name = 'CPD0_1202', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3901', loc = 'cyt') +
	met(name = 'Glucopyranose', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'XYLOSE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_12402', 1.000000), 
	Parameter('rvs_RXN_12402', 0.000000))
Rule('PEPTIDYLPROLYL_ISOMERASE_RXN',
	cplx(name = 'CPLX0_3924', loc = 'per') +
	met(name = 'CPD_8624', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3924', loc = 'per') +
	met(name = 'CPD_8625', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PEPTIDYLPROLYL_ISOMERASE_RXN', 1.000000), 
	Parameter('rvs_PEPTIDYLPROLYL_ISOMERASE_RXN', 1.000000))
Rule('DNA_DIRECTED_DNA_POLYMERASE_RXN',
	cplx(name = 'CPLX0_3925', loc = 'imem') +
	met(name = 'Deoxy_Ribonucleoside_Triphosphates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DNA_N', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3925', loc = 'imem') +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DNA_N', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DNA_DIRECTED_DNA_POLYMERASE_RXN', 1.000000), 
	Parameter('rvs_DNA_DIRECTED_DNA_POLYMERASE_RXN', 0.000000))
Rule('ATPASE_RXN',
	cplx(name = 'CPLX0_3927', loc = 'cyt') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_3927', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ATPASE_RXN', 1.000000), 
	Parameter('rvs_ATPASE_RXN', 0.000000))
Rule('RXN_11135',
	cplx(name = 'CPLX0_3931', loc = 'cyt') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Supercoiled_Duplex_DNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_3931', loc = 'cyt') +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Single_Stranded_DNAs', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11135', 1.000000), 
	Parameter('rvs_RXN_11135', 0.000000))
Rule('H2NEOPTERINALDOL_RXN',
	cplx(name = 'CPLX0_3936', loc = 'cyt') +
	met(name = 'DIHYDRO_NEO_PTERIN', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_3936', loc = 'cyt') +
	met(name = 'GLYCOLALDEHYDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMINO_OH_HYDROXYMETHYL_DIHYDROPTERIDINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_H2NEOPTERINALDOL_RXN', 1.000000), 
	Parameter('rvs_H2NEOPTERINALDOL_RXN', 0.000000))
Rule('RXN_10856',
	cplx(name = 'CPLX0_3936', loc = 'cyt') +
	met(name = 'DIHYDRO_NEO_PTERIN', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3936', loc = 'cyt') +
	met(name = 'CPD_11770', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_10856', 1.000000), 
	Parameter('rvs_RXN_10856', 1.000000))
Rule('RXN0_7104',
	cplx(name = 'CPLX0_3941', loc = 'cyt') +
	met(name = 'CPD_207', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_3941', loc = 'cyt') +
	met(name = 'PHENYLACETATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7104', 1.000000), 
	Parameter('rvs_RXN0_7104', 0.000000))
Rule('RXN0_5065',
	cplx(name = 'CPLX0_3941', loc = 'cyt') +
	met(name = '_34_DIHYDROXYPHENYLACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_3941', loc = 'cyt') +
	met(name = 'CPD_782', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5065', 1.000000), 
	Parameter('rvs_RXN0_5065', 0.000000))
Rule('RXN0_3942',
	cplx(name = 'CPLX0_3943', loc = 'cyt') +
	met(name = 'CPD_9000', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3943', loc = 'cyt') +
	met(name = '_4_AMINO_BUTYRATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_3942', 1.000000), 
	Parameter('rvs_RXN0_3942', 0.000000))
Rule('RXN0_5074',
	cplx(name = 'CPLX0_3948', loc = 'cyt') +
	met(name = 'XTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_3948', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'XDP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5074', 1.000000), 
	Parameter('rvs_RXN0_5074', 0.000000))
Rule('RXN0_5073',
	cplx(name = 'CPLX0_3948', loc = 'cyt') +
	met(name = 'ITP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_3948', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'IDP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5073', 1.000000), 
	Parameter('rvs_RXN0_5073', 0.000000))
Rule('RXN_12458',
	cplx(name = 'CPLX0_3950', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Guanine37_in_tRNA', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_3950', loc = 'cyt') +
	met(name = 'tRNA_Containing_N1_Methylguanine_37', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_12458', 1.000000), 
	Parameter('rvs_RXN_12458', 0.000000))
Rule('RXN_16650',
	cplx(name = 'CPLX0_3951', loc = 'imem') +
	met(name = 'CPD_17927', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'C6', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3951', loc = 'imem') +
	met(name = 'CPD_17927', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UNDECAPRENYL_DIPHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_16650', 1.000000), 
	Parameter('rvs_RXN_16650', 0.000000))
Rule('RXN_16659',
	cplx(name = 'CPLX0_3951', loc = 'imem') +
	met(name = 'CPD_17927', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_17931', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3951', loc = 'imem') +
	met(name = 'CPD_17932', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_ALANINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_16659', 1.000000), 
	Parameter('rvs_RXN_16659', 0.000000))
Rule('RXN_16649',
	cplx(name = 'CPLX0_3951', loc = 'imem') +
	met(name = 'CPD_17927', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3951', loc = 'imem') +
	met(name = 'CPD_17926', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_ALANINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_16649', 1.000000), 
	Parameter('rvs_RXN_16649', 0.000000))
Rule('RIBOFLAVIN_SYN_RXN',
	cplx(name = 'CPLX0_3952', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DIMETHYL_D_RIBITYL_LUMAZINE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3952', loc = 'cyt') +
	met(name = 'AMINO_RIBOSYLAMINO_1H_3H_PYR_DIONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'RIBOFLAVIN', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RIBOFLAVIN_SYN_RXN', 1.000000), 
	Parameter('rvs_RIBOFLAVIN_SYN_RXN', 0.000000))
Rule('S_FORMYLGLUTATHIONE_HYDROLASE_RXN',
	cplx(name = 'CPLX0_3954', loc = 'cyt') +
	met(name = 'CPD_548', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_3954', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FORMATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLUTATHIONE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_S_FORMYLGLUTATHIONE_HYDROLASE_RXN', 1.000000), 
	Parameter('rvs_S_FORMYLGLUTATHIONE_HYDROLASE_RXN', 0.000000))
Rule('GLYOXII_RXN',
	cplx(name = 'CPLX0_3954', loc = 'cyt') +
	met(name = 'S_LACTOYL_GLUTATHIONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_3954', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLUTATHIONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_LACTATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLYOXII_RXN', 1.000000), 
	Parameter('rvs_GLYOXII_RXN', 0.000000))
Rule('RXN_17307',
	cplx(name = 'CPLX0_3957', loc = 'cyt') +
	met(name = 'DNA_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	cplx(name = 'CPLX0_3957', loc = 'cyt') +
	met(name = 'DNA_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Deoxy_Ribonucleoside_Monophosphates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17307', 1.000000), 
	Parameter('rvs_RXN_17307', 0.000000))
Rule('_3dot1dot21dot3_RXN',
	cplx(name = 'CPLX0_3958', loc = 'cyt') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DNA_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3958', loc = 'cyt') +
	met(name = 'Double_Stranded_DNA_with_terminal_PO4s', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3dot1dot21dot3_RXN', 1.000000), 
	Parameter('rvs__3dot1dot21dot3_RXN', 0.000000))
Rule('_3dot5dot2dot17_RXN',
	cplx(name = 'CPLX0_3961', loc = 'per') +
	met(name = '_5_HYDROXYISOURATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3961', loc = 'per') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_5821', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3dot5dot2dot17_RXN', 1.000000), 
	Parameter('rvs__3dot5dot2dot17_RXN', 0.000000))
Rule('RXN_15294',
	cplx(name = 'CPLX0_3969', loc = 'cyt') +
	met(name = 'FEplus2', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_3969', loc = 'cyt') +
	met(name = 'CPD_16500', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_15294', 1.000000), 
	Parameter('rvs_RXN_15294', 0.000000))
Rule('RXN0_5108',
	cplx(name = 'CPLX0_3971', loc = 'cyt') +
	met(name = 'GDP_MANNOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_3971', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MANNOSE_1P', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5108', 1.000000), 
	Parameter('rvs_RXN0_5108', 0.000000))
Rule('NAD_KIN_RXN',
	cplx(name = 'CPLX0_682', loc = 'cyt') +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_682', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_NAD_KIN_RXN', 1.000000), 
	Parameter('rvs_NAD_KIN_RXN', 0.000000))
Rule('RXN0_302',
	cplx(name = 'CPLX0_721', loc = 'cyt') +
	met(name = '_2_PHOSPHO_4_CYTIDINE_5_DIPHOSPHO_2_C_MET', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_721', loc = 'cyt') +
	met(name = 'CMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2C_METH_D_ERYTHRITOL_CYCLODIPHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_302', 1.000000), 
	Parameter('rvs_RXN0_302', 0.000000))
Rule('LIPIDADISACCHARIDESYNTH_RXN',
	cplx(name = 'CPLX0_7415', loc = 'imem') +
	met(name = 'BISOHMYR_GLUCOSAMINYL_1P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OH_MYRISTOYL', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7415', loc = 'imem') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'BISOHMYR_GLC', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UDP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_LIPIDADISACCHARIDESYNTH_RXN', 1.000000), 
	Parameter('rvs_LIPIDADISACCHARIDESYNTH_RXN', 0.000000))
Rule('RXN_11867',
	cplx(name = 'CPLX0_7420', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Uridine32_in_tRNA', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7420', loc = 'cyt') +
	met(name = '_2_O_Methyluridine32_tRNA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11867', 1.000000), 
	Parameter('rvs_RXN_11867', 0.000000))
Rule('RXN_11866',
	cplx(name = 'CPLX0_7420', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Cytidine_32_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7420', loc = 'cyt') +
	met(name = '_2_O_Methylcytidine_32_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11866', 1.000000), 
	Parameter('rvs_RXN_11866', 0.000000))
Rule('RXN_11860',
	cplx(name = 'CPLX0_7421', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Cytidine_34_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7421', loc = 'cyt') +
	met(name = '_2_O_Methylcytidine_34_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11860', 1.000000), 
	Parameter('rvs_RXN_11860', 0.000000))
Rule('RXN_11865',
	cplx(name = 'CPLX0_7421', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_5_carbo_me_ami_me_ur_34_tRNALeu', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7421', loc = 'cyt') +
	met(name = '_5_CarboxyMeAmMe_2_O_MeU34_tRNALeu', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11865', 1.000000), 
	Parameter('rvs_RXN_11865', 0.000000))
Rule('RXN0_7168',
	cplx(name = 'CPLX0_7421', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_5_methoxycarbonylmethoxyU34_tRNA', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7421', loc = 'cyt') +
	met(name = 'mcmo5U34m_tRNA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7168', 1.000000), 
	Parameter('rvs_RXN0_7168', 0.000000))
Rule('RXN_11592',
	cplx(name = 'CPLX0_7423', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_23S_rRNA_pseudouridine1915', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7423', loc = 'cyt') +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_23S_rRNA_N3_methylpseudouridine1915', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11592', 1.000000), 
	Parameter('rvs_RXN_11592', 0.000000))
Rule('RXN_8992',
	cplx(name = 'CPLX0_7426', loc = 'cyt') +
	met(name = 'FARNESYL_PP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DELTA3_ISOPENTENYL_PP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7426', loc = 'cyt') +
	met(name = 'OCTAPRENYL_DIPHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_8992', 1.000000), 
	Parameter('rvs_RXN_8992', 0.000000))
Rule('DXS_RXN',
	cplx(name = 'CPLX0_743', loc = 'cyt') +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GAP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_743', loc = 'cyt') +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DEOXYXYLULOSE_5P', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_DXS_RXN', 1.000000), 
	Parameter('rvs_DXS_RXN', 0.000000))
Rule('GLYCOLATEDEHYDRO_RXN',
	cplx(name = 'CPLX0_7458', loc = 'cyt') +
	met(name = 'Acceptor', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLYCOLLATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7458', loc = 'cyt') +
	met(name = 'Donor_H2', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLYOX', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLYCOLATEDEHYDRO_RXN', 1.000000), 
	Parameter('rvs_GLYCOLATEDEHYDRO_RXN', 0.000000))
Rule('RXN0_7229',
	cplx(name = 'CPLX0_7458', loc = 'cyt') +
	met(name = 'ETR_Quinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLYCOLLATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7458', loc = 'cyt') +
	met(name = 'ETR_Quinols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLYOX', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7229', 1.000000), 
	Parameter('rvs_RXN0_7229', 0.000000))
Rule('RXN_7968',
	cplx(name = 'CPLX0_7462', loc = 'cyt') +
	met(name = 'NAD_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SHIKIMATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7462', loc = 'cyt') +
	met(name = 'NADH_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_3_DEHYDRO_SHIKIMATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_7968', 1.000000), 
	Parameter('rvs_RXN_7968', 0.000000))
Rule('RXN_7967',
	cplx(name = 'CPLX0_7462', loc = 'cyt') +
	met(name = 'NAD_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'QUINATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7462', loc = 'cyt') +
	met(name = 'NADH_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DEHYDROQUINATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_7967', 1.000000), 
	Parameter('rvs_RXN_7967', 0.000000))
Rule('ALARACECAT_RXN',
	cplx(name = 'CPLX0_7465', loc = 'cyt') +
	met(name = 'L_ALPHA_ALANINE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7465', loc = 'cyt') +
	met(name = 'D_ALANINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ALARACECAT_RXN', 1.000000), 
	Parameter('rvs_ALARACECAT_RXN', 1.000000))
Rule('XYLULOKIN_RXN',
	cplx(name = 'CPLX0_7466', loc = 'cyt') +
	met(name = 'D_XYLULOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7466', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'XYLULOSE_5_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_XYLULOKIN_RXN', 1.000000), 
	Parameter('rvs_XYLULOKIN_RXN', 0.000000))
Rule('RXN0_382',
	cplx(name = 'CPLX0_7466', loc = 'cyt') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_1093', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7466', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DEOXYXYLULOSE_5P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_382', 1.000000), 
	Parameter('rvs_RXN0_382', 0.000000))
Rule('_2dot5dot1dot64_RXN',
	cplx(name = 'CPLX0_7525', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ISOCHORISMATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7525', loc = 'cyt') +
	met(name = 'CPD_9924', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd__2dot5dot1dot64_RXN', 1.000000), 
	Parameter('rvs__2dot5dot1dot64_RXN', 0.000000))
Rule('RXN0_884',
	cplx(name = 'CPLX0_7564', loc = 'cyt') +
	met(name = 'CPD_4211', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Oxidized_ferredoxins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7564', loc = 'cyt') +
	met(name = 'HYDROXY_METHYL_BUTENYL_DIP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Reduced_ferredoxins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_884', 0.000000), 
	Parameter('rvs_RXN0_884', 1.000000))
Rule('ISPH2_RXN',
	cplx(name = 'CPLX0_7564', loc = 'cyt') +
	met(name = 'DELTA3_ISOPENTENYL_PP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Oxidized_ferredoxins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7564', loc = 'cyt') +
	met(name = 'HYDROXY_METHYL_BUTENYL_DIP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Reduced_ferredoxins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ISPH2_RXN', 0.000000), 
	Parameter('rvs_ISPH2_RXN', 1.000000))
Rule('RXN_18710',
	cplx(name = 'CPLX0_7609', loc = 'imem') +
	met(name = 'tRNA_2_thiouridine34', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'METHYLENE_THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLY', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Acceptor', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7609', loc = 'imem') +
	met(name = 'tRNA_containing_5_CarbMeAminome_2_ThioU', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GDP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DIHYDROFOLATE_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Donor_H2', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_18710', 1.000000), 
	Parameter('rvs_RXN_18710', 0.000000))
Rule('RXN0_7068',
	cplx(name = 'CPLX0_7609', loc = 'imem') +
	met(name = 'tRNA_uridine34', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'METHYLENE_THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLY', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Acceptor', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7609', loc = 'imem') +
	met(name = 'tRNA_containing_5_CarbMeAminome_uridine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GDP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DIHYDROFOLATE_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Donor_H2', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7068', 1.000000), 
	Parameter('rvs_RXN0_7068', 0.000000))
Rule('RXN0_7083',
	cplx(name = 'CPLX0_7609', loc = 'imem') +
	met(name = 'tRNA_2_thiouridine34', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'METHYLENE_THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7609', loc = 'imem') +
	met(name = 'tRNA_Containing_5AminoMe_2_ThioUrdines', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DIHYDROFOLATE_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GDP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_7083', 1.000000), 
	Parameter('rvs_RXN0_7083', 0.000000))
Rule('ATPPHOSPHORIBOSYLTRANS_RXN',
	cplx(name = 'CPLX0_7614', loc = 'cyt') +
	met(name = 'PHOSPHORIBOSYL_ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7614', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PRPP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ATPPHOSPHORIBOSYLTRANS_RXN', 1.000000), 
	Parameter('rvs_ATPPHOSPHORIBOSYLTRANS_RXN', 1.000000))
Rule('KDGALDOL_RXN',
	cplx(name = 'CPLX0_7615', loc = 'cyt') +
	met(name = '_5_KETO_4_DEOXY_D_GLUCARATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7615', loc = 'cyt') +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TARTRONATE_S_ALD', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_KDGALDOL_RXN', 1.000000), 
	Parameter('rvs_KDGALDOL_RXN', 1.000000))
Rule('RXN0_5289',
	cplx(name = 'CPLX0_7616', loc = 'cyt') +
	met(name = 'GLYCERATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7616', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TARTRONATE_S_ALD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5289', 1.000000), 
	Parameter('rvs_RXN0_5289', 1.000000))
Rule('RXN0_901',
	cplx(name = 'CPLX0_761', loc = 'cyt') +
	met(name = 'XANTHINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_761', loc = 'cyt') +
	met(name = 'URATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_901', 1.000000), 
	Parameter('rvs_RXN0_901', 0.000000))
Rule('RXN_7682',
	cplx(name = 'CPLX0_761', loc = 'cyt') +
	met(name = 'HYPOXANTHINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_761', loc = 'cyt') +
	met(name = 'XANTHINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_7682', 1.000000), 
	Parameter('rvs_RXN_7682', 0.000000))
Rule('_4dot3dot1dot17_RXN',
	cplx(name = 'CPLX0_7622', loc = 'cyt') +
	met(name = 'SER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7622', loc = 'cyt') +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__4dot3dot1dot17_RXN', 1.000000), 
	Parameter('rvs__4dot3dot1dot17_RXN', 0.000000))
Rule('RXN_14143',
	cplx(name = 'CPLX0_7625', loc = 'cyt') +
	met(name = 'DUMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7625', loc = 'cyt') +
	met(name = 'DEOXYURIDINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14143', 1.000000), 
	Parameter('rvs_RXN_14143', 0.000000))
Rule('RXN_9555',
	cplx(name = 'CPLX0_7630', loc = 'per') +
	met(name = 'Cis_vaccenoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7630', loc = 'per') +
	met(name = 'CPD_9247', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_9555', 1.000000), 
	Parameter('rvs_RXN_9555', 0.000000))
Rule('RXN_9550',
	cplx(name = 'CPLX0_7630', loc = 'per') +
	met(name = 'Palmitoleoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7630', loc = 'per') +
	met(name = 'CPD_9245', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_9550', 1.000000), 
	Parameter('rvs_RXN_9550', 0.000000))
Rule('LYSOPHOSPHOLIPASE_RXN',
	cplx(name = 'CPLX0_7630', loc = 'per') +
	met(name = '_2_Lysophosphatidylcholines', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7630', loc = 'per') +
	met(name = 'Carboxylates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_1_GLYCERO_PHOSPHORYLCHOLINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_LYSOPHOSPHOLIPASE_RXN', 1.000000), 
	Parameter('rvs_LYSOPHOSPHOLIPASE_RXN', 0.000000))
Rule('THIOESTER_RXN',
	cplx(name = 'CPLX0_7630', loc = 'per') +
	met(name = 'Saturated_Fatty_Acyl_CoA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7630', loc = 'per') +
	met(name = 'CPD66_39', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_THIOESTER_RXN', 1.000000), 
	Parameter('rvs_THIOESTER_RXN', 0.000000))
Rule('FUCISOM_RXN',
	cplx(name = 'CPLX0_7631', loc = 'cyt') +
	met(name = 'CPD_10329', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7631', loc = 'cyt') +
	met(name = 'L_FUCULOSE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_FUCISOM_RXN', 1.000000), 
	Parameter('rvs_FUCISOM_RXN', 1.000000))
Rule('DARABISOM_RXN',
	cplx(name = 'CPLX0_7631', loc = 'cyt') +
	met(name = 'D_arabinopyranose', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7631', loc = 'cyt') +
	met(name = 'D_RIBULOSE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DARABISOM_RXN', 1.000000), 
	Parameter('rvs_DARABISOM_RXN', 1.000000))
Rule('FUCPALDOL_RXN',
	cplx(name = 'CPLX0_7633', loc = 'cyt') +
	met(name = 'FUCULOSE_1P', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7633', loc = 'cyt') +
	met(name = 'LACTALD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DIHYDROXY_ACETONE_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_FUCPALDOL_RXN', 1.000000), 
	Parameter('rvs_FUCPALDOL_RXN', 0.000000))
Rule('DARABALDOL_RXN',
	cplx(name = 'CPLX0_7633', loc = 'cyt') +
	met(name = 'D_RIBULOSE_1_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7633', loc = 'cyt') +
	met(name = 'GLYCOLALDEHYDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DIHYDROXY_ACETONE_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DARABALDOL_RXN', 1.000000), 
	Parameter('rvs_DARABALDOL_RXN', 0.000000))
Rule('ACETOLACTREDUCTOISOM_RXN',
	cplx(name = 'CPLX0_7643', loc = 'cyt') +
	met(name = 'CPD_13357', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7643', loc = 'cyt') +
	met(name = '_2_ACETO_LACTATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ACETOLACTREDUCTOISOM_RXN', 0.000000), 
	Parameter('rvs_ACETOLACTREDUCTOISOM_RXN', 1.000000))
Rule('ACETOOHBUTREDUCTOISOM_RXN',
	cplx(name = 'CPLX0_7643', loc = 'cyt') +
	met(name = '_1_KETO_2_METHYLVALERATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7643', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_ACETO_2_HYDROXY_BUTYRATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ACETOOHBUTREDUCTOISOM_RXN', 0.000000), 
	Parameter('rvs_ACETOOHBUTREDUCTOISOM_RXN', 1.000000))
Rule('RXN0_5298',
	cplx(name = 'CPLX0_7645', loc = 'cyt') +
	met(name = 'CPD_10329', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7645', loc = 'cyt') +
	met(name = 'CPD0_1107', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5298', 1.000000), 
	Parameter('rvs_RXN0_5298', 1.000000))
Rule('RXN0_5304',
	cplx(name = 'CPLX0_7646', loc = 'cyt') +
	met(name = 'CPD0_1110', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7646', loc = 'cyt') +
	met(name = 'CPD0_1108', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5304', 1.000000), 
	Parameter('rvs_RXN0_5304', 1.000000))
Rule('RIBOKIN_RXN',
	cplx(name = 'CPLX0_7647', loc = 'cyt') +
	met(name = 'D_Ribofuranose', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7647', loc = 'cyt') +
	met(name = 'CPD_15317', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RIBOKIN_RXN', 1.000000), 
	Parameter('rvs_RIBOKIN_RXN', 0.000000))
Rule('RXN0_5306',
	cplx(name = 'CPLX0_7649', loc = 'cyt') +
	met(name = 'RHAMNOSE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7649', loc = 'cyt') +
	met(name = 'CPD0_1112', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5306', 1.000000), 
	Parameter('rvs_RXN0_5306', 0.000000))
Rule('RHAMNISOM_RXN',
	cplx(name = 'CPLX0_7652', loc = 'cyt') +
	met(name = 'CPD0_1112', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7652', loc = 'cyt') +
	met(name = 'CPD_16566', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RHAMNISOM_RXN', 1.000000), 
	Parameter('rvs_RHAMNISOM_RXN', 1.000000))
Rule('LYXISOM_RXN',
	cplx(name = 'CPLX0_7652', loc = 'cyt') +
	met(name = 'L_LYXOSE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7652', loc = 'cyt') +
	met(name = 'L_XYLULOSE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_LYXISOM_RXN', 1.000000), 
	Parameter('rvs_LYXISOM_RXN', 1.000000))
Rule('RXN0_5329',
	cplx(name = 'CPLX0_7658', loc = 'per') +
	met(name = 'CPD0_1122', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7658', loc = 'per') +
	met(name = 'CPD0_1123', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5329', 1.000000), 
	Parameter('rvs_RXN0_5329', 1.000000))
Rule('RIBOFLAVINSYNDEAM_RXN',
	cplx(name = 'CPLX0_7659', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DIAMINO_OH_PHOSPHORIBOSYLAMINO_PYR', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7659', loc = 'cyt') +
	met(name = 'CPD_602', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RIBOFLAVINSYNDEAM_RXN', 1.000000), 
	Parameter('rvs_RIBOFLAVINSYNDEAM_RXN', 0.000000))
Rule('RIBOFLAVINSYNREDUC_RXN',
	cplx(name = 'CPLX0_7659', loc = 'cyt') +
	met(name = 'CPD_1086', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7659', loc = 'cyt') +
	met(name = 'CPD_602', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RIBOFLAVINSYNREDUC_RXN', 0.000000), 
	Parameter('rvs_RIBOFLAVINSYNREDUC_RXN', 1.000000))
Rule('RXN0_4301',
	cplx(name = 'CPLX0_7660', loc = 'cyt') +
	met(name = 'D_SEDOHEPTULOSE_7_P', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7660', loc = 'cyt') +
	met(name = 'D_ALPHABETA_D_HEPTOSE_7_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_4301', 1.000000), 
	Parameter('rvs_RXN0_4301', 0.000000))
Rule('BETA_GLUCURONID_RXN',
	cplx(name = 'CPLX0_7662', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Beta_D_Glucuronides', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7662', loc = 'cyt') +
	met(name = 'D_Glucopyranuronate', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Alcohols', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_BETA_GLUCURONID_RXN', 1.000000), 
	Parameter('rvs_BETA_GLUCURONID_RXN', 0.000000))
Rule('RXN_14023',
	cplx(name = 'CPLX0_7667', loc = 'cyt') +
	met(name = 'GLYCOLALDEHYDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7667', loc = 'cyt') +
	met(name = 'GLYCOL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_14023', 1.000000), 
	Parameter('rvs_RXN_14023', 0.000000))
Rule('RXN0_4281',
	cplx(name = 'CPLX0_7667', loc = 'cyt') +
	met(name = 'ACETOL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7667', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'METHYL_GLYOXAL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_4281', 0.000000), 
	Parameter('rvs_RXN0_4281', 1.000000))
Rule('ALCOHOL_DEHYDROGENASE_NADPORNOPplus_RXN',
	cplx(name = 'CPLX0_7667', loc = 'cyt') +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Alcohols', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7667', loc = 'cyt') +
	met(name = 'Aldehydes', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ALCOHOL_DEHYDROGENASE_NADPORNOPplus_RXN', 0.000000), 
	Parameter('rvs_ALCOHOL_DEHYDROGENASE_NADPORNOPplus_RXN', 1.000000))
Rule('RXN0_6487',
	cplx(name = 'CPLX0_7667', loc = 'cyt') +
	met(name = 'CPD_347', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7667', loc = 'cyt') +
	met(name = 'HYDROXYPROPANAL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6487', 1.000000), 
	Parameter('rvs_RXN0_6487', 1.000000))
Rule('RXN0_7154',
	cplx(name = 'CPLX0_7667', loc = 'cyt') +
	met(name = 'CPD_16716', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7667', loc = 'cyt') +
	met(name = 'CPD0_2582', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7154', 0.000000), 
	Parameter('rvs_RXN0_7154', 1.000000))
Rule('RXN_15296',
	cplx(name = 'CPLX0_7683', loc = 'cyt') +
	met(name = 'CPD_10247', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7683', loc = 'cyt') +
	met(name = 'CPD_16501', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_15296', 1.000000), 
	Parameter('rvs_RXN_15296', 0.000000))
Rule('MANNOSE_ISOMERASE_RXN',
	cplx(name = 'CPLX0_7683', loc = 'cyt') +
	met(name = 'CPD_15373', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7683', loc = 'cyt') +
	met(name = 'CPD_15382', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_MANNOSE_ISOMERASE_RXN', 1.000000), 
	Parameter('rvs_MANNOSE_ISOMERASE_RXN', 1.000000))
Rule('HYPOXANPRIBOSYLTRAN_RXN',
	cplx(name = 'CPLX0_7685', loc = 'cyt') +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'IMP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7685', loc = 'cyt') +
	met(name = 'PRPP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HYPOXANTHINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_HYPOXANPRIBOSYLTRAN_RXN', 0.000000), 
	Parameter('rvs_HYPOXANPRIBOSYLTRAN_RXN', 1.000000))
Rule('GUANPRIBOSYLTRAN_RXN',
	cplx(name = 'CPLX0_7685', loc = 'cyt') +
	met(name = 'GMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7685', loc = 'cyt') +
	met(name = 'GUANINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PRPP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GUANPRIBOSYLTRAN_RXN', 0.000000), 
	Parameter('rvs_GUANPRIBOSYLTRAN_RXN', 1.000000))
Rule('SUCCSEMIALDDEHYDROG_RXN',
	cplx(name = 'CPLX0_7688', loc = 'cyt') +
	met(name = 'SUCC_S_ALD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7688', loc = 'cyt') +
	met(name = 'SUC', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_SUCCSEMIALDDEHYDROG_RXN', 1.000000), 
	Parameter('rvs_SUCCSEMIALDDEHYDROG_RXN', 0.000000))
Rule('RXN0_2301',
	cplx(name = 'CPLX0_7691', loc = 'cyt') +
	met(name = 'ISOVALERYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ETF_Oxidized', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7691', loc = 'cyt') +
	met(name = '_3_METHYL_CROTONYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ETF_Reduced', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_2301', 1.000000), 
	Parameter('rvs_RXN0_2301', 0.000000))
Rule('NUCLEOTIDE_PYROPHOSPHATASE_RXN',
	cplx(name = 'CPLX0_7692', loc = 'cyt') +
	met(name = 'Nucleoside_Triphosphates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7692', loc = 'cyt') +
	met(name = 'Nucleoside_Monophosphates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_NUCLEOTIDE_PYROPHOSPHATASE_RXN', 1.000000), 
	Parameter('rvs_NUCLEOTIDE_PYROPHOSPHATASE_RXN', 0.000000))
Rule('RXN0_6722',
	cplx(name = 'CPLX0_7693', loc = 'cyt') +
	met(name = 'Quinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7693', loc = 'cyt') +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Semiquinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_6722', 1.000000), 
	Parameter('rvs_RXN0_6722', 0.000000))
Rule('RXN0_5375',
	cplx(name = 'CPLX0_7693', loc = 'cyt') +
	met(name = 'ANTHRANILATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_1148', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7693', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_1147', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5375', 0.000000), 
	Parameter('rvs_RXN0_5375', 1.000000))
Rule('RXN0_3901',
	cplx(name = 'CPLX0_7709', loc = 'cyt') +
	met(name = 'PUTRESCINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7709', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GAMMA_GLUTAMYL_PUTRESCINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_3901', 1.000000), 
	Parameter('rvs_RXN0_3901', 0.000000))
Rule('GDPMANMANHYDRO_RXN',
	cplx(name = 'CPLX0_7712', loc = 'cyt') +
	met(name = 'GDP_MANNOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7712', loc = 'cyt') +
	met(name = 'MANNOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GDP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GDPMANMANHYDRO_RXN', 1.000000), 
	Parameter('rvs_GDPMANMANHYDRO_RXN', 0.000000))
Rule('GDP_GLUCOSIDASE_RXN',
	cplx(name = 'CPLX0_7712', loc = 'cyt') +
	met(name = 'GDP_D_GLUCOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7712', loc = 'cyt') +
	met(name = 'GDP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Glucopyranose', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GDP_GLUCOSIDASE_RXN', 1.000000), 
	Parameter('rvs_GDP_GLUCOSIDASE_RXN', 0.000000))
Rule('RXN0_1862',
	cplx(name = 'CPLX0_7718', loc = 'cyt') +
	met(name = 'UDP_4_AMINO_4_DEOXY_L_ARABINOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FORMYL_THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7718', loc = 'cyt') +
	met(name = 'UDP_L_ARA4_FORMYL_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_1862', 1.000000), 
	Parameter('rvs_RXN0_1862', 0.000000))
Rule('RXN0_1861',
	cplx(name = 'CPLX0_7718', loc = 'cyt') +
	met(name = 'UDP_GLUCURONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7718', loc = 'cyt') +
	met(name = '_5_BETA_L_THREO_PENTAPYRANOSYL_4_ULOSE_', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_1861', 1.000000), 
	Parameter('rvs_RXN0_1861', 0.000000))
Rule('QUINOLINATE_SYNTHA_RXN',
	cplx(name = 'CPLX0_7719', loc = 'cyt') +
	met(name = 'IMINOASPARTATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DIHYDROXY_ACETONE_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7719', loc = 'cyt') +
	met(name = 'QUINOLINATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_QUINOLINATE_SYNTHA_RXN', 1.000000), 
	Parameter('rvs_QUINOLINATE_SYNTHA_RXN', 0.000000))
Rule('L_RHAMNONATE_DEHYDRATASE_RXN',
	cplx(name = 'CPLX0_7722', loc = 'cyt') +
	met(name = 'L_RHAMNONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7722', loc = 'cyt') +
	met(name = 'DEHYDRO_3_DEOXY_L_RHAMNONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_L_RHAMNONATE_DEHYDRATASE_RXN', 1.000000), 
	Parameter('rvs_L_RHAMNONATE_DEHYDRATASE_RXN', 0.000000))
Rule('RXN0_5433',
	cplx(name = 'CPLX0_7723', loc = 'cyt') +
	met(name = 'DEHYDRO_3_DEOXY_L_RHAMNONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7723', loc = 'cyt') +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'LACTALD', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5433', 1.000000), 
	Parameter('rvs_RXN0_5433', 1.000000))
Rule('RXN0_5435',
	cplx(name = 'CPLX0_7725', loc = 'cyt') +
	met(name = 'Pre_crRNAs', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7725', loc = 'cyt') +
	met(name = 'crRNAs', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5435', 1.000000), 
	Parameter('rvs_RXN0_5435', 0.000000))
Rule('RXN_11602',
	cplx(name = 'CPLX0_7726', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_23S_rRNA_cytosine_1962', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7726', loc = 'cyt') +
	met(name = '_23S_rRNA_5_methylcytosine1962', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11602', 1.000000), 
	Parameter('rvs_RXN_11602', 0.000000))
Rule('RXN_11598',
	cplx(name = 'CPLX0_7727', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_16S_rRNA_uracil1498', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7727', loc = 'cyt') +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_16S_rRNA_N3_methyluracil1498', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11598', 1.000000), 
	Parameter('rvs_RXN_11598', 0.000000))
Rule('TRNA_PSEUDOURIDINE_SYNTHASE_I_RXN',
	cplx(name = 'CPLX0_7728', loc = 'cyt') +
	met(name = 'tRNA_uridine_38_40', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7728', loc = 'cyt') +
	met(name = 'tRNA_pseudouridine_38_40', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_TRNA_PSEUDOURIDINE_SYNTHASE_I_RXN', 1.000000), 
	Parameter('rvs_TRNA_PSEUDOURIDINE_SYNTHASE_I_RXN', 0.000000))
Rule('RXN0_4641',
	cplx(name = 'CPLX0_7732', loc = 'cyt') +
	met(name = 'CPD0_881', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7732', loc = 'cyt') +
	met(name = 'N_ACETYL_D_GLUCOSAMINE_6_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_LACTATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_4641', 1.000000), 
	Parameter('rvs_RXN0_4641', 1.000000))
Rule('METHYLMALONYL_COA_MUT_RXN',
	cplx(name = 'CPLX0_7741', loc = 'cyt') +
	met(name = 'METHYL_MALONYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7741', loc = 'cyt') +
	met(name = 'SUC_COA', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_METHYLMALONYL_COA_MUT_RXN', 1.000000), 
	Parameter('rvs_METHYLMALONYL_COA_MUT_RXN', 1.000000))
Rule('RXN0_705',
	cplx(name = 'CPLX0_7744', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_2343', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7744', loc = 'cyt') +
	met(name = 'L_XYLULOSE_5_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_705', 1.000000), 
	Parameter('rvs_RXN0_705', 0.000000))
Rule('_1dot11dot1dot15_RXN',
	cplx(name = 'CPLX0_7747', loc = 'cyt') +
	met(name = 'Red_Thioredoxin', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Alkyl_Hydro_Peroxides', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7747', loc = 'cyt') +
	met(name = 'Ox_Thioredoxin', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Alcohols', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__1dot11dot1dot15_RXN', 1.000000), 
	Parameter('rvs__1dot11dot1dot15_RXN', 0.000000))
Rule('RXN0_4121',
	cplx(name = 'CPLX0_7755', loc = 'cyt') +
	met(name = 'GMP_LYSINE_PHOSPHORAMIDATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7755', loc = 'cyt') +
	met(name = 'GMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_1442', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_4121', 1.000000), 
	Parameter('rvs_RXN0_4121', 0.000000))
Rule('RXN0_7013',
	cplx(name = 'CPLX0_7758', loc = 'cyt') +
	met(name = 'CPD_14762', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7758', loc = 'cyt') +
	met(name = 'ADENOSINE_DIPHOSPHATE_RIBOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACET', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7013', 1.000000), 
	Parameter('rvs_RXN0_7013', 0.000000))
Rule('ACONITATEHYDR_RXN',
	cplx(name = 'CPLX0_7760', loc = 'cyt') +
	met(name = 'CIS_ACONITATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7760', loc = 'cyt') +
	met(name = 'THREO_DS_ISO_CITRATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_ACONITATEHYDR_RXN', 1.000000), 
	Parameter('rvs_ACONITATEHYDR_RXN', 1.000000))
Rule('ACONITATEDEHYDR_RXN',
	cplx(name = 'CPLX0_7760', loc = 'cyt') +
	met(name = 'CIT', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7760', loc = 'cyt') +
	met(name = 'CIS_ACONITATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ACONITATEDEHYDR_RXN', 1.000000), 
	Parameter('rvs_ACONITATEDEHYDR_RXN', 1.000000))
Rule('_4dot2dot1dot99_RXN',
	cplx(name = 'CPLX0_7761', loc = 'cyt') +
	met(name = 'CPD_618', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7761', loc = 'cyt') +
	met(name = 'CPD_1136', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__4dot2dot1dot99_RXN', 1.000000), 
	Parameter('rvs__4dot2dot1dot99_RXN', 1.000000))
Rule('RXN0_7105',
	cplx(name = 'CPLX0_7766', loc = 'cyt') +
	met(name = 'CPLX0_7849', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7766', loc = 'cyt') +
	met(name = 'ENTB_CPLX', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_3_DIHYDROXYBENZOATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7105', 1.000000), 
	Parameter('rvs_RXN0_7105', 0.000000))
Rule('RXN0_7046',
	cplx(name = 'CPLX0_7766', loc = 'cyt') +
	met(name = 'CPD_264', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7766', loc = 'cyt') +
	met(name = '_3_HYDROXYBENZOATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7046', 1.000000), 
	Parameter('rvs_RXN0_7046', 0.000000))
Rule('DIHYDROURACIL_DEHYDROGENASE_NADplus_RXN',
	cplx(name = 'CPLX0_7788', loc = 'cyt') +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DI_H_URACIL', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7788', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'URACIL', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DIHYDROURACIL_DEHYDROGENASE_NADplus_RXN', 1.000000), 
	Parameter('rvs_DIHYDROURACIL_DEHYDROGENASE_NADplus_RXN', 1.000000))
Rule('RXN0_6565',
	cplx(name = 'CPLX0_7788', loc = 'cyt') +
	met(name = 'DIHYDRO_THYMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7788', loc = 'cyt') +
	met(name = 'THYMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6565', 1.000000), 
	Parameter('rvs_RXN0_6565', 1.000000))
Rule('RXN_15299',
	cplx(name = 'CPLX0_7794', loc = 'cyt') +
	met(name = '_2_3_dihydroxypropane_1_sulfonate', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7794', loc = 'cyt') +
	met(name = 'CPD_18717', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_15299', 0.000000), 
	Parameter('rvs_RXN_15299', 1.000000))
Rule('_4_HYDROXYBUTYRATE_DEHYDROGENASE_RXN',
	cplx(name = 'CPLX0_7794', loc = 'cyt') +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_4_HYDROXY_BUTYRATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7794', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SUCC_S_ALD', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__4_HYDROXYBUTYRATE_DEHYDROGENASE_RXN', 0.000000), 
	Parameter('rvs__4_HYDROXYBUTYRATE_DEHYDROGENASE_RXN', 1.000000))
Rule('RXN0_5359',
	cplx(name = 'CPLX0_7802', loc = 'cyt') +
	met(name = 'GTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7802', loc = 'cyt') +
	met(name = 'C_DI_GMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5359', 1.000000), 
	Parameter('rvs_RXN0_5359', 0.000000))
Rule('CARBOXYLATE_REDUCTASE_RXN',
	cplx(name = 'CPLX0_7805', loc = 'per') +
	met(name = 'Aldehydes', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Acceptor', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7805', loc = 'per') +
	met(name = 'Carboxylates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Donor_H2', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_CARBOXYLATE_REDUCTASE_RXN', 1.000000), 
	Parameter('rvs_CARBOXYLATE_REDUCTASE_RXN', 1.000000))
Rule('RXN0_6256',
	cplx(name = 'CPLX0_7806', loc = 'cyt') +
	met(name = 'CPD0_1885', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLUTATHIONE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7806', loc = 'cyt') +
	met(name = '_2_MERCAPTOETHANOL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXIDIZED_GLUTATHIONE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6256', 1.000000), 
	Parameter('rvs_RXN0_6256', 0.000000))
Rule('RXN0_1461',
	cplx(name = 'CPLX0_7808', loc = 'cyt') +
	met(name = 'COPROPORPHYRINOGEN_III', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7808', loc = 'cyt') +
	met(name = 'PROTOPORPHYRINOGEN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_1461', 1.000000), 
	Parameter('rvs_RXN0_1461', 0.000000))
Rule('PROTOHEMEFERROCHELAT_RXN',
	cplx(name = 'CPLX0_7810', loc = 'per') +
	met(name = 'PROTOHEME', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7810', loc = 'per') +
	met(name = 'PROTOPORPHYRIN_IX', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FEplus2', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PROTOHEMEFERROCHELAT_RXN', 1.000000), 
	Parameter('rvs_PROTOHEMEFERROCHELAT_RXN', 1.000000))
Rule('PROTOPORGENOXI_RXN',
	cplx(name = 'CPLX0_7811', loc = 'cyt') +
	met(name = 'PROTOPORPHYRINOGEN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7811', loc = 'cyt') +
	met(name = 'PROTOPORPHYRIN_IX', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HYDROGEN_PEROXIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PROTOPORGENOXI_RXN', 1.000000), 
	Parameter('rvs_PROTOPORGENOXI_RXN', 0.000000))
Rule('RXN0_6259',
	cplx(name = 'CPLX0_7811', loc = 'cyt') +
	met(name = 'Menaquinols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTOPORPHYRIN_IX', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7811', loc = 'cyt') +
	met(name = 'Menaquinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTOPORPHYRINOGEN', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6259', 0.000000), 
	Parameter('rvs_RXN0_6259', 1.000000))
Rule('RXN_15943',
	cplx(name = 'CPLX0_7820', loc = 'cyt') +
	met(name = 'DIHYDROXY_ACETONE_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7820', loc = 'cyt') +
	met(name = 'CPD0_2467', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_15943', 0.000000), 
	Parameter('rvs_RXN_15943', 1.000000))
Rule('RXN0_6382',
	cplx(name = 'CPLX0_7826', loc = 'cyt') +
	met(name = 'ITP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7826', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'IMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6382', 1.000000), 
	Parameter('rvs_RXN0_6382', 0.000000))
Rule('RXN0_1602',
	cplx(name = 'CPLX0_7826', loc = 'cyt') +
	met(name = 'DITP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7826', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DIMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_1602', 1.000000), 
	Parameter('rvs_RXN0_1602', 0.000000))
Rule('RXN0_1603',
	cplx(name = 'CPLX0_7826', loc = 'cyt') +
	met(name = 'XTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7826', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'XANTHOSINE_5_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_1603', 1.000000), 
	Parameter('rvs_RXN0_1603', 0.000000))
Rule('RXN0_949',
	cplx(name = 'CPLX0_782', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Octanoylated_domains', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Fe4S4_Cluster_Protein', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Reduced_ferredoxins', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	cplx(name = 'CPLX0_782', loc = 'cyt') +
	met(name = 'Dihydro_Lipoyl_Proteins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CH33ADO', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MET', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Iron_Sulfur_Cluster_Scaffold_Proteins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_7046', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FEplus2', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Oxidized_ferredoxins', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_949', 1.000000), 
	Parameter('rvs_RXN0_949', 0.000000))
Rule('NADPH_DEHYDROGENASE_FLAVIN_RXN',
	cplx(name = 'CPLX0_7841', loc = 'cyt') +
	met(name = 'CPD_316', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7841', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'RIBOFLAVIN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_NADPH_DEHYDROGENASE_FLAVIN_RXN', 0.000000), 
	Parameter('rvs_NADPH_DEHYDROGENASE_FLAVIN_RXN', 1.000000))
Rule('RXN0_5040',
	cplx(name = 'CPLX0_7844', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_889', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7844', loc = 'cyt') +
	met(name = 'P_AMINO_BENZOATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5040', 1.000000), 
	Parameter('rvs_RXN0_5040', 0.000000))
Rule('RXN_13179',
	cplx(name = 'CPLX0_7847', loc = 'cyt') +
	met(name = '_4_PHOSPHONOOXY_THREONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7847', loc = 'cyt') +
	met(name = '_1_AMINO_PROPAN_2_ONE_3_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_13179', 1.000000), 
	Parameter('rvs_RXN_13179', 0.000000))
Rule('RXN0_5214',
	cplx(name = 'CPLX0_7848', loc = 'cyt') +
	met(name = 'L_ASCORBATE_6_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7848', loc = 'cyt') +
	met(name = 'CPD_2343', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_5214', 1.000000), 
	Parameter('rvs_RXN0_5214', 0.000000))
Rule('PGLUCISOM_RXN',
	cplx(name = 'CPLX0_7877', loc = 'cyt') +
	met(name = 'D_glucopyranose_6_phosphate', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7877', loc = 'cyt') +
	met(name = 'FRUCTOSE_6P', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PGLUCISOM_RXN', 1.000000), 
	Parameter('rvs_PGLUCISOM_RXN', 1.000000))
Rule('OXALYL_COA_DECARBOXYLASE_RXN',
	cplx(name = 'CPLX0_7878', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXALYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7878', loc = 'cyt') +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FORMYL_COA', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_OXALYL_COA_DECARBOXYLASE_RXN', 1.000000), 
	Parameter('rvs_OXALYL_COA_DECARBOXYLASE_RXN', 0.000000))
Rule('NAPHTHOATE_SYN_RXN',
	cplx(name = 'CPLX0_7882', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_6972', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7882', loc = 'cyt') +
	met(name = 'CPD_9925', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_NAPHTHOATE_SYN_RXN', 1.000000), 
	Parameter('rvs_NAPHTHOATE_SYN_RXN', 0.000000))
Rule('RXN_12618',
	cplx(name = 'CPLX0_7885', loc = 'per') +
	met(name = 'GLUTATHIONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7885', loc = 'per') +
	met(name = 'CYS_GLY', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_12618', 1.000000), 
	Parameter('rvs_RXN_12618', 0.000000))
Rule('GAMMA_GLUTAMYLTRANSFERASE_RXN',
	cplx(name = 'CPLX0_7885', loc = 'per') +
	met(name = '_5_L_GLUTAMYL_PEPTIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Amino_Acids', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7885', loc = 'per') +
	met(name = '_5_L_GLUTAMYL_AMINO_ACID', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Peptides_holder', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GAMMA_GLUTAMYLTRANSFERASE_RXN', 1.000000), 
	Parameter('rvs_GAMMA_GLUTAMYLTRANSFERASE_RXN', 0.000000))
Rule('RXN_18093',
	cplx(name = 'CPLX0_7885', loc = 'per') +
	met(name = 'CPD_9385', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLYCYLGLYCINE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7885', loc = 'per') +
	met(name = '_4_NITROANILINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_19395', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_18093', 1.000000), 
	Parameter('rvs_RXN_18093', 0.000000))
Rule('RXN_18092',
	cplx(name = 'CPLX0_7885', loc = 'per') +
	met(name = 'GLUTATHIONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLYCYLGLYCINE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7885', loc = 'per') +
	met(name = 'CPD_19395', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CYS_GLY', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_18092', 1.000000), 
	Parameter('rvs_RXN_18092', 0.000000))
Rule('ALANINE_AMINOTRANSFERASE_RXN',
	cplx(name = 'CPLX0_7887', loc = 'cyt') +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_ALPHA_ALANINE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7887', loc = 'cyt') +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ALANINE_AMINOTRANSFERASE_RXN', 1.000000), 
	Parameter('rvs_ALANINE_AMINOTRANSFERASE_RXN', 1.000000))
Rule('RXN0_361',
	cplx(name = 'CPLX0_7904', loc = 'cyt') +
	met(name = 'CYTIDINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7904', loc = 'cyt') +
	met(name = 'D_Ribofuranose', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CYTOSINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_361', 1.000000), 
	Parameter('rvs_RXN0_361', 0.000000))
Rule('URIDINE_NUCLEOSIDASE_RXN',
	cplx(name = 'CPLX0_7904', loc = 'cyt') +
	met(name = 'URIDINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7904', loc = 'cyt') +
	met(name = 'D_Ribofuranose', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'URACIL', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_URIDINE_NUCLEOSIDASE_RXN', 1.000000), 
	Parameter('rvs_URIDINE_NUCLEOSIDASE_RXN', 0.000000))
Rule('RIBOSYLPYRIMIDINE_NUCLEOSIDASE_RXN',
	cplx(name = 'CPLX0_7904', loc = 'cyt') +
	met(name = 'Pyrimidine_Nucleosides', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7904', loc = 'cyt') +
	met(name = 'Pyrimidine_Bases', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_Ribofuranose', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RIBOSYLPYRIMIDINE_NUCLEOSIDASE_RXN', 1.000000), 
	Parameter('rvs_RIBOSYLPYRIMIDINE_NUCLEOSIDASE_RXN', 0.000000))
Rule('PHOSACETYLTRANS_RXN',
	cplx(name = 'CPLX0_7912', loc = 'cyt') +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7912', loc = 'cyt') +
	met(name = 'ACETYL_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PHOSACETYLTRANS_RXN', 1.000000), 
	Parameter('rvs_PHOSACETYLTRANS_RXN', 1.000000))
Rule('RXN0_6576',
	cplx(name = 'CPLX0_7913', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_4544', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7913', loc = 'cyt') +
	met(name = 'CPD0_2381', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6576', 1.000000), 
	Parameter('rvs_RXN0_6576', 0.000000))
Rule('RXN0_6677',
	cplx(name = 'CPLX0_7927', loc = 'cyt') +
	met(name = 'CPD_13314', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7927', loc = 'cyt') +
	met(name = 'CPD_13315', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_6677', 1.000000), 
	Parameter('rvs_RXN0_6677', 0.000000))
Rule('RXN0_6676',
	cplx(name = 'CPLX0_7927', loc = 'cyt') +
	met(name = 'CPD_6602', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7927', loc = 'cyt') +
	met(name = 'CPD_13314', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_6676', 1.000000), 
	Parameter('rvs_RXN0_6676', 0.000000))
Rule('CYTDEAM_RXN',
	cplx(name = 'CPLX0_7932', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CYTOSINE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7932', loc = 'cyt') +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'URACIL', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_CYTDEAM_RXN', 1.000000), 
	Parameter('rvs_CYTDEAM_RXN', 0.000000))
Rule('RXN0_6708',
	cplx(name = 'CPLX0_7932', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_2461', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7932', loc = 'cyt') +
	met(name = 'XANTHINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_6708', 1.000000), 
	Parameter('rvs_RXN0_6708', 0.000000))
Rule('RXN0_6710',
	cplx(name = 'CPLX0_7936', loc = 'cyt') +
	met(name = 'CPD0_2463', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7936', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'RIBOSE_15_BISPHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6710', 1.000000), 
	Parameter('rvs_RXN0_6710', 0.000000))
Rule('_4dot1dot2dot28_RXN',
	cplx(name = 'CPLX0_7940', loc = 'cyt') +
	met(name = '_2_DH_3_DO_D_ARABINONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7940', loc = 'cyt') +
	met(name = 'GLYCOLALDEHYDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__4dot1dot2dot28_RXN', 1.000000), 
	Parameter('rvs__4dot1dot2dot28_RXN', 1.000000))
Rule('DHDOGALDOL_RXN',
	cplx(name = 'CPLX0_7940', loc = 'cyt') +
	met(name = '_2_DEHYDRO_3_DEOXY_D_GLUCONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7940', loc = 'cyt') +
	met(name = 'GLYCERALD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DHDOGALDOL_RXN', 1.000000), 
	Parameter('rvs_DHDOGALDOL_RXN', 1.000000))
Rule('RXN0_6952',
	cplx(name = 'CPLX0_7944', loc = 'omem') +
	met(name = 'L_1_PHOSPHATIDYL_ETHANOLAMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7944', loc = 'omem') +
	met(name = '_2_ACYL_GPE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Fatty_Acids', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6952', 1.000000), 
	Parameter('rvs_RXN0_6952', 0.000000))
Rule('RXN0_6725',
	cplx(name = 'CPLX0_7944', loc = 'omem') +
	met(name = 'L_1_PHOSPHATIDYL_ETHANOLAMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7944', loc = 'omem') +
	met(name = 'Fatty_Acids', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_LYSOPHOSPHATIDYLETHANOLAMINES', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6725', 1.000000), 
	Parameter('rvs_RXN0_6725', 0.000000))
Rule('RXN_19312',
	cplx(name = 'CPLX0_7944', loc = 'omem') +
	met(name = '_2_LYSOPHOSPHATIDYLETHANOLAMINES', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7944', loc = 'omem') +
	met(name = 'Carboxylates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_1_GLYCEROPHOSPHORYLETHANOL_AMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_19312', 1.000000), 
	Parameter('rvs_RXN_19312', 0.000000))
Rule('RXN_19311',
	cplx(name = 'CPLX0_7944', loc = 'omem') +
	met(name = '_2_ACYL_GPE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7944', loc = 'omem') +
	met(name = 'Carboxylates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_1_GLYCEROPHOSPHORYLETHANOL_AMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_19311', 1.000000), 
	Parameter('rvs_RXN_19311', 0.000000))
Rule('RXN0_6726',
	cplx(name = 'CPLX0_7946', loc = 'cyt') +
	met(name = 'alpha_N_Peptidyl_LGlutamate', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7946', loc = 'cyt') +
	met(name = 'CPD0_2471', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6726', 1.000000), 
	Parameter('rvs_RXN0_6726', 0.000000))
Rule('SUCCARGDIHYDRO_RXN',
	cplx(name = 'CPLX0_7947', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_421', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7947', loc = 'cyt') +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'N2_SUCCINYLORNITHINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_SUCCARGDIHYDRO_RXN', 1.000000), 
	Parameter('rvs_SUCCARGDIHYDRO_RXN', 0.000000))
Rule('MHPCHYDROL_RXN',
	cplx(name = 'CPLX0_7950', loc = 'cyt') +
	met(name = 'CPD_157', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7950', loc = 'cyt') +
	met(name = 'CPD_14447', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SUC', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_MHPCHYDROL_RXN', 1.000000), 
	Parameter('rvs_MHPCHYDROL_RXN', 0.000000))
Rule('RXN_12070',
	cplx(name = 'CPLX0_7950', loc = 'cyt') +
	met(name = 'CPD0_2184', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7950', loc = 'cyt') +
	met(name = 'CPD_14447', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_12070', 1.000000), 
	Parameter('rvs_RXN_12070', 0.000000))
Rule('_2_OXOPENT_4_ENOATE_HYDRATASE_RXN',
	cplx(name = 'CPLX0_7951', loc = 'cyt') +
	met(name = '_4_HYDROXY_2_KETOVALERATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7951', loc = 'cyt') +
	met(name = 'CPD_14447', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__2_OXOPENT_4_ENOATE_HYDRATASE_RXN', 0.000000), 
	Parameter('rvs__2_OXOPENT_4_ENOATE_HYDRATASE_RXN', 1.000000))
Rule('_2dot7dot9dot3_RXN',
	cplx(name = 'CPLX0_7957', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SE_2', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7957', loc = 'cyt') +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SEPO3', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__2dot7dot9dot3_RXN', 1.000000), 
	Parameter('rvs__2dot7dot9dot3_RXN', 0.000000))
Rule('RXN_17954',
	cplx(name = 'CPLX0_7958', loc = 'imem') +
	met(name = 'CPD0_2518', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7958', loc = 'imem') +
	met(name = 'CPD_19235', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17954', 1.000000), 
	Parameter('rvs_RXN_17954', 0.000000))
Rule('RXN0_6732',
	cplx(name = 'CPLX0_7958', loc = 'imem') +
	met(name = 'CPD0_1068', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7958', loc = 'imem') +
	met(name = 'CPD0_2479', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6732', 1.000000), 
	Parameter('rvs_RXN0_6732', 0.000000))
Rule('AMPSYN_RXN',
	cplx(name = 'CPLX0_7959', loc = 'cyt') +
	met(name = 'ADENYLOSUCC', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7959', loc = 'cyt') +
	met(name = 'FUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_AMPSYN_RXN', 1.000000), 
	Parameter('rvs_AMPSYN_RXN', 0.000000))
Rule('AICARSYN_RXN',
	cplx(name = 'CPLX0_7959', loc = 'cyt') +
	met(name = 'P_RIBOSYL_4_SUCCCARB_AMINOIMIDAZOLE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7959', loc = 'cyt') +
	met(name = 'FUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AICAR', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_AICARSYN_RXN', 1.000000), 
	Parameter('rvs_AICARSYN_RXN', 0.000000))
Rule('RXN_17632',
	cplx(name = 'CPLX0_7960', loc = 'cyt') +
	met(name = 'Protein_Lysine_Aminocarbinol', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7960', loc = 'cyt') +
	met(name = 'Protein_L_lysine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_LACTATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17632', 1.000000), 
	Parameter('rvs_RXN_17632', 0.000000))
Rule('RXN0_7173',
	cplx(name = 'CPLX0_7960', loc = 'cyt') +
	met(name = 'CPD_8887', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7960', loc = 'cyt') +
	met(name = 'GLYCOLLATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7173', 1.000000), 
	Parameter('rvs_RXN0_7173', 0.000000))
Rule('RXN0_6948',
	cplx(name = 'CPLX0_7962', loc = 'cyt') +
	met(name = 'MET', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7962', loc = 'cyt') +
	met(name = 'CPD0_2015', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6948', 1.000000), 
	Parameter('rvs_RXN0_6948', 0.000000))
Rule('RXN0_4401',
	cplx(name = 'CPLX0_7974', loc = 'cyt') +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7974', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NMNH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_4401', 1.000000), 
	Parameter('rvs_RXN0_4401', 0.000000))
Rule('_2dot7dot7dot1_RXN',
	cplx(name = 'CPLX0_7975', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NICOTINAMIDE_NUCLEOTIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7975', loc = 'cyt') +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd__2dot7dot7dot1_RXN', 1.000000), 
	Parameter('rvs__2dot7dot7dot1_RXN', 0.000000))
Rule('RIBOSYLNICOTINAMIDE_KINASE_RXN',
	cplx(name = 'CPLX0_7975', loc = 'cyt') +
	met(name = 'NICOTINAMIDE_RIBOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7975', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NICOTINAMIDE_NUCLEOTIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RIBOSYLNICOTINAMIDE_KINASE_RXN', 1.000000), 
	Parameter('rvs_RIBOSYLNICOTINAMIDE_KINASE_RXN', 0.000000))
Rule('RXN_11638',
	cplx(name = 'CPLX0_7977', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_16S_rRNA_cytidine1402', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7977', loc = 'cyt') +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_16S_rRNA_N4_methylcytidine1402', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11638', 1.000000), 
	Parameter('rvs_RXN_11638', 0.000000))
Rule('RXN0_7002',
	cplx(name = 'CPLX0_7979', loc = 'cyt') +
	met(name = 'CPD0_2501', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7979', loc = 'cyt') +
	met(name = 'N_ACETYL_D_GLUCOSAMINE_6_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLUCOSAMINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7002', 1.000000), 
	Parameter('rvs_RXN0_7002', 0.000000))
Rule('_6_PHOSPHO_BETA_GLUCOSIDASE_RXN',
	cplx(name = 'CPLX0_7979', loc = 'cyt') +
	met(name = 'CPD_15978', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7979', loc = 'cyt') +
	met(name = 'D_glucopyranose_6_phosphate', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Glucopyranose', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__6_PHOSPHO_BETA_GLUCOSIDASE_RXN', 1.000000), 
	Parameter('rvs__6_PHOSPHO_BETA_GLUCOSIDASE_RXN', 0.000000))
Rule('RXN0_7010',
	cplx(name = 'CPLX0_7984', loc = 'cyt') +
	met(name = 'CPD0_2511', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLUTATHIONE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7984', loc = 'cyt') +
	met(name = 'CPD_16720', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXIDIZED_GLUTATHIONE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7010', 1.000000), 
	Parameter('rvs_RXN0_7010', 0.000000))
Rule('RXN0_961',
	cplx(name = 'CPLX0_7989', loc = 'cyt') +
	met(name = 'L_ALA_GAMMA_D_GLU_DAP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7989', loc = 'cyt') +
	met(name = 'CPD0_2190', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MESO_DIAMINOPIMELATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_961', 1.000000), 
	Parameter('rvs_RXN0_961', 0.000000))
Rule('RFFTRANS_RXN',
	cplx(name = 'CPLX0_7990', loc = 'cyt') +
	met(name = 'TDP_D_FUCOSAMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7990', loc = 'cyt') +
	met(name = 'DTDP_DEOH_DEOXY_GLUCOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RFFTRANS_RXN', 1.000000), 
	Parameter('rvs_RFFTRANS_RXN', 1.000000))
Rule('RXN0_7024',
	cplx(name = 'CPLX0_7993', loc = 'cyt') +
	met(name = 'CPD_1091', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_7993', loc = 'cyt') +
	met(name = 'CPD_389', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7024', 1.000000), 
	Parameter('rvs_RXN0_7024', 0.000000))
Rule('TRANS_RXN0_549',
	cplx(name = 'CPLX0_7994', loc = 'imem') +
	met(name = 'CPD0_1192', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7994', loc = 'imem') +
	met(name = 'CPD0_1192', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_TRANS_RXN0_549', 1.000000), 
	Parameter('rvs_TRANS_RXN0_549', 0.000000))
Rule('RXN0_5413',
	cplx(name = 'CPLX0_7994', loc = 'imem') +
	met(name = 'UDP_N_ACETYL_D_GLUCOSAMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'N_acetyl_D_glucosamine', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7994', loc = 'imem') +
	met(name = 'CPD0_1192', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UDP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5413', 1.000000), 
	Parameter('rvs_RXN0_5413', 0.000000))
Rule('DIAMINOPIMEPIM_RXN',
	cplx(name = 'CPLX0_7997', loc = 'cyt') +
	met(name = 'LL_DIAMINOPIMELATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_7997', loc = 'cyt') +
	met(name = 'MESO_DIAMINOPIMELATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DIAMINOPIMEPIM_RXN', 1.000000), 
	Parameter('rvs_DIAMINOPIMEPIM_RXN', 1.000000))
Rule('RXN_9556',
	cplx(name = 'CPLX0_8005', loc = 'cyt') +
	met(name = 'R_3_hydroxy_cis_vaccenoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8005', loc = 'cyt') +
	met(name = '_3_oxo_cis_vaccenoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_9556', 0.000000), 
	Parameter('rvs_RXN_9556', 1.000000))
Rule('_3_OXOACYL_ACP_REDUCT_RXN',
	cplx(name = 'CPLX0_8005', loc = 'cyt') +
	met(name = 'OH_ACYL_ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8005', loc = 'cyt') +
	met(name = 'B_KETOACYL_ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3_OXOACYL_ACP_REDUCT_RXN', 0.000000), 
	Parameter('rvs__3_OXOACYL_ACP_REDUCT_RXN', 1.000000))
Rule('RXN0_2142',
	cplx(name = 'CPLX0_8005', loc = 'cyt') +
	met(name = 'b_Hydroxy_cis_D5_dodecenoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8005', loc = 'cyt') +
	met(name = 'b_Keto_cis_D5_dodecenoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_2142', 0.000000), 
	Parameter('rvs_RXN0_2142', 1.000000))
Rule('RXN_10655',
	cplx(name = 'CPLX0_8005', loc = 'cyt') +
	met(name = '_3_hydroxy_cis_D7_tetraecenoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8005', loc = 'cyt') +
	met(name = '_3_oxo_cis_D7_tetradecenoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_10655', 0.000000), 
	Parameter('rvs_RXN_10655', 1.000000))
Rule('RXN_10659',
	cplx(name = 'CPLX0_8005', loc = 'cyt') +
	met(name = '_3_hydroxy_cis_D9_hexaecenoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8005', loc = 'cyt') +
	met(name = '_3_oxo_cis_D9_hexadecenoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_10659', 0.000000), 
	Parameter('rvs_RXN_10659', 1.000000))
Rule('RXN_11480',
	cplx(name = 'CPLX0_8005', loc = 'cyt') +
	met(name = '_3_hydroxypimeloyl_ACP_methyl_esters', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8005', loc = 'cyt') +
	met(name = '_3_Ketopimeloyl_ACP_methyl_esters', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11480', 0.000000), 
	Parameter('rvs_RXN_11480', 1.000000))
Rule('RXN_11476',
	cplx(name = 'CPLX0_8005', loc = 'cyt') +
	met(name = '_3_Hydroxyglutaryl_ACP_methyl_ester', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8005', loc = 'cyt') +
	met(name = '_3_Ketoglutaryl_ACP_methyl_ester', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11476', 0.000000), 
	Parameter('rvs_RXN_11476', 1.000000))
Rule('RXN_9514',
	cplx(name = 'CPLX0_8005', loc = 'cyt') +
	met(name = 'Beta_3_hydroxybutyryl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8005', loc = 'cyt') +
	met(name = 'Acetoacetyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_9514', 0.000000), 
	Parameter('rvs_RXN_9514', 1.000000))
Rule('_1dot3dot1dot9_RXN',
	cplx(name = 'CPLX0_8006', loc = 'cyt') +
	met(name = 'ACYL_ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8006', loc = 'cyt') +
	met(name = 'TRANS_D2_ENOYL_ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__1dot3dot1dot9_RXN', 0.000000), 
	Parameter('rvs__1dot3dot1dot9_RXN', 1.000000))
Rule('RXN_9558',
	cplx(name = 'CPLX0_8006', loc = 'cyt') +
	met(name = 'Cis_vaccenoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8006', loc = 'cyt') +
	met(name = 'cis_vaccen_2_enoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_9558', 0.000000), 
	Parameter('rvs_RXN_9558', 1.000000))
Rule('ENOYL_ACP_REDUCT_NADH_RXN',
	cplx(name = 'CPLX0_8006', loc = 'cyt') +
	met(name = 'Saturated_Fatty_Acyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8006', loc = 'cyt') +
	met(name = 'TRANS_D2_ENOYL_ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ENOYL_ACP_REDUCT_NADH_RXN', 0.000000), 
	Parameter('rvs_ENOYL_ACP_REDUCT_NADH_RXN', 1.000000))
Rule('RXN0_2145',
	cplx(name = 'CPLX0_8006', loc = 'cyt') +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Cis_Delta5_dodecenoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8006', loc = 'cyt') +
	met(name = 'Trans_D3_cis_D5_dodecenoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_2145', 0.000000), 
	Parameter('rvs_RXN0_2145', 1.000000))
Rule('RXN_10661',
	cplx(name = 'CPLX0_8006', loc = 'cyt') +
	met(name = 'Palmitoleoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8006', loc = 'cyt') +
	met(name = 'Trans_D3_cis_D9_hexadecenoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_10661', 0.000000), 
	Parameter('rvs_RXN_10661', 1.000000))
Rule('RXN_10657',
	cplx(name = 'CPLX0_8006', loc = 'cyt') +
	met(name = 'Cis_Delta7_tetradecenoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8006', loc = 'cyt') +
	met(name = 'Trans_D2_cis_D7_tetradecenoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_10657', 0.000000), 
	Parameter('rvs_RXN_10657', 1.000000))
Rule('RXN_11482',
	cplx(name = 'CPLX0_8006', loc = 'cyt') +
	met(name = 'Pimeloyl_ACP_methyl_esters', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8006', loc = 'cyt') +
	met(name = 'Enoylpimeloyl_ACP_methyl_esters', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11482', 0.000000), 
	Parameter('rvs_RXN_11482', 1.000000))
Rule('RXN_11478',
	cplx(name = 'CPLX0_8006', loc = 'cyt') +
	met(name = 'Glutaryl_ACP_methyl_esters', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8006', loc = 'cyt') +
	met(name = 'Enoylglutaryl_ACP_methyl_esters', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11478', 0.000000), 
	Parameter('rvs_RXN_11478', 1.000000))
Rule('RXN_9657',
	cplx(name = 'CPLX0_8006', loc = 'cyt') +
	met(name = 'Butanoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8006', loc = 'cyt') +
	met(name = 'Crotonyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_9657', 0.000000), 
	Parameter('rvs_RXN_9657', 1.000000))
Rule('RXN_9658',
	cplx(name = 'CPLX0_8006', loc = 'cyt') +
	met(name = 'Hexanoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8006', loc = 'cyt') +
	met(name = 'Hex_2_enoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_9658', 0.000000), 
	Parameter('rvs_RXN_9658', 1.000000))
Rule('RXN_9659',
	cplx(name = 'CPLX0_8006', loc = 'cyt') +
	met(name = 'Octanoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8006', loc = 'cyt') +
	met(name = '_2_Octenoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_9659', 0.000000), 
	Parameter('rvs_RXN_9659', 1.000000))
Rule('RXN_9660',
	cplx(name = 'CPLX0_8006', loc = 'cyt') +
	met(name = 'Decanoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8006', loc = 'cyt') +
	met(name = 'Trans_D2_decenoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_9660', 0.000000), 
	Parameter('rvs_RXN_9660', 1.000000))
Rule('RXN_9661',
	cplx(name = 'CPLX0_8006', loc = 'cyt') +
	met(name = 'Dodecanoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8006', loc = 'cyt') +
	met(name = 'Dodec_2_enoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_9661', 0.000000), 
	Parameter('rvs_RXN_9661', 1.000000))
Rule('RXN_9662',
	cplx(name = 'CPLX0_8006', loc = 'cyt') +
	met(name = 'Myristoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8006', loc = 'cyt') +
	met(name = 'Tetradec_2_enoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_9662', 0.000000), 
	Parameter('rvs_RXN_9662', 1.000000))
Rule('RXN_9663',
	cplx(name = 'CPLX0_8006', loc = 'cyt') +
	met(name = 'Palmitoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8006', loc = 'cyt') +
	met(name = '_2_Hexadecenoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_9663', 0.000000), 
	Parameter('rvs_RXN_9663', 1.000000))
Rule('UDPGLCNACEPIM_RXN',
	cplx(name = 'CPLX0_8008', loc = 'cyt') +
	met(name = 'UDP_N_ACETYL_D_GLUCOSAMINE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8008', loc = 'cyt') +
	met(name = 'UDP_MANNAC', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_UDPGLCNACEPIM_RXN', 1.000000), 
	Parameter('rvs_UDPGLCNACEPIM_RXN', 1.000000))
Rule('RXN0_7066',
	cplx(name = 'CPLX0_8010', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PREPHENATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8010', loc = 'cyt') +
	met(name = 'PHENYL_PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_15403', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7066', 1.000000), 
	Parameter('rvs_RXN0_7066', 0.000000))
Rule('GLCNACPTRANS_RXN',
	cplx(name = 'CPLX0_8011', loc = 'imem') +
	met(name = 'CPD_9646', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UDP_N_ACETYL_D_GLUCOSAMINE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8011', loc = 'imem') +
	met(name = 'ACETYL_D_GLUCOSAMINYLDIPHOSPHO_UNDECAPRE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLCNACPTRANS_RXN', 1.000000), 
	Parameter('rvs_GLCNACPTRANS_RXN', 0.000000))
Rule('DTDPGLUCOSEPP_RXN',
	cplx(name = 'CPLX0_8012', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLC_1_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TTP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8012', loc = 'cyt') +
	met(name = 'DTDP_D_GLUCOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_DTDPGLUCOSEPP_RXN', 1.000000), 
	Parameter('rvs_DTDPGLUCOSEPP_RXN', 0.000000))
Rule('UDPMANNACADEHYDROG_RXN',
	cplx(name = 'CPLX0_8013', loc = 'cyt') +
	met(name = 'UDP_MANNAC', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8013', loc = 'cyt') +
	met(name = 'UDP_MANNACA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_UDPMANNACADEHYDROG_RXN', 1.000000), 
	Parameter('rvs_UDPMANNACADEHYDROG_RXN', 0.000000))
Rule('UDP_NACMUR_ALA_LIG_RXN',
	cplx(name = 'CPLX0_8014', loc = 'cyt') +
	met(name = 'L_ALPHA_ALANINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UDP_N_ACETYLMURAMATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8014', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_1456', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_UDP_NACMUR_ALA_LIG_RXN', 1.000000), 
	Parameter('rvs_UDP_NACMUR_ALA_LIG_RXN', 0.000000))
Rule('ALCOHOL_DEHYDROG_RXN',
	cplx(name = 'CPLX0_8015', loc = 'cyt') +
	met(name = 'ETOH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8015', loc = 'cyt') +
	met(name = 'ACETALD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ALCOHOL_DEHYDROG_RXN', 1.000000), 
	Parameter('rvs_ALCOHOL_DEHYDROG_RXN', 1.000000))
Rule('ALCOHOL_DEHYDROG_GENERIC_RXN',
	cplx(name = 'CPLX0_8015', loc = 'cyt') +
	met(name = 'Primary_Alcohols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8015', loc = 'cyt') +
	met(name = 'Aldehydes', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ALCOHOL_DEHYDROG_GENERIC_RXN', 1.000000), 
	Parameter('rvs_ALCOHOL_DEHYDROG_GENERIC_RXN', 1.000000))
Rule('UDPHYDROXYMYRGLUCOSAMNACETYLTRANS_RXN',
	cplx(name = 'CPLX0_8016', loc = 'cyt') +
	met(name = 'R_3_hydroxymyristoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UDP_OHMYR_GLUCOSAMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8016', loc = 'cyt') +
	met(name = 'OH_MYRISTOYL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_UDPHYDROXYMYRGLUCOSAMNACETYLTRANS_RXN', 1.000000), 
	Parameter('rvs_UDPHYDROXYMYRGLUCOSAMNACETYLTRANS_RXN', 0.000000))
Rule('PYRIDOXKIN_RXN',
	cplx(name = 'CPLX0_8031', loc = 'cyt') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRIDOXAL', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8031', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRIDOXAL_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PYRIDOXKIN_RXN', 1.000000), 
	Parameter('rvs_PYRIDOXKIN_RXN', 0.000000))
Rule('RXN0_7075',
	cplx(name = 'CPLX0_8032', loc = 'cyt') +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXALATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8032', loc = 'cyt') +
	met(name = 'OXALYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACET', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7075', 1.000000), 
	Parameter('rvs_RXN0_7075', 1.000000))
Rule('ACETYLESTERASE_RXN',
	cplx(name = 'CPLX0_8033', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Acetate_esters', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8033', loc = 'cyt') +
	met(name = 'Alcohols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACET', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ACETYLESTERASE_RXN', 1.000000), 
	Parameter('rvs_ACETYLESTERASE_RXN', 0.000000))
Rule('RXN_8348',
	cplx(name = 'CPLX0_8045', loc = 'cyt') +
	met(name = 'CPD_8122', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_3', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8045', loc = 'cyt') +
	met(name = 'CPD_8123', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_8348', 1.000000), 
	Parameter('rvs_RXN_8348', 0.000000))
Rule('CYSTATHIONINE_BETA_LYASE_RXN',
	cplx(name = 'CPLX0_8092', loc = 'cyt') +
	met(name = 'L_CYSTATHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8092', loc = 'cyt') +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_CYSTATHIONINE_BETA_LYASE_RXN', 1.000000), 
	Parameter('rvs_CYSTATHIONINE_BETA_LYASE_RXN', 0.000000))
Rule('RXN0_5509',
	cplx(name = 'CPLX0_8095', loc = 'cyt') +
	met(name = 'mRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8095', loc = 'cyt') +
	met(name = 'mRNA_Fragments', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_5509', 1.000000), 
	Parameter('rvs_RXN0_5509', 0.000000))
Rule('UGD_RXN',
	cplx(name = 'CPLX0_8098', loc = 'cyt') +
	met(name = 'CPD_12575', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8098', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UDP_GLUCURONATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_UGD_RXN', 1.000000), 
	Parameter('rvs_UGD_RXN', 0.000000))
Rule('RXN0_5107',
	cplx(name = 'CPLX0_8106', loc = 'cyt') +
	met(name = 'TTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8106', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5107', 1.000000), 
	Parameter('rvs_RXN0_5107', 0.000000))
Rule('RXN_14139',
	cplx(name = 'CPLX0_8106', loc = 'cyt') +
	met(name = 'UTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8106', loc = 'cyt') +
	met(name = 'UMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14139', 1.000000), 
	Parameter('rvs_RXN_14139', 0.000000))
Rule('RXN0_4181',
	cplx(name = 'CPLX0_8109', loc = 'cyt') +
	met(name = 'C_DI_GMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8109', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_DI_GMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_4181', 1.000000), 
	Parameter('rvs_RXN0_4181', 0.000000))
Rule('RXN0_7090',
	cplx(name = 'CPLX0_8112', loc = 'cyt') +
	met(name = '_50S_Ribosomal_subunit_protein_L16_Arg', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8112', loc = 'cyt') +
	met(name = '_50S_Ribo_protein_L16_Hydroxylarginine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SUC', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7090', 1.000000), 
	Parameter('rvs_RXN0_7090', 0.000000))
Rule('RXN_9087',
	cplx(name = 'CPLX0_8121', loc = 'cyt') +
	met(name = 'PROPIONYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8121', loc = 'cyt') +
	met(name = 'ACRYLYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_9087', 0.000000), 
	Parameter('rvs_RXN_9087', 1.000000))
Rule('RXN0_5204',
	cplx(name = 'CPLX0_8122', loc = 'cyt') +
	met(name = 'PepB_Aminopeptidase_Substrates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8122', loc = 'cyt') +
	met(name = 'Amino_Acids_20', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Peptides_holder', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5204', 1.000000), 
	Parameter('rvs_RXN0_5204', 0.000000))
Rule('RXN0_5507',
	cplx(name = 'CPLX0_8123', loc = 'cyt') +
	met(name = 'DIHYDRONEOPTERIN_P3', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	cplx(name = 'CPLX0_8123', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_1699', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'P3I', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETALD', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5507', 1.000000), 
	Parameter('rvs_RXN0_5507', 0.000000))
Rule('TRNA_S_TRANSFERASE_RXN',
	cplx(name = 'CPLX0_8124', loc = 'cyt') +
	met(name = 'L_Cysteine_Desulfurase_persulfide', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Cytosine_32_In_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Reduced_ferredoxins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8124', loc = 'cyt') +
	met(name = 'Cysteine_Desulfurase_L_cysteine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_Thiocytosine_32_In_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Oxidized_ferredoxins', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_TRNA_S_TRANSFERASE_RXN', 1.000000), 
	Parameter('rvs_TRNA_S_TRANSFERASE_RXN', 0.000000))
Rule('CELLULOSE_SYNTHASE_UDP_FORMING_RXN',
	cplx(name = 'CPLX0_8125', loc = 'imem') +
	met(name = 'CPD_12575', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CELLULOSE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8125', loc = 'imem') +
	met(name = 'CELLULOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UDP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_CELLULOSE_SYNTHASE_UDP_FORMING_RXN', 1.000000), 
	Parameter('rvs_CELLULOSE_SYNTHASE_UDP_FORMING_RXN', 0.000000))
Rule('RXN0_7103',
	cplx(name = 'CPLX0_8127', loc = 'cyt') +
	met(name = 'CPD0_2558', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8127', loc = 'cyt') +
	met(name = 'CPD0_2559', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7103', 1.000000), 
	Parameter('rvs_RXN0_7103', 0.000000))
Rule('RXN_9311',
	cplx(name = 'CPLX0_8128', loc = 'cyt') +
	met(name = 'CPD_9925', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8128', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DIHYDROXYNAPHTHOATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_9311', 1.000000), 
	Parameter('rvs_RXN_9311', 0.000000))
Rule('_3dot4dot13dot9_RXN',
	cplx(name = 'CPLX0_8156', loc = 'cyt') +
	met(name = 'Dipeptides_With_Proline_Carboxy', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8156', loc = 'cyt') +
	met(name = 'PRO', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Amino_Acids_20', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3dot4dot13dot9_RXN', 1.000000), 
	Parameter('rvs__3dot4dot13dot9_RXN', 0.000000))
Rule('DLACTDEHYDROGNAD_RXN',
	cplx(name = 'CPLX0_8158', loc = 'cyt') +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_LACTATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8158', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DLACTDEHYDROGNAD_RXN', 0.000000), 
	Parameter('rvs_DLACTDEHYDROGNAD_RXN', 1.000000))
Rule('PUTTRANSAM_RXN',
	cplx(name = 'CPLX0_8159', loc = 'cyt') +
	met(name = 'PUTRESCINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8159', loc = 'cyt') +
	met(name = '_4_AMINO_BUTYRALDEHYDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PUTTRANSAM_RXN', 1.000000), 
	Parameter('rvs_PUTTRANSAM_RXN', 0.000000))
Rule('DIAMTRANSAM_RXN',
	cplx(name = 'CPLX0_8159', loc = 'cyt') +
	met(name = 'Aliphatic_Alpha_Omega_Diamines', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8159', loc = 'cyt') +
	met(name = 'Aliphatic_Omega_Amino_Aldehydes', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DIAMTRANSAM_RXN', 1.000000), 
	Parameter('rvs_DIAMTRANSAM_RXN', 1.000000))
Rule('SUCCINATE_DEHYDROGENASE_UBIQUINONE_RXN',
	cplx(name = 'CPLX0_8160', loc = 'imem') +
	met(name = 'Ubiquinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SUC', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8160', loc = 'imem') +
	met(name = 'Ubiquinols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FUM', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_SUCCINATE_DEHYDROGENASE_UBIQUINONE_RXN', 1.000000), 
	Parameter('rvs_SUCCINATE_DEHYDROGENASE_UBIQUINONE_RXN', 0.000000))
Rule('RXN_8344',
	cplx(name = 'CPLX0_8163', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_4', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8163', loc = 'cyt') +
	met(name = 'CPD_8122', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_8344', 1.000000), 
	Parameter('rvs_RXN_8344', 0.000000))
Rule('RXN_11361',
	cplx(name = 'CPLX0_8164', loc = 'cyt') +
	met(name = 'MPT_Synthase_small_subunits', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8164', loc = 'cyt') +
	met(name = 'Carboxyadenylated_MPT_synthases', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_11361', 1.000000), 
	Parameter('rvs_RXN_11361', 0.000000))
Rule('RXN0_5256',
	cplx(name = 'CPLX0_8167', loc = 'imem') +
	met(name = 'Menaquinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HYDROGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8167', loc = 'imem') +
	met(name = 'Menaquinols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_5256', 1.000000), 
	Parameter('rvs_RXN0_5256', 1.000000))
Rule('RXN_16420',
	cplx(name = 'CPLX0_8167', loc = 'imem') +
	met(name = 'HYDROGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8167', loc = 'imem') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_16420', 1.000000), 
	Parameter('rvs_RXN_16420', 0.000000))
Rule('RXN0_7115',
	cplx(name = 'CPLX0_8176', loc = 'mem') +
	met(name = 'N6_L_threonylcarbamoyladenine37_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	cplx(name = 'CPLX0_8176', loc = 'mem') +
	met(name = 'Cyclic_N6_threonylcarbamoyl_A37_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7115', 1.000000), 
	Parameter('rvs_RXN0_7115', 0.000000))
Rule('RXN_14570',
	cplx(name = 'CPLX0_8182', loc = 'cyt') +
	met(name = 'CPD_15435', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'tRNA_adenine_37', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8182', loc = 'cyt') +
	met(name = 'N6_L_threonylcarbamoyladenine37_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14570', 1.000000), 
	Parameter('rvs_RXN_14570', 0.000000))
Rule('RXN0_3182',
	cplx(name = 'CPLX0_8183', loc = 'per') +
	met(name = 'General_Protein_Substrates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8183', loc = 'per') +
	met(name = 'Peptides_holder', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_3182', 1.000000), 
	Parameter('rvs_RXN0_3182', 0.000000))
Rule('_1dot1dot1dot251_RXN',
	cplx(name = 'CPLX0_8186', loc = 'cyt') +
	met(name = 'GALACTITOL_1_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8186', loc = 'cyt') +
	met(name = 'CPD_15826', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__1dot1dot1dot251_RXN', 1.000000), 
	Parameter('rvs__1dot1dot1dot251_RXN', 1.000000))
Rule('RXN0_7160',
	cplx(name = 'CPLX0_8189', loc = 'imem') +
	met(name = 'Protein_L_lysine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8189', loc = 'imem') +
	met(name = 'CPD3O_0', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7160', 1.000000), 
	Parameter('rvs_RXN0_7160', 0.000000))
Rule('RXN0_7067',
	cplx(name = 'CPLX0_8190', loc = 'cyt') +
	met(name = '_5_HYDROXYU34_TRNA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_15403', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8190', loc = 'cyt') +
	met(name = '_5_oxyacetylU34_tRNA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7067', 1.000000), 
	Parameter('rvs_RXN0_7067', 0.000000))
Rule('DISULFOXRED_RXN',
	cplx(name = 'CPLX0_8191', loc = 'cyt') +
	met(name = 'Oxidized_Disulfide_Carrier_Proteins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Protein_Red_Disulfides', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8191', loc = 'cyt') +
	met(name = 'Reduced_Disulfide_Carrier_Proteins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Protein_Ox_Disulfides', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DISULFOXRED_RXN', 1.000000), 
	Parameter('rvs_DISULFOXRED_RXN', 0.000000))
Rule('GLUC1PURIDYLTRANS_RXN',
	cplx(name = 'CPLX0_8205', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLC_1_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UTP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8205', loc = 'cyt') +
	met(name = 'CPD_12575', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_GLUC1PURIDYLTRANS_RXN', 1.000000), 
	Parameter('rvs_GLUC1PURIDYLTRANS_RXN', 0.000000))
Rule('THIAZOLSYN3_RXN',
	cplx(name = 'CPLX0_8211', loc = 'cyt') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'THZ', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8211', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'THZ_P', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_THIAZOLSYN3_RXN', 1.000000), 
	Parameter('rvs_THIAZOLSYN3_RXN', 0.000000))
Rule('RXN0_7298',
	cplx(name = 'CPLX0_8211', loc = 'cyt') +
	met(name = 'PRENOL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8211', loc = 'cyt') +
	met(name = 'CPD_14332', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7298', 1.000000), 
	Parameter('rvs_RXN0_7298', 0.000000))
Rule('ERYTHRON4PDEHYDROG_RXN',
	cplx(name = 'CPLX0_8212', loc = 'cyt') +
	met(name = 'ERYTHRONATE_4P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8212', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_3OH_4P_OH_ALPHA_KETOBUTYRATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ERYTHRON4PDEHYDROG_RXN', 1.000000), 
	Parameter('rvs_ERYTHRON4PDEHYDROG_RXN', 0.000000))
Rule('RXN_17663',
	cplx(name = 'CPLX0_8213', loc = 'imem') +
	met(name = 'ETR_Quinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Protein_L_methionine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8213', loc = 'imem') +
	met(name = 'ETR_Quinols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Protein_L_methionine_R_S_oxides', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_17663', 0.000000), 
	Parameter('rvs_RXN_17663', 1.000000))
Rule('RXN_17652',
	cplx(name = 'CPLX0_8213', loc = 'imem') +
	met(name = 'ETR_Quinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Protein_L_methionine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8213', loc = 'imem') +
	met(name = 'ETR_Quinols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Protein_L_methionine_S_S_oxides', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_17652', 0.000000), 
	Parameter('rvs_RXN_17652', 1.000000))
Rule('CARBOXYLESTERASE_RXN',
	cplx(name = 'CPLX0_8214', loc = 'cyt') +
	met(name = 'Carboxylic_esters', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8214', loc = 'cyt') +
	met(name = 'Alcohols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Carboxylates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_CARBOXYLESTERASE_RXN', 1.000000), 
	Parameter('rvs_CARBOXYLESTERASE_RXN', 0.000000))
Rule('_1dot8dot4dot14_RXN',
	cplx(name = 'CPLX0_8217', loc = 'cyt') +
	met(name = 'MET', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Ox_Thioredoxin', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8217', loc = 'cyt') +
	met(name = 'CPD_8990', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Red_Thioredoxin', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd__1dot8dot4dot14_RXN', 0.000000), 
	Parameter('rvs__1dot8dot4dot14_RXN', 1.000000))
Rule('RXN0_963',
	cplx(name = 'CPLX0_821', loc = 'cyt') +
	met(name = 'FRUCTOSELYSINE_6_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_821', loc = 'cyt') +
	met(name = 'GLC_6_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'LYS', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_963', 1.000000), 
	Parameter('rvs_RXN0_963', 0.000000))
Rule('RXN0_6381',
	cplx(name = 'CPLX0_8228', loc = 'cyt') +
	met(name = 'mRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8228', loc = 'cyt') +
	met(name = 'mRNA_Fragments', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_6381', 1.000000), 
	Parameter('rvs_RXN0_6381', 0.000000))
Rule('RXN_11637',
	cplx(name = 'CPLX0_8231', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_16S_rRNA_cytidine1402', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8231', loc = 'cyt') +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_16S_rRNA_2_O_methylcytidine1402', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11637', 1.000000), 
	Parameter('rvs_RXN_11637', 0.000000))
Rule('RXN_18258',
	cplx(name = 'CPLX0_8232', loc = 'cyt') +
	met(name = 'GAMMA_BUTYROBETAINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8232', loc = 'cyt') +
	met(name = 'SUCC_S_ALD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TRIMETHYLAMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_18258', 1.000000), 
	Parameter('rvs_RXN_18258', 0.000000))
Rule('RXN_18376',
	cplx(name = 'CPLX0_8232', loc = 'cyt') +
	met(name = 'CHOLINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8232', loc = 'cyt') +
	met(name = 'GLYCOLALDEHYDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TRIMETHYLAMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_18376', 1.000000), 
	Parameter('rvs_RXN_18376', 0.000000))
Rule('RXN_5921',
	cplx(name = 'CPLX0_8232', loc = 'cyt') +
	met(name = 'CARNITINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8232', loc = 'cyt') +
	met(name = 'CPD_16618', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TRIMETHYLAMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_5921', 1.000000), 
	Parameter('rvs_RXN_5921', 0.000000))
Rule('RXN0_5398',
	cplx(name = 'CPLX0_8233', loc = 'cyt') +
	met(name = 'CPD_15317', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'URACIL', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8233', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PSEUDOURIDINE_5_P', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5398', 1.000000), 
	Parameter('rvs_RXN0_5398', 1.000000))
Rule('RXN_18604',
	cplx(name = 'CPLX0_8238', loc = 'imem') +
	met(name = 'Menaquinols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'an_oxidized_NrfB_protein', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8238', loc = 'imem') +
	met(name = 'Menaquinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'a_reduced_NrfB_protein', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_18604', 1.000000), 
	Parameter('rvs_RXN_18604', 0.000000))
Rule('_5_OXOPROLINASE_ATP_HYDROLYSING_RXN',
	cplx(name = 'CPLX0_8249', loc = 'cyt') +
	met(name = '_5_OXOPROLINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8249', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__5_OXOPROLINASE_ATP_HYDROLYSING_RXN', 1.000000), 
	Parameter('rvs__5_OXOPROLINASE_ATP_HYDROLYSING_RXN', 0.000000))
Rule('RXN0_7285',
	cplx(name = 'CPLX0_8251', loc = 'cyt') +
	met(name = 'HOMO_SER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8251', loc = 'cyt') +
	met(name = 'CPD_12255', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7285', 1.000000), 
	Parameter('rvs_RXN0_7285', 1.000000))
Rule('BETA_LACTAMASE_RXN',
	cplx(name = 'CPLX0_8252', loc = 'per') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Beta_Lactams', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8252', loc = 'per') +
	met(name = 'CPD_8550', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_BETA_LACTAMASE_RXN', 1.000000), 
	Parameter('rvs_BETA_LACTAMASE_RXN', 0.000000))
Rule('_3dot4dot17dot8_RXN',
	cplx(name = 'CPLX0_8252', loc = 'per') +
	met(name = 'C1', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8252', loc = 'per') +
	met(name = 'UDP_MURNAC_TETRAPEPTIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_ALANINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3dot4dot17dot8_RXN', 1.000000), 
	Parameter('rvs__3dot4dot17dot8_RXN', 0.000000))
Rule('RXN_19249',
	cplx(name = 'CPLX0_8252', loc = 'per') +
	met(name = 'CPD0_1965', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8252', loc = 'per') +
	met(name = 'CPD_20746', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_ALANINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_19249', 1.000000), 
	Parameter('rvs_RXN_19249', 1.000000))
Rule('RXN_19253',
	cplx(name = 'CPLX0_8252', loc = 'per') +
	met(name = 'CPD_15384', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8252', loc = 'per') +
	met(name = 'CPD_20750', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_ALANINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_19253', 1.000000), 
	Parameter('rvs_RXN_19253', 1.000000))
Rule('RXN_19256',
	cplx(name = 'CPLX0_8254', loc = 'per') +
	met(name = 'CPD_20756', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8254', loc = 'per') +
	met(name = 'CPD_20757', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_ALANINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_19256', 1.000000), 
	Parameter('rvs_RXN_19256', 1.000000))
Rule('DTMPKI_RXN',
	cplx(name = 'CPLX0_8260', loc = 'cyt') +
	met(name = 'TMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8260', loc = 'cyt') +
	met(name = 'TDP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DTMPKI_RXN', 1.000000), 
	Parameter('rvs_DTMPKI_RXN', 0.000000))
Rule('THYKI_RXN',
	cplx(name = 'CPLX0_8261', loc = 'cyt') +
	met(name = 'THYMIDINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8261', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_THYKI_RXN', 1.000000), 
	Parameter('rvs_THYKI_RXN', 0.000000))
Rule('DURIDKI_RXN',
	cplx(name = 'CPLX0_8261', loc = 'cyt') +
	met(name = 'DEOXYURIDINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8261', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DUMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DURIDKI_RXN', 1.000000), 
	Parameter('rvs_DURIDKI_RXN', 0.000000))
Rule('INOSINATE_NUCLEOSIDASE_RXN',
	cplx(name = 'CPLX0_8262', loc = 'cyt') +
	met(name = 'IMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8262', loc = 'cyt') +
	met(name = 'HYPOXANTHINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_15317', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_INOSINATE_NUCLEOSIDASE_RXN', 1.000000), 
	Parameter('rvs_INOSINATE_NUCLEOSIDASE_RXN', 0.000000))
Rule('_3dot2dot2dot10_RXN',
	cplx(name = 'CPLX0_8262', loc = 'cyt') +
	met(name = 'Pyrimidine_ribonucleotides', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_8262', loc = 'cyt') +
	met(name = 'RIBOSE_5P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pyrimidine_Bases', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3dot2dot2dot10_RXN', 1.000000), 
	Parameter('rvs__3dot2dot2dot10_RXN', 0.000000))
Rule('RXN0_7299',
	cplx(name = 'CPLX0_8270', loc = 'imem') +
	met(name = 'CPLX0_7748', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_8270', loc = 'imem') +
	met(name = 'CPXR_MONOMER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7299', 1.000000), 
	Parameter('rvs_RXN0_7299', 0.000000))
Rule('RXN_17630',
	cplx(name = 'CPLX0_861', loc = 'cyt') +
	met(name = 'Protein_Arginine_Aminocarbinol', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_861', loc = 'cyt') +
	met(name = 'Protein_L_Arginines', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_LACTATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17630', 1.000000), 
	Parameter('rvs_RXN_17630', 0.000000))
Rule('RXN_17634',
	cplx(name = 'CPLX0_861', loc = 'cyt') +
	met(name = 'Protein_Cysteine_Hemithioacetal', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CPLX0_861', loc = 'cyt') +
	met(name = 'PROT_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_LACTATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17634', 1.000000), 
	Parameter('rvs_RXN_17634', 0.000000))
Rule('GLYOXIII_RXN',
	cplx(name = 'CPLX0_861', loc = 'cyt') +
	met(name = 'D_LACTATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_861', loc = 'cyt') +
	met(name = 'METHYL_GLYOXAL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLYOXIII_RXN', 0.000000), 
	Parameter('rvs_GLYOXIII_RXN', 1.000000))
Rule('RXN0_1081',
	cplx(name = 'CPLX0_901', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'tRNA_Arg_adenosine34', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLX0_901', loc = 'cyt') +
	met(name = 'tRNA_Arg_inosine34', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_1081', 1.000000), 
	Parameter('rvs_RXN0_1081', 0.000000))
Rule('NMNAMIDOHYDRO_RXN',
	cplx(name = 'CPLXECOLI_7943', loc = 'cyt') +
	met(name = 'NICOTINAMIDE_NUCLEOTIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CPLXECOLI_7943', loc = 'cyt') +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NICOTINATE_NUCLEOTIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_NMNAMIDOHYDRO_RXN', 1.000000), 
	Parameter('rvs_NMNAMIDOHYDRO_RXN', 0.000000))
Rule('CPM_KDOSYNTH_RXN',
	prot(name = 'CPM_KDOSYNTH_MONOMER', loc = 'cyt') +
	met(name = 'KDO', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CTP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'CPM_KDOSYNTH_MONOMER', loc = 'cyt') +
	met(name = 'CMP_KDO', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_CPM_KDOSYNTH_RXN', 1.000000), 
	Parameter('rvs_CPM_KDOSYNTH_RXN', 0.000000))
Rule('CROBETREDUCT_RXN',
	prot(name = 'CROBETREDUCT_MONOMER', loc = 'cyt') +
	met(name = 'GAMMA_BUTYROBETAINYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ETF_Oxidized', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'CROBETREDUCT_MONOMER', loc = 'cyt') +
	met(name = 'CROTONOBETAINYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ETF_Reduced', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_CROBETREDUCT_RXN', 0.000000), 
	Parameter('rvs_CROBETREDUCT_RXN', 1.000000))
Rule('CTPSYN_RXN',
	cplx(name = 'CTPSYN_CPLX', loc = 'cyt') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'CTPSYN_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_CTPSYN_RXN', 1.000000), 
	Parameter('rvs_CTPSYN_RXN', 0.000000))
Rule('R524_RXN',
	cplx(name = 'CYANLY_CPLX', loc = 'cyt') +
	met(name = 'CPD_69', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HCO3', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CYANLY_CPLX', loc = 'cyt') +
	met(name = 'CARBAMATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_R524_RXN', 1.000000), 
	Parameter('rvs_R524_RXN', 0.000000))
Rule('CYSTEINE__TRNA_LIGASE_RXN',
	prot(name = 'CYSS_MONOMER', loc = 'cyt') +
	met(name = 'CYS_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'CYSS_MONOMER', loc = 'cyt') +
	met(name = 'Charged_CYS_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_CYSTEINE__TRNA_LIGASE_RXN', 1.000000), 
	Parameter('rvs_CYSTEINE__TRNA_LIGASE_RXN', 0.000000))
Rule('RXN_19778',
	cplx(name = 'CYT_D_UBIOX_CPLX', loc = 'imem') +
	met(name = 'Ubiquinols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HYDROGEN_PEROXIDE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CYT_D_UBIOX_CPLX', loc = 'imem') +
	met(name = 'Ubiquinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_19778', 1.000000), 
	Parameter('rvs_RXN_19778', 0.000000))
Rule('RXN_19777',
	cplx(name = 'CYT_D_UBIOX_CPLX', loc = 'imem') +
	met(name = 'CPD_7249', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HYDROGEN_PEROXIDE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CYT_D_UBIOX_CPLX', loc = 'imem') +
	met(name = 'CPD_7248', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_19777', 1.000000), 
	Parameter('rvs_RXN_19777', 1.000000))
Rule('RXN0_5268',
	cplx(name = 'CYT_O_UBIOX_CPLX', loc = 'imem') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Ubiquinols', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CYT_O_UBIOX_CPLX', loc = 'imem') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Ubiquinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5268', 1.000000), 
	Parameter('rvs_RXN0_5268', 0.000000))
Rule('CYTIDEAM2_RXN',
	cplx(name = 'CYTIDEAM_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CYTIDINE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CYTIDEAM_CPLX', loc = 'cyt') +
	met(name = 'URIDINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_CYTIDEAM2_RXN', 1.000000), 
	Parameter('rvs_CYTIDEAM2_RXN', 0.000000))
Rule('CYTIDEAM_RXN',
	cplx(name = 'CYTIDEAM_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DEOXYCYTIDINE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'CYTIDEAM_CPLX', loc = 'cyt') +
	met(name = 'DEOXYURIDINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_CYTIDEAM_RXN', 1.000000), 
	Parameter('rvs_CYTIDEAM_RXN', 0.000000))
Rule('RXN_18605',
	prot(name = 'CYTOCHROMEC552_MONOMER', loc = 'per') +
	met(name = 'a_reduced_NrfB_protein', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NITRITE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'CYTOCHROMEC552_MONOMER', loc = 'per') +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'an_oxidized_NrfB_protein', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_18605', 1.000000), 
	Parameter('rvs_RXN_18605', 0.000000))
Rule('DALADALALIG_RXN',
	prot(name = 'DALADALALIGA_MONOMER', loc = 'cyt') +
	met(name = 'D_ALANINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	prot(name = 'DALADALALIGA_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_ALA_D_ALA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DALADALALIG_RXN', 1.000000), 
	Parameter('rvs_DALADALALIG_RXN', 0.000000))
Rule('RXN_11193',
	cplx(name = 'DALADEHYDROG_CPLX', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_Amino_Acids', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ETR_Quinones', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'DALADEHYDROG_CPLX', loc = 'cyt') +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_Oxo_carboxylates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ETR_Quinols', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11193', 1.000000), 
	Parameter('rvs_RXN_11193', 0.000000))
Rule('DALADEHYDROG_RXN',
	cplx(name = 'DALADEHYDROG_CPLX', loc = 'cyt') +
	met(name = 'ETR_Quinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_ALANINE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'DALADEHYDROG_CPLX', loc = 'cyt') +
	met(name = 'ETR_Quinols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DALADEHYDROG_RXN', 1.000000), 
	Parameter('rvs_DALADEHYDROG_RXN', 0.000000))
Rule('DAPASYN_RXN',
	cplx(name = 'DAPASYN_CPLX', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_8_AMINO_7_OXONONANOATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'DAPASYN_CPLX', loc = 'cyt') +
	met(name = 'S_ADENOSYL_4_METHYLTHIO_2_OXOBUTANOATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DIAMINONONANOATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DAPASYN_RXN', 1.000000), 
	Parameter('rvs_DAPASYN_RXN', 1.000000))
Rule('DCTP_DEAM_RXN',
	cplx(name = 'DCTP_DEAM_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DCTP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'DCTP_DEAM_CPLX', loc = 'cyt') +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DUTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_DCTP_DEAM_RXN', 1.000000), 
	Parameter('rvs_DCTP_DEAM_RXN', 0.000000))
Rule('DCYSDESULF_RXN',
	cplx(name = 'DCYSDESULF_CPLX', loc = 'cyt') +
	met(name = 'D_CYSTEINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'DCYSDESULF_CPLX', loc = 'cyt') +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HS', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DCYSDESULF_RXN', 1.000000), 
	Parameter('rvs_DCYSDESULF_RXN', 0.000000))
Rule('ALADEHYDCHLORO_RXN',
	cplx(name = 'DCYSDESULF_CPLX', loc = 'cyt') +
	met(name = '_3_CHLORO_D_ALANINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'THIOGLYCOLATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'DCYSDESULF_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'S_CARBOXYMETHYL_D_CYSTEINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CL_', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ALADEHYDCHLORO_RXN', 1.000000), 
	Parameter('rvs_ALADEHYDCHLORO_RXN', 0.000000))
Rule('DEHYDDEOXGALACTKIN_RXN',
	prot(name = 'DEHYDDEOXGALACTKIN_MONOMER', loc = 'cyt') +
	met(name = '_2_DEHYDRO_3_DEOXY_D_GALACTONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'DEHYDDEOXGALACTKIN_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DEHYDRO_DEOXY_GALACTONATE_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DEHYDDEOXGALACTKIN_RXN', 1.000000), 
	Parameter('rvs_DEHYDDEOXGALACTKIN_RXN', 0.000000))
Rule('DEHYDDEOXPHOSGALACT_ALDOL_RXN',
	prot(name = 'DEHYDDEOXPHOSGALACT_ALDOL_MONOMER', loc = 'cyt') +
	met(name = 'DEHYDRO_DEOXY_GALACTONATE_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'DEHYDDEOXPHOSGALACT_ALDOL_MONOMER', loc = 'cyt') +
	met(name = 'GAP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DEHYDDEOXPHOSGALACT_ALDOL_RXN', 1.000000), 
	Parameter('rvs_DEHYDDEOXPHOSGALACT_ALDOL_RXN', 1.000000))
Rule('_1dot1dot1dot168_RXN',
	prot(name = 'DEHYDROPANTLACRED_MONOMER', loc = 'cyt') +
	met(name = 'PANTOYL_LACTONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'DEHYDROPANTLACRED_MONOMER', loc = 'cyt') +
	met(name = '_2_DEHYDROPANTOYL_LACTONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__1dot1dot1dot168_RXN', 1.000000), 
	Parameter('rvs__1dot1dot1dot168_RXN', 1.000000))
Rule('THYM_PHOSPH_RXN',
	cplx(name = 'DEOA_CPLX', loc = 'cyt') +
	met(name = 'THYMIDINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'DEOA_CPLX', loc = 'cyt') +
	met(name = 'DEOXY_D_RIBOSE_1_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'THYMINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_THYM_PHOSPH_RXN', 1.000000), 
	Parameter('rvs_THYM_PHOSPH_RXN', 1.000000))
Rule('URA_PHOSPH_RXN',
	cplx(name = 'DEOA_CPLX', loc = 'cyt') +
	met(name = 'DEOXYURIDINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'DEOA_CPLX', loc = 'cyt') +
	met(name = 'DEOXY_D_RIBOSE_1_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'URACIL', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_URA_PHOSPH_RXN', 1.000000), 
	Parameter('rvs_URA_PHOSPH_RXN', 1.000000))
Rule('RXN0_5199',
	cplx(name = 'DEOD_CPLX', loc = 'cyt') +
	met(name = 'GUANOSINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'DEOD_CPLX', loc = 'cyt') +
	met(name = 'RIBOSE_1P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GUANINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5199', 1.000000), 
	Parameter('rvs_RXN0_5199', 1.000000))
Rule('PNP_RXN',
	cplx(name = 'DEOD_CPLX', loc = 'cyt') +
	met(name = 'Purine_Ribonucleosides', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'DEOD_CPLX', loc = 'cyt') +
	met(name = 'Purine_Bases', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'RIBOSE_1P', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PNP_RXN', 1.000000), 
	Parameter('rvs_PNP_RXN', 1.000000))
Rule('DEOXYGUANPHOSPHOR_RXN',
	cplx(name = 'DEOD_CPLX', loc = 'cyt') +
	met(name = 'DEOXYGUANOSINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'DEOD_CPLX', loc = 'cyt') +
	met(name = 'GUANINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DEOXY_D_RIBOSE_1_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DEOXYGUANPHOSPHOR_RXN', 1.000000), 
	Parameter('rvs_DEOXYGUANPHOSPHOR_RXN', 1.000000))
Rule('INOPHOSPHOR_RXN',
	cplx(name = 'DEOD_CPLX', loc = 'cyt') +
	met(name = 'INOSINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'DEOD_CPLX', loc = 'cyt') +
	met(name = 'RIBOSE_1P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HYPOXANTHINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_INOPHOSPHOR_RXN', 1.000000), 
	Parameter('rvs_INOPHOSPHOR_RXN', 1.000000))
Rule('DEOXYINOPHOSPHOR_RXN',
	cplx(name = 'DEOD_CPLX', loc = 'cyt') +
	met(name = 'DEOXYINOSINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'DEOD_CPLX', loc = 'cyt') +
	met(name = 'HYPOXANTHINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DEOXY_D_RIBOSE_1_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DEOXYINOPHOSPHOR_RXN', 1.000000), 
	Parameter('rvs_DEOXYINOPHOSPHOR_RXN', 1.000000))
Rule('ADENPHOSPHOR_RXN',
	cplx(name = 'DEOD_CPLX', loc = 'cyt') +
	met(name = 'ADENOSINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'DEOD_CPLX', loc = 'cyt') +
	met(name = 'RIBOSE_1P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ADENPHOSPHOR_RXN', 1.000000), 
	Parameter('rvs_ADENPHOSPHOR_RXN', 1.000000))
Rule('DEOXYADENPHOSPHOR_RXN',
	cplx(name = 'DEOD_CPLX', loc = 'cyt') +
	met(name = 'DEOXYADENOSINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'DEOD_CPLX', loc = 'cyt') +
	met(name = 'ADENINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DEOXY_D_RIBOSE_1_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DEOXYADENPHOSPHOR_RXN', 1.000000), 
	Parameter('rvs_DEOXYADENPHOSPHOR_RXN', 1.000000))
Rule('DEOXYGLUCONOKIN_RXN',
	prot(name = 'DEOXYGLUCONOKIN_MONOMER', loc = 'cyt') +
	met(name = '_2_DEHYDRO_3_DEOXY_D_GLUCONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'DEOXYGLUCONOKIN_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_KETO_3_DEOXY_6_P_GLUCONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DEOXYGLUCONOKIN_RXN', 1.000000), 
	Parameter('rvs_DEOXYGLUCONOKIN_RXN', 0.000000))
Rule('DEOXYRIBOSE_P_ALD_RXN',
	prot(name = 'DEOXYRIBOSE_P_ALD_MONOMER', loc = 'cyt') +
	met(name = 'DEOXY_RIBOSE_5P', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'DEOXYRIBOSE_P_ALD_MONOMER', loc = 'cyt') +
	met(name = 'ACETALD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GAP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DEOXYRIBOSE_P_ALD_RXN', 1.000000), 
	Parameter('rvs_DEOXYRIBOSE_P_ALD_RXN', 1.000000))
Rule('DETHIOBIOTIN_SYN_RXN',
	cplx(name = 'DETHIOBIOTIN_SYN_CPLX', loc = 'cyt') +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DIAMINONONANOATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'DETHIOBIOTIN_SYN_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DETHIOBIOTIN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DETHIOBIOTIN_SYN_RXN', 1.000000), 
	Parameter('rvs_DETHIOBIOTIN_SYN_RXN', 0.000000))
Rule('DGTPTRIPHYDRO_RXN',
	cplx(name = 'DGTPTRIPHYDRO_CPLX', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DGTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'DGTPTRIPHYDRO_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'P3I', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DEOXYGUANOSINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DGTPTRIPHYDRO_RXN', 1.000000), 
	Parameter('rvs_DGTPTRIPHYDRO_RXN', 0.000000))
Rule('_2_OCTAPRENYL_6_OHPHENOL_METHY_RXN',
	cplx(name = 'DHHB_METHYLTRANSFER_CPLX', loc = 'imem') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_OCTAPRENYL_6_HYDROXYPHENOL', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'DHHB_METHYLTRANSFER_CPLX', loc = 'imem') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_OCTAPRENYL_6_METHOXYPHENOL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__2_OCTAPRENYL_6_OHPHENOL_METHY_RXN', 1.000000), 
	Parameter('rvs__2_OCTAPRENYL_6_OHPHENOL_METHY_RXN', 0.000000))
Rule('DHHB_METHYLTRANSFER_RXN',
	cplx(name = 'DHHB_METHYLTRANSFER_CPLX', loc = 'imem') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OCTAPRENYL_METHYL_OH_METHOXY_BENZQ', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'DHHB_METHYLTRANSFER_CPLX', loc = 'imem') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_9956', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DHHB_METHYLTRANSFER_RXN', 1.000000), 
	Parameter('rvs_DHHB_METHYLTRANSFER_RXN', 0.000000))
Rule('_1dot13dot11dot16_RXN',
	cplx(name = 'DHPDIOXYGEN_CPLX', loc = 'cyt') +
	met(name = '_2_3_DIHYDROXYPHENYL_PROPIONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'DHPDIOXYGEN_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_157', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__1dot13dot11dot16_RXN', 1.000000), 
	Parameter('rvs__1dot13dot11dot16_RXN', 0.000000))
Rule('RXN_12073',
	cplx(name = 'DHPDIOXYGEN_CPLX', loc = 'cyt') +
	met(name = 'CPD_10796', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'DHPDIOXYGEN_CPLX', loc = 'cyt') +
	met(name = 'CPD0_2184', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_12073', 1.000000), 
	Parameter('rvs_RXN_12073', 0.000000))
Rule('DIACYLGLYKIN_RXN',
	cplx(name = 'DIACYLGLYKIN_CPLX', loc = 'imem') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DIACYLGLYCEROL', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'DIACYLGLYKIN_CPLX', loc = 'imem') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_PHOSPHATIDATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DIACYLGLYKIN_RXN', 1.000000), 
	Parameter('rvs_DIACYLGLYKIN_RXN', 0.000000))
Rule('DIAMINOPIMDECARB_RXN',
	cplx(name = 'DIAMINOPIMDECARB_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MESO_DIAMINOPIMELATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'DIAMINOPIMDECARB_CPLX', loc = 'cyt') +
	met(name = 'LYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DIAMINOPIMDECARB_RXN', 1.000000), 
	Parameter('rvs_DIAMINOPIMDECARB_RXN', 0.000000))
Rule('DIENOYLCOAREDUCT_RXN',
	prot(name = 'DIENOYLCOAREDUCT_MONOMER', loc = 'cyt') +
	met(name = 'T2_DECENOYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'DIENOYLCOAREDUCT_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'T2_C4_DECADIENYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DIENOYLCOAREDUCT_RXN', 0.000000), 
	Parameter('rvs_DIENOYLCOAREDUCT_RXN', 1.000000))
Rule('DIHYDRODIPICSYN_RXN',
	cplx(name = 'DIHYDRODIPICSYN_CPLX', loc = 'cyt') +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_ASPARTATE_SEMIALDEHYDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'DIHYDRODIPICSYN_CPLX', loc = 'cyt') +
	met(name = 'CPD_14443', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DIHYDRODIPICSYN_RXN', 1.000000), 
	Parameter('rvs_DIHYDRODIPICSYN_RXN', 0.000000))
Rule('DIHYDROFOLATEREDUCT_RXN',
	prot(name = 'DIHYDROFOLATEREDUCT_MONOMER', loc = 'cyt') +
	met(name = 'THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'DIHYDROFOLATEREDUCT_MONOMER', loc = 'cyt') +
	met(name = 'DIHYDROFOLATE_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DIHYDROFOLATEREDUCT_RXN', 0.000000), 
	Parameter('rvs_DIHYDROFOLATEREDUCT_RXN', 1.000000))
Rule('DIHYDRONEOPTERIN_MONO_P_DEPHOS_RXN',
	prot(name = 'DIHYDRONEOPTERIN_MONO_P_DEPHOS_MONOMER', loc = 'cyt') +
	met(name = 'DIHYDRONEOPTERIN_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'DIHYDRONEOPTERIN_MONO_P_DEPHOS_MONOMER', loc = 'cyt') +
	met(name = 'DIHYDRO_NEO_PTERIN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DIHYDRONEOPTERIN_MONO_P_DEPHOS_RXN', 1.000000), 
	Parameter('rvs_DIHYDRONEOPTERIN_MONO_P_DEPHOS_RXN', 0.000000))
Rule('DIHYDROOROT_RXN',
	cplx(name = 'DIHYDROOROT_CPLX', loc = 'cyt') +
	met(name = 'DI_H_OROTATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'DIHYDROOROT_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBAMYUL_L_ASPARTATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DIHYDROOROT_RXN', 1.000000), 
	Parameter('rvs_DIHYDROOROT_RXN', 1.000000))
Rule('DIHYDROOROTATE_DEHYDROGENASE_RXN',
	prot(name = 'DIHYDROOROTOX_MONOMER', loc = 'cyt') +
	met(name = 'ETR_Quinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DI_H_OROTATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'DIHYDROOROTOX_MONOMER', loc = 'cyt') +
	met(name = 'ETR_Quinols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OROTATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DIHYDROOROTATE_DEHYDROGENASE_RXN', 1.000000), 
	Parameter('rvs_DIHYDROOROTATE_DEHYDROGENASE_RXN', 0.000000))
Rule('RXN0_6491',
	prot(name = 'DIHYDROOROTOX_MONOMER', loc = 'cyt') +
	met(name = 'DI_H_OROTATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Ubiquinones', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'DIHYDROOROTOX_MONOMER', loc = 'cyt') +
	met(name = 'OROTATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Ubiquinols', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6491', 1.000000), 
	Parameter('rvs_RXN0_6491', 0.000000))
Rule('RXN0_6554',
	prot(name = 'DIHYDROOROTOX_MONOMER', loc = 'cyt') +
	met(name = 'DI_H_OROTATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Menaquinones', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'DIHYDROOROTOX_MONOMER', loc = 'cyt') +
	met(name = 'OROTATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Menaquinols', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6554', 1.000000), 
	Parameter('rvs_RXN0_6554', 0.000000))
Rule('RXN_14014',
	cplx(name = 'DIHYDROPICRED_CPLX', loc = 'cyt') +
	met(name = 'DELTA1_PIPERIDEINE_2_6_DICARBOXYLATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'DIHYDROPICRED_CPLX', loc = 'cyt') +
	met(name = 'CPD_14443', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14014', 0.000000), 
	Parameter('rvs_RXN_14014', 1.000000))
Rule('RXN_13853',
	cplx(name = 'DIHYDROPTERIREDUCT_CPLX', loc = 'cyt') +
	met(name = 'Nitroaromatic_Ox_Compounds', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'DIHYDROPTERIREDUCT_CPLX', loc = 'cyt') +
	met(name = 'Nitroaromatic_Red_Compounds', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_13853', 1.000000), 
	Parameter('rvs_RXN_13853', 0.000000))
Rule('_1dot5dot1dot34_RXN',
	cplx(name = 'DIHYDROPTERIREDUCT_CPLX', loc = 'cyt') +
	met(name = '_5678_TETRAHYDROPTERIDINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'DIHYDROPTERIREDUCT_CPLX', loc = 'cyt') +
	met(name = '_67_DIHYDROPTERIDINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__1dot5dot1dot34_RXN', 0.000000), 
	Parameter('rvs__1dot5dot1dot34_RXN', 1.000000))
Rule('DIHYDROXYISOVALDEHYDRAT_RXN',
	cplx(name = 'DIHYDROXYACIDDEHYDRAT_CPLX', loc = 'cyt') +
	met(name = 'CPD_13357', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'DIHYDROXYACIDDEHYDRAT_CPLX', loc = 'cyt') +
	met(name = '_2_KETO_ISOVALERATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DIHYDROXYISOVALDEHYDRAT_RXN', 1.000000), 
	Parameter('rvs_DIHYDROXYISOVALDEHYDRAT_RXN', 0.000000))
Rule('DIHYDROXYMETVALDEHYDRAT_RXN',
	cplx(name = 'DIHYDROXYACIDDEHYDRAT_CPLX', loc = 'cyt') +
	met(name = '_1_KETO_2_METHYLVALERATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'DIHYDROXYACIDDEHYDRAT_CPLX', loc = 'cyt') +
	met(name = '_2_KETO_3_METHYL_VALERATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DIHYDROXYMETVALDEHYDRAT_RXN', 1.000000), 
	Parameter('rvs_DIHYDROXYMETVALDEHYDRAT_RXN', 0.000000))
Rule('DIMESULFREDUCT_RXN',
	cplx(name = 'DIMESULFREDUCT_CPLX', loc = 'imem') +
	met(name = 'Menaquinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_7670', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'DIMESULFREDUCT_CPLX', loc = 'imem') +
	met(name = 'Menaquinols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DMSO', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_DIMESULFREDUCT_RXN', 0.000000), 
	Parameter('rvs_DIMESULFREDUCT_RXN', 1.000000))
Rule('DIOHBUTANONEPSYN_RXN',
	cplx(name = 'DIOHBUTANONEPSYN_CPLX', loc = 'imem') +
	met(name = 'RIBULOSE_5P', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	cplx(name = 'DIOHBUTANONEPSYN_CPLX', loc = 'imem') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DIHYDROXY_BUTANONE_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FORMATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DIOHBUTANONEPSYN_RXN', 1.000000), 
	Parameter('rvs_DIOHBUTANONEPSYN_RXN', 0.000000))
Rule('DLACTDEHYDROGFAD_RXN',
	prot(name = 'DLACTDEHYDROGFAD_MONOMER', loc = 'imem') +
	met(name = 'Ubiquinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_LACTATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'DLACTDEHYDROGFAD_MONOMER', loc = 'imem') +
	met(name = 'Ubiquinols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DLACTDEHYDROGFAD_RXN', 1.000000), 
	Parameter('rvs_DLACTDEHYDROGFAD_RXN', 0.000000))
Rule('DMBPPRIBOSYLTRANS_RXN',
	cplx(name = 'DMBPPRIBOSYLTRANS_CPLX', loc = 'cyt') +
	met(name = 'NICOTINATE_NUCLEOTIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DIMETHYLBENZIMIDAZOLE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'DMBPPRIBOSYLTRANS_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NIACINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ALPHA_RIBAZOLE_5_P', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DMBPPRIBOSYLTRANS_RXN', 1.000000), 
	Parameter('rvs_DMBPPRIBOSYLTRANS_RXN', 0.000000))
Rule('DMK_RXN',
	prot(name = 'DMK_MONOMER', loc = 'imem') +
	met(name = 'OCTAPRENYL_DIPHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DIHYDROXYNAPHTHOATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'DMK_MONOMER', loc = 'imem') +
	met(name = 'CPD_12115', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DMK_RXN', 1.000000), 
	Parameter('rvs_DMK_RXN', 0.000000))
Rule('RXN_19988',
	prot(name = 'DSBBPROT_MONOMER', loc = 'imem') +
	met(name = 'MONOMER0_4438', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UBIQUINONE_8', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'DSBBPROT_MONOMER', loc = 'imem') +
	met(name = 'MONOMER0_4152', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_9956', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_19988', 1.000000), 
	Parameter('rvs_RXN_19988', 0.000000))
Rule('RXN_19998',
	prot(name = 'DSBBPROT_MONOMER', loc = 'imem') +
	met(name = 'MONOMER0_4438', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_9728', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'DSBBPROT_MONOMER', loc = 'imem') +
	met(name = 'MONOMER0_4152', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'REDUCED_MENAQUINONE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_19998', 1.000000), 
	Parameter('rvs_RXN_19998', 0.000000))
Rule('RXN_19950',
	prot(name = 'DSBBPROT_MONOMER', loc = 'imem') +
	met(name = 'Reduced_Disulfide_Carrier_Proteins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ETR_Quinones', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'DSBBPROT_MONOMER', loc = 'imem') +
	met(name = 'Oxidized_Disulfide_Carrier_Proteins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ETR_Quinols', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_19950', 1.000000), 
	Parameter('rvs_RXN_19950', 0.000000))
Rule('_5dot3dot4dot1_RXN',
	cplx(name = 'DSBC_CPLX', loc = 'per') +
	met(name = 'Proteins_with_incorrect_disulfides', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'DSBC_CPLX', loc = 'per') +
	met(name = 'Proteins_with_correct_disulfides', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__5dot3dot4dot1_RXN', 1.000000), 
	Parameter('rvs__5dot3dot4dot1_RXN', 1.000000))
Rule('RXN_19949',
	prot(name = 'DSBD_MONOMER', loc = 'imem') +
	met(name = 'Red_Thioredoxin', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Disulfide_Isomerase_with_Disulfide_Bond', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'DSBD_MONOMER', loc = 'imem') +
	met(name = 'Ox_Thioredoxin', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Reduced_Disulfide_Isomerases', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_19949', 1.000000), 
	Parameter('rvs_RXN_19949', 0.000000))
Rule('DSERDEAM_RXN',
	prot(name = 'DSERDEAM_MONOMER', loc = 'cyt') +
	met(name = 'D_SERINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'DSERDEAM_MONOMER', loc = 'cyt') +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DSERDEAM_RXN', 1.000000), 
	Parameter('rvs_DSERDEAM_RXN', 0.000000))
Rule('DTDPDEHYDRHAMEPIM_RXN',
	prot(name = 'DTDPDEHYDRHAMEPIM_MONOMER', loc = 'cyt') +
	met(name = 'DTDP_DEOH_DEOXY_GLUCOSE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'DTDPDEHYDRHAMEPIM_MONOMER', loc = 'cyt') +
	met(name = 'DTDP_DEOH_DEOXY_MANNOSE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DTDPDEHYDRHAMEPIM_RXN', 1.000000), 
	Parameter('rvs_DTDPDEHYDRHAMEPIM_RXN', 0.000000))
Rule('DTDPDEHYRHAMREDUCT_RXN',
	prot(name = 'DTDPDEHYRHAMREDUCT_MONOMER', loc = 'cyt') +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DTDP_RHAMNOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'DTDPDEHYRHAMREDUCT_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DTDP_DEOH_DEOXY_MANNOSE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DTDPDEHYRHAMREDUCT_RXN', 0.000000), 
	Parameter('rvs_DTDPDEHYRHAMREDUCT_RXN', 1.000000))
Rule('DTDPGLUCDEHYDRAT_RXN',
	cplx(name = 'DTDPGLUCDEHYDRAT_CPLX', loc = 'cyt') +
	met(name = 'DTDP_D_GLUCOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'DTDPGLUCDEHYDRAT_CPLX', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DTDP_DEOH_DEOXY_GLUCOSE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DTDPGLUCDEHYDRAT_RXN', 1.000000), 
	Parameter('rvs_DTDPGLUCDEHYDRAT_RXN', 0.000000))
Rule('DUTP_PYROP_RXN',
	cplx(name = 'DUTP_PYROP_CPLX', loc = 'cyt') +
	met(name = 'DUTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'DUTP_PYROP_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DUMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DUTP_PYROP_RXN', 1.000000), 
	Parameter('rvs_DUTP_PYROP_RXN', 0.000000))
Rule('DXPREDISOM_RXN',
	cplx(name = 'DXPREDISOM_CPLX', loc = 'cyt') +
	met(name = '_2_C_METHYL_D_ERYTHRITOL_4_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'DXPREDISOM_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DEOXYXYLULOSE_5P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DXPREDISOM_RXN', 1.000000), 
	Parameter('rvs_DXPREDISOM_RXN', 1.000000))
Rule('_2OXOGLUTDECARB_RXN',
	prot(name = 'E1O', loc = 'cyt') +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Oxo_glutarate_dehydrogenase_lipoyl', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'E1O', loc = 'cyt') +
	met(name = 'Oxo_glutarate_dehydro_suc_DH_lipoyl', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd__2OXOGLUTDECARB_RXN', 1.000000), 
	Parameter('rvs__2OXOGLUTDECARB_RXN', 0.000000))
Rule('RXN0_1134',
	cplx(name = 'E1P_CPLX', loc = 'cyt') +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pyruvate_dehydrogenase_lipoate', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'E1P_CPLX', loc = 'cyt') +
	met(name = 'Pyruvate_dehydrogenase_acetylDHlipoyl', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_1134', 1.000000), 
	Parameter('rvs_RXN0_1134', 0.000000))
Rule('RXN0_1147',
	prot(name = 'E2O', loc = 'cyt') +
	met(name = 'SUC_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Oxo_glutarate_dehydrogenase_DH_lipoyl', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'E2O', loc = 'cyt') +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Oxo_glutarate_dehydro_suc_DH_lipoyl', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_1147', 1.000000), 
	Parameter('rvs_RXN0_1147', 1.000000))
Rule('RXN0_1133',
	prot(name = 'E2P_MONOMER', loc = 'cyt') +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pyruvate_dehydrogenase_dihydrolipoate', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'E2P_MONOMER', loc = 'cyt') +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pyruvate_dehydrogenase_acetylDHlipoyl', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_1133', 0.000000), 
	Parameter('rvs_RXN0_1133', 1.000000))
Rule('_1dot8dot1dot4_RXN',
	cplx(name = 'E3_CPLX', loc = 'imem') +
	met(name = 'Dihydro_Lipoyl_Proteins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'E3_CPLX', loc = 'imem') +
	met(name = 'Lipoyl_Protein_N6_lipoyllysine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__1dot8dot1dot4_RXN', 1.000000), 
	Parameter('rvs__1dot8dot1dot4_RXN', 0.000000))
Rule('RXN_8629',
	cplx(name = 'E3_CPLX', loc = 'imem') +
	met(name = 'DIHYDROLIPOYL_GCVH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'E3_CPLX', loc = 'imem') +
	met(name = 'PROTEIN_LIPOYLLYSINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_8629', 1.000000), 
	Parameter('rvs_RXN_8629', 1.000000))
Rule('RXN0_1132',
	cplx(name = 'E3_CPLX', loc = 'imem') +
	met(name = 'Pyruvate_dehydrogenase_dihydrolipoate', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'E3_CPLX', loc = 'imem') +
	met(name = 'Pyruvate_dehydrogenase_lipoate', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_1132', 1.000000), 
	Parameter('rvs_RXN0_1132', 0.000000))
Rule('RXN_7716',
	cplx(name = 'E3_CPLX', loc = 'imem') +
	met(name = 'Oxo_glutarate_dehydrogenase_DH_lipoyl', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'E3_CPLX', loc = 'imem') +
	met(name = 'Oxo_glutarate_dehydrogenase_lipoyl', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_7716', 1.000000), 
	Parameter('rvs_RXN_7716', 0.000000))
Rule('RXN_15119',
	cplx(name = 'E3_CPLX', loc = 'imem') +
	met(name = 'CPD_4544', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Donor_H2', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'E3_CPLX', loc = 'imem') +
	met(name = 'CPD_16009', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Acceptor', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_15119', 1.000000), 
	Parameter('rvs_RXN_15119', 0.000000))
Rule('RXN_18737',
	prot(name = 'EG10037_MONOMER', loc = 'cyt') +
	met(name = 'an_Nsup1sup_methyladenine_in_DNA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG10037_MONOMER', loc = 'cyt') +
	met(name = 'DNA_Adenines', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FORMALDEHYDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SUC', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_18737', 1.000000), 
	Parameter('rvs_RXN_18737', 0.000000))
Rule('RXN_18738',
	prot(name = 'EG10037_MONOMER', loc = 'cyt') +
	met(name = 'an_Nsup3sup_methylcytosine_in_DNA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	prot(name = 'EG10037_MONOMER', loc = 'cyt') +
	met(name = 'DNA_Cytosines', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FORMALDEHYDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SUC', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_18738', 1.000000), 
	Parameter('rvs_RXN_18738', 0.000000))
Rule('RXN0_986',
	prot(name = 'EG10037_MONOMER', loc = 'cyt') +
	met(name = 'an_iNisup1sup_ethyladenine_in_DNA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG10037_MONOMER', loc = 'cyt') +
	met(name = 'DNA_Adenines', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETALD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SUC', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_986', 1.000000), 
	Parameter('rvs_RXN0_986', 0.000000))
Rule('RXN0_7275',
	prot(name = 'EG10037_MONOMER', loc = 'cyt') +
	met(name = '_1iNisup6sup_ethenoadenine_in_DNA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10037_MONOMER', loc = 'cyt') +
	met(name = 'DNA_Adenines', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_8887', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SUC', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7275', 1.000000), 
	Parameter('rvs_RXN0_7275', 0.000000))
Rule('RXN0_7280',
	prot(name = 'EG10037_MONOMER', loc = 'cyt') +
	met(name = 'CPD_20036', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG10037_MONOMER', loc = 'cyt') +
	met(name = 'DATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FORMALDEHYDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SUC', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7280', 1.000000), 
	Parameter('rvs_RXN0_7280', 0.000000))
Rule('RXN_18739',
	prot(name = 'EG10037_MONOMER', loc = 'cyt') +
	met(name = 'CPD_20035', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG10037_MONOMER', loc = 'cyt') +
	met(name = 'DAMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FORMALDEHYDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SUC', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_18739', 1.000000), 
	Parameter('rvs_RXN_18739', 0.000000))
Rule('RXN0_5225',
	prot(name = 'EG10041_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_1080', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10041_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_1081', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_1082', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5225', 1.000000), 
	Parameter('rvs_RXN0_5225', 0.000000))
Rule('_325_BISPHOSPHATE_NUCLEOTIDASE_RXN',
	prot(name = 'EG10043_MONOMER', loc = 'imem') +
	met(name = '_3_5_ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10043_MONOMER', loc = 'imem') +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__325_BISPHOSPHATE_NUCLEOTIDASE_RXN', 1.000000), 
	Parameter('rvs__325_BISPHOSPHATE_NUCLEOTIDASE_RXN', 0.000000))
Rule('_3dot6dot1dot41_RXN',
	prot(name = 'EG10048_MONOMER', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_P4', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10048_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3dot6dot1dot41_RXN', 1.000000), 
	Parameter('rvs__3dot6dot1dot41_RXN', 0.000000))
Rule('RXN0_5295',
	prot(name = 'EG10085_MONOMER', loc = 'cyt') +
	met(name = 'CPD_1162', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10085_MONOMER', loc = 'cyt') +
	met(name = 'GLC_6_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HYDROQUINONE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5295', 1.000000), 
	Parameter('rvs_RXN0_5295', 0.000000))
Rule('RXN0_5297',
	prot(name = 'EG10114_MONOMER', loc = 'cyt') +
	met(name = 'CPD_1181', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10114_MONOMER', loc = 'cyt') +
	met(name = 'GLC_6_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_173', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5297', 1.000000), 
	Parameter('rvs_RXN0_5297', 0.000000))
Rule('RXN_11475',
	prot(name = 'EG10119_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MALONYL_ACP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10119_MONOMER', loc = 'cyt') +
	met(name = 'Malonyl_acp_methyl_ester', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11475', 1.000000), 
	Parameter('rvs_RXN_11475', 0.000000))
Rule('RXN_11483',
	prot(name = 'EG10122_MONOMER', loc = 'cyt') +
	met(name = 'Pimeloyl_ACP_methyl_esters', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG10122_MONOMER', loc = 'cyt') +
	met(name = 'Pimeloyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'METOH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11483', 1.000000), 
	Parameter('rvs_RXN_11483', 0.000000))
Rule('_1dot8dot4dot13_RXN',
	prot(name = 'EG10124_MONOMER', loc = 'per') +
	met(name = 'MET', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Ox_Thioredoxin', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10124_MONOMER', loc = 'per') +
	met(name = 'CPD_8989', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Red_Thioredoxin', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd__1dot8dot4dot13_RXN', 0.000000), 
	Parameter('rvs__1dot8dot4dot13_RXN', 1.000000))
Rule('RXN0_6277',
	prot(name = 'EG10124_MONOMER', loc = 'per') +
	met(name = 'CPD_722', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Red_Thioredoxin', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG10124_MONOMER', loc = 'per') +
	met(name = 'BIOTIN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Ox_Thioredoxin', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6277', 1.000000), 
	Parameter('rvs_RXN0_6277', 0.000000))
Rule('TRNA_CYTIDYLYLTRANSFERASE_RXN',
	prot(name = 'EG10136_MONOMER', loc = 'cyt') +
	met(name = 'tRNA_precursors', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10136_MONOMER', loc = 'cyt') +
	met(name = 'tRNAs_with_CCA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_TRNA_CYTIDYLYLTRANSFERASE_RXN', 1.000000), 
	Parameter('rvs_TRNA_CYTIDYLYLTRANSFERASE_RXN', 0.000000))
Rule('RXN_17363',
	prot(name = 'EG10168_MONOMER', loc = 'per') +
	met(name = 'Diacylglycerol_Prolipoproteins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Phosphoglycerides', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG10168_MONOMER', loc = 'per') +
	met(name = 'a_mature_triacylated_lipoprotein', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_1_Lyso_phospholipids', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17363', 1.000000), 
	Parameter('rvs_RXN_17363', 0.000000))
Rule('RXN_19774',
	prot(name = 'EG10168_MONOMER', loc = 'per') +
	met(name = 'Diacylglycerol_Prolipoproteins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_1_PHOSPHATIDYL_ETHANOLAMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG10168_MONOMER', loc = 'per') +
	met(name = 'a_mature_triacylated_lipoprotein', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_ACYL_GPE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_19774', 1.000000), 
	Parameter('rvs_RXN_19774', 0.000000))
Rule('_2dot1dot1dot72_RXN',
	prot(name = 'EG10204_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DNA_Adenines', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG10204_MONOMER', loc = 'cyt') +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DNA_Containing_N6_Methyladenine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__2dot1dot1dot72_RXN', 1.000000), 
	Parameter('rvs__2dot1dot1dot72_RXN', 0.000000))
Rule('DNA_CYTOSINE_5__METHYLTRANSFERASE_RXN',
	prot(name = 'EG10211_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DNA_Cytosines', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG10211_MONOMER', loc = 'cyt') +
	met(name = '_5_Methylcytosine_DNA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DNA_CYTOSINE_5__METHYLTRANSFERASE_RXN', 1.000000), 
	Parameter('rvs_DNA_CYTOSINE_5__METHYLTRANSFERASE_RXN', 0.000000))
Rule('_3dot4dot15dot5_RXN',
	prot(name = 'EG10212_MONOMER', loc = 'cyt') +
	met(name = 'Peptidyl_Dipeptidase_Dcp_Substrates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10212_MONOMER', loc = 'cyt') +
	met(name = 'Peptides_holder', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DIPEPTIDES', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3dot4dot15dot5_RXN', 1.000000), 
	Parameter('rvs__3dot4dot15dot5_RXN', 0.000000))
Rule('RXN0_5021',
	prot(name = 'EG10239_MONOMER', loc = 'cyt') +
	met(name = 'Single_Stranded_DNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Ribonucleoside_Triphosphates', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10239_MONOMER', loc = 'cyt') +
	met(name = 'ssDNA_RNA_primer_hybrid', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5021', 1.000000), 
	Parameter('rvs_RXN0_5021', 0.000000))
Rule('RXN0_4961',
	prot(name = 'EG10243_MONOMER', loc = 'cyt') +
	met(name = 'DNA_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10243_MONOMER', loc = 'cyt') +
	met(name = 'Nucleoside_Monophosphates', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_4961', 1.000000), 
	Parameter('rvs_RXN0_4961', 0.000000))
Rule('RXN_17391',
	prot(name = 'EG10246_MONOMER', loc = 'per') +
	met(name = 'CPD_17989', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG10246_MONOMER', loc = 'per') +
	met(name = 'CPD_17989', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_1080', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17391', 1.000000), 
	Parameter('rvs_RXN_17391', 0.000000))
Rule('RXN_17392',
	prot(name = 'EG10246_MONOMER', loc = 'per') +
	met(name = 'CPD_18804', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG10246_MONOMER', loc = 'per') +
	met(name = 'CPD_18805', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_18806', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17392', 1.000000), 
	Parameter('rvs_RXN_17392', 0.000000))
Rule('RXN0_5190',
	prot(name = 'EG10246_MONOMER', loc = 'per') +
	met(name = 'Peptidoglycan_dimer', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG10246_MONOMER', loc = 'per') +
	met(name = 'NAcMur_Peptide_NAcGlc_Undecaprenols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GlcNAc_1_6_anhydro_MurNAc_pentapeptide', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5190', 1.000000), 
	Parameter('rvs_RXN0_5190', 0.000000))
Rule('RXN0_6938',
	prot(name = 'EG10299_MONOMER', loc = 'cyt') +
	met(name = 'FERRIC_ENTEROBACTIN_COMPLEX', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10299_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_2482', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6938', 1.000000), 
	Parameter('rvs_RXN0_6938', 0.000000))
Rule('RXN0_1661',
	prot(name = 'EG10299_MONOMER', loc = 'cyt') +
	met(name = 'ENTEROBACTIN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10299_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'N_23_DIHYDROXYBENZOYL_L_SERINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_1661', 1.000000), 
	Parameter('rvs_RXN0_1661', 0.000000))
Rule('RXN_18435',
	prot(name = 'EG10329_MONOMER', loc = 'cyt') +
	met(name = 'DNA_With_GO', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10329_MONOMER', loc = 'cyt') +
	met(name = 'CPD_12427', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DNA_containing_aPurinic_Sites', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_18435', 1.000000), 
	Parameter('rvs_RXN_18435', 0.000000))
Rule('_3dot2dot2dot23_RXN',
	prot(name = 'EG10329_MONOMER', loc = 'cyt') +
	met(name = 'DNA_containing_diamino_hydro_formamidops', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10329_MONOMER', loc = 'cyt') +
	met(name = 'CPD_16491', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DNA_containing_aPurinic_Sites', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3dot2dot2dot23_RXN', 1.000000), 
	Parameter('rvs__3dot2dot2dot23_RXN', 0.000000))
Rule('RXN0_6515',
	prot(name = 'EG10343_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_16S_rRNA_guanine_966', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG10343_MONOMER', loc = 'cyt') +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_16S_rRNA_N2_methylguanine966', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6515', 1.000000), 
	Parameter('rvs_RXN0_6515', 0.000000))
Rule('RXN_15878',
	prot(name = 'EG10370_MONOMER', loc = 'cyt') +
	met(name = 'HYDROXY_METHYL_BUTENYL_DIP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Oxidized_flavodoxins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10370_MONOMER', loc = 'cyt') +
	met(name = '_2C_METH_D_ERYTHRITOL_CYCLODIPHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Reduced_flavodoxins', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None, 
	Parameter('fwd_RXN_15878', 0.000000), 
	Parameter('rvs_RXN_15878', 1.000000))
Rule('RXN_11578',
	prot(name = 'EG10376_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_16S_rRNA_guanine_527', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10376_MONOMER', loc = 'cyt') +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_16S_rRNA_N7_methylguanine527', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11578', 1.000000), 
	Parameter('rvs_RXN_11578', 0.000000))
Rule('RXN0_5146',
	prot(name = 'EG10381_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_971', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10381_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_1027', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MALTOTETRAOSE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5146', 1.000000), 
	Parameter('rvs_RXN0_5146', 0.000000))
Rule('_3dot4dot21dot105_RXN',
	prot(name = 'EG10397_MONOMER', loc = 'imem') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Type_1_transmemberane_domains', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10397_MONOMER', loc = 'imem') +
	met(name = 'Cleaved_type_1_transmembrane_domains', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd__3dot4dot21dot105_RXN', 1.000000), 
	Parameter('rvs__3dot4dot21dot105_RXN', 0.000000))
Rule('RXN0_5211',
	prot(name = 'EG10443_MONOMER', loc = 'cyt') +
	met(name = 'EG10443_MONOMER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10443_MONOMER', loc = 'cyt') +
	met(name = 'HIPA_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5211', 1.000000), 
	Parameter('rvs_RXN0_5211', 0.000000))
Rule('R621_RXN',
	prot(name = 'EG10456_MONOMER', loc = 'per') +
	met(name = 'NADH_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NITRIC_OXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10456_MONOMER', loc = 'per') +
	met(name = 'NAD_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NITRATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_R621_RXN', 1.000000), 
	Parameter('rvs_R621_RXN', 0.000000))
Rule('RXN_17943',
	prot(name = 'EG10487_MONOMER', loc = 'cyt') +
	met(name = 'HypE_S_carboxamide', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	prot(name = 'EG10487_MONOMER', loc = 'cyt') +
	met(name = 'HypE_S_cyanate', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17943', 1.000000), 
	Parameter('rvs_RXN_17943', 0.000000))
Rule('RXN0_3261',
	prot(name = 'EG10488_MONOMER', loc = 'per') +
	met(name = 'Proteins_with_N_terminal_L_arginine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10488_MONOMER', loc = 'per') +
	met(name = 'ARG', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Peptide_Holder_Alternative', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_3261', 1.000000), 
	Parameter('rvs_RXN0_3261', 0.000000))
Rule('RXN_11633',
	prot(name = 'EG10523_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_16S_rRNA_adenine1518_adenine1519', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG10523_MONOMER', loc = 'cyt') +
	met(name = '_16S_rRNA_N6_dimethyladenine1518_1519', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11633', 1.000000), 
	Parameter('rvs_RXN_11633', 0.000000))
Rule('_3dot4dot21dot89_RXN',
	prot(name = 'EG10530_MONOMER', loc = 'imem') +
	met(name = 'Peptides_with_Leader_Sequence', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10530_MONOMER', loc = 'imem') +
	met(name = 'Peptides_holder', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Leader_Sequences', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3dot4dot21dot89_RXN', 1.000000), 
	Parameter('rvs__3dot4dot21dot89_RXN', 0.000000))
Rule('DNA_LIGASE_NADplus_RXN',
	prot(name = 'EG10534_MONOMER', loc = 'cyt') +
	met(name = '_3_Hydroxy_Terminated_DNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_5_Phospho_terminated_DNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG10534_MONOMER', loc = 'cyt') +
	met(name = 'DNA_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NICOTINAMIDE_NUCLEOTIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DNA_LIGASE_NADplus_RXN', 1.000000), 
	Parameter('rvs_DNA_LIGASE_NADplus_RXN', 0.000000))
Rule('RXN_17362',
	prot(name = 'EG10548_MONOMER', loc = 'imem') +
	met(name = 'MONOMER0_4342', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10548_MONOMER', loc = 'imem') +
	met(name = 'Diacylglycerol_Prolipoproteins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Lipoprotein_signal_peptide', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17362', 1.000000), 
	Parameter('rvs_RXN_17362', 0.000000))
Rule('_3dot4dot11dot18_RXN',
	prot(name = 'EG10570_MONOMER', loc = 'cyt') +
	met(name = 'Protein_With_N_Terminal_Met', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10570_MONOMER', loc = 'cyt') +
	met(name = 'MET', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Peptide_Holder_Alternative', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3dot4dot11dot18_RXN', 1.000000), 
	Parameter('rvs__3dot4dot11dot18_RXN', 0.000000))
Rule('RXN0_2942',
	prot(name = 'EG10573_MONOMER', loc = 'cyt') +
	met(name = 'DNA_With_Recognition_Site', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10573_MONOMER', loc = 'cyt') +
	met(name = 'DNA_Cleaved_Recognition_Site', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_2942', 1.000000), 
	Parameter('rvs_RXN0_2942', 0.000000))
Rule('RXN0_6274',
	prot(name = 'EG10595_MONOMER', loc = 'cyt') +
	met(name = 'CPD_4211', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'tRNA_Adenosines_37', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10595_MONOMER', loc = 'cyt') +
	met(name = '_6_Dimethylallyladenosine37_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6274', 1.000000), 
	Parameter('rvs_RXN0_6274', 0.000000))
Rule('RXN_14002',
	prot(name = 'EG10626_MONOMER', loc = 'cyt') +
	met(name = 'CPD_14101', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG10626_MONOMER', loc = 'cyt') +
	met(name = 'CPD_12367', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14002', 1.000000), 
	Parameter('rvs_RXN_14002', 0.000000))
Rule('RXN_12816',
	prot(name = 'EG10626_MONOMER', loc = 'cyt') +
	met(name = 'CPD_13853', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG10626_MONOMER', loc = 'cyt') +
	met(name = 'CPD_12365', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_12816', 1.000000), 
	Parameter('rvs_RXN_12816', 0.000000))
Rule('RXN_11397',
	prot(name = 'EG10626_MONOMER', loc = 'cyt') +
	met(name = 'CPD_12366', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG10626_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_12367', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11397', 1.000000), 
	Parameter('rvs_RXN_11397', 0.000000))
Rule('RXN_11396',
	prot(name = 'EG10626_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_1905', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG10626_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_12365', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11396', 1.000000), 
	Parameter('rvs_RXN_11396', 0.000000))
Rule('RXN0_2661',
	prot(name = 'EG10627_MONOMER', loc = 'per') +
	met(name = 'DNA_With_GO_A_Mismatch', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10627_MONOMER', loc = 'per') +
	met(name = 'DNA_containing_aPurinic_Sites', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_2661', 1.000000), 
	Parameter('rvs_RXN0_2661', 0.000000))
Rule('_3dot1dot21dot2_RXN',
	prot(name = 'EG10651_MONOMER', loc = 'cyt') +
	met(name = 'Single_Stranded_DNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10651_MONOMER', loc = 'cyt') +
	met(name = '_5_phosphooligonucleotides', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd__3dot1dot21dot2_RXN', 1.000000), 
	Parameter('rvs__3dot1dot21dot2_RXN', 0.000000))
Rule('RXN0_2601',
	prot(name = 'EG10662_MONOMER', loc = 'cyt') +
	met(name = 'Damaged_DNA_Pyrimidine', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10662_MONOMER', loc = 'cyt') +
	met(name = 'DNA_containing_a_Apyrimidinic_Sites', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_2601', 1.000000), 
	Parameter('rvs_RXN0_2601', 0.000000))
Rule('_4dot2dot99dot18_RXN',
	prot(name = 'EG10662_MONOMER', loc = 'cyt') +
	met(name = 'DNA_containing_abasic_Sites', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	prot(name = 'EG10662_MONOMER', loc = 'cyt') +
	met(name = '_5_Phospho_terminated_DNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_3_terminal_unsaturated_sugars', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__4dot2dot99dot18_RXN', 1.000000), 
	Parameter('rvs__4dot2dot99dot18_RXN', 0.000000))
Rule('RXN_17824',
	prot(name = 'EG10668_MONOMER', loc = 'cyt') +
	met(name = 'CPD_19186', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROT_CYS', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10668_MONOMER', loc = 'cyt') +
	met(name = 'a_thymine_in_DNA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Protein_S_methyl_L_cysteine', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17824', 1.000000), 
	Parameter('rvs_RXN_17824', 0.000000))
Rule('_2dot1dot1dot63_RXN',
	prot(name = 'EG10668_MONOMER', loc = 'cyt') +
	met(name = 'PROT_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DNA_6_O_Methyl_Guanines', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10668_MONOMER', loc = 'cyt') +
	met(name = 'Protein_S_methyl_L_cysteine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DNA_Guanines', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__2dot1dot1dot63_RXN', 1.000000), 
	Parameter('rvs__2dot1dot1dot63_RXN', 0.000000))
Rule('_3dot4dot21dot87_RXN',
	prot(name = 'EG10673_MONOMER', loc = 'omem') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'General_Protein_Substrates', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10673_MONOMER', loc = 'omem') +
	met(name = 'Peptides_holder', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd__3dot4dot21dot87_RXN', 1.000000), 
	Parameter('rvs__3dot4dot21dot87_RXN', 0.000000))
Rule('_2dot1dot1dot77_RXN',
	prot(name = 'EG10689_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTEIN_L_BETA_ISOASPARTATES', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10689_MONOMER', loc = 'cyt') +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTEIN_L_BETA_ISOSPARTATE_METHYL_ESTERS', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__2dot1dot1dot77_RXN', 1.000000), 
	Parameter('rvs__2dot1dot1dot77_RXN', 0.000000))
Rule('POLYNUCLEOTIDE_ADENYLYLTRANSFERASE_RXN',
	prot(name = 'EG10690_MONOMER', loc = 'imem') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'mRNAs', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10690_MONOMER', loc = 'imem') +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'mRNAs', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_POLYNUCLEOTIDE_ADENYLYLTRANSFERASE_RXN', 1.000000), 
	Parameter('rvs_POLYNUCLEOTIDE_ADENYLYLTRANSFERASE_RXN', 0.000000))
Rule('RXN0_5195',
	prot(name = 'EG10696_MONOMER', loc = 'cyt') +
	met(name = 'General_Protein_Substrates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10696_MONOMER', loc = 'cyt') +
	met(name = 'Peptides_holder', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5195', 1.000000), 
	Parameter('rvs_RXN0_5195', 0.000000))
Rule('_3dot4dot11dot2_RXN',
	prot(name = 'EG10696_MONOMER', loc = 'cyt') +
	met(name = 'Peptide_with_N_terminal_Alanine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10696_MONOMER', loc = 'cyt') +
	met(name = 'L_ALPHA_ALANINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Peptide_Holder_Alternative', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3dot4dot11dot2_RXN', 1.000000), 
	Parameter('rvs__3dot4dot11dot2_RXN', 0.000000))
Rule('RXN_17956',
	prot(name = 'EG10719_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_19236', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Donor_H2', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None +
	None | 
	prot(name = 'EG10719_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_2463', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_19237', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CH33ADO', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MET', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Acceptor', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17956', 1.000000), 
	Parameter('rvs_RXN_17956', 0.000000))
Rule('RXN0_6734',
	prot(name = 'EG10719_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_2480', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Donor_H2', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None +
	None | 
	prot(name = 'EG10719_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_2463', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CH4', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CH33ADO', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MET', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Acceptor', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6734', 1.000000), 
	Parameter('rvs_RXN0_6734', 0.000000))
Rule('RXN_17955',
	prot(name = 'EG10722_MONOMER', loc = 'cyt') +
	met(name = 'CPD_19235', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG10722_MONOMER', loc = 'cyt') +
	met(name = 'CPD_19236', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17955', 1.000000), 
	Parameter('rvs_RXN_17955', 0.000000))
Rule('RXN0_6733',
	prot(name = 'EG10722_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_2479', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG10722_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_2480', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6733', 1.000000), 
	Parameter('rvs_RXN0_6733', 0.000000))
Rule('RXN0_1401',
	prot(name = 'EG10723_MONOMER', loc = 'cyt') +
	met(name = 'RIBOSE_15_BISPHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10723_MONOMER', loc = 'cyt') +
	met(name = 'PRPP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_1401', 1.000000), 
	Parameter('rvs_RXN0_1401', 0.000000))
Rule('RXN0_7014',
	prot(name = 'EG10724_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_1074', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10724_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_2518', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7014', 1.000000), 
	Parameter('rvs_RXN0_7014', 0.000000))
Rule('RXN_17960',
	prot(name = 'EG10724_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_2521', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG10724_MONOMER', loc = 'cyt') +
	met(name = 'CPD_19240', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17960', 1.000000), 
	Parameter('rvs_RXN_17960', 0.000000))
Rule('RXN_17962',
	prot(name = 'EG10724_MONOMER', loc = 'cyt') +
	met(name = 'CPD_1106', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG10724_MONOMER', loc = 'cyt') +
	met(name = 'CPD_19243', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17962', 1.000000), 
	Parameter('rvs_RXN_17962', 0.000000))
Rule('RXN_17961',
	prot(name = 'EG10724_MONOMER', loc = 'cyt') +
	met(name = 'CPD_19241', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG10724_MONOMER', loc = 'cyt') +
	met(name = 'CPD_19242', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17961', 1.000000), 
	Parameter('rvs_RXN_17961', 0.000000))
Rule('RXN_19025',
	prot(name = 'EG10736_MONOMER', loc = 'cyt') +
	met(name = 'DNA_thymidine_dimer', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Light', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10736_MONOMER', loc = 'cyt') +
	met(name = 'DNA_thymidines', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_19025', 1.000000), 
	Parameter('rvs_RXN_19025', 0.000000))
Rule('RXN_19026',
	prot(name = 'EG10736_MONOMER', loc = 'cyt') +
	met(name = 'DNA_deoxycytidine_dimer', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Light', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10736_MONOMER', loc = 'cyt') +
	met(name = 'DNA_Cytidines', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_19026', 1.000000), 
	Parameter('rvs_RXN_19026', 0.000000))
Rule('DEOXYRIBODIPYRIMIDINE_PHOTOLYASE_RXN',
	prot(name = 'EG10736_MONOMER', loc = 'cyt') +
	met(name = 'DNA_deoxycytidine_thymidine_dimer', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Light', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10736_MONOMER', loc = 'cyt') +
	met(name = 'DNA_Cytidines', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DNA_thymidines', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DEOXYRIBODIPYRIMIDINE_PHOTOLYASE_RXN', 1.000000), 
	Parameter('rvs_DEOXYRIBODIPYRIMIDINE_PHOTOLYASE_RXN', 0.000000))
Rule('RXN0_5100',
	prot(name = 'EG10737_MONOMER', loc = 'cyt') +
	met(name = 'DNA_Segment_Placeholder', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10737_MONOMER', loc = 'cyt') +
	met(name = 'DNA_Segment_in_Reverse_Orientations', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5100', 1.000000), 
	Parameter('rvs_RXN0_5100', 1.000000))
Rule('RXN0_7122',
	prot(name = 'EG10739_MONOMER', loc = 'imem') +
	met(name = '_2_ACYL_GPE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLYCEROPHOSPHOGLYCEROL', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10739_MONOMER', loc = 'imem') +
	met(name = 'L_1_GLYCEROPHOSPHORYLETHANOL_AMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Lysophospholipids', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7122', 1.000000), 
	Parameter('rvs_RXN0_7122', 0.000000))
Rule('RXN0_5039',
	prot(name = 'EG10746_MONOMER', loc = 'cyt') +
	met(name = 'Double_Stranded_DNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10746_MONOMER', loc = 'cyt') +
	met(name = 'Single_Stranded_DNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_5_Phosphomononucleotides', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5039', 1.000000), 
	Parameter('rvs_RXN0_5039', 0.000000))
Rule('_3dot4dot21dot102_RXN',
	prot(name = 'EG10760_MONOMER', loc = 'per') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'General_Protein_Substrates', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10760_MONOMER', loc = 'per') +
	met(name = 'Peptides_holder', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd__3dot4dot21dot102_RXN', 1.000000), 
	Parameter('rvs__3dot4dot21dot102_RXN', 0.000000))
Rule('AMINOCYL_TRNA_HYDROLASE_RXN',
	prot(name = 'EG10785_MONOMER', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'N_Substituted_Aminoacyl_tRNA', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG10785_MONOMER', loc = 'cyt') +
	met(name = 'tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'N_Substituted_Amino_Acids', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_AMINOCYL_TRNA_HYDROLASE_RXN', 1.000000), 
	Parameter('rvs_AMINOCYL_TRNA_HYDROLASE_RXN', 0.000000))
Rule('_3dot4dot24dot55_RXN',
	prot(name = 'EG10786_MONOMER', loc = 'per') +
	met(name = 'General_Protein_Substrates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10786_MONOMER', loc = 'per') +
	met(name = 'Peptides_holder', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd__3dot4dot24dot55_RXN', 1.000000), 
	Parameter('rvs__3dot4dot24dot55_RXN', 0.000000))
Rule('RXN0_1342',
	prot(name = 'EG10812_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'tRNA_with_7_aminomethyl_7_deazaguanine', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	prot(name = 'EG10812_MONOMER', loc = 'cyt') +
	met(name = 'tRNAs_containing_epoxy_quenosine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MET', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_1342', 1.000000), 
	Parameter('rvs_RXN0_1342', 0.000000))
Rule('RXN0_2604',
	prot(name = 'EG10829_MONOMER', loc = 'cyt') +
	met(name = 'DNA_with_Holiday_Junctions', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10829_MONOMER', loc = 'cyt') +
	met(name = 'DNA_Segment_Placeholder', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_2604', 1.000000), 
	Parameter('rvs_RXN0_2604', 0.000000))
Rule('_2dot3dot1dot128_RXN',
	prot(name = 'EG10850_MONOMER', loc = 'cyt') +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'S18_N_terminal_L_alanine', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG10850_MONOMER', loc = 'cyt') +
	met(name = 'Acetylated_S18_N_terminal_L_alanine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__2dot3dot1dot128_RXN', 1.000000), 
	Parameter('rvs__2dot3dot1dot128_RXN', 0.000000))
Rule('RXN_18434',
	prot(name = 'EG10851_MONOMER', loc = 'cyt') +
	met(name = 'S5_N_terminal_L_alanine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG10851_MONOMER', loc = 'cyt') +
	met(name = 'Acetylated_S5_N_terminal_L_alanine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_18434', 1.000000), 
	Parameter('rvs_RXN_18434', 0.000000))
Rule('RXN0_5231',
	prot(name = 'EG10853_MONOMER', loc = 'cyt') +
	met(name = 'EG10873_MONOMER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10853_MONOMER', loc = 'cyt') +
	met(name = 'MONOMER0_2811', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5231', 1.000000), 
	Parameter('rvs_RXN0_5231', 0.000000))
Rule('RXN0_6527',
	prot(name = 'EG10856_MONOMER', loc = 'per') +
	met(name = 'ssRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10856_MONOMER', loc = 'per') +
	met(name = 'rRNA_fragments', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_6527', 1.000000), 
	Parameter('rvs_RXN0_6527', 0.000000))
Rule('RXN0_6526',
	prot(name = 'EG10856_MONOMER', loc = 'per') +
	met(name = '_23S_rRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10856_MONOMER', loc = 'per') +
	met(name = 'rRNA_fragments', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_6526', 1.000000), 
	Parameter('rvs_RXN0_6526', 0.000000))
Rule('_3dot1dot27dot6_RXN',
	prot(name = 'EG10856_MONOMER', loc = 'per') +
	met(name = 'mRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10856_MONOMER', loc = 'per') +
	met(name = 'mRNA_Fragments', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd__3dot1dot27dot6_RXN', 1.000000), 
	Parameter('rvs__3dot1dot27dot6_RXN', 0.000000))
Rule('_3dot1dot13dot5_RXN',
	prot(name = 'EG10858_MONOMER', loc = 'cyt') +
	met(name = 'tRNA_precursors', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10858_MONOMER', loc = 'cyt') +
	met(name = 'All_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Nucleoside_Monophosphates', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3dot1dot13dot5_RXN', 1.000000), 
	Parameter('rvs__3dot1dot13dot5_RXN', 0.000000))
Rule('_3dot1dot26dot4_RXN',
	prot(name = 'EG10860_MONOMER', loc = 'cyt') +
	met(name = 'RNA_DNA_hybrids', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10860_MONOMER', loc = 'cyt') +
	met(name = 'DNA_Holder', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Nucleoside_Monophosphates', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3dot1dot26dot4_RXN', 1.000000), 
	Parameter('rvs__3dot1dot26dot4_RXN', 0.000000))
Rule('RXN0_6482',
	prot(name = 'EG10863_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_2353', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10863_MONOMER', loc = 'cyt') +
	met(name = 'tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Ribonucleoside_Diphosphates', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6482', 1.000000), 
	Parameter('rvs_RXN0_6482', 0.000000))
Rule('RXN0_6481',
	prot(name = 'EG10863_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_2352', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10863_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_2354', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Ribonucleoside_Diphosphates', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6481', 1.000000), 
	Parameter('rvs_RXN0_6481', 0.000000))
Rule('TRNA_NUCLEOTIDYLTRANSFERASE_RXN',
	prot(name = 'EG10863_MONOMER', loc = 'cyt') +
	met(name = 'RNA_Holder', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10863_MONOMER', loc = 'cyt') +
	met(name = 'RNA_Holder', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Nucleoside_Diphosphates', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_TRNA_NUCLEOTIDYLTRANSFERASE_RXN', 1.000000), 
	Parameter('rvs_TRNA_NUCLEOTIDYLTRANSFERASE_RXN', 0.000000))
Rule('_3dot1dot11dot1_RXN',
	prot(name = 'EG10926_MONOMER', loc = 'cyt') +
	met(name = 'DNA_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10926_MONOMER', loc = 'cyt') +
	met(name = 'DNA_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Deoxy_Ribonucleoside_Monophosphates', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3dot1dot11dot1_RXN', 1.000000), 
	Parameter('rvs__3dot1dot11dot1_RXN', 0.000000))
Rule('_2dot1dot1dot34_RXN',
	prot(name = 'EG10967_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'tRNA_guanosine18', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG10967_MONOMER', loc = 'cyt') +
	met(name = '_2_O_Methylguanosine18', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__2dot1dot1dot34_RXN', 1.000000), 
	Parameter('rvs__2dot1dot1dot34_RXN', 0.000000))
Rule('RXN0_5408',
	prot(name = 'EG10983_MONOMER', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_MYO_INOSITOL_1_MONOPHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10983_MONOMER', loc = 'cyt') +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MYO_INOSITOL', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5408', 1.000000), 
	Parameter('rvs_RXN0_5408', 0.000000))
Rule('RXN_7253',
	prot(name = 'EG10983_MONOMER', loc = 'cyt') +
	met(name = 'CPD_6746', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10983_MONOMER', loc = 'cyt') +
	met(name = 'MYO_INOSITOL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_7253', 1.000000), 
	Parameter('rvs_RXN_7253', 0.000000))
Rule('RXN0_5189',
	prot(name = 'EG10986_MONOMER', loc = 'cyt') +
	met(name = 'DNA_3_methyladenines', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG10986_MONOMER', loc = 'cyt') +
	met(name = 'DNA_containing_aPurinic_Sites', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_3_Methyl_Adenines', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5189', 1.000000), 
	Parameter('rvs_RXN0_5189', 0.000000))
Rule('_3dot4dot21dot83_RXN',
	prot(name = 'EG11004_MONOMER', loc = 'cyt') +
	met(name = 'OLIGOPEPTIDES', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11004_MONOMER', loc = 'cyt') +
	met(name = 'Peptides_holder', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd__3dot4dot21dot83_RXN', 1.000000), 
	Parameter('rvs__3dot4dot21dot83_RXN', 0.000000))
Rule('_5dot99dot1dot2_RXN',
	prot(name = 'EG11013_MONOMER', loc = 'cyt') +
	met(name = 'Negatively_super_coiled_DNAs', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11013_MONOMER', loc = 'cyt') +
	met(name = 'Relaxed_DNAs', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__5dot99dot1dot2_RXN', 1.000000), 
	Parameter('rvs__5dot99dot1dot2_RXN', 0.000000))
Rule('TRNA_URACIL_5__METHYLTRANSFERASE_RXN',
	prot(name = 'EG11022_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Uracil_54_in_tRNA', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11022_MONOMER', loc = 'cyt') +
	met(name = 'tRNA_containing_5Me_uridine54', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_TRNA_URACIL_5__METHYLTRANSFERASE_RXN', 1.000000), 
	Parameter('rvs_TRNA_URACIL_5__METHYLTRANSFERASE_RXN', 0.000000))
Rule('RXN0_2584',
	prot(name = 'EG11058_MONOMER', loc = 'cyt') +
	met(name = 'DNA_with_Uracils', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11058_MONOMER', loc = 'cyt') +
	met(name = 'DNA_containing_a_Apyrimidinic_Sites', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'URACIL', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_2584', 1.000000), 
	Parameter('rvs_RXN0_2584', 0.000000))
Rule('_3dot1dot11dot2_RXN',
	prot(name = 'EG11073_MONOMER', loc = 'cyt') +
	met(name = 'DNA_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11073_MONOMER', loc = 'cyt') +
	met(name = 'DNA_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Deoxy_Ribonucleoside_Monophosphates', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3dot1dot11dot2_RXN', 1.000000), 
	Parameter('rvs__3dot1dot11dot2_RXN', 0.000000))
Rule('RXN0_363',
	prot(name = 'EG11082_MONOMER', loc = 'cyt') +
	met(name = 'XANTHOSINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11082_MONOMER', loc = 'cyt') +
	met(name = 'D_Ribofuranose', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'XANTHINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_363', 1.000000), 
	Parameter('rvs_RXN0_363', 0.000000))
Rule('INOSINE_NUCLEOSIDASE_RXN',
	prot(name = 'EG11082_MONOMER', loc = 'cyt') +
	met(name = 'INOSINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11082_MONOMER', loc = 'cyt') +
	met(name = 'D_Ribofuranose', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HYPOXANTHINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_INOSINE_NUCLEOSIDASE_RXN', 1.000000), 
	Parameter('rvs_INOSINE_NUCLEOSIDASE_RXN', 0.000000))
Rule('ADENOSINE_NUCLEOSIDASE_RXN',
	prot(name = 'EG11082_MONOMER', loc = 'cyt') +
	met(name = 'ADENOSINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11082_MONOMER', loc = 'cyt') +
	met(name = 'D_Ribofuranose', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ADENOSINE_NUCLEOSIDASE_RXN', 1.000000), 
	Parameter('rvs_ADENOSINE_NUCLEOSIDASE_RXN', 0.000000))
Rule('_3dot1dot4dot14_RXN',
	prot(name = 'EG11095_MONOMER', loc = 'cyt') +
	met(name = 'All_holo_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11095_MONOMER', loc = 'cyt') +
	met(name = 'PANTETHEINE_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'All_apo_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3dot1dot4dot14_RXN', 1.000000), 
	Parameter('rvs__3dot1dot4dot14_RXN', 0.000000))
Rule('RXN_17846',
	prot(name = 'EG11112_MONOMER', loc = 'cyt') +
	met(name = 'Charged_LEU_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Protein_N_terminal_L_Arginine', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11112_MONOMER', loc = 'cyt') +
	met(name = 'L_leucyl_L_arginyl_Protein', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'LEU_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17846', 1.000000), 
	Parameter('rvs_RXN_17846', 0.000000))
Rule('RXN_17847',
	prot(name = 'EG11112_MONOMER', loc = 'cyt') +
	met(name = 'Charged_PHE_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Protein_N_terminal_L_Arginine', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11112_MONOMER', loc = 'cyt') +
	met(name = 'L_phenylalanyl_L_arginyl_Protein', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PHE_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17847', 1.000000), 
	Parameter('rvs_RXN_17847', 0.000000))
Rule('RXN_17848',
	prot(name = 'EG11112_MONOMER', loc = 'cyt') +
	met(name = 'Charged_PHE_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Protein_N_terminal_L_Lysine', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11112_MONOMER', loc = 'cyt') +
	met(name = 'L_phenylalanyl_L_lysyl_Protein', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PHE_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17848', 1.000000), 
	Parameter('rvs_RXN_17848', 0.000000))
Rule('LEUCYLTRANSFERASE_RXN',
	prot(name = 'EG11112_MONOMER', loc = 'cyt') +
	met(name = 'Charged_LEU_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Protein_N_terminal_L_Lysine', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11112_MONOMER', loc = 'cyt') +
	met(name = 'L_leucyl_L_lysyl_Protein', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'LEU_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_LEUCYLTRANSFERASE_RXN', 1.000000), 
	Parameter('rvs_LEUCYLTRANSFERASE_RXN', 0.000000))
Rule('RXN_11838',
	prot(name = 'EG11118_MONOMER', loc = 'cyt') +
	met(name = '_23S_rRNA_uridine955_2504_2580', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11118_MONOMER', loc = 'cyt') +
	met(name = '_23S_rRNA_pseudouridine955_2504_2580', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11838', 1.000000), 
	Parameter('rvs_RXN_11838', 0.000000))
Rule('ACYL_COA_HYDROLASE_RXN',
	prot(name = 'EG11121_MONOMER', loc = 'cyt') +
	met(name = 'ACYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11121_MONOMER', loc = 'cyt') +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Carboxylates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ACYL_COA_HYDROLASE_RXN', 1.000000), 
	Parameter('rvs_ACYL_COA_HYDROLASE_RXN', 0.000000))
Rule('_5_FORMYL_THF_CYCLO_LIGASE_RXN',
	prot(name = 'EG11158_MONOMER', loc = 'cyt') +
	met(name = 'N5_Formyl_THF_Glu_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11158_MONOMER', loc = 'cyt') +
	met(name = '_5_10_METHENYL_THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__5_FORMYL_THF_CYCLO_LIGASE_RXN', 1.000000), 
	Parameter('rvs__5_FORMYL_THF_CYCLO_LIGASE_RXN', 0.000000))
Rule('FUMHYDR_RXN',
	prot(name = 'EG11162_MONOMER', loc = 'cyt') +
	met(name = 'MAL', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11162_MONOMER', loc = 'cyt') +
	met(name = 'FUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_FUMHYDR_RXN', 1.000000), 
	Parameter('rvs_FUMHYDR_RXN', 1.000000))
Rule('RXN_8460',
	prot(name = 'EG11166_MONOMER', loc = 'cyt') +
	met(name = 'L_DIHYDROXY_PHENYLALANINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11166_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_253', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_8460', 1.000000), 
	Parameter('rvs_RXN_8460', 0.000000))
Rule('RXN_11839',
	prot(name = 'EG11177_MONOMER', loc = 'cyt') +
	met(name = 'tRNA_uridine55', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11177_MONOMER', loc = 'cyt') +
	met(name = 'tRNA_pseudouridine55', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11839', 1.000000), 
	Parameter('rvs_RXN_11839', 0.000000))
Rule('RXN0_5118',
	prot(name = 'EG11189_MONOMER', loc = 'cyt') +
	met(name = 'KDO2_LIPID_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP_L_GLYCERO_D_MANNO_HEPTOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11189_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_929', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5118', 1.000000), 
	Parameter('rvs_RXN0_5118', 0.000000))
Rule('RXN0_5057',
	prot(name = 'EG11189_MONOMER', loc = 'cyt') +
	met(name = 'KDO2_LIPID_IVA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP_L_GLYCERO_D_MANNO_HEPTOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11189_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HEPTOSYL_KDO2_LIPID_IVA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5057', 1.000000), 
	Parameter('rvs_RXN0_5057', 0.000000))
Rule('RIBOPHOSPHAT_RXN',
	prot(name = 'EG11202_MONOMER', loc = 'cyt') +
	met(name = 'CPD_1086', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11202_MONOMER', loc = 'cyt') +
	met(name = 'AMINO_RIBOSYLAMINO_1H_3H_PYR_DIONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RIBOPHOSPHAT_RXN', 1.000000), 
	Parameter('rvs_RIBOPHOSPHAT_RXN', 0.000000))
Rule('_3dot2dot2dot21_RXN',
	prot(name = 'EG11222_MONOMER', loc = 'cyt') +
	met(name = 'Alkylated_DNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11222_MONOMER', loc = 'cyt') +
	met(name = 'DNA_containing_abasic_Sites', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Alkylated_Bases', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3dot2dot2dot21_RXN', 1.000000), 
	Parameter('rvs__3dot2dot2dot21_RXN', 0.000000))
Rule('_3dot2dot1dot14_RXN',
	prot(name = 'EG11237_MONOMER', loc = 'ex') +
	met(name = 'CHITIN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11237_MONOMER', loc = 'ex') +
	met(name = 'Chitodextrins', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd__3dot2dot1dot14_RXN', 1.000000), 
	Parameter('rvs__3dot2dot1dot14_RXN', 0.000000))
Rule('RXN_11601',
	prot(name = 'EG11247_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_23S_rRNA_uracil_1939', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11247_MONOMER', loc = 'cyt') +
	met(name = '_23S_rRNA_5_methyluracil1939', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11601', 1.000000), 
	Parameter('rvs_RXN_11601', 0.000000))
Rule('RXN_16665',
	prot(name = 'EG11253_MONOMER', loc = 'imem') +
	met(name = 'CPD_17926', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLY', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11253_MONOMER', loc = 'imem') +
	met(name = 'CPD_17969', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_ALANINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_16665', 1.000000), 
	Parameter('rvs_RXN_16665', 0.000000))
Rule('RXN_16660',
	prot(name = 'EG11253_MONOMER', loc = 'imem') +
	met(name = 'CPD_17926', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_17931', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11253_MONOMER', loc = 'imem') +
	met(name = 'CPD_17947', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_ALANINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_16660', 1.000000), 
	Parameter('rvs_RXN_16660', 0.000000))
Rule('RXN_16664',
	prot(name = 'EG11253_MONOMER', loc = 'imem') +
	met(name = 'CPD_17926', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11253_MONOMER', loc = 'imem') +
	met(name = 'CPD_17968', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_ALANINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_16664', 1.000000), 
	Parameter('rvs_RXN_16664', 0.000000))
Rule('RXN0_5402',
	prot(name = 'EG11253_MONOMER', loc = 'imem') +
	met(name = 'CPD0_1183', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_1182', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11253_MONOMER', loc = 'imem') +
	met(name = 'CPD0_1185', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_ALANINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5402', 1.000000), 
	Parameter('rvs_RXN0_5402', 0.000000))
Rule('RXN0_7023',
	prot(name = 'EG11259_MONOMER', loc = 'cyt') +
	met(name = 'RNASE_R_DEGRADATION_SUBSTRATE_RNA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11259_MONOMER', loc = 'cyt') +
	met(name = 'Nucleoside_Monophosphates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Diribonucleotide', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7023', 1.000000), 
	Parameter('rvs_RXN0_7023', 0.000000))
Rule('RXN_14361',
	prot(name = 'EG11266_MONOMER', loc = 'cyt') +
	met(name = 'UDP_GLUCURONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_934', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11266_MONOMER', loc = 'cyt') +
	met(name = 'CPD_15237', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UDP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14361', 1.000000), 
	Parameter('rvs_RXN_14361', 0.000000))
Rule('METHIONYL_TRNA_FORMYLTRANSFERASE_RXN',
	prot(name = 'EG11268_MONOMER', loc = 'cyt') +
	met(name = 'FORMYL_THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_methionyl_tRNAfmet', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11268_MONOMER', loc = 'cyt') +
	met(name = 'THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'N_formyl_L_methionyl_tRNAfmet', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_METHIONYL_TRNA_FORMYLTRANSFERASE_RXN', 1.000000), 
	Parameter('rvs_METHIONYL_TRNA_FORMYLTRANSFERASE_RXN', 0.000000))
Rule('FRUCTOKINASE_RXN',
	prot(name = 'EG11288_MONOMER', loc = 'cyt') +
	met(name = 'BETA_D_FRUCTOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11288_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FRUCTOSE_6P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_FRUCTOKINASE_RXN', 1.000000), 
	Parameter('rvs_FRUCTOKINASE_RXN', 0.000000))
Rule('RXN0_7119',
	prot(name = 'EG11292_MONOMER', loc = 'cyt') +
	met(name = 'ISOBUTANOL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11292_MONOMER', loc = 'cyt') +
	met(name = 'CPD_7000', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7119', 0.000000), 
	Parameter('rvs_RXN0_7119', 1.000000))
Rule('PYRIDOXINE_4_DEHYDROGENASE_RXN',
	prot(name = 'EG11309_MONOMER', loc = 'cyt') +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRIDOXINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11309_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRIDOXAL', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PYRIDOXINE_4_DEHYDROGENASE_RXN', 1.000000), 
	Parameter('rvs_PYRIDOXINE_4_DEHYDROGENASE_RXN', 1.000000))
Rule('RXN0_7143',
	prot(name = 'EG11309_MONOMER', loc = 'cyt') +
	met(name = 'CPD_17752', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11309_MONOMER', loc = 'cyt') +
	met(name = 'CPD_17753', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7143', 1.000000), 
	Parameter('rvs_RXN0_7143', 0.000000))
Rule('RXN0_1281',
	prot(name = 'EG11311_MONOMER', loc = 'cyt') +
	met(name = 'tRNA_Dihydrouridines', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11311_MONOMER', loc = 'cyt') +
	met(name = 'tRNA_uridines', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_1281', 0.000000), 
	Parameter('rvs_RXN0_1281', 1.000000))
Rule('_2_OCTAPRENYLPHENOL_HYDROX_RXN',
	prot(name = 'EG11333_MONOMER', loc = 'cyt') +
	met(name = '_2_OCTAPRENYLPHENOL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11333_MONOMER', loc = 'cyt') +
	met(name = '_2_OCTAPRENYL_6_HYDROXYPHENOL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd__2_OCTAPRENYLPHENOL_HYDROX_RXN', 1.000000), 
	Parameter('rvs__2_OCTAPRENYLPHENOL_HYDROX_RXN', 0.000000))
Rule('_3dot1dot21dot1_RXN',
	prot(name = 'EG11336_MONOMER', loc = 'per') +
	met(name = 'Double_Stranded_DNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11336_MONOMER', loc = 'per') +
	met(name = '_5_phosphooligonucleotides', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd__3dot1dot21dot1_RXN', 1.000000), 
	Parameter('rvs__3dot1dot21dot1_RXN', 0.000000))
Rule('RXN0_5120',
	prot(name = 'EG11339_MONOMER', loc = 'cyt') +
	met(name = 'CPD_12575', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_930', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11339_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_932', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UDP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5120', 1.000000), 
	Parameter('rvs_RXN0_5120', 0.000000))
Rule('RXN0_5121',
	prot(name = 'EG11340_MONOMER', loc = 'mem') +
	met(name = 'CPD0_932', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11340_MONOMER', loc = 'mem') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_933', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5121', 1.000000), 
	Parameter('rvs_RXN0_5121', 0.000000))
Rule('RXN0_5122',
	prot(name = 'EG11341_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_933', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP_L_GLYCERO_D_MANNO_HEPTOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11341_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_934', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5122', 1.000000), 
	Parameter('rvs_RXN0_5122', 0.000000))
Rule('RXN0_2023',
	prot(name = 'EG11344_MONOMER', loc = 'cyt') +
	met(name = 'tRNA_uridine34', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TusE_S_sulfanylcysteine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Donor_H2', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	prot(name = 'EG11344_MONOMER', loc = 'cyt') +
	met(name = 'tRNA_2_thiouridine34', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TusE_L_cysteine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Acceptor', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_2023', 1.000000), 
	Parameter('rvs_RXN0_2023', 0.000000))
Rule('RXN0_5129',
	prot(name = 'EG11350_MONOMER', loc = 'cyt') +
	met(name = 'Lipopolysaccharides', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DTDP_RHAMNOSE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11350_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_944', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TDP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5129', 1.000000), 
	Parameter('rvs_RXN0_5129', 0.000000))
Rule('RXN0_5124',
	prot(name = 'EG11351_MONOMER', loc = 'cyt') +
	met(name = 'CPD_14553', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_935', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11351_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_936', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UDP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5124', 1.000000), 
	Parameter('rvs_RXN0_5124', 0.000000))
Rule('RXN0_5125',
	prot(name = 'EG11352_MONOMER', loc = 'cyt') +
	met(name = 'CPD_12575', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_936', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11352_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_937', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UDP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5125', 1.000000), 
	Parameter('rvs_RXN0_5125', 0.000000))
Rule('RXN0_5126',
	prot(name = 'EG11353_MONOMER', loc = 'cyt') +
	met(name = 'CPD_12575', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_937', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11353_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_938', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UDP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5126', 1.000000), 
	Parameter('rvs_RXN0_5126', 0.000000))
Rule('_3dot4dot23dot43_RXN',
	prot(name = 'EG11359_MONOMER', loc = 'imem') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'type_IV_prepillin', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11359_MONOMER', loc = 'imem') +
	met(name = 'Cleaved_Type_IV_Prepillins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Peptides_holder', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3dot4dot23dot43_RXN', 1.000000), 
	Parameter('rvs__3dot4dot23dot43_RXN', 0.000000))
Rule('RXN0_5422',
	prot(name = 'EG11362_MONOMER', loc = 'cyt') +
	met(name = 'tRNAs_Asp_with_queuosine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11362_MONOMER', loc = 'cyt') +
	met(name = 'tRNAs_with_glutamylated_queuosine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5422', 1.000000), 
	Parameter('rvs_RXN0_5422', 0.000000))
Rule('PGPPHOSPHA_RXN',
	prot(name = 'EG11371_MONOMER', loc = 'imem') +
	met(name = 'L_1_PHOSPHATIDYL_GLYCEROL_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11371_MONOMER', loc = 'imem') +
	met(name = 'L_1_PHOSPHATIDYL_GLYCEROL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PGPPHOSPHA_RXN', 1.000000), 
	Parameter('rvs_PGPPHOSPHA_RXN', 0.000000))
Rule('RXN0_5127',
	prot(name = 'EG11423_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_938', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP_L_GLYCERO_D_MANNO_HEPTOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11423_MONOMER', loc = 'cyt') +
	met(name = 'CPD_21359', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5127', 1.000000), 
	Parameter('rvs_RXN0_5127', 0.000000))
Rule('RXN0_5294',
	prot(name = 'EG11424_MONOMER', loc = 'imem') +
	met(name = 'CPD_21531', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_21359', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11424_MONOMER', loc = 'imem') +
	met(name = 'CPD0_1101', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UNDECAPRENYL_DIPHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5294', 1.000000), 
	Parameter('rvs_RXN0_5294', 0.000000))
Rule('RXN0_5123',
	prot(name = 'EG11425_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_934', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11425_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_935', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5123', 1.000000), 
	Parameter('rvs_RXN0_5123', 0.000000))
Rule('RXN_11326',
	prot(name = 'EG11426_MONOMER', loc = 'cyt') +
	met(name = 'KDO2_LIPID_IVA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CMP_KDO', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11426_MONOMER', loc = 'cyt') +
	met(name = 'CPD_12284', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11326', 1.000000), 
	Parameter('rvs_RXN_11326', 0.000000))
Rule('RXN_8668',
	prot(name = 'EG11433_MONOMER', loc = 'cyt') +
	met(name = 'Protein_L_methionine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Ox_Thioredoxin', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11433_MONOMER', loc = 'cyt') +
	met(name = 'Protein_L_methionine_S_S_oxides', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Red_Thioredoxin', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_8668', 0.000000), 
	Parameter('rvs_RXN_8668', 1.000000))
Rule('RXN_9590',
	prot(name = 'EG11437_MONOMER', loc = 'cyt') +
	met(name = 'ACYL_ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11437_MONOMER', loc = 'cyt') +
	met(name = 'Acyl_Phosphates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_9590', 1.000000), 
	Parameter('rvs_RXN_9590', 1.000000))
Rule('RXN0_7079',
	prot(name = 'EG11438_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_2552', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11438_MONOMER', loc = 'cyt') +
	met(name = '_7_METHYLGUANOSINE_5_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7079', 1.000000), 
	Parameter('rvs_RXN0_7079', 0.000000))
Rule('_3dot5dot1dot88_RXN',
	prot(name = 'EG11440_MONOMER', loc = 'cyt') +
	met(name = 'FORMYL_L_METHIONYL_PEPTIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11440_MONOMER', loc = 'cyt') +
	met(name = 'METHIONYL_PEPTIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FORMATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3dot5dot1dot88_RXN', 1.000000), 
	Parameter('rvs__3dot5dot1dot88_RXN', 0.000000))
Rule('_3dot4dot24dot70_RXN',
	prot(name = 'EG11441_MONOMER', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OLIGOPEPTIDES', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11441_MONOMER', loc = 'cyt') +
	met(name = 'Peptides_holder', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd__3dot4dot24dot70_RXN', 1.000000), 
	Parameter('rvs__3dot4dot24dot70_RXN', 0.000000))
Rule('RXN_17393',
	prot(name = 'EG11494_MONOMER', loc = 'per') +
	met(name = 'CPD_18807', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11494_MONOMER', loc = 'per') +
	met(name = 'CPD_18808', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_18806', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17393', 1.000000), 
	Parameter('rvs_RXN_17393', 0.000000))
Rule('RXN0_5419',
	prot(name = 'EG11497_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Nonmethylated_Ribosomal_Protein_L11s', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11497_MONOMER', loc = 'cyt') +
	met(name = 'Methylated_Ribosomal_Protein_L11s', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5419', 1.000000), 
	Parameter('rvs_RXN0_5419', 0.000000))
Rule('RXN0_7114',
	prot(name = 'EG11503_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'N6_L_threonylcarbamoyladenine37_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11503_MONOMER', loc = 'cyt') +
	met(name = 'N6_met_threonylcarbamoyl_A37_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7114', 1.000000), 
	Parameter('rvs_RXN0_7114', 0.000000))
Rule('RXN_11845',
	prot(name = 'EG11507_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_23S_rRNA_uridine_2552', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11507_MONOMER', loc = 'cyt') +
	met(name = '_23S_rRNA_2_O_methyluridine2552', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11845', 1.000000), 
	Parameter('rvs_RXN_11845', 0.000000))
Rule('RXN_12480',
	prot(name = 'EG11538_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Val_tRNA1_Adenine37', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11538_MONOMER', loc = 'cyt') +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Val_tRNA1_N6_MeAdenine37', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_12480', 1.000000), 
	Parameter('rvs_RXN_12480', 0.000000))
Rule('RXN0_6435',
	prot(name = 'EG11551_MONOMER', loc = 'cyt') +
	met(name = 'CARBAMOYL_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HypE_Proteins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11551_MONOMER', loc = 'cyt') +
	met(name = 'HypE_S_carboxamide', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6435', 1.000000), 
	Parameter('rvs_RXN0_6435', 0.000000))
Rule('RXN_19407',
	prot(name = 'EG11579_MONOMER', loc = 'cyt') +
	met(name = 'CPD_602', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11579_MONOMER', loc = 'cyt') +
	met(name = 'CPD_20969', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_15317', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_19407', 1.000000), 
	Parameter('rvs_RXN_19407', 0.000000))
Rule('RXN_7632',
	prot(name = 'EG11581_MONOMER', loc = 'cyt') +
	met(name = 'CPD_6982', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11581_MONOMER', loc = 'cyt') +
	met(name = '_34_DIHYDROXYPHENYLPYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_7632', 0.000000), 
	Parameter('rvs_RXN_7632', 1.000000))
Rule('RXN0_947',
	prot(name = 'EG11591_MONOMER', loc = 'cyt') +
	met(name = 'Octanoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Lipoyl_Protein_L_Lysine', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11591_MONOMER', loc = 'cyt') +
	met(name = 'Octanoylated_domains', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_947', 1.000000), 
	Parameter('rvs_RXN0_947', 0.000000))
Rule('RXN0_1137',
	prot(name = 'EG11591_MONOMER', loc = 'cyt') +
	met(name = 'E2O_MONOMER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'LIPOYL_ACP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11591_MONOMER', loc = 'cyt') +
	met(name = 'SUCB_LIPOATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_1137', 1.000000), 
	Parameter('rvs_RXN0_1137', 0.000000))
Rule('RXN0_1130',
	prot(name = 'EG11591_MONOMER', loc = 'cyt') +
	met(name = 'E2P_MONOMER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'LIPOYL_ACP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11591_MONOMER', loc = 'cyt') +
	met(name = 'ACEF_LIPOATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_1130', 1.000000), 
	Parameter('rvs_RXN0_1130', 0.000000))
Rule('RXN0_1138',
	prot(name = 'EG11591_MONOMER', loc = 'cyt') +
	met(name = 'Gcv_H', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Lipoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11591_MONOMER', loc = 'cyt') +
	met(name = 'PROTEIN_LIPOYLLYSINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_1138', 1.000000), 
	Parameter('rvs_RXN0_1138', 0.000000))
Rule('RXN_8340',
	prot(name = 'EG11595_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Donor_H2', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	prot(name = 'EG11595_MONOMER', loc = 'cyt') +
	met(name = 'CPD_19179', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MET', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CH33ADO', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Acceptor', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_8340', 1.000000), 
	Parameter('rvs_RXN_8340', 0.000000))
Rule('RXN0_6945',
	prot(name = 'EG11600_MONOMER', loc = 'cyt') +
	met(name = '_3_MERCAPTO_PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11600_MONOMER', loc = 'cyt') +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HS', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6945', 1.000000), 
	Parameter('rvs_RXN0_6945', 0.000000))
Rule('MERCAPYSTRANS_RXN',
	prot(name = 'EG11600_MONOMER', loc = 'cyt') +
	met(name = '_3_MERCAPTO_PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Red_Thioredoxin', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11600_MONOMER', loc = 'cyt') +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Ox_Thioredoxin', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_MERCAPYSTRANS_RXN', 1.000000), 
	Parameter('rvs_MERCAPYSTRANS_RXN', 0.000000))
Rule('RXN_14379',
	prot(name = 'EG11613_MONOMER', loc = 'imem') +
	met(name = 'L_1_PHOSPHATIDYL_ETHANOLAMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_939', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11613_MONOMER', loc = 'imem') +
	met(name = 'DIACYLGLYCEROL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_15242', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_14379', 1.000000), 
	Parameter('rvs_RXN_14379', 0.000000))
Rule('RXN0_6524',
	prot(name = 'EG11620_MONOMER', loc = 'cyt') +
	met(name = 'RNASE_II_POLY_A_SUBSTRATE_MRNA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11620_MONOMER', loc = 'cyt') +
	met(name = 'RNASE_II_SUBSTRATE_WITH_NO_POLY_A_TAIL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6524', 1.000000), 
	Parameter('rvs_RXN0_6524', 0.000000))
Rule('_3dot1dot13dot1_RXN',
	prot(name = 'EG11620_MONOMER', loc = 'cyt') +
	met(name = 'RNASE_II_DEGRADATION_SUBSTRATE_MRNA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11620_MONOMER', loc = 'cyt') +
	met(name = 'Nucleoside_Monophosphates', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd__3dot1dot13dot1_RXN', 1.000000), 
	Parameter('rvs__3dot1dot13dot1_RXN', 0.000000))
Rule('PSEUDOURIDINE_KINASE_RXN',
	prot(name = 'EG11646_MONOMER', loc = 'cyt') +
	met(name = 'CPD_497', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11646_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PSEUDOURIDINE_5_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PSEUDOURIDINE_KINASE_RXN', 1.000000), 
	Parameter('rvs_PSEUDOURIDINE_KINASE_RXN', 0.000000))
Rule('UNDECAPRENYL_DIPHOSPHATASE_RXN',
	prot(name = 'EG11665_MONOMER', loc = 'imem') +
	met(name = 'UNDECAPRENYL_DIPHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11665_MONOMER', loc = 'imem') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_9646', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_UNDECAPRENYL_DIPHOSPHATASE_RXN', 1.000000), 
	Parameter('rvs_UNDECAPRENYL_DIPHOSPHATASE_RXN', 0.000000))
Rule('RXN_11776',
	prot(name = 'EG11665_MONOMER', loc = 'imem') +
	met(name = 'FARNESYL_PP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11665_MONOMER', loc = 'imem') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_12587', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11776', 1.000000), 
	Parameter('rvs_RXN_11776', 0.000000))
Rule('RXN0_4361',
	prot(name = 'EG11736_MONOMER', loc = 'cyt') +
	met(name = 'D_BETA_D_HEPTOSE_17_DIPHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11736_MONOMER', loc = 'cyt') +
	met(name = 'D_BETA_D_HEPTOSE_1_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_4361', 1.000000), 
	Parameter('rvs_RXN0_4361', 0.000000))
Rule('RXN0_7100',
	prot(name = 'EG11750_MONOMER', loc = 'cyt') +
	met(name = 'Double_Stranded_DNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11750_MONOMER', loc = 'cyt') +
	met(name = '_5_phosphooligonucleotides', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_7100', 1.000000), 
	Parameter('rvs_RXN0_7100', 0.000000))
Rule('RXN0_6727',
	prot(name = 'EG11758_MONOMER', loc = 'cyt') +
	met(name = 'CPD_653', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	prot(name = 'EG11758_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6727', 1.000000), 
	Parameter('rvs_RXN0_6727', 0.000000))
Rule('RXN_13141',
	prot(name = 'EG11758_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_2474', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	prot(name = 'EG11758_MONOMER', loc = 'cyt') +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_13141', 1.000000), 
	Parameter('rvs_RXN_13141', 0.000000))
Rule('RXN_12752',
	prot(name = 'EG11758_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_2472', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11758_MONOMER', loc = 'cyt') +
	met(name = 'CPD_653', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_12752', 1.000000), 
	Parameter('rvs_RXN_12752', 0.000000))
Rule('RXN_13142',
	prot(name = 'EG11758_MONOMER', loc = 'cyt') +
	met(name = 'CPD_14133', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11758_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_2474', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_13142', 1.000000), 
	Parameter('rvs_RXN_13142', 0.000000))
Rule('RXN0_2281',
	prot(name = 'EG11768_MONOMER', loc = 'cyt') +
	met(name = 'tRNA_Containing_5MeAminoMe_2_ThioU', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SEPO3', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11768_MONOMER', loc = 'cyt') +
	met(name = 'Mnm5Se2U_containing_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_3734', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_2281', 1.000000), 
	Parameter('rvs_RXN0_2281', 0.000000))
Rule('TRNA_GUANINE_N7__METHYLTRANSFERASE_RXN',
	prot(name = 'EG11779_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Guanine46_in_tRNA', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11779_MONOMER', loc = 'cyt') +
	met(name = 'tRNA_Containing_N7_Methylguanine_46', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_TRNA_GUANINE_N7__METHYLTRANSFERASE_RXN', 1.000000), 
	Parameter('rvs_TRNA_GUANINE_N7__METHYLTRANSFERASE_RXN', 0.000000))
Rule('RXN_11589',
	prot(name = 'EG11794_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_23S_rRNA_cytidine_2498', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11794_MONOMER', loc = 'cyt') +
	met(name = '_23S_rRNA_2_O_methylcytidine2498', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11589', 1.000000), 
	Parameter('rvs_RXN_11589', 0.000000))
Rule('RXN_8654',
	prot(name = 'EG11796_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'LIPOIC_ACID', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11796_MONOMER', loc = 'cyt') +
	met(name = 'LIPOYL_AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_8654', 1.000000), 
	Parameter('rvs_RXN_8654', 0.000000))
Rule('RXN_8655',
	prot(name = 'EG11796_MONOMER', loc = 'cyt') +
	met(name = 'LIPOYL_AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Lipoyl_Protein_L_Lysine', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11796_MONOMER', loc = 'cyt') +
	met(name = 'Lipoyl_Protein_N6_lipoyllysine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_8655', 1.000000), 
	Parameter('rvs_RXN_8655', 0.000000))
Rule('RXN0_1139',
	prot(name = 'EG11796_MONOMER', loc = 'cyt') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'E2P_MONOMER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'LIPOIC_ACID', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11796_MONOMER', loc = 'cyt') +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACEF_LIPOATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_1139', 1.000000), 
	Parameter('rvs_RXN0_1139', 0.000000))
Rule('RXN0_1140',
	prot(name = 'EG11796_MONOMER', loc = 'cyt') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'E2O_MONOMER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'LIPOIC_ACID', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11796_MONOMER', loc = 'cyt') +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SUCB_LIPOATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_1140', 1.000000), 
	Parameter('rvs_RXN0_1140', 0.000000))
Rule('RXN0_1141',
	prot(name = 'EG11796_MONOMER', loc = 'cyt') +
	met(name = 'Gcv_H', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'LIPOIC_ACID', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11796_MONOMER', loc = 'cyt') +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTEIN_LIPOYLLYSINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_1141', 1.000000), 
	Parameter('rvs_RXN0_1141', 0.000000))
Rule('RXN0_5098',
	prot(name = 'EG11796_MONOMER', loc = 'cyt') +
	met(name = 'Lipoyl_Protein_L_Lysine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_195', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11796_MONOMER', loc = 'cyt') +
	met(name = 'Octanoylated_domains', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5098', 1.000000), 
	Parameter('rvs_RXN0_5098', 0.000000))
Rule('RXN0_3921',
	prot(name = 'EG11822_MONOMER', loc = 'cyt') +
	met(name = 'GAMMA_GLUTAMYL_PUTRESCINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11822_MONOMER', loc = 'cyt') +
	met(name = 'GAMMA_GLUTAMYL_GAMMA_AMINOBUTYRALDEH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HYDROGEN_PEROXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_3921', 1.000000), 
	Parameter('rvs_RXN0_3921', 0.000000))
Rule('_2dot7dot10dot1_RXN',
	prot(name = 'EG11826_MONOMER', loc = 'imem') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Protein_Tyrosines', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11826_MONOMER', loc = 'imem') +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Protein_tyrosine_phosphates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__2dot7dot10dot1_RXN', 1.000000), 
	Parameter('rvs__2dot7dot10dot1_RXN', 0.000000))
Rule('RXN0_262',
	prot(name = 'EG11829_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_8123', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GTP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11829_MONOMER', loc = 'cyt') +
	met(name = 'CPD_582', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_262', 1.000000), 
	Parameter('rvs_RXN0_262', 0.000000))
Rule('RXN_16457',
	prot(name = 'EG11829_MONOMER', loc = 'cyt') +
	met(name = 'CPD_8123', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_4', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11829_MONOMER', loc = 'cyt') +
	met(name = 'CPD_15874', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_16457', 1.000000), 
	Parameter('rvs_RXN_16457', 0.000000))
Rule('RXN_16456',
	prot(name = 'EG11829_MONOMER', loc = 'cyt') +
	met(name = 'CPD_15874', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11829_MONOMER', loc = 'cyt') +
	met(name = 'CPD_15873', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_16456', 1.000000), 
	Parameter('rvs_RXN_16456', 0.000000))
Rule('PROTEIN_KINASE_RXN',
	prot(name = 'EG11831_MONOMER', loc = 'cyt') +
	met(name = 'Protein_L_serine_or_L_threonine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11831_MONOMER', loc = 'cyt') +
	met(name = 'Protein_Ser_or_Thr_phosphate', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PROTEIN_KINASE_RXN', 1.000000), 
	Parameter('rvs_PROTEIN_KINASE_RXN', 0.000000))
Rule('RXN_17700',
	prot(name = 'EG11843_MONOMER', loc = 'cyt') +
	met(name = 'SULFOQUINOVOSYLDIACYLGLYCEROL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11843_MONOMER', loc = 'cyt') +
	met(name = 'CPD_10247', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_1_2_Diglycerides', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17700', 1.000000), 
	Parameter('rvs_RXN_17700', 0.000000))
Rule('RXN_17701',
	prot(name = 'EG11843_MONOMER', loc = 'cyt') +
	met(name = 'CPD_19111', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11843_MONOMER', loc = 'cyt') +
	met(name = 'CPD_10247', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLYCEROL', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17701', 1.000000), 
	Parameter('rvs_RXN_17701', 0.000000))
Rule('RXN_15298',
	prot(name = 'EG11846_MONOMER', loc = 'cyt') +
	met(name = 'CPD_16502', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11846_MONOMER', loc = 'cyt') +
	met(name = 'CPD_18717', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DIHYDROXY_ACETONE_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_15298', 1.000000), 
	Parameter('rvs_RXN_15298', 0.000000))
Rule('RXN_15297',
	prot(name = 'EG11848_MONOMER', loc = 'cyt') +
	met(name = 'CPD_16501', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11848_MONOMER', loc = 'cyt') +
	met(name = 'CPD_16502', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_15297', 1.000000), 
	Parameter('rvs_RXN_15297', 0.000000))
Rule('GLUCOSE_1_PHOSPHAT_RXN',
	prot(name = 'EG11850_MONOMER', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLC_1_P', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11850_MONOMER', loc = 'cyt') +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Glucopyranose', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLUCOSE_1_PHOSPHAT_RXN', 1.000000), 
	Parameter('rvs_GLUCOSE_1_PHOSPHAT_RXN', 0.000000))
Rule('RXN_14363',
	prot(name = 'EG11914_MONOMER', loc = 'imem') +
	met(name = 'L_1_PHOSPHATIDYL_ETHANOLAMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_939', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11914_MONOMER', loc = 'imem') +
	met(name = 'DIACYLGLYCEROL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_15238', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_14363', 1.000000), 
	Parameter('rvs_RXN_14363', 0.000000))
Rule('_3dot1dot21dot7_RXN',
	prot(name = 'EG11915_MONOMER', loc = 'cyt') +
	met(name = 'DNA_containing_abasic_Sites', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11915_MONOMER', loc = 'cyt') +
	met(name = 'Deoxy_Ribonucleoside_Monophosphates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3dot1dot21dot7_RXN', 1.000000), 
	Parameter('rvs__3dot1dot21dot7_RXN', 0.000000))
Rule('_3dot4dot13dot21_RXN',
	prot(name = 'EG11920_MONOMER', loc = 'cyt') +
	met(name = 'Dipeptides_With_Asp_At_N_Terminal', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11920_MONOMER', loc = 'cyt') +
	met(name = 'L_ASPARTATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Amino_Acids_20', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3dot4dot13dot21_RXN', 1.000000), 
	Parameter('rvs__3dot4dot13dot21_RXN', 0.000000))
Rule('RXN_11835',
	prot(name = 'EG11921_MONOMER', loc = 'cyt') +
	met(name = '_23S_rRNA_uridine2604', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11921_MONOMER', loc = 'cyt') +
	met(name = '_23S_rRNA_pseudouridine2604', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11835', 1.000000), 
	Parameter('rvs_RXN_11835', 0.000000))
Rule('RXN0_7253',
	prot(name = 'EG11921_MONOMER', loc = 'cyt') +
	met(name = 'tRNA_uridine35', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11921_MONOMER', loc = 'cyt') +
	met(name = 'tRNA_pseudouridine35', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7253', 1.000000), 
	Parameter('rvs_RXN0_7253', 0.000000))
Rule('RXN_15761',
	prot(name = 'EG11955_MONOMER', loc = 'per') +
	met(name = 'CPD_8876', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11955_MONOMER', loc = 'per') +
	met(name = 'CPD_7867', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SULFATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_15761', 1.000000), 
	Parameter('rvs_RXN_15761', 0.000000))
Rule('ALLOSE_KINASE_RXN',
	prot(name = 'EG11956_MONOMER', loc = 'cyt') +
	met(name = 'D_Allopyranose', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11956_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_ALLOSE_6_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ALLOSE_KINASE_RXN', 1.000000), 
	Parameter('rvs_ALLOSE_KINASE_RXN', 0.000000))
Rule('RXN0_304',
	prot(name = 'EG11957_MONOMER', loc = 'cyt') +
	met(name = 'D_ALLULOSE_6_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG11957_MONOMER', loc = 'cyt') +
	met(name = 'FRUCTOSE_6P', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_304', 1.000000), 
	Parameter('rvs_RXN0_304', 0.000000))
Rule('RXN0_5210',
	prot(name = 'EG11983_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_1048', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UDP_D_GALACTO_14_FURANOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG11983_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_1049', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UDP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5210', 1.000000), 
	Parameter('rvs_RXN0_5210', 0.000000))
Rule('_3dot2dot1dot21_RXN',
	prot(name = 'EG12013_MONOMER', loc = 'imem') +
	met(name = 'Beta_D_glucosides', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG12013_MONOMER', loc = 'imem') +
	met(name = 'Non_Glucosylated_Glucose_Acceptors', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Glucopyranose', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3dot2dot1dot21_RXN', 1.000000), 
	Parameter('rvs__3dot2dot1dot21_RXN', 0.000000))
Rule('ACETOINDEHYDROG_A_RXN',
	prot(name = 'EG12019_MONOMER', loc = 'cyt') +
	met(name = 'ACETOIN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG12019_MONOMER', loc = 'cyt') +
	met(name = 'DIACETYL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ACETOINDEHYDROG_A_RXN', 0.000000), 
	Parameter('rvs_ACETOINDEHYDROG_A_RXN', 1.000000))
Rule('RXN_11833',
	prot(name = 'EG12044_MONOMER', loc = 'cyt') +
	met(name = '_16S_rRNA_uridine516', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG12044_MONOMER', loc = 'cyt') +
	met(name = '_16S_rRNA_pseudouridine516', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11833', 1.000000), 
	Parameter('rvs_RXN_11833', 0.000000))
Rule('MALATE_DEHYDROGENASE_ACCEPTOR_RXN',
	prot(name = 'EG12069_MONOMER', loc = 'cyt') +
	met(name = 'ETR_Quinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MAL', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG12069_MONOMER', loc = 'cyt') +
	met(name = 'ETR_Quinols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXALACETIC_ACID', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_MALATE_DEHYDROGENASE_ACCEPTOR_RXN', 1.000000), 
	Parameter('rvs_MALATE_DEHYDROGENASE_ACCEPTOR_RXN', 0.000000))
Rule('RXN_19924',
	prot(name = 'EG12096_MONOMER', loc = 'cyt') +
	met(name = 'RNA_Holder', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG12096_MONOMER', loc = 'cyt') +
	met(name = 'Cyclic_Phosphate_Terminated_RNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_5Prime_OH_Terminated_RNAs', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_19924', 1.000000), 
	Parameter('rvs_RXN_19924', 0.000000))
Rule('RXN_16312',
	prot(name = 'EG12097_MONOMER', loc = 'cyt') +
	met(name = 'CPD_17573', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG12097_MONOMER', loc = 'cyt') +
	met(name = 'CPD_17574', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_16312', 1.000000), 
	Parameter('rvs_RXN_16312', 0.000000))
Rule('RXN_11837',
	prot(name = 'EG12098_MONOMER', loc = 'cyt') +
	met(name = '_23S_rRNA_uridine1911_1915_1917', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG12098_MONOMER', loc = 'cyt') +
	met(name = '_23S_rRNA_pseudouridine1911_1915_1917', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11837', 1.000000), 
	Parameter('rvs_RXN_11837', 0.000000))
Rule('RXN0_20',
	prot(name = 'EG12128_MONOMER', loc = 'imem') +
	met(name = 'Prolipoprotein_Cysteines', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_1_PHOSPHATIDYL_GLYCEROL', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG12128_MONOMER', loc = 'imem') +
	met(name = 'MONOMER0_4342', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SN_GLYCEROL_1_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_20', 1.000000), 
	Parameter('rvs_RXN0_20', 0.000000))
Rule('RXN_14391',
	prot(name = 'EG12130_MONOMER', loc = 'cyt') +
	met(name = 'Chap_ADP_apo_SP_Complex', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG12130_MONOMER', loc = 'cyt') +
	met(name = 'FeS_Cluster_Chaperones_ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_form_FeS_Cluster_Scaffold_Proteins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14391', 1.000000), 
	Parameter('rvs_RXN_14391', 0.000000))
Rule('URPHOS_RXN',
	prot(name = 'EG12159_MONOMER', loc = 'cyt') +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'URIDINE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG12159_MONOMER', loc = 'cyt') +
	met(name = 'RIBOSE_1P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'URACIL', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_URPHOS_RXN', 1.000000), 
	Parameter('rvs_URPHOS_RXN', 1.000000))
Rule('XANTHOSINEPHOSPHORY_RXN',
	prot(name = 'EG12159_MONOMER', loc = 'cyt') +
	met(name = 'XANTHOSINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG12159_MONOMER', loc = 'cyt') +
	met(name = 'RIBOSE_1P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'XANTHINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_XANTHOSINEPHOSPHORY_RXN', 1.000000), 
	Parameter('rvs_XANTHOSINEPHOSPHORY_RXN', 0.000000))
Rule('RXN_11591',
	prot(name = 'EG12163_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_16S_rRNA_cytosine967', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG12163_MONOMER', loc = 'cyt') +
	met(name = '_16S_rRNA_5_O_methylcytosine967', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11591', 1.000000), 
	Parameter('rvs_RXN_11591', 0.000000))
Rule('RXN0_7167',
	prot(name = 'EG12167_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_5_oxyacetylU34_tRNA', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG12167_MONOMER', loc = 'cyt') +
	met(name = '_5_methoxycarbonylmethoxyU34_tRNA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7167', 1.000000), 
	Parameter('rvs_RXN0_7167', 0.000000))
Rule('RXN0_7001',
	prot(name = 'EG12198_MONOMER', loc = 'cyt') +
	met(name = 'DIACETYLCHITOBIOSE_6_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG12198_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_2501', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACET', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7001', 1.000000), 
	Parameter('rvs_RXN0_7001', 0.000000))
Rule('RXN_11313',
	prot(name = 'EG12198_MONOMER', loc = 'cyt') +
	met(name = 'CHITOBIOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG12198_MONOMER', loc = 'cyt') +
	met(name = 'CPD_12274', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACET', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11313', 1.000000), 
	Parameter('rvs_RXN_11313', 0.000000))
Rule('RXN_11573',
	prot(name = 'EG12207_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_23S_rRNA_guanine_745', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG12207_MONOMER', loc = 'cyt') +
	met(name = '_23S_rRNA_N1_methylguanine745', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11573', 1.000000), 
	Parameter('rvs_RXN_11573', 0.000000))
Rule('RXN0_5061',
	prot(name = 'EG12210_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_929', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP_L_GLYCERO_D_MANNO_HEPTOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG12210_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_930', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5061', 1.000000), 
	Parameter('rvs_RXN0_5061', 0.000000))
Rule('RXN_18707',
	prot(name = 'EG12216_MONOMER', loc = 'cyt') +
	met(name = 'L_Cysteine_Desulfurase_persulfide', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TusA_L_cysteine', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG12216_MONOMER', loc = 'cyt') +
	met(name = 'Cysteine_Desulfurase_L_cysteine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TusA_Persulfides', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_18707', 1.000000), 
	Parameter('rvs_RXN_18707', 0.000000))
Rule('HOLO_ACP_SYNTH_RXN',
	prot(name = 'EG12221_MONOMER', loc = 'cyt') +
	met(name = 'All_apo_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG12221_MONOMER', loc = 'cyt') +
	met(name = '_3_5_ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'All_holo_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_HOLO_ACP_SYNTH_RXN', 1.000000), 
	Parameter('rvs_HOLO_ACP_SYNTH_RXN', 0.000000))
Rule('RXN0_6731',
	prot(name = 'EG12233_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_16S_rRNA_guanine1516', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG12233_MONOMER', loc = 'cyt') +
	met(name = '_16S_rRNA_N2methylguanine1516', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6731', 1.000000), 
	Parameter('rvs_RXN0_6731', 0.000000))
Rule('RXN0_6998',
	prot(name = 'EG12234_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_23S_rRNA_adenine_2030', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG12234_MONOMER', loc = 'cyt') +
	met(name = '_23S_rRNA_N6_methyladenine_2030', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6998', 1.000000), 
	Parameter('rvs_RXN0_6998', 0.000000))
Rule('RXN_982',
	prot(name = 'EG12237_MONOMER', loc = 'cyt') +
	met(name = 'ARSENATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Red_Glutaredoxins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG12237_MONOMER', loc = 'cyt') +
	met(name = 'CPD_763', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Ox_Glutaredoxins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_982', 1.000000), 
	Parameter('rvs_RXN_982', 1.000000))
Rule('RXN_19020',
	prot(name = 'EG12244_MONOMER', loc = 'imem') +
	met(name = 'Menaquinols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HYDROGEN_PEROXIDE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG12244_MONOMER', loc = 'imem') +
	met(name = 'Menaquinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_19020', 1.000000), 
	Parameter('rvs_RXN_19020', 0.000000))
Rule('RXN_19776',
	prot(name = 'EG12244_MONOMER', loc = 'imem') +
	met(name = 'MENADIOL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HYDROGEN_PEROXIDE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG12244_MONOMER', loc = 'imem') +
	met(name = 'CPD_3766', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_19776', 1.000000), 
	Parameter('rvs_RXN_19776', 1.000000))
Rule('RXN_19775',
	prot(name = 'EG12244_MONOMER', loc = 'imem') +
	met(name = 'HYDROQUINONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HYDROGEN_PEROXIDE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG12244_MONOMER', loc = 'imem') +
	met(name = 'P_BENZOQUINONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_19775', 1.000000), 
	Parameter('rvs_RXN_19775', 1.000000))
Rule('RXN_2043',
	prot(name = 'EG12258_MONOMER', loc = 'ex') +
	met(name = 'CELLULOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG12258_MONOMER', loc = 'ex') +
	met(name = 'Cellodextrins', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_2043', 1.000000), 
	Parameter('rvs_RXN_2043', 0.000000))
Rule('RXN_19630',
	prot(name = 'EG12265_MONOMER', loc = 'imem') +
	met(name = 'L_1_PHOSPHATIDYL_ETHANOLAMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CELLULOSE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG12265_MONOMER', loc = 'imem') +
	met(name = 'DIACYLGLYCEROL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'phosphoethanolamine_cellulose', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_19630', 1.000000), 
	Parameter('rvs_RXN_19630', 1.000000))
Rule('RXN_16286',
	prot(name = 'EG12267_MONOMER', loc = 'imem') +
	met(name = 'L_1_PHOSPHATIDYL_ETHANOLAMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'KDO2_LIPID_A', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG12267_MONOMER', loc = 'imem') +
	met(name = 'DIACYLGLYCEROL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_11653', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_16286', 1.000000), 
	Parameter('rvs_RXN_16286', 0.000000))
Rule('RXN0_4581',
	prot(name = 'EG12267_MONOMER', loc = 'imem') +
	met(name = 'L_1_PHOSPHATIDYL_ETHANOLAMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'KDO2_LIPID_IVA', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG12267_MONOMER', loc = 'imem') +
	met(name = 'DIACYLGLYCEROL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PHOSPHATIDYLETHANOLAMINE_KDO2', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_4581', 1.000000), 
	Parameter('rvs_RXN0_4581', 0.000000))
Rule('LXULRU5P_RXN',
	prot(name = 'EG12286_MONOMER', loc = 'cyt') +
	met(name = 'L_RIBULOSE_5_P', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG12286_MONOMER', loc = 'cyt') +
	met(name = 'L_XYLULOSE_5_P', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_LXULRU5P_RXN', 0.000000), 
	Parameter('rvs_LXULRU5P_RXN', 1.000000))
Rule('RIBULPEPIM_RXN',
	prot(name = 'EG12287_MONOMER', loc = 'cyt') +
	met(name = 'L_RIBULOSE_5_P', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG12287_MONOMER', loc = 'cyt') +
	met(name = 'XYLULOSE_5_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RIBULPEPIM_RXN', 1.000000), 
	Parameter('rvs_RIBULPEPIM_RXN', 1.000000))
Rule('THREODEHYD_RXN',
	prot(name = 'EG12293_MONOMER', loc = 'cyt') +
	met(name = 'THR', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG12293_MONOMER', loc = 'cyt') +
	met(name = 'AMINO_OXOBUT', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_THREODEHYD_RXN', 1.000000), 
	Parameter('rvs_THREODEHYD_RXN', 0.000000))
Rule('DEPHOSPHOCOAKIN_RXN',
	prot(name = 'EG12312_MONOMER', loc = 'cyt') +
	met(name = 'DEPHOSPHO_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG12312_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DEPHOSPHOCOAKIN_RXN', 1.000000), 
	Parameter('rvs_DEPHOSPHOCOAKIN_RXN', 0.000000))
Rule('RXN0_2945',
	prot(name = 'EG12318_MONOMER', loc = 'per') +
	met(name = 'CUplus', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG12318_MONOMER', loc = 'per') +
	met(name = 'CUplus2', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_2945', 1.000000), 
	Parameter('rvs_RXN0_2945', 0.000000))
Rule('RXN0_2943',
	prot(name = 'EG12318_MONOMER', loc = 'per') +
	met(name = '_2_3_DIHYDROXYBENZOATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG12318_MONOMER', loc = 'per') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_CARBOXYMUCONATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_2943', 1.000000), 
	Parameter('rvs_RXN0_2943', 0.000000))
Rule('RXN_17944',
	prot(name = 'EG12318_MONOMER', loc = 'per') +
	met(name = 'CPD_12797', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG12318_MONOMER', loc = 'per') +
	met(name = 'CPD_19233', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17944', 1.000000), 
	Parameter('rvs_RXN_17944', 0.000000))
Rule('RXN_15952',
	prot(name = 'EG12330_MONOMER', loc = 'cyt') +
	met(name = 'Cyclic_Phosphate_Terminated_RNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG12330_MONOMER', loc = 'cyt') +
	met(name = '_2_Prime_Phosphate_Terminated_RNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_15952', 1.000000), 
	Parameter('rvs_RXN_15952', 0.000000))
Rule('RXN0_5062',
	prot(name = 'EG12330_MONOMER', loc = 'cyt') +
	met(name = 'Pre_tRNA_5_prime_half_molecules', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pre_tRNA_3_prime_half_molecules', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG12330_MONOMER', loc = 'cyt') +
	met(name = 'ligated_tRNAs_with_2prime_5prime_linkage', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_5062', 1.000000), 
	Parameter('rvs_RXN0_5062', 1.000000))
Rule('RXN_14196',
	prot(name = 'EG12384_MONOMER', loc = 'cyt') +
	met(name = 'CARBAMATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG12384_MONOMER', loc = 'cyt') +
	met(name = 'CARBAMOYL_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14196', 1.000000), 
	Parameter('rvs_RXN_14196', 1.000000))
Rule('RXN0_5364',
	prot(name = 'EG12387_MONOMER', loc = 'imem') +
	met(name = 'CPD_381', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG12387_MONOMER', loc = 'imem') +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HYDROGEN_PEROXIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5364', 1.000000), 
	Parameter('rvs_RXN0_5364', 0.000000))
Rule('_1dot8dot4dot12_RXN',
	prot(name = 'EG12394_MONOMER', loc = 'cyt') +
	met(name = 'Protein_L_methionine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Ox_Thioredoxin', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG12394_MONOMER', loc = 'cyt') +
	met(name = 'Protein_L_methionine_R_S_oxides', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Red_Thioredoxin', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd__1dot8dot4dot12_RXN', 1.000000), 
	Parameter('rvs__1dot8dot4dot12_RXN', 0.000000))
Rule('RXN_11586',
	prot(name = 'EG12401_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_23S_rRNA_adenine_2503', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Reduced_2Fe_2S_Ferredoxins', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	prot(name = 'EG12401_MONOMER', loc = 'cyt') +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MET', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CH33ADO', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_23S_rRNA_2_methyladenine2503', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Oxidized_2Fe_2S_Ferredoxins', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11586', 1.000000), 
	Parameter('rvs_RXN_11586', 0.000000))
Rule('RXN0_7007',
	prot(name = 'EG12401_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'tRNA_adenine_37', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Reduced_2Fe_2S_Ferredoxins', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	prot(name = 'EG12401_MONOMER', loc = 'cyt') +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MET', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CH33ADO', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'tRNA_2methyladenine_37', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Oxidized_2Fe_2S_Ferredoxins', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7007', 1.000000), 
	Parameter('rvs_RXN0_7007', 0.000000))
Rule('RXN_19024',
	prot(name = 'EG12403_MONOMER', loc = 'cyt') +
	met(name = 'GLUTATHIONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG12403_MONOMER', loc = 'cyt') +
	met(name = 'CYS_GLY', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_5_OXOPROLINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_19024', 1.000000), 
	Parameter('rvs_RXN_19024', 0.000000))
Rule('RXN_14992',
	prot(name = 'EG12424_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Release_factor_L_glutamine', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG12424_MONOMER', loc = 'cyt') +
	met(name = 'Release_factor_N5_Methyl_L_glutamine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14992', 1.000000), 
	Parameter('rvs_RXN_14992', 0.000000))
Rule('RXN_11836',
	prot(name = 'EG12433_MONOMER', loc = 'cyt') +
	met(name = '_23S_rRNA_uridine2605', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG12433_MONOMER', loc = 'cyt') +
	met(name = '_23S_rRNA_pseudouridine2605', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11836', 1.000000), 
	Parameter('rvs_RXN_11836', 0.000000))
Rule('RXN_18678',
	prot(name = 'EG12436_MONOMER', loc = 'imem') +
	met(name = 'signal_peptide', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG12436_MONOMER', loc = 'imem') +
	met(name = 'Peptides_holder', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_18678', 1.000000), 
	Parameter('rvs_RXN_18678', 0.000000))
Rule('RXN_9310',
	prot(name = 'EG12438_MONOMER', loc = 'cyt') +
	met(name = 'CPD_9924', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG12438_MONOMER', loc = 'cyt') +
	met(name = 'CPD_9923', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_9310', 1.000000), 
	Parameter('rvs_RXN_9310', 0.000000))
Rule('RXN0_7022',
	prot(name = 'EG12440_MONOMER', loc = 'cyt') +
	met(name = 'UDP_N_ACETYLMURAMATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_1082', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG12440_MONOMER', loc = 'cyt') +
	met(name = 'UDP_MURNAC_TETRAPEPTIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7022', 1.000000), 
	Parameter('rvs_RXN0_7022', 0.000000))
Rule('RXN0_2361',
	prot(name = 'EG12440_MONOMER', loc = 'cyt') +
	met(name = 'UDP_N_ACETYLMURAMATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_ALA_GAMMA_D_GLU_DAP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG12440_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UDP_AAGM_DIAMINOHEPTANEDIOATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_2361', 1.000000), 
	Parameter('rvs_RXN0_2361', 0.000000))
Rule('RXN0_1241',
	prot(name = 'EG12449_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Ribosomal_protein_L3_L_glutamine', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG12449_MONOMER', loc = 'cyt') +
	met(name = 'Ribosomal_protein_L3_N5M_L_glutamine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_1241', 1.000000), 
	Parameter('rvs_RXN0_1241', 0.000000))
Rule('RXN0_7108',
	prot(name = 'EG12450_MONOMER', loc = 'cyt') +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPLX0_2', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG12450_MONOMER', loc = 'cyt') +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPLX0_1', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7108', 1.000000), 
	Parameter('rvs_RXN0_7108', 0.000000))
Rule('RXN_11842',
	prot(name = 'EG12609_MONOMER', loc = 'cyt') +
	met(name = 'Uridine32_in_tRNA', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG12609_MONOMER', loc = 'cyt') +
	met(name = 'tRNA_pseudouridine32', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11842', 1.000000), 
	Parameter('rvs_RXN_11842', 0.000000))
Rule('RXN_11843',
	prot(name = 'EG12609_MONOMER', loc = 'cyt') +
	met(name = '_23S_rRNA_uridine746', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG12609_MONOMER', loc = 'cyt') +
	met(name = '_23S_rRNA_pseudouridine746', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11843', 1.000000), 
	Parameter('rvs_RXN_11843', 0.000000))
Rule('LIPIDXSYNTHESIS_RXN',
	prot(name = 'EG12666_MONOMER', loc = 'imem') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OH_MYRISTOYL', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG12666_MONOMER', loc = 'imem') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'BISOHMYR_GLUCOSAMINYL_1P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_LIPIDXSYNTHESIS_RXN', 1.000000), 
	Parameter('rvs_LIPIDXSYNTHESIS_RXN', 0.000000))
Rule('RXN0_6562',
	prot(name = 'EG12693_MONOMER', loc = 'cyt') +
	met(name = '_3_P_HYDROXYPYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG12693_MONOMER', loc = 'cyt') +
	met(name = 'OH_PYR', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6562', 1.000000), 
	Parameter('rvs_RXN0_6562', 0.000000))
Rule('RIBOSYLHOMOCYSTEINASE_RXN',
	prot(name = 'EG12712_MONOMER', loc = 'cyt') +
	met(name = 'CPD_564', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'EG12712_MONOMER', loc = 'cyt') +
	met(name = 'HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DIHYDROXYPENTANEDIONE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RIBOSYLHOMOCYSTEINASE_RXN', 1.000000), 
	Parameter('rvs_RIBOSYLHOMOCYSTEINASE_RXN', 0.000000))
Rule('RXN0_1922',
	prot(name = 'EG12717_MONOMER', loc = 'cyt') +
	met(name = 'CPD_8521', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG12717_MONOMER', loc = 'cyt') +
	met(name = 'DNA_containing_abasic_Sites', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Modified_Bases', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_1922', 1.000000), 
	Parameter('rvs_RXN0_1922', 0.000000))
Rule('RXN_18708',
	prot(name = 'EG12876_MONOMER', loc = 'cyt') +
	met(name = 'TusD_Persulfides', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TusE_L_cysteine', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG12876_MONOMER', loc = 'cyt') +
	met(name = 'TusD_L_cysteine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TusE_S_sulfanylcysteine', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_18708', 1.000000), 
	Parameter('rvs_RXN_18708', 0.000000))
Rule('RXN0_5216',
	prot(name = 'EG13236_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_1063', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'EG13236_MONOMER', loc = 'cyt') +
	met(name = 'CPD_15979', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLYCERATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5216', 1.000000), 
	Parameter('rvs_RXN0_5216', 0.000000))
Rule('_2PGADEHYDRAT_RXN',
	cplx(name = 'ENOLASE_CPLX', loc = 'cyt') +
	met(name = '_2_PG', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'ENOLASE_CPLX', loc = 'cyt') +
	met(name = 'PHOSPHO_ENOL_PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__2PGADEHYDRAT_RXN', 1.000000), 
	Parameter('rvs__2PGADEHYDRAT_RXN', 1.000000))
Rule('DHBDEHYD_RXN',
	cplx(name = 'ENTA_CPLX', loc = 'cyt') +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DIHYDRO_DIOH_BENZOATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'ENTA_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_3_DIHYDROXYBENZOATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DHBDEHYD_RXN', 1.000000), 
	Parameter('rvs_DHBDEHYD_RXN', 0.000000))
Rule('ISOCHORMAT_RXN',
	cplx(name = 'ENTB_CPLX', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ISOCHORISMATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ENTB_CPLX', loc = 'cyt') +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DIHYDRO_DIOH_BENZOATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ISOCHORMAT_RXN', 1.000000), 
	Parameter('rvs_ISOCHORMAT_RXN', 0.000000))
Rule('ISOCHORSYN_RXN',
	prot(name = 'ENTC_MONOMER', loc = 'cyt') +
	met(name = 'CHORISMATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'ENTC_MONOMER', loc = 'cyt') +
	met(name = 'ISOCHORISMATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ISOCHORSYN_RXN', 1.000000), 
	Parameter('rvs_ISOCHORSYN_RXN', 1.000000))
Rule('RXN_15889',
	prot(name = 'ENTD_MONOMER', loc = 'imem') +
	met(name = 'Apo_EntF', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'ENTD_MONOMER', loc = 'imem') +
	met(name = 'Holo_EntF', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_3_5_ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_15889', 1.000000), 
	Parameter('rvs_RXN_15889', 0.000000))
Rule('ENTDB_RXN',
	prot(name = 'ENTD_MONOMER', loc = 'imem') +
	met(name = 'Apo_EntB', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'ENTD_MONOMER', loc = 'imem') +
	met(name = 'Holo_EntB', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_3_5_ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ENTDB_RXN', 1.000000), 
	Parameter('rvs_ENTDB_RXN', 0.000000))
Rule('RXN_19445',
	cplx(name = 'ENTE_CPLX', loc = 'cyt') +
	met(name = '_2_3_DIHYDROXYBENZOATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Holo_EntB', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ENTE_CPLX', loc = 'cyt') +
	met(name = '_23DHB_EntB', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_19445', 1.000000), 
	Parameter('rvs_RXN_19445', 0.000000))
Rule('RXN0_5208',
	cplx(name = 'ENTE_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ENTE_CPLX', loc = 'cyt') +
	met(name = 'ADENOSYL_P4', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5208', 1.000000), 
	Parameter('rvs_RXN0_5208', 0.000000))
Rule('RXN_15891',
	prot(name = 'ENTF_PANT', loc = 'cyt') +
	met(name = '_23DHB_EntB', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Seryl_EntF', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'ENTF_PANT', loc = 'cyt') +
	met(name = 'Holo_EntB', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DHB_Seryl_EntF', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_15891', 1.000000), 
	Parameter('rvs_RXN_15891', 0.000000))
Rule('ENTG_RXN',
	prot(name = 'ENTF_PANT', loc = 'cyt') +
	met(name = 'DHB_Seryl_EntF', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'ENTF_PANT', loc = 'cyt') +
	met(name = 'ENTEROBACTIN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Holo_EntF', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ENTG_RXN', 1.000000), 
	Parameter('rvs_ENTG_RXN', 0.000000))
Rule('RXN_19474',
	prot(name = 'ENTF_PANT', loc = 'cyt') +
	met(name = 'SER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Holo_EntF', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'ENTF_PANT', loc = 'cyt') +
	met(name = 'Seryl_EntF', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_19474', 1.000000), 
	Parameter('rvs_RXN_19474', 0.000000))
Rule('ENTMULTI_RXN',
	cplx(name = 'ENTMULTI_CPLX', loc = 'cyt') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_3_DIHYDROXYBENZOATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'ENTMULTI_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ENTEROBACTIN', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ENTMULTI_RXN', 1.000000), 
	Parameter('rvs_ENTMULTI_RXN', 0.000000))
Rule('ERYTH4PDEHYDROG_RXN',
	cplx(name = 'ERYTH4PDEHYDROG_CPLX', loc = 'cyt') +
	met(name = 'ERYTHROSE_4P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ERYTH4PDEHYDROG_CPLX', loc = 'cyt') +
	met(name = 'ERYTHRONATE_4P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ERYTH4PDEHYDROG_RXN', 1.000000), 
	Parameter('rvs_ERYTH4PDEHYDROG_RXN', 0.000000))
Rule('ETHAMLY_RXN',
	cplx(name = 'ETHAMLY_CPLX', loc = 'cyt') +
	met(name = 'ETHANOL_AMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'ETHAMLY_CPLX', loc = 'cyt') +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETALD', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ETHAMLY_RXN', 1.000000), 
	Parameter('rvs_ETHAMLY_RXN', 0.000000))
Rule('RXN_9655',
	cplx(name = 'FABA_CPLX', loc = 'cyt') +
	met(name = 'Beta_hydroxydecanoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'FABA_CPLX', loc = 'cyt') +
	met(name = 'Trans_D2_decenoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_9655', 1.000000), 
	Parameter('rvs_RXN_9655', 0.000000))
Rule('_3_HYDROXYDECANOYL_ACP_DEHYDR_RXN',
	cplx(name = 'FABA_CPLX', loc = 'cyt') +
	met(name = 'OH_ACYL_ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'FABA_CPLX', loc = 'cyt') +
	met(name = 'TRANS_D2_ENOYL_ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3_HYDROXYDECANOYL_ACP_DEHYDR_RXN', 1.000000), 
	Parameter('rvs__3_HYDROXYDECANOYL_ACP_DEHYDR_RXN', 0.000000))
Rule('_5dot3dot3dot14_RXN',
	cplx(name = 'FABA_CPLX', loc = 'cyt') +
	met(name = 'Trans_D2_decenoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'FABA_CPLX', loc = 'cyt') +
	met(name = 'Cis_delta_3_decenoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__5dot3dot3dot14_RXN', 1.000000), 
	Parameter('rvs__5dot3dot3dot14_RXN', 1.000000))
Rule('_2dot3dot1dot41_RXN',
	cplx(name = 'FABB_CPLX', loc = 'cyt') +
	met(name = 'ACYL_ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MALONYL_ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'FABB_CPLX', loc = 'cyt') +
	met(name = 'B_KETOACYL_ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__2dot3dot1dot41_RXN', 1.000000), 
	Parameter('rvs__2dot3dot1dot41_RXN', 0.000000))
Rule('RXN_11479',
	cplx(name = 'FABB_CPLX', loc = 'cyt') +
	met(name = 'Glutaryl_ACP_methyl_esters', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MALONYL_ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'FABB_CPLX', loc = 'cyt') +
	met(name = '_3_Ketopimeloyl_ACP_methyl_esters', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11479', 1.000000), 
	Parameter('rvs_RXN_11479', 0.000000))
Rule('RXN_10654',
	cplx(name = 'FABB_CPLX', loc = 'cyt') +
	met(name = 'Cis_Delta5_dodecenoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MALONYL_ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'FABB_CPLX', loc = 'cyt') +
	met(name = '_3_oxo_cis_D7_tetradecenoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_10654', 1.000000), 
	Parameter('rvs_RXN_10654', 0.000000))
Rule('RXN_10658',
	cplx(name = 'FABB_CPLX', loc = 'cyt') +
	met(name = 'Cis_Delta7_tetradecenoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MALONYL_ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'FABB_CPLX', loc = 'cyt') +
	met(name = '_3_oxo_cis_D9_hexadecenoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_10658', 1.000000), 
	Parameter('rvs_RXN_10658', 0.000000))
Rule('RXN_9527',
	cplx(name = 'FABB_CPLX', loc = 'cyt') +
	met(name = 'Octanoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MALONYL_ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'FABB_CPLX', loc = 'cyt') +
	met(name = '_3_oxo_decanoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_9527', 1.000000), 
	Parameter('rvs_RXN_9527', 0.000000))
Rule('RXN_9531',
	cplx(name = 'FABB_CPLX', loc = 'cyt') +
	met(name = 'Decanoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MALONYL_ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'FABB_CPLX', loc = 'cyt') +
	met(name = '_3_oxo_dodecanoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_9531', 1.000000), 
	Parameter('rvs_RXN_9531', 0.000000))
Rule('RXN_9535',
	cplx(name = 'FABB_CPLX', loc = 'cyt') +
	met(name = 'Dodecanoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MALONYL_ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'FABB_CPLX', loc = 'cyt') +
	met(name = '_3_oxo_myristoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_9535', 1.000000), 
	Parameter('rvs_RXN_9535', 0.000000))
Rule('RXN_9539',
	cplx(name = 'FABB_CPLX', loc = 'cyt') +
	met(name = 'Myristoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MALONYL_ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'FABB_CPLX', loc = 'cyt') +
	met(name = '_3_oxo_palmitoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_9539', 1.000000), 
	Parameter('rvs_RXN_9539', 0.000000))
Rule('RXN_9516',
	cplx(name = 'FABB_CPLX', loc = 'cyt') +
	met(name = 'Butanoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MALONYL_ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'FABB_CPLX', loc = 'cyt') +
	met(name = '_3_oxo_hexanoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_9516', 1.000000), 
	Parameter('rvs_RXN_9516', 0.000000))
Rule('RXN_9523',
	cplx(name = 'FABB_CPLX', loc = 'cyt') +
	met(name = 'Hexanoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MALONYL_ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'FABB_CPLX', loc = 'cyt') +
	met(name = '_3_Oxo_octanoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_9523', 1.000000), 
	Parameter('rvs_RXN_9523', 0.000000))
Rule('RXN0_2141',
	cplx(name = 'FABB_CPLX', loc = 'cyt') +
	met(name = 'Cis_delta_3_decenoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MALONYL_ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'FABB_CPLX', loc = 'cyt') +
	met(name = 'b_Keto_cis_D5_dodecenoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_2141', 1.000000), 
	Parameter('rvs_RXN0_2141', 0.000000))
Rule('MALONYL_ACPDECARBOX_RXN',
	cplx(name = 'FABB_CPLX', loc = 'cyt') +
	met(name = 'MALONYL_ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'FABB_CPLX', loc = 'cyt') +
	met(name = 'ACETYL_ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_MALONYL_ACPDECARBOX_RXN', 1.000000), 
	Parameter('rvs_MALONYL_ACPDECARBOX_RXN', 0.000000))
Rule('_4dot2dot1dot61_RXN',
	cplx(name = 'FABZ_CPLX', loc = 'cyt') +
	met(name = 'R_3_Hydroxypalmitoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'FABZ_CPLX', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_Hexadecenoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__4dot2dot1dot61_RXN', 1.000000), 
	Parameter('rvs__4dot2dot1dot61_RXN', 0.000000))
Rule('_4dot2dot1dot59_RXN',
	cplx(name = 'FABZ_CPLX', loc = 'cyt') +
	met(name = '_3_Hydroxy_octanoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'FABZ_CPLX', loc = 'cyt') +
	met(name = '_2_Octenoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__4dot2dot1dot59_RXN', 1.000000), 
	Parameter('rvs__4dot2dot1dot59_RXN', 0.000000))
Rule('_4dot2dot1dot58_RXN',
	cplx(name = 'FABZ_CPLX', loc = 'cyt') +
	met(name = 'Beta_3_hydroxybutyryl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'FABZ_CPLX', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Crotonyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__4dot2dot1dot58_RXN', 1.000000), 
	Parameter('rvs__4dot2dot1dot58_RXN', 0.000000))
Rule('RXN_9537',
	cplx(name = 'FABZ_CPLX', loc = 'cyt') +
	met(name = 'R_3_hydroxymyristoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'FABZ_CPLX', loc = 'cyt') +
	met(name = 'Tetradec_2_enoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_9537', 1.000000), 
	Parameter('rvs_RXN_9537', 0.000000))
Rule('RXN_9520',
	cplx(name = 'FABZ_CPLX', loc = 'cyt') +
	met(name = 'R_3_hydroxyhexanoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'FABZ_CPLX', loc = 'cyt') +
	met(name = 'Hex_2_enoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_9520', 1.000000), 
	Parameter('rvs_RXN_9520', 0.000000))
Rule('RXN_9533',
	cplx(name = 'FABZ_CPLX', loc = 'cyt') +
	met(name = 'R_3_hydroxydodecanoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'FABZ_CPLX', loc = 'cyt') +
	met(name = 'Dodec_2_enoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_9533', 1.000000), 
	Parameter('rvs_RXN_9533', 0.000000))
Rule('RXN_9557',
	cplx(name = 'FABZ_CPLX', loc = 'cyt') +
	met(name = 'R_3_hydroxy_cis_vaccenoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'FABZ_CPLX', loc = 'cyt') +
	met(name = 'cis_vaccen_2_enoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_9557', 1.000000), 
	Parameter('rvs_RXN_9557', 0.000000))
Rule('RXN_11477',
	cplx(name = 'FABZ_CPLX', loc = 'cyt') +
	met(name = '_3_Hydroxyglutaryl_ACP_methyl_ester', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'FABZ_CPLX', loc = 'cyt') +
	met(name = 'Enoylglutaryl_ACP_methyl_esters', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11477', 1.000000), 
	Parameter('rvs_RXN_11477', 0.000000))
Rule('RXN_11481',
	cplx(name = 'FABZ_CPLX', loc = 'cyt') +
	met(name = '_3_hydroxypimeloyl_ACP_methyl_esters', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'FABZ_CPLX', loc = 'cyt') +
	met(name = 'Enoylpimeloyl_ACP_methyl_esters', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11481', 1.000000), 
	Parameter('rvs_RXN_11481', 0.000000))
Rule('RXN_10656',
	cplx(name = 'FABZ_CPLX', loc = 'cyt') +
	met(name = '_3_hydroxy_cis_D7_tetraecenoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'FABZ_CPLX', loc = 'cyt') +
	met(name = 'Trans_D2_cis_D7_tetradecenoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_10656', 1.000000), 
	Parameter('rvs_RXN_10656', 0.000000))
Rule('RXN_10660',
	cplx(name = 'FABZ_CPLX', loc = 'cyt') +
	met(name = '_3_hydroxy_cis_D9_hexaecenoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'FABZ_CPLX', loc = 'cyt') +
	met(name = 'Trans_D3_cis_D9_hexadecenoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_10660', 1.000000), 
	Parameter('rvs_RXN_10660', 0.000000))
Rule('RXN0_2144',
	cplx(name = 'FABZ_CPLX', loc = 'cyt') +
	met(name = 'b_Hydroxy_cis_D5_dodecenoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'FABZ_CPLX', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Trans_D3_cis_D5_dodecenoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_2144', 1.000000), 
	Parameter('rvs_RXN0_2144', 0.000000))
Rule('KETOACYLCOATHIOL_RXN',
	cplx(name = 'FADA_CPLX', loc = 'cyt') +
	met(name = 'Saturated_Fatty_Acyl_CoA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'FADA_CPLX', loc = 'cyt') +
	met(name = '_3_KETOACYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_KETOACYLCOATHIOL_RXN', 0.000000), 
	Parameter('rvs_KETOACYLCOATHIOL_RXN', 1.000000))
Rule('RXN_17778',
	cplx(name = 'FADA_CPLX', loc = 'cyt') +
	met(name = 'CPD_19144', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'FADA_CPLX', loc = 'cyt') +
	met(name = 'CPD_19169', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17778', 0.000000), 
	Parameter('rvs_RXN_17778', 1.000000))
Rule('RXN_17782',
	cplx(name = 'FADA_CPLX', loc = 'cyt') +
	met(name = 'CPD_15436', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'FADA_CPLX', loc = 'cyt') +
	met(name = 'CPD_19167', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17782', 0.000000), 
	Parameter('rvs_RXN_17782', 1.000000))
Rule('RXN_17787',
	cplx(name = 'FADA_CPLX', loc = 'cyt') +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_10269', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'FADA_CPLX', loc = 'cyt') +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_19160', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17787', 0.000000), 
	Parameter('rvs_RXN_17787', 1.000000))
Rule('RXN_17791',
	cplx(name = 'FADA_CPLX', loc = 'cyt') +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_19147', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'FADA_CPLX', loc = 'cyt') +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_19158', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17791', 0.000000), 
	Parameter('rvs_RXN_17791', 1.000000))
Rule('RXN_17795',
	cplx(name = 'FADA_CPLX', loc = 'cyt') +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_19148', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'FADA_CPLX', loc = 'cyt') +
	met(name = 'CPD_19157', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17795', 0.000000), 
	Parameter('rvs_RXN_17795', 1.000000))
Rule('RXN_17799',
	cplx(name = 'FADA_CPLX', loc = 'cyt') +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_14925', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'FADA_CPLX', loc = 'cyt') +
	met(name = 'CPD_19153', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17799', 0.000000), 
	Parameter('rvs_RXN_17799', 1.000000))
Rule('RXN_14394',
	cplx(name = 'FADA_CPLX', loc = 'cyt') +
	met(name = 'CPD_7221', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'FADA_CPLX', loc = 'cyt') +
	met(name = 'CPD_15244', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14394', 0.000000), 
	Parameter('rvs_RXN_14394', 1.000000))
Rule('OHACYL_COA_DEHYDROG_RXN',
	cplx(name = 'FADB_CPLX', loc = 'cyt') +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_3_HYDROXYACYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'FADB_CPLX', loc = 'cyt') +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_3_KETOACYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_OHACYL_COA_DEHYDROG_RXN', 1.000000), 
	Parameter('rvs_OHACYL_COA_DEHYDROG_RXN', 0.000000))
Rule('RXN_17777',
	cplx(name = 'FADB_CPLX', loc = 'cyt') +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_19171', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'FADB_CPLX', loc = 'cyt') +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_19169', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17777', 1.000000), 
	Parameter('rvs_RXN_17777', 0.000000))
Rule('RXN_17781',
	cplx(name = 'FADB_CPLX', loc = 'cyt') +
	met(name = 'CPD_19167', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'FADB_CPLX', loc = 'cyt') +
	met(name = 'CPD_19168', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_17781', 0.000000), 
	Parameter('rvs_RXN_17781', 1.000000))
Rule('RXN_14393',
	cplx(name = 'FADB_CPLX', loc = 'cyt') +
	met(name = 'CPD0_1163', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'FADB_CPLX', loc = 'cyt') +
	met(name = 'CPD_15244', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14393', 1.000000), 
	Parameter('rvs_RXN_14393', 1.000000))
Rule('RXN_17786',
	cplx(name = 'FADB_CPLX', loc = 'cyt') +
	met(name = 'CPD_19160', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'FADB_CPLX', loc = 'cyt') +
	met(name = 'CPD_19159', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_17786', 0.000000), 
	Parameter('rvs_RXN_17786', 1.000000))
Rule('RXN_17790',
	cplx(name = 'FADB_CPLX', loc = 'cyt') +
	met(name = 'CPD_19158', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'FADB_CPLX', loc = 'cyt') +
	met(name = 'CPD_19155', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_17790', 0.000000), 
	Parameter('rvs_RXN_17790', 1.000000))
Rule('RXN_17794',
	cplx(name = 'FADB_CPLX', loc = 'cyt') +
	met(name = 'CPD_19157', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'FADB_CPLX', loc = 'cyt') +
	met(name = 'CPD_19154', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_17794', 0.000000), 
	Parameter('rvs_RXN_17794', 1.000000))
Rule('RXN_17798',
	cplx(name = 'FADB_CPLX', loc = 'cyt') +
	met(name = 'CPD_19153', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'FADB_CPLX', loc = 'cyt') +
	met(name = 'CPD_19151', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_17798', 0.000000), 
	Parameter('rvs_RXN_17798', 1.000000))
Rule('FGAMSYN_RXN',
	prot(name = 'FGAMSYN_MONOMER', loc = 'cyt') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_5_P_RIBOSYL_N_FORMYLGLYCINEAMIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'FGAMSYN_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_5_PHOSPHORIBOSYL_N_FORMYLGLYCINEAMIDINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_FGAMSYN_RXN', 1.000000), 
	Parameter('rvs_FGAMSYN_RXN', 0.000000))
Rule('FHLMULTI_RXN',
	cplx(name = 'FHLMULTI_CPLX', loc = 'per') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FORMATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'FHLMULTI_CPLX', loc = 'per') +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HYDROGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_FHLMULTI_RXN', 1.000000), 
	Parameter('rvs_FHLMULTI_RXN', 0.000000))
Rule('FLAVONADPREDUCT_RXN',
	prot(name = 'FLAVONADPREDUCT_MONOMER', loc = 'cyt') +
	met(name = 'Reduced_flavodoxins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'FLAVONADPREDUCT_MONOMER', loc = 'cyt') +
	met(name = 'Oxidized_flavodoxins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_FLAVONADPREDUCT_RXN', 1.000000), 
	Parameter('rvs_FLAVONADPREDUCT_RXN', 1.000000))
Rule('RXN_17897',
	prot(name = 'FLAVONADPREDUCT_MONOMER', loc = 'cyt') +
	met(name = 'Reduced_ferredoxins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'FLAVONADPREDUCT_MONOMER', loc = 'cyt') +
	met(name = 'Oxidized_ferredoxins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_17897', 1.000000), 
	Parameter('rvs_RXN_17897', 1.000000))
Rule('RXN_12445',
	prot(name = 'FMNREDUCT_MONOMER', loc = 'cyt') +
	met(name = 'CPD_316', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'FMNREDUCT_MONOMER', loc = 'cyt') +
	met(name = 'RIBOFLAVIN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_12445', 0.000000), 
	Parameter('rvs_RXN_12445', 1.000000))
Rule('FMNREDUCT_RXN',
	prot(name = 'FMNREDUCT_MONOMER', loc = 'cyt') +
	met(name = 'NAD_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FMNH2', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'FMNREDUCT_MONOMER', loc = 'cyt') +
	met(name = 'NADH_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FMN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_FMNREDUCT_RXN', 0.000000), 
	Parameter('rvs_FMNREDUCT_RXN', 1.000000))
Rule('RXN_8506',
	prot(name = 'FMNREDUCT_MONOMER', loc = 'cyt') +
	met(name = 'FADH2', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'FMNREDUCT_MONOMER', loc = 'cyt') +
	met(name = 'FAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_8506', 0.000000), 
	Parameter('rvs_RXN_8506', 1.000000))
Rule('RXN0_2921',
	prot(name = 'FOLC_MONOMER', loc = 'cyt') +
	met(name = 'METHYLENE_THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'FOLC_MONOMER', loc = 'cyt') +
	met(name = 'METHYLENE_THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_2921', 1.000000), 
	Parameter('rvs_RXN0_2921', 0.000000))
Rule('FORMYLTHFGLUSYNTH_RXN',
	prot(name = 'FOLC_MONOMER', loc = 'cyt') +
	met(name = 'FORMYL_THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'FOLC_MONOMER', loc = 'cyt') +
	met(name = 'FORMYL_THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_FORMYLTHFGLUSYNTH_RXN', 1.000000), 
	Parameter('rvs_FORMYLTHFGLUSYNTH_RXN', 0.000000))
Rule('FOLYLPOLYGLUTAMATESYNTH_RXN',
	prot(name = 'FOLC_MONOMER', loc = 'cyt') +
	met(name = 'THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'FOLC_MONOMER', loc = 'cyt') +
	met(name = 'THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_FOLYLPOLYGLUTAMATESYNTH_RXN', 1.000000), 
	Parameter('rvs_FOLYLPOLYGLUTAMATESYNTH_RXN', 0.000000))
Rule('DIHYDROFOLATESYNTH_RXN',
	prot(name = 'FOLC_MONOMER', loc = 'cyt') +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_7_8_DIHYDROPTEROATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'FOLC_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DIHYDROFOLATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DIHYDROFOLATESYNTH_RXN', 1.000000), 
	Parameter('rvs_DIHYDROFOLATESYNTH_RXN', 0.000000))
Rule('METHENYLTHFCYCLOHYDRO_RXN',
	cplx(name = 'FOLD_CPLX', loc = 'cyt') +
	met(name = '_5_10_METHENYL_THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'FOLD_CPLX', loc = 'cyt') +
	met(name = 'FORMYL_THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_METHENYLTHFCYCLOHYDRO_RXN', 1.000000), 
	Parameter('rvs_METHENYLTHFCYCLOHYDRO_RXN', 1.000000))
Rule('METHYLENETHFDEHYDROG_NADP_RXN',
	cplx(name = 'FOLD_CPLX', loc = 'cyt') +
	met(name = 'METHYLENE_THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'FOLD_CPLX', loc = 'cyt') +
	met(name = '_5_10_METHENYL_THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_METHYLENETHFDEHYDROG_NADP_RXN', 1.000000), 
	Parameter('rvs_METHYLENETHFDEHYDROG_NADP_RXN', 1.000000))
Rule('GTP_CYCLOHYDRO_I_RXN',
	cplx(name = 'FOLE_CPLX', loc = 'cyt') +
	met(name = 'GTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'FOLE_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FORMATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DIHYDRONEOPTERIN_P3', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GTP_CYCLOHYDRO_I_RXN', 1.000000), 
	Parameter('rvs_GTP_CYCLOHYDRO_I_RXN', 0.000000))
Rule('H2NTPEPIM_RXN',
	cplx(name = 'FOLXTET_CPLX', loc = 'cyt') +
	met(name = 'DIHYDRONEOPTERIN_P3', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'FOLXTET_CPLX', loc = 'cyt') +
	met(name = 'DIHYDROMONAPTERIN_TRIPHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_H2NTPEPIM_RXN', 1.000000), 
	Parameter('rvs_H2NTPEPIM_RXN', 1.000000))
Rule('RXN_12274',
	prot(name = 'FORMATEDEHYDROGH_MONOMER', loc = 'per') +
	met(name = 'FORMATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Oxidized_hydrogenase_3', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'FORMATEDEHYDROGH_MONOMER', loc = 'per') +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Reduced_hydrogenase_3', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_12274', 1.000000), 
	Parameter('rvs_RXN_12274', 0.000000))
Rule('RXN0_3281',
	prot(name = 'FORMATEDEHYDROGH_MONOMER', loc = 'per') +
	met(name = 'FORMATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Acceptor', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'FORMATEDEHYDROGH_MONOMER', loc = 'per') +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Donor_H2', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_3281', 1.000000), 
	Parameter('rvs_RXN0_3281', 0.000000))
Rule('FORMATEDEHYDROG_RXN',
	cplx(name = 'FORMATEDEHYDROGN_CPLX', loc = 'imem') +
	met(name = 'FORMATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Menaquinones', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'FORMATEDEHYDROGN_CPLX', loc = 'imem') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Menaquinols', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_FORMATEDEHYDROG_RXN', 1.000000), 
	Parameter('rvs_FORMATEDEHYDROG_RXN', 0.000000))
Rule('FORMYLTHFDEFORMYL_RXN',
	cplx(name = 'FORMYLTHFDEFORMYL_CPLX', loc = 'cyt') +
	met(name = 'FORMYL_THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'FORMYLTHFDEFORMYL_CPLX', loc = 'cyt') +
	met(name = 'THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FORMATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_FORMYLTHFDEFORMYL_RXN', 1.000000), 
	Parameter('rvs_FORMYLTHFDEFORMYL_RXN', 0.000000))
Rule('GPPSYN_RXN',
	prot(name = 'FPPSYN_MONOMER', loc = 'cyt') +
	met(name = 'CPD_4211', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DELTA3_ISOPENTENYL_PP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'FPPSYN_MONOMER', loc = 'cyt') +
	met(name = 'GERANYL_PP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GPPSYN_RXN', 1.000000), 
	Parameter('rvs_GPPSYN_RXN', 0.000000))
Rule('FPPSYN_RXN',
	prot(name = 'FPPSYN_MONOMER', loc = 'cyt') +
	met(name = 'GERANYL_PP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DELTA3_ISOPENTENYL_PP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'FPPSYN_MONOMER', loc = 'cyt') +
	met(name = 'FARNESYL_PP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_FPPSYN_RXN', 1.000000), 
	Parameter('rvs_FPPSYN_RXN', 0.000000))
Rule('F16ALDOLASE_RXN',
	prot(name = 'FRUCBISALD_CLASSII', loc = 'imem') +
	met(name = 'FRUCTOSE_16_DIPHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'FRUCBISALD_CLASSII', loc = 'imem') +
	met(name = 'DIHYDROXY_ACETONE_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GAP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_F16ALDOLASE_RXN', 1.000000), 
	Parameter('rvs_F16ALDOLASE_RXN', 1.000000))
Rule('SEDOBISALDOL_RXN',
	prot(name = 'FRUCBISALD_CLASSII', loc = 'imem') +
	met(name = 'DIHYDROXY_ACETONE_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ERYTHROSE_4P', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'FRUCBISALD_CLASSII', loc = 'imem') +
	met(name = 'D_SEDOHEPTULOSE_1_7_P2', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_SEDOBISALDOL_RXN', 0.000000), 
	Parameter('rvs_SEDOBISALDOL_RXN', 1.000000))
Rule('FUCULOKIN_RXN',
	prot(name = 'FUCULOKIN_MONOMER', loc = 'cyt') +
	met(name = 'L_FUCULOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'FUCULOKIN_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FUCULOSE_1P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_FUCULOKIN_RXN', 1.000000), 
	Parameter('rvs_FUCULOKIN_RXN', 0.000000))
Rule('DARABKIN_RXN',
	prot(name = 'FUCULOKIN_MONOMER', loc = 'cyt') +
	met(name = 'D_RIBULOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'FUCULOKIN_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_RIBULOSE_1_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DARABKIN_RXN', 1.000000), 
	Parameter('rvs_DARABKIN_RXN', 0.000000))
Rule('OXALOACETATE_TAUTOMERASE_RXN',
	prot(name = 'FUMARASE_A', loc = 'cyt') +
	met(name = 'OXALACETIC_ACID', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'FUMARASE_A', loc = 'cyt') +
	met(name = 'ENOL_OXALOACETATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_OXALOACETATE_TAUTOMERASE_RXN', 0.000000), 
	Parameter('rvs_OXALOACETATE_TAUTOMERASE_RXN', 1.000000))
Rule('D__TARTRATE_DEHYDRATASE_RXN',
	prot(name = 'FUMARASE_B', loc = 'cyt') +
	met(name = 'D_TARTRATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'FUMARASE_B', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXALACETIC_ACID', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_D__TARTRATE_DEHYDRATASE_RXN', 1.000000), 
	Parameter('rvs_D__TARTRATE_DEHYDRATASE_RXN', 1.000000))
Rule('R601_RXN',
	prot(name = 'FUMARATE_REDUCTASE', loc = 'imem') +
	met(name = 'Menaquinols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FUM', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'FUMARATE_REDUCTASE', loc = 'imem') +
	met(name = 'Menaquinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SUC', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_R601_RXN', 1.000000), 
	Parameter('rvs_R601_RXN', 1.000000))
Rule('RXN0_6994',
	prot(name = 'G495_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_2499', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G495_MONOMER', loc = 'cyt') +
	met(name = 'GLC_6_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'METOH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6994', 1.000000), 
	Parameter('rvs_RXN0_6994', 0.000000))
Rule('RXN_1961',
	prot(name = 'G6096_MONOMER', loc = 'cyt') +
	met(name = 'Cytidine_34_tRNAIle2', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'LYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G6096_MONOMER', loc = 'cyt') +
	met(name = 'Lysidine_tRNA_Ile2', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_1961', 1.000000), 
	Parameter('rvs_RXN_1961', 0.000000))
Rule('RXN_13072',
	prot(name = 'G6103_MONOMER', loc = 'cyt') +
	met(name = '_2_KETO_GLUTARAMATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6103_MONOMER', loc = 'cyt') +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_13072', 1.000000), 
	Parameter('rvs_RXN_13072', 0.000000))
Rule('RXN0_5131',
	prot(name = 'G6131_MONOMER', loc = 'cyt') +
	met(name = 'IS30_Insertion_Sequences', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6131_MONOMER', loc = 'cyt') +
	met(name = 'IS30_with_Integrated_Transposon', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5131', 1.000000), 
	Parameter('rvs_RXN0_5131', 0.000000))
Rule('XYLONATE_DEHYDRATASE_RXN',
	prot(name = 'G6141_MONOMER', loc = 'cyt') +
	met(name = 'D_XYLONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G6141_MONOMER', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_DH_3_DO_D_ARABINONATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_XYLONATE_DEHYDRATASE_RXN', 1.000000), 
	Parameter('rvs_XYLONATE_DEHYDRATASE_RXN', 0.000000))
Rule('RXN_15744',
	prot(name = 'G6190_MONOMER', loc = 'cyt') +
	met(name = 'PROPANE_1_2_DIOL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G6190_MONOMER', loc = 'cyt') +
	met(name = 'LACTALD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_15744', 0.000000), 
	Parameter('rvs_RXN_15744', 1.000000))
Rule('RXN_15743',
	prot(name = 'G6190_MONOMER', loc = 'cyt') +
	met(name = 'CPD_8891', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G6190_MONOMER', loc = 'cyt') +
	met(name = 'CPD_358', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_15743', 0.000000), 
	Parameter('rvs_RXN_15743', 1.000000))
Rule('_2_METHYLCITRATE_DEHYDRATASE_RXN',
	prot(name = 'G6199_MONOMER', loc = 'cyt') +
	met(name = 'CPD_622', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G6199_MONOMER', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_1136', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__2_METHYLCITRATE_DEHYDRATASE_RXN', 1.000000), 
	Parameter('rvs__2_METHYLCITRATE_DEHYDRATASE_RXN', 0.000000))
Rule('RXN0_7141',
	prot(name = 'G6236_MONOMER', loc = 'cyt') +
	met(name = 'DEOXYXYLULOSE_5P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6236_MONOMER', loc = 'cyt') +
	met(name = 'RIBULOSE_5P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7141', 0.000000), 
	Parameter('rvs_RXN0_7141', 1.000000))
Rule('RXN0_5390',
	prot(name = 'G6244_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_1158', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G6244_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_1159', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5390', 1.000000), 
	Parameter('rvs_RXN0_5390', 0.000000))
Rule('RXN_12093',
	prot(name = 'G6245_MONOMER', loc = 'cyt') +
	met(name = 'CPD_13043', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	prot(name = 'G6245_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_7_CYANO_7_DEAZAGUANINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_12093', 1.000000), 
	Parameter('rvs_RXN_12093', 0.000000))
Rule('RXN0_3543',
	prot(name = 'G6246_MONOMER', loc = 'cyt') +
	met(name = 'AMINO_HYDROXYMETHYL_METHYLPYRIMIDINE_PP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G6246_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMINO_HYDROXYMETHYL_METHYL_PYR_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_3543', 1.000000), 
	Parameter('rvs_RXN0_3543', 0.000000))
Rule('UREIDOGLYCOLATE_LYASE_RXN',
	prot(name = 'G6275_MONOMER', loc = 'cyt') +
	met(name = 'CPD_1091', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G6275_MONOMER', loc = 'cyt') +
	met(name = 'UREA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLYOX', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_UREIDOGLYCOLATE_LYASE_RXN', 1.000000), 
	Parameter('rvs_UREIDOGLYCOLATE_LYASE_RXN', 0.000000))
Rule('URUR_RXN',
	prot(name = 'G6284_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_2298', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6284_MONOMER', loc = 'cyt') +
	met(name = 'CPD_1091', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_URUR_RXN', 1.000000), 
	Parameter('rvs_URUR_RXN', 0.000000))
Rule('_3dot2dot1dot17_RXN',
	prot(name = 'G6310_MONOMER', loc = 'cyt') +
	met(name = 'Peptidoglycans', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6310_MONOMER', loc = 'cyt') +
	met(name = 'NAcMur_Peptide_Undecaprenols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'N_acetyl_D_glucosamine', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3dot2dot1dot17_RXN', 1.000000), 
	Parameter('rvs__3dot2dot1dot17_RXN', 0.000000))
Rule('R15_RXN',
	prot(name = 'G6329_MONOMER', loc = 'cyt') +
	met(name = 'MET', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_Oxo_carboxylates', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6329_MONOMER', loc = 'cyt') +
	met(name = 'CPD_479', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Amino_Acids_20', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_R15_RXN', 1.000000), 
	Parameter('rvs_R15_RXN', 0.000000))
Rule('_2dot7dot8dot25_RXN',
	prot(name = 'G6339_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DEPHOSPHO_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6339_MONOMER', loc = 'cyt') +
	met(name = '_2_5_TRIPHOSPHORIBOSYL_3_DEPHOSPHO_', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd__2dot7dot8dot25_RXN', 1.000000), 
	Parameter('rvs__2dot7dot8dot25_RXN', 0.000000))
Rule('_2dot7dot7dot61_RXN',
	prot(name = 'G6340_MONOMER', loc = 'cyt') +
	met(name = '_2_5_TRIPHOSPHORIBOSYL_3_DEPHOSPHO_', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'APO_CITRATE_LYASE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G6340_MONOMER', loc = 'cyt') +
	met(name = 'HOLO_CITRATE_LYASE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__2dot7dot7dot61_RXN', 1.000000), 
	Parameter('rvs__2dot7dot7dot61_RXN', 0.000000))
Rule('RXN0_5063',
	prot(name = 'G6364_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_6_Dimethylallyladenosine37_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Sulfurated_Sulfur_Acceptors', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Donor_H2', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None +
	None | 
	prot(name = 'G6364_MONOMER', loc = 'cyt') +
	met(name = 'CPD_11592', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Unsulfurated_Sulfur_Acceptors', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CH33ADO', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MET', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Acceptor', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5063', 1.000000), 
	Parameter('rvs_RXN0_5063', 0.000000))
Rule('RXN0_7272',
	prot(name = 'G6406_MONOMER', loc = 'cyt') +
	met(name = 'L_1_PHOSPHATIDYL_ETHANOLAMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLYCEROL', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6406_MONOMER', loc = 'cyt') +
	met(name = 'L_1_PHOSPHATIDYL_GLYCEROL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ETHANOL_AMINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7272', 1.000000), 
	Parameter('rvs_RXN0_7272', 0.000000))
Rule('RXN_11596',
	prot(name = 'G6416_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_23S_rRNA_adenine_1618', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G6416_MONOMER', loc = 'cyt') +
	met(name = '_23S_rRNA_N6_m_adenine1618', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11596', 1.000000), 
	Parameter('rvs_RXN_11596', 0.000000))
Rule('RXN_15210',
	prot(name = 'G6418_MONOMER', loc = 'imem') +
	met(name = 'CPD_16398', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_1_PHOSPHATIDYL_ETHANOLAMINE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6418_MONOMER', loc = 'imem') +
	met(name = 'CPD_16401', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DIACYLGLYCEROL', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_15210', 1.000000), 
	Parameter('rvs_RXN_15210', 0.000000))
Rule('RXN0_5401',
	prot(name = 'G6422_MONOMER', loc = 'per') +
	met(name = 'EG10544_MONOMER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_17931', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6422_MONOMER', loc = 'per') +
	met(name = 'CPD0_1171', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_ALANINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5401', 1.000000), 
	Parameter('rvs_RXN0_5401', 0.000000))
Rule('RXN0_6366',
	prot(name = 'G6435_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Ribosomal_protein_S12_Asp89', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Sulfurated_Sulfur_Acceptors', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Donor_H2', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None +
	None | 
	prot(name = 'G6435_MONOMER', loc = 'cyt') +
	met(name = 'Ribosomal_protein_S12_3_methylthio_Asp89', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Unsulfurated_Sulfur_Acceptors', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MET', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CH33ADO', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Acceptor', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6366', 1.000000), 
	Parameter('rvs_RXN0_6366', 0.000000))
Rule('RXN0_6371',
	prot(name = 'G6437_MONOMER', loc = 'omem') +
	met(name = 'Aldoses', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Acceptor', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6437_MONOMER', loc = 'omem') +
	met(name = 'Aldonic_Acids', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Donor_H2', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6371', 1.000000), 
	Parameter('rvs_RXN0_6371', 0.000000))
Rule('RXN0_6549',
	prot(name = 'G6438_MONOMER', loc = 'cyt') +
	met(name = 'BROMOACETATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLUTATHIONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G6438_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_2370', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'BR_', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6549', 1.000000), 
	Parameter('rvs_RXN0_6549', 0.000000))
Rule('RXN_11600',
	prot(name = 'G6449_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_23S_rRNA_uracil_747', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G6449_MONOMER', loc = 'cyt') +
	met(name = '_23S_rRNA_5_methyluracil747', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11600', 1.000000), 
	Parameter('rvs_RXN_11600', 0.000000))
Rule('RXN0_307',
	prot(name = 'G6456_MONOMER', loc = 'cyt') +
	met(name = 'Red_Hybrid_Cluster_Proteins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6456_MONOMER', loc = 'cyt') +
	met(name = 'Ox_Hybrid_Cluster_Proteins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_307', 0.000000), 
	Parameter('rvs_RXN0_307', 1.000000))
Rule('HYDROXYLAMINE_REDUCTASE_RXN',
	prot(name = 'G6457_MONOMER', loc = 'cyt') +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Acceptor', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6457_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Donor_H2', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HYDROXYLAMINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_HYDROXYLAMINE_REDUCTASE_RXN', 0.000000), 
	Parameter('rvs_HYDROXYLAMINE_REDUCTASE_RXN', 1.000000))
Rule('ATP_PYROPHOSPHATASE_RXN',
	prot(name = 'G6468_MONOMER', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G6468_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ATP_PYROPHOSPHATASE_RXN', 1.000000), 
	Parameter('rvs_ATP_PYROPHOSPHATASE_RXN', 0.000000))
Rule('RXN0_6950',
	prot(name = 'G6488_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_23S_rRNA_guanine_2069', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6488_MONOMER', loc = 'cyt') +
	met(name = '_23S_rRNA_N7_methylguanine_2069', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6950', 1.000000), 
	Parameter('rvs_RXN0_6950', 0.000000))
Rule('RXN_11574',
	prot(name = 'G6488_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_23S_rRNA_guanine_2445', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G6488_MONOMER', loc = 'cyt') +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_23S_RRNA_N2_METHYLGUANINE2445', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11574', 1.000000), 
	Parameter('rvs_RXN_11574', 0.000000))
Rule('ACYLPHOSPHATASE_RXN',
	prot(name = 'G6502_MONOMER', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Acyl_Phosphates', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G6502_MONOMER', loc = 'cyt') +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Carboxylates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ACYLPHOSPHATASE_RXN', 1.000000), 
	Parameter('rvs_ACYLPHOSPHATASE_RXN', 0.000000))
Rule('PROTEIN_TYROSINE_PHOSPHATASE_RXN',
	prot(name = 'G6503_MONOMER', loc = 'cyt') +
	met(name = 'Protein_tyrosine_phosphates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6503_MONOMER', loc = 'cyt') +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Protein_Tyrosines', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PROTEIN_TYROSINE_PHOSPHATASE_RXN', 1.000000), 
	Parameter('rvs_PROTEIN_TYROSINE_PHOSPHATASE_RXN', 0.000000))
Rule('RXN0_6452',
	prot(name = 'G6520_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_2339', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6520_MONOMER', loc = 'cyt') +
	met(name = 'MALONATE_S_ALD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_6452', 1.000000), 
	Parameter('rvs_RXN0_6452', 0.000000))
Rule('RXN0_6461',
	prot(name = 'G6521_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_2340', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Donor_H2', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	prot(name = 'G6521_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_2339', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Acceptor', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6461', 1.000000), 
	Parameter('rvs_RXN0_6461', 0.000000))
Rule('RXN0_6460',
	prot(name = 'G6522_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_2338', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G6522_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBAMATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_2340', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6460', 1.000000), 
	Parameter('rvs_RXN0_6460', 0.000000))
Rule('RXN0_6451',
	prot(name = 'G6522_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_2331', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G6522_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBAMATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_2339', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6451', 1.000000), 
	Parameter('rvs_RXN0_6451', 0.000000))
Rule('RXN_12896',
	prot(name = 'G6522_MONOMER', loc = 'cyt') +
	met(name = 'CPD_13927', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G6522_MONOMER', loc = 'cyt') +
	met(name = 'CPD_13930', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBAMATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_12896', 1.000000), 
	Parameter('rvs_RXN_12896', 0.000000))
Rule('RXN0_6444',
	prot(name = 'G6523_MONOMER', loc = 'cyt') +
	met(name = 'URACIL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FMNH2', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6523_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_2338', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FMN', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6444', 1.000000), 
	Parameter('rvs_RXN0_6444', 0.000000))
Rule('RXN_12886',
	prot(name = 'G6523_MONOMER', loc = 'cyt') +
	met(name = 'THYMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FMNH2', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6523_MONOMER', loc = 'cyt') +
	met(name = 'CPD_13927', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FMN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_12886', 1.000000), 
	Parameter('rvs_RXN_12886', 0.000000))
Rule('RXN0_5414',
	prot(name = 'G6530_MONOMER', loc = 'omem') +
	met(name = 'CPD0_1192', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6530_MONOMER', loc = 'omem') +
	met(name = 'CPD0_1193', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACET', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5414', 1.000000), 
	Parameter('rvs_RXN0_5414', 0.000000))
Rule('RXN_19793',
	prot(name = 'G6530_MONOMER', loc = 'omem') +
	met(name = 'CPD_21409', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6530_MONOMER', loc = 'omem') +
	met(name = 'CPD_21406', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_21407', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_19793', 1.000000), 
	Parameter('rvs_RXN_19793', 0.000000))
Rule('RXN0_7012',
	prot(name = 'G6551_MONOMER', loc = 'mem') +
	met(name = 'L_1_PHOSPHATIDYL_GLYCEROL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_1_PHOSPHATIDYL_ETHANOLAMINE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6551_MONOMER', loc = 'mem') +
	met(name = 'CARDIOLIPIN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ETHANOL_AMINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7012', 1.000000), 
	Parameter('rvs_RXN0_7012', 0.000000))
Rule('RXN0_5226',
	prot(name = 'G6567_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_1081', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6567_MONOMER', loc = 'cyt') +
	met(name = 'N_ACETYL_D_GLUCOSAMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_882', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5226', 1.000000), 
	Parameter('rvs_RXN0_5226', 0.000000))
Rule('_3dot2dot1dot52_RXN',
	prot(name = 'G6567_MONOMER', loc = 'cyt') +
	met(name = 'N_Acetyl_beta_D_Hexosaminides', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6567_MONOMER', loc = 'cyt') +
	met(name = 'N_acetyl_beta_D_hexosamines', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Alcohols', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3dot2dot1dot52_RXN', 1.000000), 
	Parameter('rvs__3dot2dot1dot52_RXN', 0.000000))
Rule('N_ACETYLGLUCOSAMINE_KINASE_RXN',
	prot(name = 'G6576_MONOMER', loc = 'cyt') +
	met(name = 'N_acetyl_D_glucosamine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G6576_MONOMER', loc = 'cyt') +
	met(name = 'N_ACETYL_D_GLUCOSAMINE_6_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_N_ACETYLGLUCOSAMINE_KINASE_RXN', 1.000000), 
	Parameter('rvs_N_ACETYLGLUCOSAMINE_KINASE_RXN', 0.000000))
Rule('RXN0_7078',
	prot(name = 'G6577_MONOMER', loc = 'cyt') +
	met(name = 'CPD3O_0', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6577_MONOMER', loc = 'cyt') +
	met(name = 'Protein_L_lysine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_14762', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NIACINAMIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7078', 1.000000), 
	Parameter('rvs_RXN0_7078', 0.000000))
Rule('RXN0_6445',
	prot(name = 'G6577_MONOMER', loc = 'cyt') +
	met(name = 'MONOMER0_4170', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6577_MONOMER', loc = 'cyt') +
	met(name = 'CHEY_MONOMER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_14762', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NIACINAMIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6445', 1.000000), 
	Parameter('rvs_RXN0_6445', 0.000000))
Rule('GUANOSINE_DIPHOSPHATASE_RXN',
	prot(name = 'G6580_MONOMER', loc = 'cyt') +
	met(name = 'GDP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G6580_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GUANOSINE_DIPHOSPHATASE_RXN', 1.000000), 
	Parameter('rvs_GUANOSINE_DIPHOSPHATASE_RXN', 0.000000))
Rule('RXN0_3542',
	prot(name = 'G6580_MONOMER', loc = 'cyt') +
	met(name = 'THIAMINE_PYROPHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G6580_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'THIAMINE_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_3542', 1.000000), 
	Parameter('rvs_RXN0_3542', 1.000000))
Rule('RXN_11834',
	prot(name = 'G6581_MONOMER', loc = 'cyt') +
	met(name = '_23S_rRNA_uridine2457', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6581_MONOMER', loc = 'cyt') +
	met(name = '_23S_rRNA_pseudouridine2457', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11834', 1.000000), 
	Parameter('rvs_RXN_11834', 0.000000))
Rule('RXN0_5227',
	prot(name = 'G6621_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_1082', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6621_MONOMER', loc = 'cyt') +
	met(name = 'L_ALA_GAMMA_D_GLU_DAP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_ALANINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5227', 1.000000), 
	Parameter('rvs_RXN0_5227', 0.000000))
Rule('RXN0_2061',
	prot(name = 'G6621_MONOMER', loc = 'cyt') +
	met(name = 'UDP_MURNAC_TETRAPEPTIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6621_MONOMER', loc = 'cyt') +
	met(name = 'D_ALANINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UDP_AAGM_DIAMINOHEPTANEDIOATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_2061', 1.000000), 
	Parameter('rvs_RXN0_2061', 0.000000))
Rule('RXN_16009',
	prot(name = 'G6634_MONOMER', loc = 'cyt') +
	met(name = 'Nucleoside_3_5_bisphosphate', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6634_MONOMER', loc = 'cyt') +
	met(name = 'Nucleoside_Monophosphates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_16009', 1.000000), 
	Parameter('rvs_RXN_16009', 0.000000))
Rule('GABATRANSAM_RXN',
	prot(name = 'G6646_MONOMER', loc = 'cyt') +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_4_AMINO_BUTYRATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6646_MONOMER', loc = 'cyt') +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SUCC_S_ALD', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GABATRANSAM_RXN', 1.000000), 
	Parameter('rvs_GABATRANSAM_RXN', 1.000000))
Rule('RXN_18999',
	prot(name = 'G6647_MONOMER', loc = 'cyt') +
	met(name = 'CPD_9190', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6647_MONOMER', loc = 'cyt') +
	met(name = 'GLC_1_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLYCERATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_18999', 1.000000), 
	Parameter('rvs_RXN_18999', 1.000000))
Rule('_2dot4dot1dot230_RXN',
	prot(name = 'G6654_MONOMER', loc = 'wall') +
	met(name = 'CPD_16569', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6654_MONOMER', loc = 'wall') +
	met(name = 'Glucopyranose', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_448', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__2dot4dot1dot230_RXN', 1.000000), 
	Parameter('rvs__2dot4dot1dot230_RXN', 1.000000))
Rule('BETA_PHOSPHOGLUCOMUTASE_RXN',
	prot(name = 'G6655_MONOMER', loc = 'cyt') +
	met(name = 'CPD_448', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6655_MONOMER', loc = 'cyt') +
	met(name = 'GLC_6_P', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_BETA_PHOSPHOGLUCOMUTASE_RXN', 1.000000), 
	Parameter('rvs_BETA_PHOSPHOGLUCOMUTASE_RXN', 1.000000))
Rule('RXN0_5228',
	prot(name = 'G6661_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_2190', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6661_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_1445', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5228', 1.000000), 
	Parameter('rvs_RXN0_5228', 1.000000))
Rule('PYFLAVOXRE_RXN',
	prot(name = 'G6701_MONOMER', loc = 'cyt') +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Oxidized_flavodoxins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6701_MONOMER', loc = 'cyt') +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Reduced_flavodoxins', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_PYFLAVOXRE_RXN', 1.000000), 
	Parameter('rvs_PYFLAVOXRE_RXN', 1.000000))
Rule('RXNMETA_12671',
	prot(name = 'G6708_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_2363', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6708_MONOMER', loc = 'cyt') +
	met(name = 'CPDMETA_13650', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXNMETA_12671', 1.000000), 
	Parameter('rvs_RXNMETA_12671', 0.000000))
Rule('RXNMETA_12672',
	prot(name = 'G6708_MONOMER', loc = 'cyt') +
	met(name = 'CPDMETA_13650', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6708_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_2364', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXNMETA_12672', 1.000000), 
	Parameter('rvs_RXNMETA_12672', 0.000000))
Rule('_3_HYDROXBUTYRYL_COA_DEHYDRATASE_RXN',
	prot(name = 'G6708_MONOMER', loc = 'cyt') +
	met(name = 'CPD_650', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G6708_MONOMER', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CROTONYL_COA', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3_HYDROXBUTYRYL_COA_DEHYDRATASE_RXN', 1.000000), 
	Parameter('rvs__3_HYDROXBUTYRYL_COA_DEHYDRATASE_RXN', 1.000000))
Rule('RXN_2425',
	prot(name = 'G6714_MONOMER', loc = 'imem') +
	met(name = '_3_HYDROXYADIPYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G6714_MONOMER', loc = 'imem') +
	met(name = 'TRANS_23_DEHYDROADIPYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_2425', 0.000000), 
	Parameter('rvs_RXN_2425', 1.000000))
Rule('RXN0_6510',
	prot(name = 'G6715_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_2362', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6715_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_2363', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6510', 1.000000), 
	Parameter('rvs_RXN0_6510', 1.000000))
Rule('RXN0_2044',
	prot(name = 'G6716_MONOMER', loc = 'cyt') +
	met(name = '_3_HYDROXYADIPYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G6716_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_3_KETO_ADIPYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_2044', 1.000000), 
	Parameter('rvs_RXN0_2044', 1.000000))
Rule('RXN0_6512',
	prot(name = 'G6718_MONOMER', loc = 'cyt') +
	met(name = 'TRANS_23_DEHYDROADIPYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6718_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_2364', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6512', 0.000000), 
	Parameter('rvs_RXN0_6512', 1.000000))
Rule('RXN_3641',
	prot(name = 'G6718_MONOMER', loc = 'cyt') +
	met(name = 'SUC_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6718_MONOMER', loc = 'cyt') +
	met(name = '_3_KETO_ADIPYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_3641', 0.000000), 
	Parameter('rvs_RXN_3641', 1.000000))
Rule('RXN_10819',
	prot(name = 'G6719_MONOMER', loc = 'cyt') +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PHENYLACETATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6719_MONOMER', loc = 'cyt') +
	met(name = 'CPD_207', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_10819', 1.000000), 
	Parameter('rvs_RXN_10819', 0.000000))
Rule('_3dot4dot13dot22_RXN',
	prot(name = 'G6782_MONOMER', loc = 'cyt') +
	met(name = 'D_ALA_D_ALA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6782_MONOMER', loc = 'cyt') +
	met(name = 'D_ALANINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd__3dot4dot13dot22_RXN', 1.000000), 
	Parameter('rvs__3dot4dot13dot22_RXN', 0.000000))
Rule('RXN0_5461',
	prot(name = 'G6798_MONOMER', loc = 'cyt') +
	met(name = 'DIHYDROXYPENTANEDIONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G6798_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_10551', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5461', 1.000000), 
	Parameter('rvs_RXN0_5461', 0.000000))
Rule('RXN_15216',
	prot(name = 'G6805_MONOMER', loc = 'cyt') +
	met(name = 'CPD_10551', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6805_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_2467', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_15216', 1.000000), 
	Parameter('rvs_RXN_15216', 0.000000))
Rule('RXN0_6720',
	prot(name = 'G6805_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_2467', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6805_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_2468', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_6720', 1.000000), 
	Parameter('rvs_RXN0_6720', 1.000000))
Rule('RXN0_2441',
	prot(name = 'G6806_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_225', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6806_MONOMER', loc = 'cyt') +
	met(name = 'MONOMETHYL_ESTER_OF_TRANS_ACONITATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_2441', 1.000000), 
	Parameter('rvs_RXN0_2441', 0.000000))
Rule('RXN0_6367',
	prot(name = 'G6862_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_2101', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G6862_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_11770', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6367', 0.000000), 
	Parameter('rvs_RXN0_6367', 1.000000))
Rule('RXN0_4621',
	prot(name = 'G6880_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_882', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6880_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_881', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_4621', 1.000000), 
	Parameter('rvs_RXN0_4621', 0.000000))
Rule('SUPEROX_DISMUT_RXN',
	prot(name = 'G6886_MONOMER', loc = 'ex') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SUPER_OXIDE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6886_MONOMER', loc = 'ex') +
	met(name = 'HYDROGEN_PEROXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_SUPEROX_DISMUT_RXN', 1.000000), 
	Parameter('rvs_SUPEROX_DISMUT_RXN', 0.000000))
Rule('RXN0_5101',
	prot(name = 'G6890_MONOMER', loc = 'cyt') +
	met(name = 'N_ETHYLMALEIMIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6890_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_903', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_5101', 1.000000), 
	Parameter('rvs_RXN0_5101', 0.000000))
Rule('SORBITOL_6_PHOSPHATASE_RXN',
	prot(name = 'G6932_MONOMER', loc = 'cyt') +
	met(name = 'D_SORBITOL_6_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6932_MONOMER', loc = 'cyt') +
	met(name = 'SORBITOL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_SORBITOL_6_PHOSPHATASE_RXN', 1.000000), 
	Parameter('rvs_SORBITOL_6_PHOSPHATASE_RXN', 0.000000))
Rule('MANNITOL_1_PHOSPHATASE_RXN',
	prot(name = 'G6932_MONOMER', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MANNITOL_1P', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6932_MONOMER', loc = 'cyt') +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MANNITOL', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_MANNITOL_1_PHOSPHATASE_RXN', 1.000000), 
	Parameter('rvs_MANNITOL_1_PHOSPHATASE_RXN', 0.000000))
Rule('RXN_12473',
	prot(name = 'G6952_MONOMER', loc = 'per') +
	met(name = 'Carboxyadenylated_MPT_synthases', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_Cysteine_Desulfurase_persulfide', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Donor_H2', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	prot(name = 'G6952_MONOMER', loc = 'per') +
	met(name = 'Thiocarboxylated_MPT_synthases', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Cysteine_Desulfurase_L_cysteine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Acceptor', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_12473', 1.000000), 
	Parameter('rvs_RXN_12473', 0.000000))
Rule('RXN0_6957',
	prot(name = 'G6954_MONOMER', loc = 'cyt') +
	met(name = 'CPD_13851', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G6954_MONOMER', loc = 'cyt') +
	met(name = 'CPD_13852', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6957', 1.000000), 
	Parameter('rvs_RXN0_6957', 0.000000))
Rule('RXN_14188',
	prot(name = 'G6954_MONOMER', loc = 'cyt') +
	met(name = '_5_HYDROXY_CTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G6954_MONOMER', loc = 'cyt') +
	met(name = 'CPD_15158', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14188', 1.000000), 
	Parameter('rvs_RXN_14188', 0.000000))
Rule('RXN0_7291',
	prot(name = 'G6954_MONOMER', loc = 'cyt') +
	met(name = 'GUANOSINE_5DP_3DP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6954_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_2634', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7291', 1.000000), 
	Parameter('rvs_RXN0_7291', 0.000000))
Rule('RXN0_5213',
	prot(name = 'G6958_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'METHYL_GLYOXAL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6958_MONOMER', loc = 'cyt') +
	met(name = 'ACETOL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_5213', 1.000000), 
	Parameter('rvs_RXN0_5213', 0.000000))
Rule('_1dot1dot1dot83_RXN',
	prot(name = 'G6986_MONOMER', loc = 'cyt') +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_660', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G6986_MONOMER', loc = 'cyt') +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__1dot1dot1dot83_RXN', 1.000000), 
	Parameter('rvs__1dot1dot1dot83_RXN', 0.000000))
Rule('TARTRATE_DEHYDROGENASE_RXN',
	prot(name = 'G6986_MONOMER', loc = 'cyt') +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TARTRATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G6986_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_66', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_TARTRATE_DEHYDROGENASE_RXN', 1.000000), 
	Parameter('rvs_TARTRATE_DEHYDROGENASE_RXN', 1.000000))
Rule('RXN0_5522',
	prot(name = 'G6991_MONOMER', loc = 'cyt') +
	met(name = 'EG11171_MONOMER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G6991_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_1719', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5522', 1.000000), 
	Parameter('rvs_RXN0_5522', 0.000000))
Rule('RXN_11593',
	prot(name = 'G7008_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_16S_rRNA_cytosine1407', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G7008_MONOMER', loc = 'cyt') +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_16S_rRNA_5_O_methylcytosine1407', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11593', 1.000000), 
	Parameter('rvs_RXN_11593', 0.000000))
Rule('_3dot1dot3dot16_RXN',
	prot(name = 'G7011_MONOMER', loc = 'cyt') +
	met(name = 'Protein_Ser_or_Thr_phosphate', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7011_MONOMER', loc = 'cyt') +
	met(name = 'Protein_L_serine_or_L_threonine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3dot1dot3dot16_RXN', 1.000000), 
	Parameter('rvs__3dot1dot3dot16_RXN', 0.000000))
Rule('RXN_19619',
	prot(name = 'G7022_MONOMER', loc = 'per') +
	met(name = 'TRIMETHYLAMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'an_oxidized_TorY_protein', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7022_MONOMER', loc = 'per') +
	met(name = 'TRIMETHYLAMINE_N_O', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'A_REDUCED_TORY_PROTEIN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_19619', 0.000000), 
	Parameter('rvs_RXN_19619', 1.000000))
Rule('RXN0_5052',
	prot(name = 'G7063_MONOMER', loc = 'cyt') +
	met(name = 'Aminopeptidase_Substrates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G7063_MONOMER', loc = 'cyt') +
	met(name = 'Peptides_holder', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Amino_Acids_20', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5052', 1.000000), 
	Parameter('rvs_RXN0_5052', 0.000000))
Rule('RXN_11791',
	prot(name = 'G7098_MONOMER', loc = 'imem') +
	met(name = 'CPD_12575', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_9646', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7098_MONOMER', loc = 'imem') +
	met(name = 'UMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_12773', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11791', 1.000000), 
	Parameter('rvs_RXN_11791', 0.000000))
Rule('RXN0_5223',
	prot(name = 'G7123_MONOMER', loc = 'cyt') +
	met(name = 'L_1_PHOSPHATIDYL_GLYCEROL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G7123_MONOMER', loc = 'cyt') +
	met(name = 'L_1_PHOSPHATIDYL_GLYCEROL_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5223', 1.000000), 
	Parameter('rvs_RXN0_5223', 0.000000))
Rule('RXN_16281',
	prot(name = 'G7146_MONOMER', loc = 'imem') +
	met(name = 'KDO2_LIPID_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UNDECAPRENYL_DIPHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7146_MONOMER', loc = 'imem') +
	met(name = 'CPD_17530', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_9646', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_16281', 1.000000), 
	Parameter('rvs_RXN_16281', 0.000000))
Rule('RXN0_5383',
	prot(name = 'G7146_MONOMER', loc = 'imem') +
	met(name = 'CPD0_939', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UNDECAPRENYL_DIPHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7146_MONOMER', loc = 'imem') +
	met(name = 'CPD0_1151', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_9646', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5383', 1.000000), 
	Parameter('rvs_RXN0_5383', 0.000000))
Rule('DCTP_PYROPHOSPHATASE_RXN',
	prot(name = 'G7164_MONOMER', loc = 'cyt') +
	met(name = 'DCTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G7164_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DCMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DCTP_PYROPHOSPHATASE_RXN', 1.000000), 
	Parameter('rvs_DCTP_PYROPHOSPHATASE_RXN', 0.000000))
Rule('RXN0_1863',
	prot(name = 'G7166_MONOMER', loc = 'cyt') +
	met(name = 'UDP_4_AMINO_4_DEOXY_L_ARABINOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7166_MONOMER', loc = 'cyt') +
	met(name = '_5_BETA_L_THREO_PENTAPYRANOSYL_4_ULOSE_', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_1863', 1.000000), 
	Parameter('rvs_RXN0_1863', 1.000000))
Rule('RXN0_3521',
	prot(name = 'G7167_MONOMER', loc = 'imem') +
	met(name = 'UDP_L_ARA4_FORMYL_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_9646', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7167_MONOMER', loc = 'imem') +
	met(name = 'CPD0_888', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UDP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_3521', 1.000000), 
	Parameter('rvs_RXN0_3521', 0.000000))
Rule('RXN0_5409',
	prot(name = 'G7169_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_888', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7169_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_1189', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FORMATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5409', 1.000000), 
	Parameter('rvs_RXN0_5409', 0.000000))
Rule('RXN0_2001',
	prot(name = 'G7170_MONOMER', loc = 'imem') +
	met(name = 'KDO2_LIPID_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_1189', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7170_MONOMER', loc = 'imem') +
	met(name = 'L_ARA4N_MODIFIED_KDO2_LIPID_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_9646', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_2001', 1.000000), 
	Parameter('rvs_RXN0_2001', 0.000000))
Rule('_3dot4dot19dot12_RXN',
	prot(name = 'G7176_MONOMER', loc = 'cyt') +
	met(name = 'PROTEIN_N_UBIQUITYL_LYSINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7176_MONOMER', loc = 'cyt') +
	met(name = 'Protein_L_lysine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Ubiquitin_C_Terminal_Glycine', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3dot4dot19dot12_RXN', 1.000000), 
	Parameter('rvs__3dot4dot19dot12_RXN', 0.000000))
Rule('GLYCEROL_1_PHOSPHATASE_RXN',
	prot(name = 'G7187_MONOMER', loc = 'cyt') +
	met(name = 'Glycerol_1_phosphate', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7187_MONOMER', loc = 'cyt') +
	met(name = 'GLYCEROL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLYCEROL_1_PHOSPHATASE_RXN', 1.000000), 
	Parameter('rvs_GLYCEROL_1_PHOSPHATASE_RXN', 0.000000))
Rule('GST_RXN',
	prot(name = 'G7193_MONOMER', loc = 'cyt') +
	met(name = '_1_CHLORO_24_DINITROBENZENE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLUTATHIONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G7193_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'S_24_DINITROPHENYLGLUTATHIONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CL_', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GST_RXN', 1.000000), 
	Parameter('rvs_GST_RXN', 0.000000))
Rule('RXN0_7081',
	prot(name = 'G7199_MONOMER', loc = 'cyt') +
	met(name = 'tRNA_containing_5_CarbMeAminome_2_ThioU', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7199_MONOMER', loc = 'cyt') +
	met(name = 'tRNA_Containing_5AminoMe_2_ThioUrdines', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLYOX', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FADH2', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_7081', 1.000000), 
	Parameter('rvs_RXN0_7081', 0.000000))
Rule('RXN0_5144',
	prot(name = 'G7199_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'tRNA_Containing_5AminoMe_2_ThioUrdines', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G7199_MONOMER', loc = 'cyt') +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'tRNA_Containing_5MeAminoMe_2_ThioU', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5144', 1.000000), 
	Parameter('rvs_RXN0_5144', 0.000000))
Rule('RXN0_7000',
	prot(name = 'G7201_MONOMER', loc = 'cyt') +
	met(name = 'EF_P_L_lysine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7201_MONOMER', loc = 'cyt') +
	met(name = 'EF_P_lysyl_hydroxylysine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_7000', 1.000000), 
	Parameter('rvs_RXN0_7000', 0.000000))
Rule('RXN0_312',
	prot(name = 'G7211_MONOMER', loc = 'cyt') +
	met(name = 'PHOSPHO_ARCB717', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7211_MONOMER', loc = 'cyt') +
	met(name = 'ARCB_MONOMER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_312', 1.000000), 
	Parameter('rvs_RXN0_312', 0.000000))
Rule('ENOYL_COA_HYDRAT_RXN',
	prot(name = 'G7212_MONOMER', loc = 'cyt') +
	met(name = 'L_3_HYDROXYACYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G7212_MONOMER', loc = 'cyt') +
	met(name = 'TRANS_D2_ENOYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ENOYL_COA_HYDRAT_RXN', 0.000000), 
	Parameter('rvs_ENOYL_COA_HYDRAT_RXN', 1.000000))
Rule('RXN_17776',
	prot(name = 'G7212_MONOMER', loc = 'cyt') +
	met(name = 'CPD_19171', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G7212_MONOMER', loc = 'cyt') +
	met(name = 'CPD_19172', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17776', 0.000000), 
	Parameter('rvs_RXN_17776', 1.000000))
Rule('RXN_17780',
	prot(name = 'G7212_MONOMER', loc = 'cyt') +
	met(name = 'CPD_19170', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7212_MONOMER', loc = 'cyt') +
	met(name = 'CPD_19168', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_17780', 1.000000), 
	Parameter('rvs_RXN_17780', 0.000000))
Rule('RXN0_5393',
	prot(name = 'G7212_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_1163', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G7212_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_1162', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5393', 0.000000), 
	Parameter('rvs_RXN0_5393', 1.000000))
Rule('RXN_17785',
	prot(name = 'G7212_MONOMER', loc = 'cyt') +
	met(name = 'CPD_19163', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7212_MONOMER', loc = 'cyt') +
	met(name = 'CPD_19159', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_17785', 1.000000), 
	Parameter('rvs_RXN_17785', 0.000000))
Rule('RXN_17789',
	prot(name = 'G7212_MONOMER', loc = 'cyt') +
	met(name = 'CPD_19162', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7212_MONOMER', loc = 'cyt') +
	met(name = 'CPD_19155', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_17789', 1.000000), 
	Parameter('rvs_RXN_17789', 0.000000))
Rule('RXN_17793',
	prot(name = 'G7212_MONOMER', loc = 'cyt') +
	met(name = 'CPD_19154', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G7212_MONOMER', loc = 'cyt') +
	met(name = 'CPD_19161', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17793', 0.000000), 
	Parameter('rvs_RXN_17793', 1.000000))
Rule('RXN_17797',
	prot(name = 'G7212_MONOMER', loc = 'cyt') +
	met(name = 'CPD_19151', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G7212_MONOMER', loc = 'cyt') +
	met(name = 'CPD_19150', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17797', 0.000000), 
	Parameter('rvs_RXN_17797', 1.000000))
Rule('OHBUTYRYL_COA_EPIM_RXN',
	prot(name = 'G7212_MONOMER', loc = 'cyt') +
	met(name = 'D_3_HYDROXYACYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7212_MONOMER', loc = 'cyt') +
	met(name = 'L_3_HYDROXYACYL_COA', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_OHBUTYRYL_COA_EPIM_RXN', 1.000000), 
	Parameter('rvs_OHBUTYRYL_COA_EPIM_RXN', 1.000000))
Rule('ENOYL_COA_DELTA_ISOM_RXN',
	prot(name = 'G7212_MONOMER', loc = 'cyt') +
	met(name = 'CIS_DELTA3_ENOYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7212_MONOMER', loc = 'cyt') +
	met(name = 'TRANS_D2_ENOYL_COA', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ENOYL_COA_DELTA_ISOM_RXN', 1.000000), 
	Parameter('rvs_ENOYL_COA_DELTA_ISOM_RXN', 1.000000))
Rule('_2dot4dot1dot78_RXN',
	prot(name = 'G7220_MONOMER', loc = 'imem') +
	met(name = 'CPD_12575', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_9646', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7220_MONOMER', loc = 'imem') +
	met(name = 'CPD_20966', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UDP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__2dot4dot1dot78_RXN', 1.000000), 
	Parameter('rvs__2dot4dot1dot78_RXN', 0.000000))
Rule('RXN_19362',
	prot(name = 'G7221_MONOMER', loc = 'imem') +
	met(name = 'CPD_20966', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Lipopolysaccharides', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7221_MONOMER', loc = 'imem') +
	met(name = 'Glucosyl_Lipopolysaccharides', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_9646', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_19362', 1.000000), 
	Parameter('rvs_RXN_19362', 0.000000))
Rule('RXN0_5051',
	prot(name = 'G7247_MONOMER', loc = 'cyt') +
	met(name = 'Exoaminopeptidase_Substrates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G7247_MONOMER', loc = 'cyt') +
	met(name = 'Peptides_holder', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Amino_Acids_20', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5051', 1.000000), 
	Parameter('rvs_RXN0_5051', 0.000000))
Rule('RXN0_5418',
	prot(name = 'G7297_MONOMER', loc = 'cyt') +
	met(name = 'Cytidine_34_tRNAmet', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G7297_MONOMER', loc = 'cyt') +
	met(name = 'Elongator_tRNAMet_acetylcytidine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5418', 1.000000), 
	Parameter('rvs_RXN0_5418', 0.000000))
Rule('RXN_14381',
	prot(name = 'G7324_MONOMER', loc = 'cyt') +
	met(name = 'Persulfurated_L_cysteine_desulfurases', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_form_FeS_Cluster_Scaffold_Proteins', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7324_MONOMER', loc = 'cyt') +
	met(name = 'S_CD_Apo_SP_Complex', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_14381', 1.000000), 
	Parameter('rvs_RXN_14381', 0.000000))
Rule('RXN0_5186',
	prot(name = 'G7408_MONOMER', loc = 'cyt') +
	met(name = 'FRU1P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7408_MONOMER', loc = 'cyt') +
	met(name = 'BETA_D_FRUCTOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5186', 1.000000), 
	Parameter('rvs_RXN0_5186', 0.000000))
Rule('RXN0_3364',
	prot(name = 'G7414_MONOMER', loc = 'cyt') +
	met(name = 'a_precursor_of_large_subunit_of_hydrogen', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7414_MONOMER', loc = 'cyt') +
	met(name = 'C_terminal_32_aminoacid_Peptides', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Precursor_of_hydrogenase_3', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_3364', 1.000000), 
	Parameter('rvs_RXN0_3364', 0.000000))
Rule('RXN_11841',
	prot(name = 'G7422_MONOMER', loc = 'cyt') +
	met(name = 'tRNA_uridine13', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7422_MONOMER', loc = 'cyt') +
	met(name = 'tRNA_pseudouridine13', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11841', 1.000000), 
	Parameter('rvs_RXN_11841', 0.000000))
Rule('RXN_11840',
	prot(name = 'G7449_MONOMER', loc = 'cyt') +
	met(name = 'tRNA_uridine65', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7449_MONOMER', loc = 'cyt') +
	met(name = 'tRNA_pseudouridine65', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11840', 1.000000), 
	Parameter('rvs_RXN_11840', 0.000000))
Rule('RXN_16938',
	prot(name = 'G7458_MONOMER', loc = 'per') +
	met(name = 'CPD0_2283', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7458_MONOMER', loc = 'per') +
	met(name = 'CPD_18259', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_1085', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_16938', 1.000000), 
	Parameter('rvs_RXN_16938', 0.000000))
Rule('RXN0_7283',
	prot(name = 'G7459_MONOMER', loc = 'cyt') +
	met(name = 'mRNAs_with_5_diphosphate', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G7459_MONOMER', loc = 'cyt') +
	met(name = 'mRNAs_with_5_monophosphate', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7283', 1.000000), 
	Parameter('rvs_RXN0_7283', 0.000000))
Rule('RXN0_5510',
	prot(name = 'G7459_MONOMER', loc = 'cyt') +
	met(name = 'mRNAs_with_5_triphosphate', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G7459_MONOMER', loc = 'cyt') +
	met(name = 'mRNAs_with_5_monophosphate', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5510', 1.000000), 
	Parameter('rvs_RXN0_5510', 0.000000))
Rule('RXN0_6254',
	prot(name = 'G7496_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_8123', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CTP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7496_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_1882', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_6254', 1.000000), 
	Parameter('rvs_RXN0_6254', 0.000000))
Rule('GUANINE_DEAMINASE_RXN',
	prot(name = 'G7502_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GUANINE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7502_MONOMER', loc = 'cyt') +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'XANTHINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_GUANINE_DEAMINASE_RXN', 1.000000), 
	Parameter('rvs_GUANINE_DEAMINASE_RXN', 0.000000))
Rule('RXN0_268',
	prot(name = 'G7517_MONOMER', loc = 'cyt') +
	met(name = 'PROPIONYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SUC', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7517_MONOMER', loc = 'cyt') +
	met(name = 'PROPIONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SUC_COA', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_268', 1.000000), 
	Parameter('rvs_RXN0_268', 1.000000))
Rule('RXN0_5410',
	prot(name = 'G7558_MONOMER', loc = 'cyt') +
	met(name = 'GLYCEROL_3P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G7558_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_GLYCERALDEHYDE_3_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5410', 0.000000), 
	Parameter('rvs_RXN0_5410', 1.000000))
Rule('RXN0_5038',
	prot(name = 'G7579_MONOMER', loc = 'cyt') +
	met(name = 'CAMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7579_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5038', 1.000000), 
	Parameter('rvs_RXN0_5038', 0.000000))
Rule('RXN0_6941',
	prot(name = 'G7593_MONOMER', loc = 'cyt') +
	met(name = 'FEplus2', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_2483', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7593_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_2482', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6941', 0.000000), 
	Parameter('rvs_RXN0_6941', 1.000000))
Rule('RXN0_6555',
	prot(name = 'G7593_MONOMER', loc = 'cyt') +
	met(name = 'FEplus2', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Siderophore', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7593_MONOMER', loc = 'cyt') +
	met(name = 'Fe3_siderophores', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6555', 0.000000), 
	Parameter('rvs_RXN0_6555', 1.000000))
Rule('RXN0_5395',
	prot(name = 'G7599_MONOMER', loc = 'per') +
	met(name = '_3_BETA_D_GLUCOSYLGLUCOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7599_MONOMER', loc = 'per') +
	met(name = 'Glucopyranose', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_5395', 1.000000), 
	Parameter('rvs_RXN0_5395', 0.000000))
Rule('RXN_11635',
	prot(name = 'G7603_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_23S_rRNA_guanine_1835', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G7603_MONOMER', loc = 'cyt') +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_23S_rRNA_N2_methylguanine1835', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11635', 1.000000), 
	Parameter('rvs_RXN_11635', 0.000000))
Rule('RXN0_6528',
	prot(name = 'G7629_MONOMER', loc = 'cyt') +
	met(name = 'YHAV_DEGRADATION_SUBSTRATE_MRNA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7629_MONOMER', loc = 'cyt') +
	met(name = 'mRNA_Fragments', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_6528', 1.000000), 
	Parameter('rvs_RXN0_6528', 0.000000))
Rule('RXN_13548',
	prot(name = 'G7634_MONOMER', loc = 'imem') +
	met(name = 'D_GALACTOSAMINE_6_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7634_MONOMER', loc = 'imem') +
	met(name = 'TAGATOSE_6_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_13548', 1.000000), 
	Parameter('rvs_RXN_13548', 0.000000))
Rule('RXN_14569',
	prot(name = 'G7698_MONOMER', loc = 'cyt') +
	met(name = 'THR', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HCO3', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7698_MONOMER', loc = 'cyt') +
	met(name = 'CPD_15435', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14569', 1.000000), 
	Parameter('rvs_RXN_14569', 1.000000))
Rule('RXN0_962',
	prot(name = 'G7726_MONOMER', loc = 'cyt') +
	met(name = 'FRUCTOSELYSINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G7726_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FRUCTOSELYSINE_6_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_962', 1.000000), 
	Parameter('rvs_RXN0_962', 0.000000))
Rule('RXN_7609',
	prot(name = 'G7742_MONOMER', loc = 'cyt') +
	met(name = 'GMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7742_MONOMER', loc = 'cyt') +
	met(name = 'GUANOSINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_7609', 1.000000), 
	Parameter('rvs_RXN_7609', 0.000000))
Rule('RXN_17916',
	prot(name = 'G7750_MONOMER', loc = 'cyt') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_5_Phospho_RNA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7750_MONOMER', loc = 'cyt') +
	met(name = 'A_5_prime_PP_5_prime_RNA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_17916', 1.000000), 
	Parameter('rvs_RXN_17916', 0.000000))
Rule('RNA_3_PHOSPHATE_CYCLASE_RXN',
	prot(name = 'G7750_MONOMER', loc = 'cyt') +
	met(name = '_3_Prime_Phosphate_Terminated_RNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G7750_MONOMER', loc = 'cyt') +
	met(name = 'Cyclic_Phosphate_Terminated_RNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RNA_3_PHOSPHATE_CYCLASE_RXN', 1.000000), 
	Parameter('rvs_RNA_3_PHOSPHATE_CYCLASE_RXN', 0.000000))
Rule('RXN0_6556',
	prot(name = 'G7750_MONOMER', loc = 'cyt') +
	met(name = '_5_Phospho_DNA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7750_MONOMER', loc = 'cyt') +
	met(name = 'A_5_prime_PP_5_prime_DNA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_6556', 1.000000), 
	Parameter('rvs_RXN0_6556', 0.000000))
Rule('RXN_17905',
	prot(name = 'G7751_MONOMER', loc = 'cyt') +
	met(name = '_3_Prime_Phosphate_Terminated_RNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_5Prime_OH_Terminated_RNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GTP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7751_MONOMER', loc = 'cyt') +
	met(name = 'RNA_Holder', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17905', 1.000000), 
	Parameter('rvs_RXN_17905', 0.000000))
Rule('RXN0_6566',
	prot(name = 'G7751_MONOMER', loc = 'cyt') +
	met(name = 'Cyclic_Phosphate_Terminated_RNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_5Prime_OH_Terminated_RNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7751_MONOMER', loc = 'cyt') +
	met(name = 'RNA_Holder', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6566', 1.000000), 
	Parameter('rvs_RXN0_6566', 0.000000))
Rule('QUERCETIN_23_DIOXYGENASE_RXN',
	prot(name = 'G7756_MONOMER', loc = 'cyt') +
	met(name = 'CPD_520', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7756_MONOMER', loc = 'cyt') +
	met(name = '_2_PROTOCATECHUOYLPHLOROGLUCINOLCARBOXYLA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_MONOXIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_QUERCETIN_23_DIOXYGENASE_RXN', 1.000000), 
	Parameter('rvs_QUERCETIN_23_DIOXYGENASE_RXN', 0.000000))
Rule('FUC4NACTRANS_RXN',
	prot(name = 'G7800_MONOMER', loc = 'imem') +
	met(name = 'C55_PP_GLCNAC_MANNACA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TDP_FUC4NAC', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G7800_MONOMER', loc = 'imem') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'C55_PP_GLCNAC_MANNACA_FUC4NAC', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TDP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_FUC4NACTRANS_RXN', 1.000000), 
	Parameter('rvs_FUC4NACTRANS_RXN', 0.000000))
Rule('RXN0_5192',
	prot(name = 'G7836_MONOMER', loc = 'cyt') +
	met(name = 'LYS', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7836_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_1032', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5192', 1.000000), 
	Parameter('rvs_RXN0_5192', 1.000000))
Rule('RXN_12104',
	prot(name = 'G7843_MONOMER', loc = 'cyt') +
	met(name = 'tRNAs_with_queuine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Acceptor', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7843_MONOMER', loc = 'cyt') +
	met(name = 'tRNAs_containing_epoxy_quenosine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Donor_H2', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_12104', 0.000000), 
	Parameter('rvs_RXN_12104', 1.000000))
Rule('RXN0_5387',
	prot(name = 'G7868_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_1156', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'G7868_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_1157', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_5387', 1.000000), 
	Parameter('rvs_RXN0_5387', 0.000000))
Rule('RXN_13182',
	prot(name = 'G7919_MONOMER', loc = 'per') +
	met(name = 'N_ACETYL_9_O_ACETYLNEURAMINATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G7919_MONOMER', loc = 'per') +
	met(name = 'N_ACETYLNEURAMINATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACET', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_13182', 1.000000), 
	Parameter('rvs_RXN_13182', 0.000000))
Rule('RXN0_5229',
	prot(name = 'G7945_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_1083', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G7945_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_TAGATURONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5229', 1.000000), 
	Parameter('rvs_RXN0_5229', 0.000000))
Rule('RXN_11576',
	prot(name = 'G7950_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_16S_rRNA_guanine_1207', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'G7950_MONOMER', loc = 'cyt') +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_16S_rRNA_N2_methylguanine1207', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11576', 1.000000), 
	Parameter('rvs_RXN_11576', 0.000000))
Rule('GALACTARDEHYDRA_RXN',
	prot(name = 'GALACTARDEHYDRA_MONOMER', loc = 'cyt') +
	met(name = 'D_GALACTARATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'GALACTARDEHYDRA_MONOMER', loc = 'cyt') +
	met(name = '_5_KETO_4_DEOXY_D_GLUCARATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GALACTARDEHYDRA_RXN', 1.000000), 
	Parameter('rvs_GALACTARDEHYDRA_RXN', 0.000000))
Rule('GALACTOACETYLTRAN_RXN',
	cplx(name = 'GALACTOACETYLTRAN_CPLX', loc = 'cyt') +
	met(name = 'Beta_D_Galactosides', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'GALACTOACETYLTRAN_CPLX', loc = 'cyt') +
	met(name = '_6_Acetyl_Beta_D_Galactosides', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GALACTOACETYLTRAN_RXN', 1.000000), 
	Parameter('rvs_GALACTOACETYLTRAN_RXN', 0.000000))
Rule('GALACTOKIN_RXN',
	prot(name = 'GALACTOKIN_MONOMER', loc = 'cyt') +
	met(name = 'ALPHA_D_GALACTOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'GALACTOKIN_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GALACTOSE_1P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GALACTOKIN_RXN', 1.000000), 
	Parameter('rvs_GALACTOKIN_RXN', 0.000000))
Rule('GALACTONDEHYDRAT_RXN',
	prot(name = 'GALACTONATE_DEHYDRATASE_MONOMER', loc = 'cyt') +
	met(name = 'D_GALACTONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'GALACTONATE_DEHYDRATASE_MONOMER', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_DEHYDRO_3_DEOXY_D_GALACTONATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GALACTONDEHYDRAT_RXN', 1.000000), 
	Parameter('rvs_GALACTONDEHYDRAT_RXN', 0.000000))
Rule('GALACTURIDYLYLTRANS_RXN',
	cplx(name = 'GALACTURIDYLYLTRANS_CPLX', loc = 'cyt') +
	met(name = 'CPD_12575', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GALACTOSE_1P', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'GALACTURIDYLYLTRANS_CPLX', loc = 'cyt') +
	met(name = 'CPD_14553', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLC_1_P', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GALACTURIDYLYLTRANS_RXN', 1.000000), 
	Parameter('rvs_GALACTURIDYLYLTRANS_RXN', 1.000000))
Rule('GALPMUT_RXN',
	prot(name = 'GALPMUT_MONOMER', loc = 'cyt') +
	met(name = 'CPD_14553', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'GALPMUT_MONOMER', loc = 'cyt') +
	met(name = 'UDP_D_GALACTO_14_FURANOSE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GALPMUT_RXN', 1.000000), 
	Parameter('rvs_GALPMUT_RXN', 1.000000))
Rule('GAPOXNPHOSPHN_RXN',
	cplx(name = 'GAPDH_A_CPLX', loc = 'cyt') +
	met(name = 'GAP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'GAPDH_A_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DPG', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GAPOXNPHOSPHN_RXN', 1.000000), 
	Parameter('rvs_GAPOXNPHOSPHN_RXN', 1.000000))
Rule('GART_RXN',
	prot(name = 'GART_MONOMER', loc = 'cyt') +
	met(name = 'FORMYL_THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_5_PHOSPHO_RIBOSYL_GLYCINEAMIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'GART_MONOMER', loc = 'cyt') +
	met(name = 'THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_5_P_RIBOSYL_N_FORMYLGLYCINEAMIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GART_RXN', 1.000000), 
	Parameter('rvs_GART_RXN', 1.000000))
Rule('GARTRANSFORMYL2_RXN',
	prot(name = 'GARTRANSFORMYL2_MONOMER', loc = 'cyt') +
	met(name = '_5_PHOSPHO_RIBOSYL_GLYCINEAMIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FORMATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'GARTRANSFORMYL2_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_5_P_RIBOSYL_N_FORMYLGLYCINEAMIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GARTRANSFORMYL2_RXN', 1.000000), 
	Parameter('rvs_GARTRANSFORMYL2_RXN', 0.000000))
Rule('GCVMULTI_RXN',
	cplx(name = 'GCVMULTI_CPLX', loc = 'imem') +
	met(name = 'GLY', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'GCVMULTI_CPLX', loc = 'imem') +
	met(name = 'METHYLENE_THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GCVMULTI_RXN', 1.000000), 
	Parameter('rvs_GCVMULTI_RXN', 0.000000))
Rule('GCVP_RXN',
	cplx(name = 'GCVP_CPLX', loc = 'cyt') +
	met(name = 'GLY', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTEIN_LIPOYLLYSINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'GCVP_CPLX', loc = 'cyt') +
	met(name = 'AMINOMETHYLDIHYDROLIPOYL_GCVH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_GCVP_RXN', 1.000000), 
	Parameter('rvs_GCVP_RXN', 1.000000))
Rule('GCVT_RXN',
	prot(name = 'GCVT_MONOMER', loc = 'cyt') +
	met(name = 'AMINOMETHYLDIHYDROLIPOYL_GCVH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'GCVT_MONOMER', loc = 'cyt') +
	met(name = 'DIHYDROLIPOYL_GCVH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'METHYLENE_THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GCVT_RXN', 1.000000), 
	Parameter('rvs_GCVT_RXN', 1.000000))
Rule('GLUTDEHYD_RXN',
	cplx(name = 'GDHA_CPLX', loc = 'cyt') +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'GDHA_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLUTDEHYD_RXN', 1.000000), 
	Parameter('rvs_GLUTDEHYD_RXN', 1.000000))
Rule('GDPMANDEHYDRA_RXN',
	cplx(name = 'GDPMANDEHYDRA_CPLX', loc = 'cyt') +
	met(name = 'GDP_MANNOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'GDPMANDEHYDRA_CPLX', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GDP_4_DEHYDRO_6_DEOXY_D_MANNOSE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GDPMANDEHYDRA_RXN', 1.000000), 
	Parameter('rvs_GDPMANDEHYDRA_RXN', 0.000000))
Rule('GKI_RXN',
	prot(name = 'GKI_MONOMER', loc = 'cyt') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLYCERATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'GKI_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_PG', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GKI_RXN', 1.000000), 
	Parameter('rvs_GKI_RXN', 0.000000))
Rule('URITRANS_RXN',
	prot(name = 'GLND_MONOMER', loc = 'cyt') +
	met(name = 'Gln_B', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UTP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'GLND_MONOMER', loc = 'cyt') +
	met(name = 'URIDYLYL_PROTEIN_PII', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_URITRANS_RXN', 1.000000), 
	Parameter('rvs_URITRANS_RXN', 0.000000))
Rule('RXN_16381',
	prot(name = 'GLND_MONOMER', loc = 'cyt') +
	met(name = 'URIDYLYL_PROTEIN_PII', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'GLND_MONOMER', loc = 'cyt') +
	met(name = 'Gln_B', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_16381', 1.000000), 
	Parameter('rvs_RXN_16381', 0.000000))
Rule('RXN0_801',
	prot(name = 'GLND_MONOMER', loc = 'cyt') +
	met(name = 'PROTEIN_PII2', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UTP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'GLND_MONOMER', loc = 'cyt') +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'URIDYLYL_PII2', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_801', 1.000000), 
	Parameter('rvs_RXN0_801', 0.000000))
Rule('GSADENYLATION_RXN',
	prot(name = 'GLNE_MONOMER', loc = 'cyt') +
	met(name = 'Glutamine_synthetase_Tyr', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'GLNE_MONOMER', loc = 'cyt') +
	met(name = 'Glutamine_synthetase_adenylyl_Tyr', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GSADENYLATION_RXN', 1.000000), 
	Parameter('rvs_GSADENYLATION_RXN', 0.000000))
Rule('GSDEADENYLATION_RXN',
	prot(name = 'GLNE_MONOMER', loc = 'cyt') +
	met(name = 'Glutamine_synthetase_adenylyl_Tyr', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'GLNE_MONOMER', loc = 'cyt') +
	met(name = 'Glutamine_synthetase_Tyr', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GSDEADENYLATION_RXN', 1.000000), 
	Parameter('rvs_GSDEADENYLATION_RXN', 0.000000))
Rule('GLUTAMINE__TRNA_LIGASE_RXN',
	prot(name = 'GLNS_MONOMER', loc = 'cyt') +
	met(name = 'GLN_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'GLNS_MONOMER', loc = 'cyt') +
	met(name = 'Charged_GLN_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLUTAMINE__TRNA_LIGASE_RXN', 1.000000), 
	Parameter('rvs_GLUTAMINE__TRNA_LIGASE_RXN', 0.000000))
Rule('GLU6PDEHYDROG_RXN',
	prot(name = 'GLU6PDEHYDROG_MONOMER', loc = 'cyt') +
	met(name = 'D_glucopyranose_6_phosphate', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'GLU6PDEHYDROG_MONOMER', loc = 'cyt') +
	met(name = 'D_6_P_GLUCONO_DELTA_LACTONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLU6PDEHYDROG_RXN', 1.000000), 
	Parameter('rvs_GLU6PDEHYDROG_RXN', 0.000000))
Rule('GLUC1PADENYLTRANS_RXN',
	cplx(name = 'GLUC1PADENYLTRANS_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLC_1_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'GLUC1PADENYLTRANS_CPLX', loc = 'cyt') +
	met(name = 'ADP_D_GLUCOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_GLUC1PADENYLTRANS_RXN', 1.000000), 
	Parameter('rvs_GLUC1PADENYLTRANS_RXN', 0.000000))
Rule('GLUCARDEHYDRA_RXN',
	prot(name = 'GLUCARDEHYDRA_MONOMER', loc = 'cyt') +
	met(name = 'D_GLUCARATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'GLUCARDEHYDRA_MONOMER', loc = 'cyt') +
	met(name = '_5_KETO_4_DEOXY_D_GLUCARATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLUCARDEHYDRA_RXN', 1.000000), 
	Parameter('rvs_GLUCARDEHYDRA_RXN', 0.000000))
Rule('RXN0_5285',
	prot(name = 'GLUCARDEHYDRA_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_1090', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'GLUCARDEHYDRA_MONOMER', loc = 'cyt') +
	met(name = 'D_GLUCARATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5285', 1.000000), 
	Parameter('rvs_RXN0_5285', 1.000000))
Rule('RXN0_6373',
	prot(name = 'GLUCDEHYDROG_MONOMER', loc = 'per') +
	met(name = 'Ubiquinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Glucopyranose', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'GLUCDEHYDROG_MONOMER', loc = 'per') +
	met(name = 'Ubiquinols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLC_D_LACTONE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6373', 1.000000), 
	Parameter('rvs_RXN0_6373', 0.000000))
Rule('GLUCOKIN_RXN',
	prot(name = 'GLUCOKIN_MONOMER', loc = 'cyt') +
	met(name = 'Glucopyranose', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'GLUCOKIN_MONOMER', loc = 'cyt') +
	met(name = 'D_glucopyranose_6_phosphate', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLUCOKIN_RXN', 1.000000), 
	Parameter('rvs_GLUCOKIN_RXN', 0.000000))
Rule('GLUCOSAMINE_KINASE_RXN',
	prot(name = 'GLUCOKIN_MONOMER', loc = 'cyt') +
	met(name = 'GLUCOSAMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'GLUCOKIN_MONOMER', loc = 'cyt') +
	met(name = 'D_GLUCOSAMINE_6_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLUCOSAMINE_KINASE_RXN', 1.000000), 
	Parameter('rvs_GLUCOSAMINE_KINASE_RXN', 0.000000))
Rule('GLUCONOKIN_RXN',
	prot(name = 'GLUCONOKINI_MONOMER', loc = 'cyt') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLUCONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'GLUCONOKINI_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_2961', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLUCONOKIN_RXN', 1.000000), 
	Parameter('rvs_GLUCONOKIN_RXN', 0.000000))
Rule('RXN_11152',
	prot(name = 'GLUCONOLACT_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_1083', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'GLUCONOLACT_MONOMER', loc = 'cyt') +
	met(name = 'CPD_330', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11152', 1.000000), 
	Parameter('rvs_RXN_11152', 1.000000))
Rule('GALACTONOLACTONASE_RXN',
	prot(name = 'GLUCONOLACT_MONOMER', loc = 'cyt') +
	met(name = 'D_GALACTONO_1_4_LACTONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'GLUCONOLACT_MONOMER', loc = 'cyt') +
	met(name = 'D_GALACTONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GALACTONOLACTONASE_RXN', 1.000000), 
	Parameter('rvs_GALACTONOLACTONASE_RXN', 0.000000))
Rule('GLUCONOLACT_RXN',
	prot(name = 'GLUCONOLACT_MONOMER', loc = 'cyt') +
	met(name = 'GLC_D_LACTONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'GLUCONOLACT_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLUCONATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLUCONOLACT_RXN', 1.000000), 
	Parameter('rvs_GLUCONOLACT_RXN', 0.000000))
Rule('GLUCONATE_5_DEHYDROGENASE_RXN',
	prot(name = 'GLUCONREDUCT_MONOMER', loc = 'cyt') +
	met(name = 'NAD_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLUCONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'GLUCONREDUCT_MONOMER', loc = 'cyt') +
	met(name = 'NADH_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_5_DEHYDROGLUCONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLUCONATE_5_DEHYDROGENASE_RXN', 1.000000), 
	Parameter('rvs_GLUCONATE_5_DEHYDROGENASE_RXN', 1.000000))
Rule('GLUCOSAMINE_6_P_DEAMIN_RXN',
	cplx(name = 'GLUCOSAMINE_6_P_DEAMIN_CPLX', loc = 'cyt') +
	met(name = 'CPD_13469', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'GLUCOSAMINE_6_P_DEAMIN_CPLX', loc = 'cyt') +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FRUCTOSE_6P', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLUCOSAMINE_6_P_DEAMIN_RXN', 1.000000), 
	Parameter('rvs_GLUCOSAMINE_6_P_DEAMIN_RXN', 1.000000))
Rule('RXN0_1001',
	cplx(name = 'GLUCOSE_1_PHOSPHAT_CPLX', loc = 'per') +
	met(name = 'MI_HEXAKISPHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'GLUCOSE_1_PHOSPHAT_CPLX', loc = 'per') +
	met(name = 'CPD_534', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_1001', 1.000000), 
	Parameter('rvs_RXN0_1001', 0.000000))
Rule('GLURS_RXN',
	prot(name = 'GLURS_MONOMER', loc = 'cyt') +
	met(name = 'GLT_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'GLURS_MONOMER', loc = 'cyt') +
	met(name = 'Charged_GLT_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLURS_RXN', 1.000000), 
	Parameter('rvs_GLURS_RXN', 0.000000))
Rule('GLUTAMATESYN_RXN',
	cplx(name = 'GLUTAMATESYN_CPLX', loc = 'cyt') +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	cplx(name = 'GLUTAMATESYN_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLUTAMATESYN_RXN', 0.000000), 
	Parameter('rvs_GLUTAMATESYN_RXN', 1.000000))
Rule('GLUTAMIDOTRANS_RXN',
	cplx(name = 'GLUTAMIDOTRANS_CPLX', loc = 'cyt') +
	met(name = 'PHOSPHORIBULOSYL_FORMIMINO_AICAR_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLN', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	cplx(name = 'GLUTAMIDOTRANS_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_ERYTHRO_IMIDAZOLE_GLYCEROL_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AICAR', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLUTAMIDOTRANS_RXN', 1.000000), 
	Parameter('rvs_GLUTAMIDOTRANS_RXN', 0.000000))
Rule('GLUTAMINESYN_RXN',
	prot(name = 'GLUTAMINESYN_OLIGOMER', loc = 'cyt') +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'GLUTAMINESYN_OLIGOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLUTAMINESYN_RXN', 1.000000), 
	Parameter('rvs_GLUTAMINESYN_RXN', 0.000000))
Rule('GLUTATHIONE_REDUCT_NADPH_RXN',
	cplx(name = 'GLUTATHIONE_REDUCT_NADPH_CPLX', loc = 'cyt') +
	met(name = 'GLUTATHIONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'GLUTATHIONE_REDUCT_NADPH_CPLX', loc = 'cyt') +
	met(name = 'OXIDIZED_GLUTATHIONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLUTATHIONE_REDUCT_NADPH_RXN', 0.000000), 
	Parameter('rvs_GLUTATHIONE_REDUCT_NADPH_RXN', 1.000000))
Rule('GLUTATHIONE_SYN_RXN',
	cplx(name = 'GLUTATHIONE_SYN_CPLX', loc = 'cyt') +
	met(name = 'GLY', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_GAMMA_GLUTAMYLCYSTEINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'GLUTATHIONE_SYN_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLUTATHIONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLUTATHIONE_SYN_RXN', 1.000000), 
	Parameter('rvs_GLUTATHIONE_SYN_RXN', 0.000000))
Rule('GLUTCYSLIG_RXN',
	prot(name = 'GLUTCYSLIG_MONOMER', loc = 'cyt') +
	met(name = 'CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'GLUTCYSLIG_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_GAMMA_GLUTAMYLCYSTEINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLUTCYSLIG_RXN', 1.000000), 
	Parameter('rvs_GLUTCYSLIG_RXN', 0.000000))
Rule('GLUTDECARBOX_RXN',
	cplx(name = 'GLUTDECARBOXA_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'GLUTDECARBOXA_CPLX', loc = 'cyt') +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_4_AMINO_BUTYRATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLUTDECARBOX_RXN', 1.000000), 
	Parameter('rvs_GLUTDECARBOX_RXN', 0.000000))
Rule('GLUTKIN_RXN',
	cplx(name = 'GLUTKIN_CPLX', loc = 'cyt') +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'GLUTKIN_CPLX', loc = 'cyt') +
	met(name = 'L_GLUTAMATE_5_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLUTKIN_RXN', 1.000000), 
	Parameter('rvs_GLUTKIN_RXN', 0.000000))
Rule('GLUTRACE_RXN',
	prot(name = 'GLUTRACE_MONOMER', loc = 'cyt') +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'GLUTRACE_MONOMER', loc = 'cyt') +
	met(name = 'D_GLT', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLUTRACE_RXN', 1.000000), 
	Parameter('rvs_GLUTRACE_RXN', 1.000000))
Rule('GLUTSEMIALDEHYDROG_RXN',
	cplx(name = 'GLUTSEMIALDEHYDROG_CPLX', loc = 'cyt') +
	met(name = 'L_GLUTAMATE_GAMMA_SEMIALDEHYDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'GLUTSEMIALDEHYDROG_CPLX', loc = 'cyt') +
	met(name = 'L_GLUTAMATE_5_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLUTSEMIALDEHYDROG_RXN', 0.000000), 
	Parameter('rvs_GLUTSEMIALDEHYDROG_RXN', 1.000000))
Rule('GLYC3PDEHYDROGBIOSYN_RXN',
	cplx(name = 'GLYC3PDEHYDROGBIOSYN_CPLX', loc = 'cyt') +
	met(name = 'NAD_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLYCEROL_3P', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'GLYC3PDEHYDROGBIOSYN_CPLX', loc = 'cyt') +
	met(name = 'NADH_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DIHYDROXY_ACETONE_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLYC3PDEHYDROGBIOSYN_RXN', 0.000000), 
	Parameter('rvs_GLYC3PDEHYDROGBIOSYN_RXN', 1.000000))
Rule('RXN_8632',
	cplx(name = 'GLYCDEH_CPLX', loc = 'cyt') +
	met(name = 'PROPANE_1_2_DIOL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'GLYCDEH_CPLX', loc = 'cyt') +
	met(name = 'ACETOL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_8632', 1.000000), 
	Parameter('rvs_RXN_8632', 1.000000))
Rule('AMINOPROPDEHYDROG_RXN',
	cplx(name = 'GLYCDEH_CPLX', loc = 'cyt') +
	met(name = '_1_AMINO_PROPAN_2_OL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'GLYCDEH_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMINO_ACETONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_AMINOPROPDEHYDROG_RXN', 0.000000), 
	Parameter('rvs_AMINOPROPDEHYDROG_RXN', 1.000000))
Rule('GLYCDEH_RXN',
	cplx(name = 'GLYCDEH_CPLX', loc = 'cyt') +
	met(name = 'GLYCEROL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'GLYCDEH_CPLX', loc = 'cyt') +
	met(name = 'DIHYDROXYACETONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLYCDEH_RXN', 1.000000), 
	Parameter('rvs_GLYCDEH_RXN', 1.000000))
Rule('RXN_10462',
	prot(name = 'GLYCEROL_3_P_ACYLTRANSFER_MONOMER', loc = 'imem') +
	met(name = 'GLYCEROL_3P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACYL_ACP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'GLYCEROL_3_P_ACYLTRANSFER_MONOMER', loc = 'imem') +
	met(name = 'ACYL_SN_GLYCEROL_3P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_10462', 1.000000), 
	Parameter('rvs_RXN_10462', 0.000000))
Rule('RXN_17018',
	prot(name = 'GLYCEROL_3_P_ACYLTRANSFER_MONOMER', loc = 'imem') +
	met(name = 'Palmitoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLYCEROL_3P', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'GLYCEROL_3_P_ACYLTRANSFER_MONOMER', loc = 'imem') +
	met(name = '_1_PALMITOYLGLYCEROL_3_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17018', 1.000000), 
	Parameter('rvs_RXN_17018', 0.000000))
Rule('RXN_17017',
	prot(name = 'GLYCEROL_3_P_ACYLTRANSFER_MONOMER', loc = 'imem') +
	met(name = 'Myristoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLYCEROL_3P', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'GLYCEROL_3_P_ACYLTRANSFER_MONOMER', loc = 'imem') +
	met(name = 'CPD_18379', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17017', 1.000000), 
	Parameter('rvs_RXN_17017', 0.000000))
Rule('RXN_17016',
	prot(name = 'GLYCEROL_3_P_ACYLTRANSFER_MONOMER', loc = 'imem') +
	met(name = 'Cis_vaccenoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLYCEROL_3P', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'GLYCEROL_3_P_ACYLTRANSFER_MONOMER', loc = 'imem') +
	met(name = 'CPD_18348', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17016', 1.000000), 
	Parameter('rvs_RXN_17016', 0.000000))
Rule('RXN_1381',
	prot(name = 'GLYCEROL_3_P_ACYLTRANSFER_MONOMER', loc = 'imem') +
	met(name = 'ACYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLYCEROL_3P', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'GLYCEROL_3_P_ACYLTRANSFER_MONOMER', loc = 'imem') +
	met(name = 'ACYL_SN_GLYCEROL_3P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_1381', 1.000000), 
	Parameter('rvs_RXN_1381', 0.000000))
Rule('GLYCEROL_KIN_RXN',
	cplx(name = 'GLYCEROL_KIN_CPLX', loc = 'cyt') +
	met(name = 'GLYCEROL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'GLYCEROL_KIN_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLYCEROL_3P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLYCEROL_KIN_RXN', 1.000000), 
	Parameter('rvs_GLYCEROL_KIN_RXN', 0.000000))
Rule('GLYCOGEN_BRANCH_RXN',
	prot(name = 'GLYCOGEN_BRANCH_MONOMER', loc = 'cyt') +
	met(name = '_1_4_alpha_D_Glucan', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'GLYCOGEN_BRANCH_MONOMER', loc = 'cyt') +
	met(name = 'Glycogens', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLYCOGEN_BRANCH_RXN', 1.000000), 
	Parameter('rvs_GLYCOGEN_BRANCH_RXN', 0.000000))
Rule('GLYCOGENSYN_RXN',
	prot(name = 'GLYCOGENSYN_MONOMER', loc = 'cyt') +
	met(name = '_1_4_alpha_D_Glucan', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP_D_GLUCOSE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'GLYCOGENSYN_MONOMER', loc = 'cyt') +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_1_4_alpha_D_Glucan', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLYCOGENSYN_RXN', 1.000000), 
	Parameter('rvs_GLYCOGENSYN_RXN', 1.000000))
Rule('GLYCOPHOSPHORYL_RXN',
	cplx(name = 'GLYCOPHOSPHORYL_CPLX', loc = 'cyt') +
	met(name = 'Glycogens', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'GLYCOPHOSPHORYL_CPLX', loc = 'cyt') +
	met(name = 'CPD0_971', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLC_1_P', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLYCOPHOSPHORYL_RXN', 1.000000), 
	Parameter('rvs_GLYCOPHOSPHORYL_RXN', 0.000000))
Rule('GLYCPDIESTER_RXN',
	prot(name = 'GLYCPDIESTER_CYTO_MONOMER', loc = 'cyt') +
	met(name = 'Glycerophosphodiesters', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'GLYCPDIESTER_CYTO_MONOMER', loc = 'cyt') +
	met(name = 'Alcohols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLYCEROL_3P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLYCPDIESTER_RXN', 1.000000), 
	Parameter('rvs_GLYCPDIESTER_RXN', 0.000000))
Rule('RXN_14073',
	prot(name = 'GLYCPDIESTER_CYTO_MONOMER', loc = 'cyt') +
	met(name = 'GLYCEROPHOSPHOGLYCEROL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'GLYCPDIESTER_CYTO_MONOMER', loc = 'cyt') +
	met(name = 'GLYCEROL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLYCEROL_3P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14073', 1.000000), 
	Parameter('rvs_RXN_14073', 0.000000))
Rule('RXN_14136',
	prot(name = 'GLYCPDIESTER_CYTO_MONOMER', loc = 'cyt') +
	met(name = 'CPD0_2030', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'GLYCPDIESTER_CYTO_MONOMER', loc = 'cyt') +
	met(name = 'GLYCEROL_3P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14136', 1.000000), 
	Parameter('rvs_RXN_14136', 0.000000))
Rule('RXN_14160',
	prot(name = 'GLYCPDIESTER_CYTO_MONOMER', loc = 'cyt') +
	met(name = 'L_1_GLYCEROPHOSPHORYLETHANOL_AMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'GLYCPDIESTER_CYTO_MONOMER', loc = 'cyt') +
	met(name = 'GLYCEROL_3P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ETHANOL_AMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14160', 1.000000), 
	Parameter('rvs_RXN_14160', 0.000000))
Rule('GLYRIBONUCSYN_RXN',
	prot(name = 'GLYCRIBONUCSYN_MONOMER', loc = 'cyt') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_5_P_BETA_D_RIBOSYL_AMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLY', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'GLYCRIBONUCSYN_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_5_PHOSPHO_RIBOSYL_GLYCINEAMIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLYRIBONUCSYN_RXN', 1.000000), 
	Parameter('rvs_GLYRIBONUCSYN_RXN', 0.000000))
Rule('GLYOCARBOLIG_RXN',
	cplx(name = 'GLYOCARBOLIG_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLYOX', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'GLYOCARBOLIG_CPLX', loc = 'cyt') +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TARTRONATE_S_ALD', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLYOCARBOLIG_RXN', 1.000000), 
	Parameter('rvs_GLYOCARBOLIG_RXN', 0.000000))
Rule('GLYOHMETRANS_RXN',
	cplx(name = 'GLYOHMETRANS_CPLX', loc = 'cyt') +
	met(name = 'SER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'GLYOHMETRANS_CPLX', loc = 'cyt') +
	met(name = 'GLY', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'METHYLENE_THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLYOHMETRANS_RXN', 1.000000), 
	Parameter('rvs_GLYOHMETRANS_RXN', 1.000000))
Rule('RXN_6321',
	cplx(name = 'GLYOHMETRANS_CPLX', loc = 'cyt') +
	met(name = '_5_10_METHENYL_THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'GLYOHMETRANS_CPLX', loc = 'cyt') +
	met(name = 'N5_Formyl_THF_Glu_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_6321', 1.000000), 
	Parameter('rvs_RXN_6321', 0.000000))
Rule('RXN0_5240',
	cplx(name = 'GLYOHMETRANS_CPLX', loc = 'cyt') +
	met(name = 'D_ALANINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRIDOXAL_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'GLYOHMETRANS_CPLX', loc = 'cyt') +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRIDOXAMINE_5P', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5240', 1.000000), 
	Parameter('rvs_RXN0_5240', 1.000000))
Rule('RXN0_5234',
	cplx(name = 'GLYOHMETRANS_CPLX', loc = 'cyt') +
	met(name = 'ALLO_THR', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'GLYOHMETRANS_CPLX', loc = 'cyt') +
	met(name = 'ACETALD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLY', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5234', 1.000000), 
	Parameter('rvs_RXN0_5234', 0.000000))
Rule('GLYOXI_RXN',
	cplx(name = 'GLYOXI_CPLX', loc = 'cyt') +
	met(name = 'S_LACTOYL_GLUTATHIONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'GLYOXI_CPLX', loc = 'cyt') +
	met(name = 'METHYL_GLYOXAL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLUTATHIONE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLYOXI_RXN', 0.000000), 
	Parameter('rvs_GLYOXI_RXN', 1.000000))
Rule('GLYCINE__TRNA_LIGASE_RXN',
	cplx(name = 'GLYS_CPLX', loc = 'cyt') +
	met(name = 'GLY_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLY', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'GLYS_CPLX', loc = 'cyt') +
	met(name = 'Charged_GLY_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLYCINE__TRNA_LIGASE_RXN', 1.000000), 
	Parameter('rvs_GLYCINE__TRNA_LIGASE_RXN', 0.000000))
Rule('GMP_REDUCT_RXN',
	cplx(name = 'GMP_REDUCT_CPLX', loc = 'cyt') +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'IMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'GMP_REDUCT_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GMP_REDUCT_RXN', 0.000000), 
	Parameter('rvs_GMP_REDUCT_RXN', 1.000000))
Rule('GMP_SYN_GLUT_RXN',
	cplx(name = 'GMP_SYN_CPLX', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'XANTHOSINE_5_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'GMP_SYN_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GMP_SYN_GLUT_RXN', 1.000000), 
	Parameter('rvs_GMP_SYN_GLUT_RXN', 0.000000))
Rule('GMP_SYN_NH3_RXN',
	cplx(name = 'GMP_SYN_CPLX', loc = 'cyt') +
	met(name = 'XANTHOSINE_5_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'GMP_SYN_CPLX', loc = 'cyt') +
	met(name = 'GMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GMP_SYN_NH3_RXN', 1.000000), 
	Parameter('rvs_GMP_SYN_NH3_RXN', 0.000000))
Rule('XANPRIBOSYLTRAN_RXN',
	cplx(name = 'GPT_CPLX', loc = 'imem') +
	met(name = 'XANTHOSINE_5_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'GPT_CPLX', loc = 'imem') +
	met(name = 'XANTHINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PRPP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_XANPRIBOSYLTRAN_RXN', 0.000000), 
	Parameter('rvs_XANPRIBOSYLTRAN_RXN', 1.000000))
Rule('RXN0_7271',
	prot(name = 'GRXB_MONOMER', loc = 'cyt') +
	met(name = 'Protein_Disulfides', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Red_Glutaredoxins', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'GRXB_MONOMER', loc = 'cyt') +
	met(name = 'Protein_Dithiols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Ox_Glutaredoxins', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7271', 1.000000), 
	Parameter('rvs_RXN0_7271', 0.000000))
Rule('GSAAMINOTRANS_RXN',
	cplx(name = 'GSAAMINOTRANS_CPLX', loc = 'cyt') +
	met(name = 'GLUTAMATE_1_SEMIALDEHYDE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'GSAAMINOTRANS_CPLX', loc = 'cyt') +
	met(name = '_5_AMINO_LEVULINATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GSAAMINOTRANS_RXN', 1.000000), 
	Parameter('rvs_GSAAMINOTRANS_RXN', 0.000000))
Rule('GSPSYN_RXN',
	cplx(name = 'GSP_CPLX', loc = 'cyt') +
	met(name = 'SPERMIDINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLUTATHIONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'GSP_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLUTATHIONYLSPERMIDINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GSPSYN_RXN', 1.000000), 
	Parameter('rvs_GSPSYN_RXN', 0.000000))
Rule('GSPAMID_RXN',
	cplx(name = 'GSP_CPLX', loc = 'cyt') +
	met(name = 'GLUTATHIONYLSPERMIDINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'GSP_CPLX', loc = 'cyt') +
	met(name = 'GLUTATHIONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SPERMIDINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GSPAMID_RXN', 1.000000), 
	Parameter('rvs_GSPAMID_RXN', 0.000000))
Rule('GTP_CYCLOHYDRO_II_RXN',
	cplx(name = 'GTP_CYCLOHYDRO_II_CPLX', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	cplx(name = 'GTP_CYCLOHYDRO_II_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DIAMINO_OH_PHOSPHORIBOSYLAMINO_PYR', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FORMATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GTP_CYCLOHYDRO_II_RXN', 1.000000), 
	Parameter('rvs_GTP_CYCLOHYDRO_II_RXN', 0.000000))
Rule('GUANYL_KIN_RXN',
	cplx(name = 'GUANYL_KIN_CPLX', loc = 'cyt') +
	met(name = 'GMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'GUANYL_KIN_CPLX', loc = 'cyt') +
	met(name = 'GDP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GUANYL_KIN_RXN', 1.000000), 
	Parameter('rvs_GUANYL_KIN_RXN', 1.000000))
Rule('GMKALT_RXN',
	cplx(name = 'GUANYL_KIN_CPLX', loc = 'cyt') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DGMP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'GUANYL_KIN_CPLX', loc = 'cyt') +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DGDP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GMKALT_RXN', 1.000000), 
	Parameter('rvs_GMKALT_RXN', 1.000000))
Rule('GUANYLCYC_RXN',
	prot(name = 'GUANYLCYC_MONOMER', loc = 'cyt') +
	met(name = 'GTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'GUANYLCYC_MONOMER', loc = 'cyt') +
	met(name = 'CGMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GUANYLCYC_RXN', 1.000000), 
	Parameter('rvs_GUANYLCYC_RXN', 0.000000))
Rule('H2NEOPTERINP3PYROPHOSPHOHYDRO_RXN',
	prot(name = 'H2NEOPTERINP3PYROPHOSPHOHYDRO_MONOMER', loc = 'cyt') +
	met(name = 'DIHYDRONEOPTERIN_P3', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'H2NEOPTERINP3PYROPHOSPHOHYDRO_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DIHYDRONEOPTERIN_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_H2NEOPTERINP3PYROPHOSPHOHYDRO_RXN', 1.000000), 
	Parameter('rvs_H2NEOPTERINP3PYROPHOSPHOHYDRO_RXN', 0.000000))
Rule('RXN0_384',
	prot(name = 'H2NEOPTERINP3PYROPHOSPHOHYDRO_MONOMER', loc = 'cyt') +
	met(name = 'DATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'H2NEOPTERINP3PYROPHOSPHOHYDRO_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DAMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_384', 1.000000), 
	Parameter('rvs_RXN0_384', 0.000000))
Rule('H2PTERIDINEPYROPHOSPHOKIN_RXN',
	prot(name = 'H2PTERIDINEPYROPHOSPHOKIN_MONOMER', loc = 'cyt') +
	met(name = 'AMINO_OH_HYDROXYMETHYL_DIHYDROPTERIDINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'H2PTERIDINEPYROPHOSPHOKIN_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DIHYDROPTERIN_CH2OH_PP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_H2PTERIDINEPYROPHOSPHOKIN_RXN', 1.000000), 
	Parameter('rvs_H2PTERIDINEPYROPHOSPHOKIN_RXN', 0.000000))
Rule('H2PTEROATESYNTH_RXN',
	cplx(name = 'H2PTEROATESYNTH_CPLX', loc = 'cyt') +
	met(name = 'P_AMINO_BENZOATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DIHYDROPTERIN_CH2OH_PP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'H2PTEROATESYNTH_CPLX', loc = 'cyt') +
	met(name = '_7_8_DIHYDROPTEROATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_H2PTEROATESYNTH_RXN', 1.000000), 
	Parameter('rvs_H2PTEROATESYNTH_RXN', 0.000000))
Rule('RXN_12072',
	cplx(name = 'HCAMULTI_CPLX', loc = 'cyt') +
	met(name = 'CPD_674', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'HCAMULTI_CPLX', loc = 'cyt') +
	met(name = 'CPD_13034', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None, 
	Parameter('fwd_RXN_12072', 1.000000), 
	Parameter('rvs_RXN_12072', 0.000000))
Rule('HCAMULTI_RXN',
	cplx(name = 'HCAMULTI_CPLX', loc = 'cyt') +
	met(name = '_3_PHENYLPROPIONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'HCAMULTI_CPLX', loc = 'cyt') +
	met(name = 'CARBOXYETHYL_3_5_CYCLOHEXADIENE_1_2_DIOL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None, 
	Parameter('fwd_HCAMULTI_RXN', 1.000000), 
	Parameter('rvs_HCAMULTI_RXN', 0.000000))
Rule('HEMEOSYN_RXN',
	prot(name = 'HEMEOSYN_MONOMER', loc = 'imem') +
	met(name = 'PROTOHEME', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FARNESYL_PP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'HEMEOSYN_MONOMER', loc = 'imem') +
	met(name = 'CPD_17063', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_HEMEOSYN_RXN', 1.000000), 
	Parameter('rvs_HEMEOSYN_RXN', 0.000000))
Rule('HEMN_RXN',
	prot(name = 'HEMN_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'COPROPORPHYRINOGEN_III', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	prot(name = 'HEMN_MONOMER', loc = 'cyt') +
	met(name = 'PROTOPORPHYRINOGEN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MET', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CH33ADO', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_HEMN_RXN', 1.000000), 
	Parameter('rvs_HEMN_RXN', 0.000000))
Rule('HISTIDINE__TRNA_LIGASE_RXN',
	cplx(name = 'HISS_CPLX', loc = 'cyt') +
	met(name = 'HIS_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HIS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'HISS_CPLX', loc = 'cyt') +
	met(name = 'Charged_HIS_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_HISTIDINE__TRNA_LIGASE_RXN', 1.000000), 
	Parameter('rvs_HISTIDINE__TRNA_LIGASE_RXN', 0.000000))
Rule('HISTCYCLOHYD_RXN',
	prot(name = 'HISTCYCLOPRATPPHOS', loc = 'cyt') +
	met(name = 'PHOSPHORIBOSYL_AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'HISTCYCLOPRATPPHOS', loc = 'cyt') +
	met(name = 'PHOSPHORIBOSYL_FORMIMINO_AICAR_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_HISTCYCLOHYD_RXN', 1.000000), 
	Parameter('rvs_HISTCYCLOHYD_RXN', 0.000000))
Rule('HISTPRATPHYD_RXN',
	prot(name = 'HISTCYCLOPRATPPHOS', loc = 'cyt') +
	met(name = 'PHOSPHORIBOSYL_ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'HISTCYCLOPRATPPHOS', loc = 'cyt') +
	met(name = 'PHOSPHORIBOSYL_AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_HISTPRATPHYD_RXN', 1.000000), 
	Parameter('rvs_HISTPRATPHYD_RXN', 0.000000))
Rule('HISTALDEHYD_RXN',
	cplx(name = 'HISTDEHYD_CPLX', loc = 'cyt') +
	met(name = 'HISTIDINAL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'HISTDEHYD_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HIS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_HISTALDEHYD_RXN', 1.000000), 
	Parameter('rvs_HISTALDEHYD_RXN', 0.000000))
Rule('HISTOLDEHYD_RXN',
	cplx(name = 'HISTDEHYD_CPLX', loc = 'cyt') +
	met(name = 'HISTIDINOL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'HISTDEHYD_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HISTIDINAL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_HISTOLDEHYD_RXN', 1.000000), 
	Parameter('rvs_HISTOLDEHYD_RXN', 1.000000))
Rule('HISTAMINOTRANS_RXN',
	cplx(name = 'HISTPHOSTRANS_CPLX', loc = 'cyt') +
	met(name = 'L_HISTIDINOL_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'HISTPHOSTRANS_CPLX', loc = 'cyt') +
	met(name = 'IMIDAZOLE_ACETOL_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_HISTAMINOTRANS_RXN', 1.000000), 
	Parameter('rvs_HISTAMINOTRANS_RXN', 1.000000))
Rule('OHMETPYRKIN_RXN',
	cplx(name = 'HMP_P_KIN_CPLX', loc = 'cyt') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'HMP_P_KIN_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMINO_HYDROXYMETHYL_METHYL_PYR_P', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_OHMETPYRKIN_RXN', 1.000000), 
	Parameter('rvs_OHMETPYRKIN_RXN', 0.000000))
Rule('PYRIMSYN3_RXN',
	cplx(name = 'HMP_P_KIN_CPLX', loc = 'cyt') +
	met(name = 'AMINO_HYDROXYMETHYL_METHYL_PYR_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'HMP_P_KIN_CPLX', loc = 'cyt') +
	met(name = 'AMINO_HYDROXYMETHYL_METHYLPYRIMIDINE_PP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PYRIMSYN3_RXN', 1.000000), 
	Parameter('rvs_PYRIMSYN3_RXN', 0.000000))
Rule('HOMOCYSMET_RXN',
	prot(name = 'HOMOCYSMET_MONOMER', loc = 'ex') +
	met(name = 'CPD_1302', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'HOMOCYSMET_MONOMER', loc = 'ex') +
	met(name = 'MET', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_1301', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_HOMOCYSMET_RXN', 1.000000), 
	Parameter('rvs_HOMOCYSMET_RXN', 0.000000))
Rule('HOMOCYSMETB12_RXN',
	prot(name = 'HOMOCYSMETB12_MONOMER', loc = 'cyt') +
	met(name = 'HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_5_METHYL_THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'HOMOCYSMETB12_MONOMER', loc = 'cyt') +
	met(name = 'MET', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_HOMOCYSMETB12_RXN', 1.000000), 
	Parameter('rvs_HOMOCYSMETB12_RXN', 0.000000))
Rule('HOMOSERKIN_RXN',
	cplx(name = 'HOMOSERKIN_CPLX', loc = 'cyt') +
	met(name = 'HOMO_SER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'HOMOSERKIN_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'O_PHOSPHO_L_HOMOSERINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_HOMOSERKIN_RXN', 1.000000), 
	Parameter('rvs_HOMOSERKIN_RXN', 0.000000))
Rule('RXN0_6564',
	cplx(name = 'HOMOSERKIN_CPLX', loc = 'cyt') +
	met(name = 'CPD0_2189', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'HOMOSERKIN_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_4_PHOSPHONOOXY_THREONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6564', 1.000000), 
	Parameter('rvs_RXN0_6564', 0.000000))
Rule('HOMSUCTRAN_RXN',
	cplx(name = 'HOMSUCTRAN_CPLX', loc = 'cyt') +
	met(name = 'HOMO_SER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SUC_COA', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'HOMSUCTRAN_CPLX', loc = 'cyt') +
	met(name = 'O_SUCCINYL_L_HOMOSERINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_HOMSUCTRAN_RXN', 1.000000), 
	Parameter('rvs_HOMSUCTRAN_RXN', 0.000000))
Rule('HYDGLUTSYN_RXN',
	prot(name = 'HYDGLUTSYN_MONOMER', loc = 'cyt') +
	met(name = 'PROPIONYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLYOX', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'HYDGLUTSYN_MONOMER', loc = 'cyt') +
	met(name = '_2_HYDROXYGLUTARIC_ACID', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_HYDGLUTSYN_RXN', 1.000000), 
	Parameter('rvs_HYDGLUTSYN_RXN', 0.000000))
Rule('RXN_12275',
	cplx(name = 'HYDROG3_CPLX', loc = 'imem') +
	met(name = 'Reduced_hydrogenase_3', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'HYDROG3_CPLX', loc = 'imem') +
	met(name = 'HYDROGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Oxidized_hydrogenase_3', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_12275', 1.000000), 
	Parameter('rvs_RXN_12275', 0.000000))
Rule('RXN_8667',
	cplx(name = 'HYDROPEROXIDI_CPLX', loc = 'ex') +
	met(name = 'Donor_H2', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HYDROGEN_PEROXIDE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'HYDROPEROXIDI_CPLX', loc = 'ex') +
	met(name = 'Acceptor', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_8667', 1.000000), 
	Parameter('rvs_RXN_8667', 0.000000))
Rule('RXN_8073',
	cplx(name = 'HYDROPEROXIDII_CPLX', loc = 'cyt') +
	met(name = 'Heme_b', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HYDROGEN_PEROXIDE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'HYDROPEROXIDII_CPLX', loc = 'cyt') +
	met(name = 'HEME_D', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_8073', 1.000000), 
	Parameter('rvs_RXN_8073', 0.000000))
Rule('_1dot1dot1dot264_RXN',
	prot(name = 'IDONDEHYD_MONOMER', loc = 'cyt') +
	met(name = 'NAD_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_IDONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'IDONDEHYD_MONOMER', loc = 'cyt') +
	met(name = 'NADH_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_5_DEHYDROGLUCONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__1dot1dot1dot264_RXN', 1.000000), 
	Parameter('rvs__1dot1dot1dot264_RXN', 1.000000))
Rule('ISOLEUCINE__TRNA_LIGASE_RXN',
	prot(name = 'ILES_MONOMER', loc = 'cyt') +
	met(name = 'ILE_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ILE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'ILES_MONOMER', loc = 'cyt') +
	met(name = 'Charged_ILE_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ISOLEUCINE__TRNA_LIGASE_RXN', 1.000000), 
	Parameter('rvs_ISOLEUCINE__TRNA_LIGASE_RXN', 0.000000))
Rule('IMIDPHOSDEHYD_RXN',
	cplx(name = 'IMIDHISTID_CPLX', loc = 'cyt') +
	met(name = 'D_ERYTHRO_IMIDAZOLE_GLYCEROL_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'IMIDHISTID_CPLX', loc = 'cyt') +
	met(name = 'IMIDAZOLE_ACETOL_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_IMIDPHOSDEHYD_RXN', 1.000000), 
	Parameter('rvs_IMIDPHOSDEHYD_RXN', 0.000000))
Rule('IMP_DEHYDROG_RXN',
	cplx(name = 'IMP_DEHYDROG_CPLX', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'IMP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'IMP_DEHYDROG_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'XANTHOSINE_5_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_IMP_DEHYDROG_RXN', 1.000000), 
	Parameter('rvs_IMP_DEHYDROG_RXN', 1.000000))
Rule('IPPISOM_RXN',
	prot(name = 'IPPISOM_MONOMER', loc = 'cyt') +
	met(name = 'DELTA3_ISOPENTENYL_PP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'IPPISOM_MONOMER', loc = 'cyt') +
	met(name = 'CPD_4211', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_IPPISOM_RXN', 1.000000), 
	Parameter('rvs_IPPISOM_RXN', 1.000000))
Rule('ISOCIT_CLEAV_RXN',
	prot(name = 'ISOCIT_LYASE', loc = 'cyt') +
	met(name = 'THREO_DS_ISO_CITRATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'ISOCIT_LYASE', loc = 'cyt') +
	met(name = 'GLYOX', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SUC', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ISOCIT_CLEAV_RXN', 1.000000), 
	Parameter('rvs_ISOCIT_CLEAV_RXN', 1.000000))
Rule('ISOCITDEH_RXN',
	cplx(name = 'ISOCITHASE_CPLX', loc = 'cyt') +
	met(name = 'THREO_DS_ISO_CITRATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'ISOCITHASE_CPLX', loc = 'cyt') +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ISOCITDEH_RXN', 1.000000), 
	Parameter('rvs_ISOCITDEH_RXN', 1.000000))
Rule('KDO_8PPHOSPHAT_RXN',
	cplx(name = 'KDO_8PPHOSPHAT_CPLX', loc = 'cyt') +
	met(name = 'KDO_8P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'KDO_8PPHOSPHAT_CPLX', loc = 'cyt') +
	met(name = 'KDO', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_KDO_8PPHOSPHAT_RXN', 1.000000), 
	Parameter('rvs_KDO_8PPHOSPHAT_RXN', 0.000000))
Rule('KDO_8PSYNTH_RXN',
	cplx(name = 'KDO_8PSYNTH_CPLX', loc = 'cyt') +
	met(name = 'CPD_18118', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PHOSPHO_ENOL_PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'KDO_8PSYNTH_CPLX', loc = 'cyt') +
	met(name = 'KDO_8P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_KDO_8PSYNTH_RXN', 1.000000), 
	Parameter('rvs_KDO_8PSYNTH_RXN', 0.000000))
Rule('KDOTRANS2_RXN',
	prot(name = 'KDOTRANS_MONOMER', loc = 'imem') +
	met(name = 'KDO_LIPID_IVA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CMP_KDO', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'KDOTRANS_MONOMER', loc = 'imem') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'KDO2_LIPID_IVA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_KDOTRANS2_RXN', 1.000000), 
	Parameter('rvs_KDOTRANS2_RXN', 0.000000))
Rule('KDOTRANS_RXN',
	prot(name = 'KDOTRANS_MONOMER', loc = 'imem') +
	met(name = 'CMP_KDO', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'LIPID_IV_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'KDOTRANS_MONOMER', loc = 'imem') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'KDO_LIPID_IVA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_KDOTRANS_RXN', 1.000000), 
	Parameter('rvs_KDOTRANS_RXN', 0.000000))
Rule('KDPGALDOL_RXN',
	cplx(name = 'KDPGALDOL_4OH2OXOGLUTARALDOL_CPLX', loc = 'cyt') +
	met(name = '_2_KETO_3_DEOXY_6_P_GLUCONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'KDPGALDOL_4OH2OXOGLUTARALDOL_CPLX', loc = 'cyt') +
	met(name = 'GAP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_KDPGALDOL_RXN', 1.000000), 
	Parameter('rvs_KDPGALDOL_RXN', 0.000000))
Rule('RXN_13990',
	cplx(name = 'KDPGALDOL_4OH2OXOGLUTARALDOL_CPLX', loc = 'cyt') +
	met(name = 'CPD_15016', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'KDPGALDOL_4OH2OXOGLUTARALDOL_CPLX', loc = 'cyt') +
	met(name = 'GLYOX', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_13990', 1.000000), 
	Parameter('rvs_RXN_13990', 1.000000))
Rule('OXALODECARB_RXN',
	cplx(name = 'KDPGALDOL_4OH2OXOGLUTARALDOL_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXALACETIC_ACID', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'KDPGALDOL_4OH2OXOGLUTARALDOL_CPLX', loc = 'cyt') +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_OXALODECARB_RXN', 1.000000), 
	Parameter('rvs_OXALODECARB_RXN', 0.000000))
Rule('_1dot1dot1dot127_RXN',
	prot(name = 'KDUD_MONOMER', loc = 'cyt') +
	met(name = '_2_DEHYDRO_3_DEOXY_D_GLUCONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'KDUD_MONOMER', loc = 'cyt') +
	met(name = 'CPD_343', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__1dot1dot1dot127_RXN', 1.000000), 
	Parameter('rvs__1dot1dot1dot127_RXN', 1.000000))
Rule('RXN0_7101',
	prot(name = 'KDUD_MONOMER', loc = 'cyt') +
	met(name = 'GLUCONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'KDUD_MONOMER', loc = 'cyt') +
	met(name = '_5_DEHYDROGLUCONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7101', 1.000000), 
	Parameter('rvs_RXN0_7101', 1.000000))
Rule('RXN_15607',
	prot(name = 'KDUD_MONOMER', loc = 'cyt') +
	met(name = '_11_DEOXYCORTICOSTERONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'KDUD_MONOMER', loc = 'cyt') +
	met(name = 'CPD_16843', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_15607', 1.000000), 
	Parameter('rvs_RXN_15607', 0.000000))
Rule('KETOBUTFORMLY_RXN',
	prot(name = 'KETOBUTFORMLY_MONOMER', loc = 'cyt') +
	met(name = '_2_OXOBUTANOATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'KETOBUTFORMLY_MONOMER', loc = 'cyt') +
	met(name = 'PROPIONYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FORMATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_KETOBUTFORMLY_RXN', 1.000000), 
	Parameter('rvs_KETOBUTFORMLY_RXN', 0.000000))
Rule('PYRUVFORMLY_RXN',
	prot(name = 'KETOBUTFORMLY_MONOMER', loc = 'cyt') +
	met(name = 'FORMATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'KETOBUTFORMLY_MONOMER', loc = 'cyt') +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PYRUVFORMLY_RXN', 0.000000), 
	Parameter('rvs_PYRUVFORMLY_RXN', 1.000000))
Rule('L_ASPARTATE_OXID_RXN',
	prot(name = 'L_ASPARTATE_OXID_MONOMER', loc = 'cyt') +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_ASPARTATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'L_ASPARTATE_OXID_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HYDROGEN_PEROXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'IMINOASPARTATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_L_ASPARTATE_OXID_RXN', 1.000000), 
	Parameter('rvs_L_ASPARTATE_OXID_RXN', 0.000000))
Rule('RXN_9772',
	prot(name = 'L_ASPARTATE_OXID_MONOMER', loc = 'cyt') +
	met(name = 'L_ASPARTATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'L_ASPARTATE_OXID_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'IMINOASPARTATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SUC', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_9772', 1.000000), 
	Parameter('rvs_RXN_9772', 0.000000))
Rule('L_GLN_FRUCT_6_P_AMINOTRANS_RXN',
	cplx(name = 'L_GLN_FRUCT_6_P_AMINOTRANS_CPLX', loc = 'cyt') +
	met(name = 'FRUCTOSE_6P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLN', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'L_GLN_FRUCT_6_P_AMINOTRANS_CPLX', loc = 'cyt') +
	met(name = 'D_GLUCOSAMINE_6_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_L_GLN_FRUCT_6_P_AMINOTRANS_RXN', 1.000000), 
	Parameter('rvs_L_GLN_FRUCT_6_P_AMINOTRANS_RXN', 1.000000))
Rule('L_LACTDEHYDROGFMN_RXN',
	prot(name = 'L_LACTDEHYDROGFMN_MONOMER', loc = 'imem') +
	met(name = 'ETR_Quinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_LACTATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'L_LACTDEHYDROGFMN_MONOMER', loc = 'imem') +
	met(name = 'ETR_Quinols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_L_LACTDEHYDROGFMN_RXN', 1.000000), 
	Parameter('rvs_L_LACTDEHYDROGFMN_RXN', 0.000000))
Rule('RXN0_7227',
	prot(name = 'L_LACTDEHYDROGFMN_MONOMER', loc = 'imem') +
	met(name = 'ETR_Quinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_3564', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'L_LACTDEHYDROGFMN_MONOMER', loc = 'imem') +
	met(name = 'ETR_Quinols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_OXOBUTANOATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7227', 1.000000), 
	Parameter('rvs_RXN0_7227', 0.000000))
Rule('GLYCOLALDREDUCT_RXN',
	cplx(name = 'LACTALDREDUCT_CPLX', loc = 'cyt') +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLYCOL', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'LACTALDREDUCT_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLYCOLALDEHYDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLYCOLALDREDUCT_RXN', 1.000000), 
	Parameter('rvs_GLYCOLALDREDUCT_RXN', 1.000000))
Rule('LACTALDREDUCT_RXN',
	cplx(name = 'LACTALDREDUCT_CPLX', loc = 'cyt') +
	met(name = 'PROPANE_1_2_DIOL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'LACTALDREDUCT_CPLX', loc = 'cyt') +
	met(name = 'LACTALD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_LACTALDREDUCT_RXN', 1.000000), 
	Parameter('rvs_LACTALDREDUCT_RXN', 1.000000))
Rule('LAUROYLACYLTRAN_RXN',
	prot(name = 'LAUROYLACYLTRAN_MONOMER', loc = 'imem') +
	met(name = 'Dodecanoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'KDO2_LIPID_IVA', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'LAUROYLACYLTRAN_MONOMER', loc = 'imem') +
	met(name = 'KDO2_LAUROYL_LIPID_IVA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_LAUROYLACYLTRAN_RXN', 1.000000), 
	Parameter('rvs_LAUROYLACYLTRAN_RXN', 0.000000))
Rule('LYSDECARBOX_RXN',
	cplx(name = 'LDC2_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'LYS', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'LDC2_CPLX', loc = 'cyt') +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CADAVERINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_LYSDECARBOX_RXN', 1.000000), 
	Parameter('rvs_LYSDECARBOX_RXN', 0.000000))
Rule('LEUCINE__TRNA_LIGASE_RXN',
	prot(name = 'LEUS_MONOMER', loc = 'cyt') +
	met(name = 'LEU_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'LEU', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'LEUS_MONOMER', loc = 'cyt') +
	met(name = 'Charged_LEU_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_LEUCINE__TRNA_LIGASE_RXN', 1.000000), 
	Parameter('rvs_LEUCINE__TRNA_LIGASE_RXN', 0.000000))
Rule('RXN0_6563',
	cplx(name = 'LTAA_CPLX', loc = 'cyt') +
	met(name = 'CPD0_2189', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'LTAA_CPLX', loc = 'cyt') +
	met(name = 'GLYCOLALDEHYDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLY', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6563', 1.000000), 
	Parameter('rvs_RXN0_6563', 1.000000))
Rule('THREONINE_ALDOLASE_RXN',
	cplx(name = 'LTAA_CPLX', loc = 'cyt') +
	met(name = 'THR', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'LTAA_CPLX', loc = 'cyt') +
	met(name = 'ACETALD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLY', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_THREONINE_ALDOLASE_RXN', 1.000000), 
	Parameter('rvs_THREONINE_ALDOLASE_RXN', 0.000000))
Rule('PHENYLSERINE_ALDOLASE_RXN',
	cplx(name = 'LTAA_CPLX', loc = 'cyt') +
	met(name = 'CPD_644', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'LTAA_CPLX', loc = 'cyt') +
	met(name = 'BENZALDEHYDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLY', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PHENYLSERINE_ALDOLASE_RXN', 1.000000), 
	Parameter('rvs_PHENYLSERINE_ALDOLASE_RXN', 0.000000))
Rule('LTAA_RXN',
	cplx(name = 'LTAA_CPLX', loc = 'cyt') +
	met(name = 'L_ALLO_THREONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'LTAA_CPLX', loc = 'cyt') +
	met(name = 'GLY', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETALD', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_LTAA_RXN', 1.000000), 
	Parameter('rvs_LTAA_RXN', 0.000000))
Rule('LTARTDEHYDRA_RXN',
	cplx(name = 'LTARTDEHYDRA_CPLX', loc = 'cyt') +
	met(name = 'TARTRATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'LTARTDEHYDRA_CPLX', loc = 'cyt') +
	met(name = 'OXALACETIC_ACID', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_LTARTDEHYDRA_RXN', 1.000000), 
	Parameter('rvs_LTARTDEHYDRA_RXN', 0.000000))
Rule('LUMAZINESYN_RXN',
	cplx(name = 'LUMAZINESYN_CPLX', loc = 'cyt') +
	met(name = 'AMINO_RIBOSYLAMINO_1H_3H_PYR_DIONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DIHYDROXY_BUTANONE_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	cplx(name = 'LUMAZINESYN_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DIMETHYL_D_RIBITYL_LUMAZINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_LUMAZINESYN_RXN', 1.000000), 
	Parameter('rvs_LUMAZINESYN_RXN', 0.000000))
Rule('LYSINE__TRNA_LIGASE_RXN',
	cplx(name = 'LYSS_CPLX', loc = 'cyt') +
	met(name = 'LYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'LYS_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'LYSS_CPLX', loc = 'cyt') +
	met(name = 'Charged_LYS_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_LYSINE__TRNA_LIGASE_RXN', 1.000000), 
	Parameter('rvs_LYSINE__TRNA_LIGASE_RXN', 0.000000))
Rule('RXN0_5209',
	cplx(name = 'LYSU_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'LYSU_CPLX', loc = 'cyt') +
	met(name = 'ADENOSINE5TRIPHOSPHO5ADENOSINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_5209', 1.000000), 
	Parameter('rvs_RXN0_5209', 0.000000))
Rule('LYXK_RXN',
	cplx(name = 'LYXK_CPLX', loc = 'cyt') +
	met(name = 'L_XYLULOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'LYXK_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_XYLULOSE_5_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_LYXK_RXN', 1.000000), 
	Parameter('rvs_LYXK_RXN', 0.000000))
Rule('RXN0_704',
	cplx(name = 'LYXK_CPLX', loc = 'cyt') +
	met(name = '_3_KETO_L_GULONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'LYXK_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_2343', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_704', 1.000000), 
	Parameter('rvs_RXN0_704', 0.000000))
Rule('MALATE_DEH_RXN',
	prot(name = 'MALATE_DEHASE', loc = 'cyt') +
	met(name = 'MAL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'MALATE_DEHASE', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXALACETIC_ACID', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_MALATE_DEH_RXN', 1.000000), 
	Parameter('rvs_MALATE_DEH_RXN', 1.000000))
Rule('MALSYN_RXN',
	prot(name = 'MALATE_SYNTHASE', loc = 'cyt') +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLYOX', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'MALATE_SYNTHASE', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MAL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_MALSYN_RXN', 1.000000), 
	Parameter('rvs_MALSYN_RXN', 0.000000))
Rule('RXN_9025',
	cplx(name = 'MALDEXPHOSPHORYL_CPLX', loc = 'cyt') +
	met(name = 'CPD0_1027', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'MALDEXPHOSPHORYL_CPLX', loc = 'cyt') +
	met(name = 'GLC_1_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_9025', 1.000000), 
	Parameter('rvs_RXN_9025', 0.000000))
Rule('RXN_14286',
	cplx(name = 'MALDEXPHOSPHORYL_CPLX', loc = 'cyt') +
	met(name = 'CPD0_1133', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'MALDEXPHOSPHORYL_CPLX', loc = 'cyt') +
	met(name = 'MALTOHEXAOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLC_1_P', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14286', 1.000000), 
	Parameter('rvs_RXN_14286', 0.000000))
Rule('RXN_14285',
	cplx(name = 'MALDEXPHOSPHORYL_CPLX', loc = 'cyt') +
	met(name = 'MALTOHEXAOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'MALDEXPHOSPHORYL_CPLX', loc = 'cyt') +
	met(name = 'MALTOPENTAOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLC_1_P', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14285', 1.000000), 
	Parameter('rvs_RXN_14285', 0.000000))
Rule('RXN_14284',
	cplx(name = 'MALDEXPHOSPHORYL_CPLX', loc = 'cyt') +
	met(name = 'MALTOPENTAOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'MALDEXPHOSPHORYL_CPLX', loc = 'cyt') +
	met(name = 'GLC_1_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MALTOTETRAOSE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14284', 1.000000), 
	Parameter('rvs_RXN_14284', 0.000000))
Rule('_1dot1dot1dot39_RXN',
	cplx(name = 'MALIC_NAD_CPLX', loc = 'cyt') +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MAL', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'MALIC_NAD_CPLX', loc = 'cyt') +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__1dot1dot1dot39_RXN', 1.000000), 
	Parameter('rvs__1dot1dot1dot39_RXN', 0.000000))
Rule('MALIC_NADP_RXN',
	cplx(name = 'MALIC_NADP_CPLX', loc = 'cyt') +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MAL', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'MALIC_NADP_CPLX', loc = 'cyt') +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_MALIC_NADP_RXN', 1.000000), 
	Parameter('rvs_MALIC_NADP_RXN', 0.000000))
Rule('MALONYL_COA_ACP_TRANSACYL_RXN',
	prot(name = 'MALONYL_COA_ACP_TRANSACYL_MONOMER', loc = 'cyt') +
	met(name = 'ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MALONYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'MALONYL_COA_ACP_TRANSACYL_MONOMER', loc = 'cyt') +
	met(name = 'MALONYL_ACP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_MALONYL_COA_ACP_TRANSACYL_RXN', 1.000000), 
	Parameter('rvs_MALONYL_COA_ACP_TRANSACYL_RXN', 0.000000))
Rule('MALTACETYLTRAN_RXN',
	cplx(name = 'MALTACETYLTRAN_CPLX', loc = 'cyt') +
	met(name = 'MALTOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'MALTACETYLTRAN_CPLX', loc = 'cyt') +
	met(name = 'CPD_18529', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_MALTACETYLTRAN_RXN', 1.000000), 
	Parameter('rvs_MALTACETYLTRAN_RXN', 0.000000))
Rule('MANNKIN_RXN',
	prot(name = 'MANNKIN_MONOMER', loc = 'cyt') +
	met(name = 'D_mannopyranose', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'MANNKIN_MONOMER', loc = 'cyt') +
	met(name = 'CPD_15979', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_MANNKIN_RXN', 1.000000), 
	Parameter('rvs_MANNKIN_RXN', 0.000000))
Rule('MANNONDEHYDRAT_RXN',
	prot(name = 'MANNONDEHYDRAT_MONOMER', loc = 'cyt') +
	met(name = 'D_MANNONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'MANNONDEHYDRAT_MONOMER', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_DEHYDRO_3_DEOXY_D_GLUCONATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_MANNONDEHYDRAT_RXN', 1.000000), 
	Parameter('rvs_MANNONDEHYDRAT_RXN', 0.000000))
Rule('MANNONOXIDOREDUCT_RXN',
	prot(name = 'MANNONOXIDOREDUCT_MONOMER', loc = 'cyt') +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_MANNONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'MANNONOXIDOREDUCT_MONOMER', loc = 'cyt') +
	met(name = 'FRUCTURONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_MANNONOXIDOREDUCT_RXN', 1.000000), 
	Parameter('rvs_MANNONOXIDOREDUCT_RXN', 1.000000))
Rule('MANNPDEHYDROG_RXN',
	prot(name = 'MANNPDEHYDROG_MONOMER', loc = 'cyt') +
	met(name = 'MANNITOL_1P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'MANNPDEHYDROG_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FRUCTOSE_6P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_MANNPDEHYDROG_RXN', 1.000000), 
	Parameter('rvs_MANNPDEHYDROG_RXN', 1.000000))
Rule('_2dot7dot7dot13_RXN',
	prot(name = 'MANNPGUANYLTRANGDP_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MANNOSE_1P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GTP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'MANNPGUANYLTRANGDP_MONOMER', loc = 'cyt') +
	met(name = 'GDP_MANNOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd__2dot7dot7dot13_RXN', 1.000000), 
	Parameter('rvs__2dot7dot7dot13_RXN', 0.000000))
Rule('MANNPISOM_RXN',
	prot(name = 'MANNPISOM_MONOMER', loc = 'cyt') +
	met(name = 'CPD_15979', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'MANNPISOM_MONOMER', loc = 'cyt') +
	met(name = 'FRUCTOSE_6P', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_MANNPISOM_RXN', 1.000000), 
	Parameter('rvs_MANNPISOM_RXN', 1.000000))
Rule('O_SUCCINYLBENZOATE_COA_LIG_RXN',
	cplx(name = 'MENE_CPLX', loc = 'cyt') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'O_SUCCINYLBENZOATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'MENE_CPLX', loc = 'cyt') +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_6972', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_O_SUCCINYLBENZOATE_COA_LIG_RXN', 1.000000), 
	Parameter('rvs_O_SUCCINYLBENZOATE_COA_LIG_RXN', 0.000000))
Rule('RXN_16165',
	cplx(name = 'METG_CPLX', loc = 'cyt') +
	met(name = 'Initiation_tRNAmet', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MET', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'METG_CPLX', loc = 'cyt') +
	met(name = 'L_methionyl_tRNAfmet', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_16165', 1.000000), 
	Parameter('rvs_RXN_16165', 0.000000))
Rule('METHIONINE__TRNA_LIGASE_RXN',
	cplx(name = 'METG_CPLX', loc = 'cyt') +
	met(name = 'Elongation_tRNAMet', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MET', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'METG_CPLX', loc = 'cyt') +
	met(name = 'Charged_MET_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_METHIONINE__TRNA_LIGASE_RXN', 1.000000), 
	Parameter('rvs_METHIONINE__TRNA_LIGASE_RXN', 0.000000))
Rule('METHGLYSYN_RXN',
	cplx(name = 'METHGLYSYN_CPLX', loc = 'cyt') +
	met(name = 'DIHYDROXY_ACETONE_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'METHGLYSYN_CPLX', loc = 'cyt') +
	met(name = 'METHYL_GLYOXAL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_METHGLYSYN_RXN', 1.000000), 
	Parameter('rvs_METHGLYSYN_RXN', 0.000000))
Rule('_1dot5dot1dot20_RXN',
	cplx(name = 'METHYLENETHFREDUCT_CPLX', loc = 'cyt') +
	met(name = '_5_METHYL_THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'METHYLENETHFREDUCT_CPLX', loc = 'cyt') +
	met(name = 'METHYLENE_THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__1dot5dot1dot20_RXN', 0.000000), 
	Parameter('rvs__1dot5dot1dot20_RXN', 1.000000))
Rule('_1dot1dot1dot283_RXN',
	prot(name = 'METHYLGLYREDUCT_MONOMER', loc = 'cyt') +
	met(name = 'LACTALD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'METHYLGLYREDUCT_MONOMER', loc = 'cyt') +
	met(name = 'METHYL_GLYOXAL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__1dot1dot1dot283_RXN', 0.000000), 
	Parameter('rvs__1dot1dot1dot283_RXN', 1.000000))
Rule('METHYLMALONYL_COA_EPIM_RXN',
	prot(name = 'METHYLMALONYL_COA_EPIM_MONOMER', loc = 'cyt') +
	met(name = 'METHYL_MALONYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'METHYLMALONYL_COA_EPIM_MONOMER', loc = 'cyt') +
	met(name = 'D_METHYL_MALONYL_COA', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_METHYLMALONYL_COA_EPIM_RXN', 1.000000), 
	Parameter('rvs_METHYLMALONYL_COA_EPIM_RXN', 1.000000))
Rule('MHPELY_RXN',
	prot(name = 'MHPELY_MONOMER', loc = 'cyt') +
	met(name = '_4_HYDROXY_2_KETOVALERATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'MHPELY_MONOMER', loc = 'cyt') +
	met(name = 'ACETALD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_MHPELY_RXN', 1.000000), 
	Parameter('rvs_MHPELY_RXN', 1.000000))
Rule('MHPHYDROXY_RXN',
	prot(name = 'MHPHYDROXY_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_3_HYDROXYPHENYL_PROPIONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'MHPHYDROXY_MONOMER', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_3_DIHYDROXYPHENYL_PROPIONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_MHPHYDROXY_RXN', 1.000000), 
	Parameter('rvs_MHPHYDROXY_RXN', 0.000000))
Rule('RXN_10040',
	prot(name = 'MHPHYDROXY_MONOMER', loc = 'cyt') +
	met(name = 'CPD_10797', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'MHPHYDROXY_MONOMER', loc = 'cyt') +
	met(name = 'CPD_10796', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_10040', 1.000000), 
	Parameter('rvs_RXN_10040', 0.000000))
Rule('MMUM_RXN',
	prot(name = 'MMUM_MONOMER', loc = 'cyt') +
	met(name = 'CPD_397', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'MMUM_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MET', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_MMUM_RXN', 1.000000), 
	Parameter('rvs_MMUM_RXN', 0.000000))
Rule('RXN0_4701',
	prot(name = 'MONOMER0_1041', loc = 'cyt') +
	met(name = 'mRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'MONOMER0_1041', loc = 'cyt') +
	met(name = 'ssRNA_with_3phosphate', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ssRNA_with_5OH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_4701', 1.000000), 
	Parameter('rvs_RXN0_4701', 0.000000))
Rule('RXN0_1941',
	prot(name = 'MONOMER0_148', loc = 'cyt') +
	met(name = 'ETHYL_2R_METHYL_3S_HYDROXYBUTANOATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'MONOMER0_148', loc = 'cyt') +
	met(name = 'ETHYL_2_METHYLACETOACETATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_1941', 0.000000), 
	Parameter('rvs_RXN0_1941', 1.000000))
Rule('RXN0_7020',
	prot(name = 'MONOMER0_148', loc = 'cyt') +
	met(name = 'CPD_13059', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'MONOMER0_148', loc = 'cyt') +
	met(name = '_25_DIDEHYDRO_D_GLUCONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7020', 0.000000), 
	Parameter('rvs_RXN0_7020', 1.000000))
Rule('RXN0_5141',
	prot(name = 'MONOMER0_149', loc = 'cyt') +
	met(name = 'CPD_702', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'MONOMER0_149', loc = 'cyt') +
	met(name = 'CPD_703', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5141', 0.000000), 
	Parameter('rvs_RXN0_5141', 1.000000))
Rule('RXN0_5291',
	prot(name = 'MONOMER0_2838', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'THIAMINE_PYROPHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'MONOMER0_2838', loc = 'cyt') +
	met(name = 'CPD0_1095', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_5291', 1.000000), 
	Parameter('rvs_RXN0_5291', 1.000000))
Rule('RXN0_1402',
	prot(name = 'MONOMER0_702', loc = 'cyt') +
	met(name = 'RIBOSE_1P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'MONOMER0_702', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'RIBOSE_15_BISPHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_1402', 1.000000), 
	Parameter('rvs_RXN0_1402', 0.000000))
Rule('RXN0_2625',
	cplx(name = 'MUTHLS_CPLX', loc = 'cyt') +
	met(name = 'CPD_8199', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'MUTHLS_CPLX', loc = 'cyt') +
	met(name = 'CPD_8200', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_2625', 1.000000), 
	Parameter('rvs_RXN0_2625', 0.000000))
Rule('N_ACETYLGLUTPREDUCT_RXN',
	prot(name = 'N_ACETYLGLUTPREDUCT_MONOMER', loc = 'cyt') +
	met(name = 'CPD_469', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'N_ACETYLGLUTPREDUCT_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'N_ACETYL_GLUTAMYL_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_N_ACETYLGLUTPREDUCT_RXN', 1.000000), 
	Parameter('rvs_N_ACETYLGLUTPREDUCT_RXN', 1.000000))
Rule('N_ACETYLTRANSFER_RXN',
	cplx(name = 'N_ACETYLTRANSFER_CPLX', loc = 'cyt') +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'N_ACETYLTRANSFER_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETYL_GLU', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_N_ACETYLTRANSFER_RXN', 1.000000), 
	Parameter('rvs_N_ACETYLTRANSFER_RXN', 1.000000))
Rule('NACGLCTRANS_RXN',
	prot(name = 'NACGLCTRANS_MONOMER', loc = 'imem') +
	met(name = 'C5', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UDP_N_ACETYL_D_GLUCOSAMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'NACGLCTRANS_MONOMER', loc = 'imem') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'C6', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UDP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_NACGLCTRANS_RXN', 1.000000), 
	Parameter('rvs_NACGLCTRANS_RXN', 1.000000))
Rule('NAD_SYNTH_GLN_RXN',
	cplx(name = 'NAD_SYNTH_CPLX', loc = 'cyt') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DEAMIDO_NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'NAD_SYNTH_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_NAD_SYNTH_GLN_RXN', 1.000000), 
	Parameter('rvs_NAD_SYNTH_GLN_RXN', 0.000000))
Rule('NAD_SYNTH_NH3_RXN',
	cplx(name = 'NAD_SYNTH_CPLX', loc = 'cyt') +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DEAMIDO_NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'NAD_SYNTH_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_NAD_SYNTH_NH3_RXN', 1.000000), 
	Parameter('rvs_NAD_SYNTH_NH3_RXN', 0.000000))
Rule('NADH_DEHYDROG_A_RXN',
	cplx(name = 'NADH_DHI_CPLX', loc = 'imem') +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Ubiquinones', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'NADH_DHI_CPLX', loc = 'imem') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Ubiquinols', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_NADH_DEHYDROG_A_RXN', 1.000000), 
	Parameter('rvs_NADH_DEHYDROG_A_RXN', 1.000000))
Rule('RXN0_5388',
	cplx(name = 'NADH_DHI_CPLX', loc = 'imem') +
	met(name = 'Menaquinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'NADH_DHI_CPLX', loc = 'imem') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Menaquinols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5388', 1.000000), 
	Parameter('rvs_RXN0_5388', 0.000000))
Rule('RXN0_5330',
	prot(name = 'NADH_DHII_MONOMER', loc = 'imem') +
	met(name = 'Ubiquinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'NADH_DHII_MONOMER', loc = 'imem') +
	met(name = 'Ubiquinols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_5330', 1.000000), 
	Parameter('rvs_RXN0_5330', 0.000000))
Rule('RXN0_7123',
	prot(name = 'NADH_DHII_MONOMER', loc = 'imem') +
	met(name = 'Menaquinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'NADH_DHII_MONOMER', loc = 'imem') +
	met(name = 'Menaquinols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_7123', 1.000000), 
	Parameter('rvs_RXN0_7123', 0.000000))
Rule('R170_RXN',
	prot(name = 'NADH_DHII_MONOMER', loc = 'imem') +
	met(name = 'CUplus2', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'NADH_DHII_MONOMER', loc = 'imem') +
	met(name = 'CUplus', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_R170_RXN', 1.000000), 
	Parameter('rvs_R170_RXN', 0.000000))
Rule('RXN_13859',
	prot(name = 'NADNUCLEOSID_MONOMER', loc = 'mem') +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'NADNUCLEOSID_MONOMER', loc = 'mem') +
	met(name = 'ADENOSINE_DIPHOSPHATE_RIBOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NIACINAMIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_13859', 1.000000), 
	Parameter('rvs_RXN_13859', 0.000000))
Rule('NAG1P_URIDYLTRANS_RXN',
	cplx(name = 'NAG1P_URIDYLTRANS_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'N_ACETYL_D_GLUCOSAMINE_1_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UTP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'NAG1P_URIDYLTRANS_CPLX', loc = 'cyt') +
	met(name = 'UDP_N_ACETYL_D_GLUCOSAMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_NAG1P_URIDYLTRANS_RXN', 1.000000), 
	Parameter('rvs_NAG1P_URIDYLTRANS_RXN', 0.000000))
Rule('_2dot3dot1dot157_RXN',
	cplx(name = 'NAG1P_URIDYLTRANS_CPLX', loc = 'cyt') +
	met(name = 'GLUCOSAMINE_1P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'NAG1P_URIDYLTRANS_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'N_ACETYL_D_GLUCOSAMINE_1_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__2dot3dot1dot157_RXN', 1.000000), 
	Parameter('rvs__2dot3dot1dot157_RXN', 0.000000))
Rule('NAG6PDEACET_RXN',
	cplx(name = 'NAG6PDEACET_CPLX', loc = 'cyt') +
	met(name = 'N_ACETYL_D_GLUCOSAMINE_6_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'NAG6PDEACET_CPLX', loc = 'cyt') +
	met(name = 'D_GLUCOSAMINE_6_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACET', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_NAG6PDEACET_RXN', 1.000000), 
	Parameter('rvs_NAG6PDEACET_RXN', 0.000000))
Rule('NANE_RXN',
	prot(name = 'NANE_MONOMER', loc = 'cyt') +
	met(name = 'N_ACETYL_D_MANNOSAMINE_6P', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'NANE_MONOMER', loc = 'cyt') +
	met(name = 'N_ACETYL_D_GLUCOSAMINE_6_P', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_NANE_RXN', 1.000000), 
	Parameter('rvs_NANE_RXN', 1.000000))
Rule('NANK_RXN',
	prot(name = 'NANK_MONOMER', loc = 'cyt') +
	met(name = 'N_acetyl_D_mannosamine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'NANK_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'N_ACETYL_D_MANNOSAMINE_6P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_NANK_RXN', 1.000000), 
	Parameter('rvs_NANK_RXN', 0.000000))
Rule('NITRATE_REDUCTASE_CYTOCHROME_RXN',
	cplx(name = 'NAP_CPLX', loc = 'per') +
	met(name = 'Reduced_NapC_proteins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NITRATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'NAP_CPLX', loc = 'per') +
	met(name = 'Oxidized_NapC_proteins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NITRITE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_NITRATE_REDUCTASE_CYTOCHROME_RXN', 1.000000), 
	Parameter('rvs_NITRATE_REDUCTASE_CYTOCHROME_RXN', 0.000000))
Rule('RXN_14107',
	prot(name = 'NAPC_MONOMER', loc = 'imem') +
	met(name = 'Menaquinols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Cytochromes_C_Oxidized', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'NAPC_MONOMER', loc = 'imem') +
	met(name = 'Menaquinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Cytochromes_C_Reduced', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14107', 1.000000), 
	Parameter('rvs_RXN_14107', 0.000000))
Rule('RXN0_7297',
	cplx(name = 'NARX_CPLX', loc = 'imem') +
	met(name = 'PHOSPHO_NARL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'NARX_CPLX', loc = 'imem') +
	met(name = 'NARL_MONOMER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7297', 1.000000), 
	Parameter('rvs_RXN0_7297', 0.000000))
Rule('NICONUCADENYLYLTRAN_RXN',
	prot(name = 'NICONUCADENYLYLTRAN_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NICOTINATE_NUCLEOTIDE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'NICONUCADENYLYLTRAN_MONOMER', loc = 'cyt') +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DEAMIDO_NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_NICONUCADENYLYLTRAN_RXN', 1.000000), 
	Parameter('rvs_NICONUCADENYLYLTRAN_RXN', 0.000000))
Rule('NICOTINAMID_RXN',
	prot(name = 'NICOTINAMID_MONOMER', loc = 'cyt') +
	met(name = 'NIACINAMIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'NICOTINAMID_MONOMER', loc = 'cyt') +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NIACINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_NICOTINAMID_RXN', 1.000000), 
	Parameter('rvs_NICOTINAMID_RXN', 0.000000))
Rule('PYRAZIN_RXN',
	prot(name = 'NICOTINAMID_MONOMER', loc = 'cyt') +
	met(name = 'PYRAZINAMIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'NICOTINAMID_MONOMER', loc = 'cyt') +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRAZINOIC_ACID', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PYRAZIN_RXN', 1.000000), 
	Parameter('rvs_PYRAZIN_RXN', 0.000000))
Rule('NICOTINATEPRIBOSYLTRANS_RXN',
	prot(name = 'NICOTINATEPRIBOSYLTRANS_MONOMER', loc = 'cyt') +
	met(name = 'NIACINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PRPP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'NICOTINATEPRIBOSYLTRANS_MONOMER', loc = 'cyt') +
	met(name = 'NICOTINATE_NUCLEOTIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_NICOTINATEPRIBOSYLTRANS_RXN', 1.000000), 
	Parameter('rvs_NICOTINATEPRIBOSYLTRANS_RXN', 0.000000))
Rule('RXN0_3501',
	cplx(name = 'NITRATREDUCTA_CPLX', loc = 'imem') +
	met(name = 'Menaquinols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NITRATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'NITRATREDUCTA_CPLX', loc = 'imem') +
	met(name = 'Menaquinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NITRITE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_3501', 1.000000), 
	Parameter('rvs_RXN0_3501', 0.000000))
Rule('RXN0_7124',
	cplx(name = 'NITRATREDUCTA_CPLX', loc = 'imem') +
	met(name = 'Ubiquinols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NITRATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'NITRATREDUCTA_CPLX', loc = 'imem') +
	met(name = 'Ubiquinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NITRITE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7124', 1.000000), 
	Parameter('rvs_RXN0_7124', 0.000000))
Rule('RXN_13854',
	cplx(name = 'NITRITREDUCT_CPLX', loc = 'cyt') +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'NITRITREDUCT_CPLX', loc = 'cyt') +
	met(name = 'NITRITE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_13854', 0.000000), 
	Parameter('rvs_RXN_13854', 1.000000))
Rule('NMNNUCLEOSID_RXN',
	prot(name = 'NMNNUCLEOSID_MONOMER', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NICOTINAMIDE_NUCLEOTIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'NMNNUCLEOSID_MONOMER', loc = 'cyt') +
	met(name = 'CPD_15317', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NIACINAMIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_NMNNUCLEOSID_RXN', 1.000000), 
	Parameter('rvs_NMNNUCLEOSID_RXN', 0.000000))
Rule('NADH_DEHYDROGENASE_QUINONE_RXN',
	cplx(name = 'NQOR_CPLX', loc = 'cyt') +
	met(name = 'CPD_3766', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'NQOR_CPLX', loc = 'cyt') +
	met(name = 'MENADIOL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_NADH_DEHYDROGENASE_QUINONE_RXN', 1.000000), 
	Parameter('rvs_NADH_DEHYDROGENASE_QUINONE_RXN', 0.000000))
Rule('NUCLEOSIDE_DIP_KIN_RXN',
	cplx(name = 'NUCLEOSIDE_DIP_KIN_CPLX', loc = 'cyt') +
	met(name = 'Nucleoside_Diphosphates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'NUCLEOSIDE_DIP_KIN_CPLX', loc = 'cyt') +
	met(name = 'Nucleoside_Triphosphates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_NUCLEOSIDE_DIP_KIN_RXN', 1.000000), 
	Parameter('rvs_NUCLEOSIDE_DIP_KIN_RXN', 0.000000))
Rule('DUDPKIN_RXN',
	cplx(name = 'NUCLEOSIDE_DIP_KIN_CPLX', loc = 'cyt') +
	met(name = 'DUDP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'NUCLEOSIDE_DIP_KIN_CPLX', loc = 'cyt') +
	met(name = 'DUTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DUDPKIN_RXN', 1.000000), 
	Parameter('rvs_DUDPKIN_RXN', 0.000000))
Rule('DADPKIN_RXN',
	cplx(name = 'NUCLEOSIDE_DIP_KIN_CPLX', loc = 'cyt') +
	met(name = 'DADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'NUCLEOSIDE_DIP_KIN_CPLX', loc = 'cyt') +
	met(name = 'DATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DADPKIN_RXN', 1.000000), 
	Parameter('rvs_DADPKIN_RXN', 0.000000))
Rule('O_SUCCHOMOSERLYASE_RXN',
	cplx(name = 'O_SUCCHOMOSERLYASE_CPLX', loc = 'cyt') +
	met(name = 'CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'O_SUCCINYL_L_HOMOSERINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'O_SUCCHOMOSERLYASE_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SUC', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_CYSTATHIONINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_O_SUCCHOMOSERLYASE_RXN', 1.000000), 
	Parameter('rvs_O_SUCCHOMOSERLYASE_RXN', 1.000000))
Rule('METBALT_RXN',
	cplx(name = 'O_SUCCHOMOSERLYASE_CPLX', loc = 'cyt') +
	met(name = 'O_SUCCINYL_L_HOMOSERINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	cplx(name = 'O_SUCCHOMOSERLYASE_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_OXOBUTANOATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SUC', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_METBALT_RXN', 1.000000), 
	Parameter('rvs_METBALT_RXN', 0.000000))
Rule('O_SUCCINYLBENZOATE_COA_SYN_RXN',
	prot(name = 'O_SUCCINYLBENZOATE_COA_SYN_MONOMER', loc = 'cyt') +
	met(name = 'CPD_9923', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'O_SUCCINYLBENZOATE_COA_SYN_MONOMER', loc = 'cyt') +
	met(name = 'O_SUCCINYLBENZOATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_O_SUCCINYLBENZOATE_COA_SYN_RXN', 1.000000), 
	Parameter('rvs_O_SUCCINYLBENZOATE_COA_SYN_RXN', 0.000000))
Rule('_2_OCTAPRENYL_6_METHOXYPHENOL_HYDROX_RXN',
	prot(name = 'OCTAPRENYL_METHOXYPHENOL_OH_MONOMER', loc = 'cyt') +
	met(name = '_2_OCTAPRENYL_6_METHOXYPHENOL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'OCTAPRENYL_METHOXYPHENOL_OH_MONOMER', loc = 'cyt') +
	met(name = 'OCTAPRENYL_METHOXY_BENZOQUINONE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd__2_OCTAPRENYL_6_METHOXYPHENOL_HYDROX_RXN', 1.000000), 
	Parameter('rvs__2_OCTAPRENYL_6_METHOXYPHENOL_HYDROX_RXN', 0.000000))
Rule('OCTAPRENYL_METHYL_METHOXY_BENZOQ_OH_RXN',
	prot(name = 'OCTAPRENYL_METHYL_METHOXY_BENZOQ_OH_MON', loc = 'cyt') +
	met(name = 'OCTAPRENYL_METHYL_METHOXY_BENZQ', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Donor_H2', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'OCTAPRENYL_METHYL_METHOXY_BENZOQ_OH_MON', loc = 'cyt') +
	met(name = 'OCTAPRENYL_METHYL_OH_METHOXY_BENZQ', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Acceptor', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_OCTAPRENYL_METHYL_METHOXY_BENZOQ_OH_RXN', 1.000000), 
	Parameter('rvs_OCTAPRENYL_METHYL_METHOXY_BENZOQ_OH_RXN', 0.000000))
Rule('OHMETHYLBILANESYN_RXN',
	prot(name = 'OHMETHYLBILANESYN_MONOMER', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PORPHOBILINOGEN', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'OHMETHYLBILANESYN_MONOMER', loc = 'cyt') +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HYDROXYMETHYLBILANE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_OHMETHYLBILANESYN_RXN', 1.000000), 
	Parameter('rvs_OHMETHYLBILANESYN_RXN', 0.000000))
Rule('ORNCARBAMTRANSFER_RXN',
	cplx(name = 'ORNCARBAMTRANSFERF_CPLX', loc = 'cyt') +
	met(name = 'L_ORNITHINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBAMOYL_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'ORNCARBAMTRANSFERF_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_CITRULLINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ORNCARBAMTRANSFER_RXN', 1.000000), 
	Parameter('rvs_ORNCARBAMTRANSFER_RXN', 1.000000))
Rule('ORNDECARBOX_RXN',
	cplx(name = 'ORNDECARBOX_BIO_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_ORNITHINE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'ORNDECARBOX_BIO_CPLX', loc = 'cyt') +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PUTRESCINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_ORNDECARBOX_RXN', 1.000000), 
	Parameter('rvs_ORNDECARBOX_RXN', 0.000000))
Rule('OROPRIBTRANS_RXN',
	cplx(name = 'OROPRIBTRANS_CPLX', loc = 'cyt') +
	met(name = 'OROTIDINE_5_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'OROPRIBTRANS_CPLX', loc = 'cyt') +
	met(name = 'PRPP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OROTATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_OROPRIBTRANS_RXN', 1.000000), 
	Parameter('rvs_OROPRIBTRANS_RXN', 1.000000))
Rule('OROTPDECARB_RXN',
	cplx(name = 'OROTPDECARB_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OROTIDINE_5_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'OROTPDECARB_CPLX', loc = 'cyt') +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_OROTPDECARB_RXN', 1.000000), 
	Parameter('rvs_OROTPDECARB_RXN', 0.000000))
Rule('PABASYN_RXN',
	cplx(name = 'PABASYN_CPLX', loc = 'cyt') +
	met(name = 'GLN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CHORISMATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'PABASYN_CPLX', loc = 'cyt') +
	met(name = '_4_AMINO_4_DEOXYCHORISMATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PABASYN_RXN', 1.000000), 
	Parameter('rvs_PABASYN_RXN', 1.000000))
Rule('PALMITOTRANS_RXN',
	prot(name = 'PALMITOTRANS_MONOMER', loc = 'imem') +
	met(name = 'Palmitoleoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'KDO2_LIPID_IVA', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'PALMITOTRANS_MONOMER', loc = 'imem') +
	met(name = 'KDO2_PALMITOLEOYL_LIPID_IVA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PALMITOTRANS_RXN', 1.000000), 
	Parameter('rvs_PALMITOTRANS_RXN', 0.000000))
Rule('PANTOATE_BETA_ALANINE_LIG_RXN',
	cplx(name = 'PANTOATE_BETA_ALANINE_LIG_CPLX', loc = 'cyt') +
	met(name = 'B_ALANINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_PANTOATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'PANTOATE_BETA_ALANINE_LIG_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PANTOTHENATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PANTOATE_BETA_ALANINE_LIG_RXN', 1.000000), 
	Parameter('rvs_PANTOATE_BETA_ALANINE_LIG_RXN', 0.000000))
Rule('PANTOTHENATE_KIN_RXN',
	cplx(name = 'PANTOTHENATE_KIN_CPLX', loc = 'cyt') +
	met(name = 'PANTOTHENATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'PANTOTHENATE_KIN_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_4_P_PANTOTHENATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PANTOTHENATE_KIN_RXN', 1.000000), 
	Parameter('rvs_PANTOTHENATE_KIN_RXN', 0.000000))
Rule('_1dot8dot4dot8_RXN',
	cplx(name = 'PAPSSULFOTRANS_CPLX', loc = 'cyt') +
	met(name = '_3_5_ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SO3', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Ox_Thioredoxin', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'PAPSSULFOTRANS_CPLX', loc = 'cyt') +
	met(name = 'PAPS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Red_Thioredoxin', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None, 
	Parameter('fwd__1dot8dot4dot8_RXN', 0.000000), 
	Parameter('rvs__1dot8dot4dot8_RXN', 1.000000))
Rule('RXN_17823',
	prot(name = 'PD00230', loc = 'cyt') +
	met(name = 'CPD_19181', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROT_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'PD00230', loc = 'cyt') +
	met(name = 'CPD_19185', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Protein_S_methyl_L_cysteine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_17823', 1.000000), 
	Parameter('rvs_RXN_17823', 0.000000))
Rule('PNPOXI_RXN',
	cplx(name = 'PDXH_CPLX', loc = 'cyt') +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRIDOXINE_5P', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'PDXH_CPLX', loc = 'cyt') +
	met(name = 'HYDROGEN_PEROXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRIDOXAL_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PNPOXI_RXN', 1.000000), 
	Parameter('rvs_PNPOXI_RXN', 0.000000))
Rule('PMPOXI_RXN',
	cplx(name = 'PDXH_CPLX', loc = 'cyt') +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRIDOXAMINE_5P', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'PDXH_CPLX', loc = 'cyt') +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HYDROGEN_PEROXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRIDOXAL_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PMPOXI_RXN', 1.000000), 
	Parameter('rvs_PMPOXI_RXN', 0.000000))
Rule('PNKIN_RXN',
	cplx(name = 'PDXK_CPLX', loc = 'cyt') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRIDOXINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'PDXK_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRIDOXINE_5P', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PNKIN_RXN', 1.000000), 
	Parameter('rvs_PNKIN_RXN', 0.000000))
Rule('PYRAMKIN_RXN',
	cplx(name = 'PDXK_CPLX', loc = 'cyt') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRIDOXAMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'PDXK_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRIDOXAMINE_5P', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PYRAMKIN_RXN', 1.000000), 
	Parameter('rvs_PYRAMKIN_RXN', 0.000000))
Rule('PEPCARBOX_RXN',
	cplx(name = 'PEPCARBOX_CPLX', loc = 'cyt') +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXALACETIC_ACID', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'PEPCARBOX_CPLX', loc = 'cyt') +
	met(name = 'PHOSPHO_ENOL_PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HCO3', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PEPCARBOX_RXN', 0.000000), 
	Parameter('rvs_PEPCARBOX_RXN', 1.000000))
Rule('PEPCARBOXYKIN_RXN',
	prot(name = 'PEPCARBOXYKIN_MONOMER', loc = 'cyt') +
	met(name = 'OXALACETIC_ACID', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'PEPCARBOXYKIN_MONOMER', loc = 'cyt') +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PHOSPHO_ENOL_PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PEPCARBOXYKIN_RXN', 1.000000), 
	Parameter('rvs_PEPCARBOXYKIN_RXN', 0.000000))
Rule('PEPSYNTH_RXN',
	cplx(name = 'PEPSYNTH_CPLX', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'PEPSYNTH_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PHOSPHO_ENOL_PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PEPSYNTH_RXN', 1.000000), 
	Parameter('rvs_PEPSYNTH_RXN', 1.000000))
Rule('_1dot97dot1dot4_A_RXN',
	prot(name = 'PFLACTENZ_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRUVFORMLY_INACTIVE_CPLX', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Reduced_flavodoxins', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'PFLACTENZ_MONOMER', loc = 'cyt') +
	met(name = 'CH33ADO', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MET', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRUVFORMLY_CPLX', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Oxidized_flavodoxins', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__1dot97dot1dot4_A_RXN', 1.000000), 
	Parameter('rvs__1dot97dot1dot4_A_RXN', 0.000000))
Rule('TDCEACT1_RXN',
	prot(name = 'PFLACTENZ_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'KETOBUTFORMLY_INACT_MONOMER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Reduced_flavodoxins', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'PFLACTENZ_MONOMER', loc = 'cyt') +
	met(name = 'CH33ADO', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'KETOBUTFORMLY_MONOMER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Oxidized_flavodoxins', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_TDCEACT1_RXN', 1.000000), 
	Parameter('rvs_TDCEACT1_RXN', 0.000000))
Rule('PHOSGLYPHOS_RXN',
	prot(name = 'PGK', loc = 'cyt') +
	met(name = 'G3P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'PGK', loc = 'cyt') +
	met(name = 'DPG', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PHOSGLYPHOS_RXN', 1.000000), 
	Parameter('rvs_PHOSGLYPHOS_RXN', 1.000000))
Rule('PGLUCONDEHYDRAT_RXN',
	prot(name = 'PGLUCONDEHYDRAT_MONOMER', loc = 'cyt') +
	met(name = 'CPD_2961', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'PGLUCONDEHYDRAT_MONOMER', loc = 'cyt') +
	met(name = '_2_KETO_3_DEOXY_6_P_GLUCONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PGLUCONDEHYDRAT_RXN', 1.000000), 
	Parameter('rvs_PGLUCONDEHYDRAT_RXN', 0.000000))
Rule('PGLYCDEHYDROG_RXN',
	cplx(name = 'PGLYCDEHYDROG_CPLX', loc = 'cyt') +
	met(name = 'G3P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'PGLYCDEHYDROG_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_3_P_HYDROXYPYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PGLYCDEHYDROG_RXN', 1.000000), 
	Parameter('rvs_PGLYCDEHYDROG_RXN', 1.000000))
Rule('KETOGLUTREDUCT_RXN',
	cplx(name = 'PGLYCDEHYDROG_CPLX', loc = 'cyt') +
	met(name = 'R_2_HYDROXYGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'PGLYCDEHYDROG_CPLX', loc = 'cyt') +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_KETOGLUTREDUCT_RXN', 1.000000), 
	Parameter('rvs_KETOGLUTREDUCT_RXN', 1.000000))
Rule('RXN_16701',
	cplx(name = 'PGLYCDEHYDROG_CPLX', loc = 'cyt') +
	met(name = 'CPD_381', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'PGLYCDEHYDROG_CPLX', loc = 'cyt') +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_16701', 1.000000), 
	Parameter('rvs_RXN_16701', 1.000000))
Rule('PGLYCEROLTRANSI_RXN',
	prot(name = 'PGLYCEROLTRANSI_MONOMER', loc = 'imem') +
	met(name = 'MDO_D_Glucoses', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_1_PHOSPHATIDYL_GLYCEROL', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'PGLYCEROLTRANSI_MONOMER', loc = 'imem') +
	met(name = 'CPD_16400', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DIACYLGLYCEROL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PGLYCEROLTRANSI_RXN', 1.000000), 
	Parameter('rvs_PGLYCEROLTRANSI_RXN', 1.000000))
Rule('_3PGAREARR_RXN',
	prot(name = 'PGMI_MONOMER', loc = 'cyt') +
	met(name = '_2_PG', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'PGMI_MONOMER', loc = 'cyt') +
	met(name = 'G3P', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__3PGAREARR_RXN', 1.000000), 
	Parameter('rvs__3PGAREARR_RXN', 1.000000))
Rule('RXN_11277',
	prot(name = 'PGPPHOSPHAB_MONOMER', loc = 'imem') +
	met(name = 'DIACYLGLYCEROL_PYROPHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'PGPPHOSPHAB_MONOMER', loc = 'imem') +
	met(name = 'L_PHOSPHATIDATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11277', 1.000000), 
	Parameter('rvs_RXN_11277', 0.000000))
Rule('PHENDEHYD_RXN',
	cplx(name = 'PHENDEHYD_CPLX', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PHENYLACETALDEHYDE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'PHENDEHYD_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PHENYLACETATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PHENDEHYD_RXN', 1.000000), 
	Parameter('rvs_PHENDEHYD_RXN', 0.000000))
Rule('RXN_12071',
	prot(name = 'PHENPRODIOLDEHYDROG_MONOMER', loc = 'cyt') +
	met(name = 'CPD_13034', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'PHENPRODIOLDEHYDROG_MONOMER', loc = 'cyt') +
	met(name = 'CPD_10796', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_12071', 1.000000), 
	Parameter('rvs_RXN_12071', 0.000000))
Rule('PHENPRODIOLDEHYDROG_RXN',
	prot(name = 'PHENPRODIOLDEHYDROG_MONOMER', loc = 'cyt') +
	met(name = 'CARBOXYETHYL_3_5_CYCLOHEXADIENE_1_2_DIOL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'PHENPRODIOLDEHYDROG_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_3_DIHYDROXYPHENYL_PROPIONATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PHENPRODIOLDEHYDROG_RXN', 1.000000), 
	Parameter('rvs_PHENPRODIOLDEHYDROG_RXN', 0.000000))
Rule('PHENYLALANINE__TRNA_LIGASE_RXN',
	cplx(name = 'PHES_CPLX', loc = 'cyt') +
	met(name = 'PHE_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PHE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'PHES_CPLX', loc = 'cyt') +
	met(name = 'Charged_PHE_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PHENYLALANINE__TRNA_LIGASE_RXN', 1.000000), 
	Parameter('rvs_PHENYLALANINE__TRNA_LIGASE_RXN', 0.000000))
Rule('PTAALT_RXN',
	cplx(name = 'PHOSACETYLTRANS_CPLX', loc = 'cyt') +
	met(name = 'PROPIONYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'PHOSACETYLTRANS_CPLX', loc = 'cyt') +
	met(name = 'PROPIONYL_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PTAALT_RXN', 1.000000), 
	Parameter('rvs_PTAALT_RXN', 0.000000))
Rule('_5dot4dot2dot10_RXN',
	prot(name = 'PHOSGLUCOSAMINEMUT_MONOMER', loc = 'cyt') +
	met(name = 'D_GLUCOSAMINE_6_P', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'PHOSGLUCOSAMINEMUT_MONOMER', loc = 'cyt') +
	met(name = 'GLUCOSAMINE_1P', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__5dot4dot2dot10_RXN', 1.000000), 
	Parameter('rvs__5dot4dot2dot10_RXN', 1.000000))
Rule('RXN_15513',
	prot(name = 'PHOSGLYCMUTASE', loc = 'cyt') +
	met(name = '_2_PG', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'PHOSGLYCMUTASE', loc = 'cyt') +
	met(name = 'G3P', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_15513', 1.000000), 
	Parameter('rvs_RXN_15513', 1.000000))
Rule('PHOSMANMUT_RXN',
	prot(name = 'PHOSMANMUT_MONOMER', loc = 'cyt') +
	met(name = 'MANNOSE_1P', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'PHOSMANMUT_MONOMER', loc = 'cyt') +
	met(name = 'CPD_15979', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PHOSMANMUT_RXN', 1.000000), 
	Parameter('rvs_PHOSMANMUT_RXN', 1.000000))
Rule('PHOSNACMURPENTATRANS_RXN',
	prot(name = 'PHOSNACMURPENTATRANS_MONOMER', loc = 'imem') +
	met(name = 'C1', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_9646', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'PHOSNACMURPENTATRANS_MONOMER', loc = 'imem') +
	met(name = 'C5', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PHOSNACMURPENTATRANS_RXN', 1.000000), 
	Parameter('rvs_PHOSNACMURPENTATRANS_RXN', 0.000000))
Rule('PHOSPHAGLYPSYN_RXN',
	prot(name = 'PHOSPHAGLYPSYN_MONOMER', loc = 'imem') +
	met(name = 'CDPDIACYLGLYCEROL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLYCEROL_3P', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'PHOSPHAGLYPSYN_MONOMER', loc = 'imem') +
	met(name = 'CMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_1_PHOSPHATIDYL_GLYCEROL_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PHOSPHAGLYPSYN_RXN', 1.000000), 
	Parameter('rvs_PHOSPHAGLYPSYN_RXN', 0.000000))
Rule('PHOSPHASERDECARB_RXN',
	cplx(name = 'PHOSPHASERDECARB_DIMER', loc = 'cyt') +
	met(name = 'L_1_PHOSPHATIDYL_SERINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'PHOSPHASERDECARB_DIMER', loc = 'cyt') +
	met(name = 'L_1_PHOSPHATIDYL_ETHANOLAMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PHOSPHASERDECARB_RXN', 1.000000), 
	Parameter('rvs_PHOSPHASERDECARB_RXN', 0.000000))
Rule('PHOSPHASERSYN_RXN',
	cplx(name = 'PHOSPHASERSYN_CPLX', loc = 'cyt') +
	met(name = 'CDPDIACYLGLYCEROL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'PHOSPHASERSYN_CPLX', loc = 'cyt') +
	met(name = 'CMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_1_PHOSPHATIDYL_SERINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PHOSPHASERSYN_RXN', 1.000000), 
	Parameter('rvs_PHOSPHASERSYN_RXN', 1.000000))
Rule('MCPMETEST_RXN',
	prot(name = 'PHOSPHO_CHEB', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'protein_L_glutamate_O4_methyl_ester', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'PHOSPHO_CHEB', loc = 'cyt') +
	met(name = 'Protein_alpha_L_Glutamates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'METOH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_MCPMETEST_RXN', 1.000000), 
	Parameter('rvs_MCPMETEST_RXN', 0.000000))
Rule('CHEBDEAMID_RXN',
	prot(name = 'PHOSPHO_CHEB', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Protein_L_glutamine', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'PHOSPHO_CHEB', loc = 'cyt') +
	met(name = 'Protein_alpha_L_Glutamates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_CHEBDEAMID_RXN', 1.000000), 
	Parameter('rvs_CHEBDEAMID_RXN', 0.000000))
Rule('MCPTAP_RXN',
	prot(name = 'PHOSPHO_CHEB', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TAP_GLUME', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'PHOSPHO_CHEB', loc = 'cyt') +
	met(name = 'METOH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TAP_GLU', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_MCPTAP_RXN', 1.000000), 
	Parameter('rvs_MCPTAP_RXN', 0.000000))
Rule('MCPTAR_RXN',
	prot(name = 'PHOSPHO_CHEB', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TAR_GLUME', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'PHOSPHO_CHEB', loc = 'cyt') +
	met(name = 'METOH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TAR_GLU', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_MCPTAR_RXN', 1.000000), 
	Parameter('rvs_MCPTAR_RXN', 0.000000))
Rule('MCPTRG_RXN',
	prot(name = 'PHOSPHO_CHEB', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TRG_GLUME', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'PHOSPHO_CHEB', loc = 'cyt') +
	met(name = 'METOH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TRG_GLU', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_MCPTRG_RXN', 1.000000), 
	Parameter('rvs_MCPTRG_RXN', 0.000000))
Rule('MCPTSR_RXN',
	prot(name = 'PHOSPHO_CHEB', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TSR_GLUME', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'PHOSPHO_CHEB', loc = 'cyt') +
	met(name = 'METOH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TSR_GLU', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_MCPTSR_RXN', 1.000000), 
	Parameter('rvs_MCPTSR_RXN', 0.000000))
Rule('CHEBTSRD_RXN',
	prot(name = 'PHOSPHO_CHEB', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TSR_GLN', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'PHOSPHO_CHEB', loc = 'cyt') +
	met(name = 'AMMONIA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TSR_GLU', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_CHEBTSRD_RXN', 1.000000), 
	Parameter('rvs_CHEBTSRD_RXN', 0.000000))
Rule('CHEBTRGD_RXN',
	prot(name = 'PHOSPHO_CHEB', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TRG_GLN', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'PHOSPHO_CHEB', loc = 'cyt') +
	met(name = 'AMMONIA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TRG_GLU', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_CHEBTRGD_RXN', 1.000000), 
	Parameter('rvs_CHEBTRGD_RXN', 0.000000))
Rule('CHEBTARD_RXN',
	prot(name = 'PHOSPHO_CHEB', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TAR_GLN', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'PHOSPHO_CHEB', loc = 'cyt') +
	met(name = 'AMMONIA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TAR_GLU', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_CHEBTARD_RXN', 1.000000), 
	Parameter('rvs_CHEBTARD_RXN', 0.000000))
Rule('CHEBTAPD_RXN',
	prot(name = 'PHOSPHO_CHEB', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TAP_GLN', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'PHOSPHO_CHEB', loc = 'cyt') +
	met(name = 'AMMONIA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TAP_GLU', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_CHEBTAPD_RXN', 1.000000), 
	Parameter('rvs_CHEBTAPD_RXN', 0.000000))
Rule('PHOSPHOGLUCMUT_RXN',
	prot(name = 'PHOSPHOGLUCMUT_MONOMER', loc = 'cyt') +
	met(name = 'GLC_1_P', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'PHOSPHOGLUCMUT_MONOMER', loc = 'cyt') +
	met(name = 'D_glucopyranose_6_phosphate', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PHOSPHOGLUCMUT_RXN', 1.000000), 
	Parameter('rvs_PHOSPHOGLUCMUT_RXN', 1.000000))
Rule('PEPDEPHOS_RXN',
	cplx(name = 'PKI_COMPLEX', loc = 'cyt') +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'PKI_COMPLEX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PHOSPHO_ENOL_PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PEPDEPHOS_RXN', 0.000000), 
	Parameter('rvs_PEPDEPHOS_RXN', 1.000000))
Rule('PORPHOBILSYNTH_RXN',
	cplx(name = 'PORPHOBILSYNTH_CPLX', loc = 'cyt') +
	met(name = '_5_AMINO_LEVULINATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	cplx(name = 'PORPHOBILSYNTH_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PORPHOBILINOGEN', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PORPHOBILSYNTH_RXN', 1.000000), 
	Parameter('rvs_PORPHOBILSYNTH_RXN', 0.000000))
Rule('D_PPENTOMUT_RXN',
	prot(name = 'PPENTOMUT_MONOMER', loc = 'cyt') +
	met(name = 'DEOXY_D_RIBOSE_1_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'PPENTOMUT_MONOMER', loc = 'cyt') +
	met(name = 'DEOXY_RIBOSE_5P', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_D_PPENTOMUT_RXN', 1.000000), 
	Parameter('rvs_D_PPENTOMUT_RXN', 1.000000))
Rule('PPENTOMUT_RXN',
	prot(name = 'PPENTOMUT_MONOMER', loc = 'cyt') +
	met(name = 'RIBOSE_1P', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'PPENTOMUT_MONOMER', loc = 'cyt') +
	met(name = 'RIBOSE_5P', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PPENTOMUT_RXN', 1.000000), 
	Parameter('rvs_PPENTOMUT_RXN', 1.000000))
Rule('POLYPHOSPHATE_KINASE_RXN',
	cplx(name = 'PPK_CPLX', loc = 'omem') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Long_Chain_Polyphosphate', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'PPK_CPLX', loc = 'omem') +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Long_Chain_Polyphosphate', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_POLYPHOSPHATE_KINASE_RXN', 1.000000), 
	Parameter('rvs_POLYPHOSPHATE_KINASE_RXN', 1.000000))
Rule('PPPGPPHYDRO_RXN',
	cplx(name = 'PPPGPPHYDRO_CPLX', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GDP_TP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'PPPGPPHYDRO_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GUANOSINE_5DP_3DP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PPPGPPHYDRO_RXN', 1.000000), 
	Parameter('rvs_PPPGPPHYDRO_RXN', 0.000000))
Rule('EXOPOLYPHOSPHATASE_RXN',
	cplx(name = 'PPX_CPLX', loc = 'cyt') +
	met(name = 'Long_Chain_Polyphosphate', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'PPX_CPLX', loc = 'cyt') +
	met(name = 'Long_Chain_Polyphosphate', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_EXOPOLYPHOSPHATASE_RXN', 1.000000), 
	Parameter('rvs_EXOPOLYPHOSPHATASE_RXN', 0.000000))
Rule('IGPSYN_RXN',
	prot(name = 'PRAI_IGPS', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBOXYPHENYLAMINO_DEOXYRIBULOSE_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'PRAI_IGPS', loc = 'cyt') +
	met(name = 'INDOLE_3_GLYCEROL_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_IGPSYN_RXN', 1.000000), 
	Parameter('rvs_IGPSYN_RXN', 0.000000))
Rule('PRAISOM_RXN',
	prot(name = 'PRAI_IGPS', loc = 'cyt') +
	met(name = 'N_5_PHOSPHORIBOSYL_ANTHRANILATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'PRAI_IGPS', loc = 'cyt') +
	met(name = 'CARBOXYPHENYLAMINO_DEOXYRIBULOSE_P', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PRAISOM_RXN', 1.000000), 
	Parameter('rvs_PRAISOM_RXN', 0.000000))
Rule('PRIBFAICARPISOM_RXN',
	prot(name = 'PRIBFAICARPISOM_MONOMER', loc = 'cyt') +
	met(name = 'PHOSPHORIBOSYL_FORMIMINO_AICAR_P', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'PRIBFAICARPISOM_MONOMER', loc = 'cyt') +
	met(name = 'PHOSPHORIBULOSYL_FORMIMINO_AICAR_P', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PRIBFAICARPISOM_RXN', 1.000000), 
	Parameter('rvs_PRIBFAICARPISOM_RXN', 0.000000))
Rule('PROPIONYL_COA_CARBOXY_RXN',
	prot(name = 'PROPIONYL_COA_CARBOXY_MONOMER', loc = 'cyt') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HCO3', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROPIONYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'PROPIONYL_COA_CARBOXY_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_METHYL_MALONYL_COA', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PROPIONYL_COA_CARBOXY_RXN', 1.000000), 
	Parameter('rvs_PROPIONYL_COA_CARBOXY_RXN', 1.000000))
Rule('PROLINE__TRNA_LIGASE_RXN',
	cplx(name = 'PROS_CPLX', loc = 'cyt') +
	met(name = 'PRO_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PRO', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'PROS_CPLX', loc = 'cyt') +
	met(name = 'Charged_PRO_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PROLINE__TRNA_LIGASE_RXN', 1.000000), 
	Parameter('rvs_PROLINE__TRNA_LIGASE_RXN', 0.000000))
Rule('PRPPAMIDOTRANS_RXN',
	cplx(name = 'PRPPAMIDOTRANS_CPLX', loc = 'cyt') +
	met(name = '_5_P_BETA_D_RIBOSYL_AMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'PRPPAMIDOTRANS_CPLX', loc = 'cyt') +
	met(name = 'PRPP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PRPPAMIDOTRANS_RXN', 0.000000), 
	Parameter('rvs_PRPPAMIDOTRANS_RXN', 1.000000))
Rule('PRPPSYN_RXN',
	prot(name = 'PRPPSYN_MONOMER', loc = 'cyt') +
	met(name = 'RIBOSE_5P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'PRPPSYN_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PRPP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PRPPSYN_RXN', 1.000000), 
	Parameter('rvs_PRPPSYN_RXN', 0.000000))
Rule('PSERTRANSAM_RXN',
	cplx(name = 'PSERTRANSAM_CPLX', loc = 'cyt') +
	met(name = '_3_P_SERINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'PSERTRANSAM_CPLX', loc = 'cyt') +
	met(name = '_3_P_HYDROXYPYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PSERTRANSAM_RXN', 1.000000), 
	Parameter('rvs_PSERTRANSAM_RXN', 1.000000))
Rule('PSERTRANSAMPYR_RXN',
	cplx(name = 'PSERTRANSAM_CPLX', loc = 'cyt') +
	met(name = '_3OH_4P_OH_ALPHA_KETOBUTYRATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'PSERTRANSAM_CPLX', loc = 'cyt') +
	met(name = '_4_PHOSPHONOOXY_THREONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PSERTRANSAMPYR_RXN', 1.000000), 
	Parameter('rvs_PSERTRANSAMPYR_RXN', 1.000000))
Rule('RXN0_743',
	cplx(name = 'PURE_CPLX', loc = 'cyt') +
	met(name = 'CPD0_181', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'PURE_CPLX', loc = 'cyt') +
	met(name = 'PHOSPHORIBOSYL_CARBOXY_AMINOIMIDAZOLE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_743', 1.000000), 
	Parameter('rvs_RXN0_743', 0.000000))
Rule('RXN0_742',
	cplx(name = 'PURK_CPLX', loc = 'cyt') +
	met(name = '_5_PHOSPHORIBOSYL_5_AMINOIMIDAZOLE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HCO3', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'PURK_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_181', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_742', 1.000000), 
	Parameter('rvs_RXN0_742', 0.000000))
Rule('RXN0_7008',
	cplx(name = 'PUTA_CPLX', loc = 'imem') +
	met(name = 'Ubiquinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PRO', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'PUTA_CPLX', loc = 'imem') +
	met(name = 'Ubiquinols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_DELTA1_PYRROLINE_5_CARBOXYLATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7008', 1.000000), 
	Parameter('rvs_RXN0_7008', 0.000000))
Rule('RXN_14116',
	cplx(name = 'PUTA_CPLX', loc = 'imem') +
	met(name = 'L_GLUTAMATE_GAMMA_SEMIALDEHYDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'PUTA_CPLX', loc = 'imem') +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14116', 1.000000), 
	Parameter('rvs_RXN_14116', 0.000000))
Rule('RXN0_7074',
	prot(name = 'PYRDAMPTRANS_MONOMER', loc = 'cyt') +
	met(name = 'PYRIDOXAMINE_5P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Deaminated_Amine_Donors', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'PYRDAMPTRANS_MONOMER', loc = 'cyt') +
	met(name = 'PYRIDOXAL_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Aminated_Amine_Donors', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7074', 1.000000), 
	Parameter('rvs_RXN0_7074', 1.000000))
Rule('PYROXALTRANSAM_RXN',
	prot(name = 'PYROXALTRANSAM_MONOMER', loc = 'cyt') +
	met(name = 'PYRIDOXAMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'OXALACETIC_ACID', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'PYROXALTRANSAM_MONOMER', loc = 'cyt') +
	met(name = 'PYRIDOXAL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_ASPARTATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PYROXALTRANSAM_RXN', 1.000000), 
	Parameter('rvs_PYROXALTRANSAM_RXN', 1.000000))
Rule('PYRROLINECARBREDUCT_RXN',
	cplx(name = 'PYRROLINECARBREDUCT_CPLX', loc = 'cyt') +
	met(name = 'NAD_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PRO', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'PYRROLINECARBREDUCT_CPLX', loc = 'cyt') +
	met(name = 'NADH_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_DELTA1_PYRROLINE_5_CARBOXYLATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PYRROLINECARBREDUCT_RXN', 0.000000), 
	Parameter('rvs_PYRROLINECARBREDUCT_RXN', 1.000000))
Rule('PYRUFLAVREDUCT_RXN',
	prot(name = 'PYRUFLAVREDUCT_MONOMER', loc = 'cyt') +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Oxidized_ferredoxins', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'PYRUFLAVREDUCT_MONOMER', loc = 'cyt') +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Reduced_ferredoxins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PYRUFLAVREDUCT_RXN', 1.000000), 
	Parameter('rvs_PYRUFLAVREDUCT_RXN', 1.000000))
Rule('PYRUVDEH_RXN',
	cplx(name = 'PYRUVATEDEH_CPLX', loc = 'cyt') +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'PYRUVATEDEH_CPLX', loc = 'cyt') +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PYRUVDEH_RXN', 1.000000), 
	Parameter('rvs_PYRUVDEH_RXN', 0.000000))
Rule('RXN_11496',
	cplx(name = 'PYRUVOXID_CPLX', loc = 'imem') +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Ubiquinones', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'PYRUVOXID_CPLX', loc = 'imem') +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Ubiquinols', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACET', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11496', 1.000000), 
	Parameter('rvs_RXN_11496', 0.000000))
Rule('RXN0_2022',
	cplx(name = 'PYRUVOXID_CPLX', loc = 'imem') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETALD', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'PYRUVOXID_CPLX', loc = 'imem') +
	met(name = 'ACETOIN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_2022', 1.000000), 
	Parameter('rvs_RXN0_2022', 0.000000))
Rule('QOR_RXN',
	cplx(name = 'QOR_CPLX', loc = 'cyt') +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Quinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'QOR_CPLX', loc = 'cyt') +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Semiquinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_QOR_RXN', 1.000000), 
	Parameter('rvs_QOR_RXN', 0.000000))
Rule('QUINOPRIBOTRANS_RXN',
	cplx(name = 'QUINOPRIBOTRANS_CPLX', loc = 'cyt') +
	met(name = 'NICOTINATE_NUCLEOTIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'QUINOPRIBOTRANS_CPLX', loc = 'cyt') +
	met(name = 'PRPP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'QUINOLINATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_QUINOPRIBOTRANS_RXN', 0.000000), 
	Parameter('rvs_QUINOPRIBOTRANS_RXN', 1.000000))
Rule('RXN_19004',
	prot(name = 'RECBCD', loc = 'cyt') +
	met(name = 'a_double_stranded_DNA_with_a_blunt_end', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'EG10823_MONOMER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'RECBCD', loc = 'cyt') +
	met(name = 'A_DOUBLE_STRANDED_DNA_WITH_A_3_OVERHANG', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_19004', 1.000000), 
	Parameter('rvs_RXN_19004', 0.000000))
Rule('RXN0_2605',
	prot(name = 'RECBCD', loc = 'cyt') +
	met(name = 'Double_Stranded_DNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'RECBCD', loc = 'cyt') +
	met(name = '_5_phosphooligonucleotides', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_2605', 1.000000), 
	Parameter('rvs_RXN0_2605', 0.000000))
Rule('RXN0_2606',
	cplx(name = 'RECFOR_CPLX', loc = 'cyt') +
	met(name = 'Unstable_RecA_Filament_DNA_Complex', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'RECFOR_CPLX', loc = 'cyt') +
	met(name = 'Stabilized_RecA_Filament_DNA_Complex', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_2606', 1.000000), 
	Parameter('rvs_RXN0_2606', 0.000000))
Rule('RXN_18586',
	prot(name = 'RED_GLUTAREDOXIN', loc = 'cyt') +
	met(name = 'SULFO_CYSTEINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Red_Glutaredoxins', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	prot(name = 'RED_GLUTAREDOXIN', loc = 'cyt') +
	met(name = 'CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SO3', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Ox_Glutaredoxins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_18586', 1.000000), 
	Parameter('rvs_RXN_18586', 0.000000))
Rule('GDPPYPHOSKIN_RXN',
	prot(name = 'RELA_MONOMER', loc = 'imem') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GDP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'RELA_MONOMER', loc = 'imem') +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GUANOSINE_5DP_3DP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GDPPYPHOSKIN_RXN', 1.000000), 
	Parameter('rvs_GDPPYPHOSKIN_RXN', 0.000000))
Rule('GTPPYPHOSKIN_RXN',
	prot(name = 'RELA_MONOMER', loc = 'imem') +
	met(name = 'GTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'RELA_MONOMER', loc = 'imem') +
	met(name = 'GDP_TP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GTPPYPHOSKIN_RXN', 1.000000), 
	Parameter('rvs_GTPPYPHOSKIN_RXN', 0.000000))
Rule('RHAMNULOKIN_RXN',
	prot(name = 'RHAMNULOKIN_MONOMER', loc = 'cyt') +
	met(name = 'CPD_16567', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'RHAMNULOKIN_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'RHAMNULOSE_1P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RHAMNULOKIN_RXN', 1.000000), 
	Parameter('rvs_RHAMNULOKIN_RXN', 0.000000))
Rule('RHAMNULPALDOL_RXN',
	cplx(name = 'RHAMNULPALDOL_CPLX', loc = 'cyt') +
	met(name = 'RHAMNULOSE_1P', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'RHAMNULPALDOL_CPLX', loc = 'cyt') +
	met(name = 'LACTALD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DIHYDROXY_ACETONE_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RHAMNULPALDOL_RXN', 1.000000), 
	Parameter('rvs_RHAMNULPALDOL_RXN', 1.000000))
Rule('RIB5PISOM_RXN',
	cplx(name = 'RIB5PISOMA_CPLX', loc = 'cyt') +
	met(name = 'RIBOSE_5P', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'RIB5PISOMA_CPLX', loc = 'cyt') +
	met(name = 'RIBULOSE_5P', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RIB5PISOM_RXN', 1.000000), 
	Parameter('rvs_RIB5PISOM_RXN', 1.000000))
Rule('RXN0_303',
	cplx(name = 'RIB5PISOMB_CPLX', loc = 'cyt') +
	met(name = 'D_ALLOSE_6_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'RIB5PISOMB_CPLX', loc = 'cyt') +
	met(name = 'D_ALLULOSE_6_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_303', 1.000000), 
	Parameter('rvs_RXN0_303', 1.000000))
Rule('RXN_8770',
	prot(name = 'RIBAZOLEPHOSPHAT_MONOMER', loc = 'cyt') +
	met(name = 'ADENOSYLCOBALAMIN_5_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'RIBAZOLEPHOSPHAT_MONOMER', loc = 'cyt') +
	met(name = 'ADENOSYLCOBALAMIN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_8770', 1.000000), 
	Parameter('rvs_RXN_8770', 0.000000))
Rule('RXN_16788',
	prot(name = 'RIBAZOLEPHOSPHAT_MONOMER', loc = 'cyt') +
	met(name = 'ALPHA_RIBAZOLE_5_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'RIBAZOLEPHOSPHAT_MONOMER', loc = 'cyt') +
	met(name = 'ALPHA_RIBAZOLE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_16788', 1.000000), 
	Parameter('rvs_RXN_16788', 0.000000))
Rule('RIBOFLAVINKIN_RXN',
	prot(name = 'RIBF_MONOMER', loc = 'cyt') +
	met(name = 'RIBOFLAVIN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'RIBF_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FMN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RIBOFLAVINKIN_RXN', 1.000000), 
	Parameter('rvs_RIBOFLAVINKIN_RXN', 0.000000))
Rule('FADSYN_RXN',
	prot(name = 'RIBF_MONOMER', loc = 'cyt') +
	met(name = 'FMN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'RIBF_MONOMER', loc = 'cyt') +
	met(name = 'FAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_FADSYN_RXN', 1.000000), 
	Parameter('rvs_FADSYN_RXN', 0.000000))
Rule('RIBONUCLEOSIDE_DIP_REDUCTI_RXN',
	cplx(name = 'RIBONUCLEOSIDE_DIP_REDUCTI_CPLX', loc = 'cyt') +
	met(name = 'Ox_Thioredoxin', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Deoxy_Ribonucleoside_Diphosphates', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'RIBONUCLEOSIDE_DIP_REDUCTI_CPLX', loc = 'cyt') +
	met(name = 'Red_Thioredoxin', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Ribonucleoside_Diphosphates', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RIBONUCLEOSIDE_DIP_REDUCTI_RXN', 0.000000), 
	Parameter('rvs_RIBONUCLEOSIDE_DIP_REDUCTI_RXN', 1.000000))
Rule('CDPREDUCT_RXN',
	cplx(name = 'RIBONUCLEOSIDE_DIP_REDUCTI_CPLX', loc = 'cyt') +
	met(name = 'DCDP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Ox_Thioredoxin', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'RIBONUCLEOSIDE_DIP_REDUCTI_CPLX', loc = 'cyt') +
	met(name = 'CDP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Red_Thioredoxin', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_CDPREDUCT_RXN', 0.000000), 
	Parameter('rvs_CDPREDUCT_RXN', 1.000000))
Rule('UDPREDUCT_RXN',
	cplx(name = 'RIBONUCLEOSIDE_DIP_REDUCTI_CPLX', loc = 'cyt') +
	met(name = 'DUDP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Ox_Thioredoxin', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'RIBONUCLEOSIDE_DIP_REDUCTI_CPLX', loc = 'cyt') +
	met(name = 'UDP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Red_Thioredoxin', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_UDPREDUCT_RXN', 0.000000), 
	Parameter('rvs_UDPREDUCT_RXN', 1.000000))
Rule('ADPREDUCT_RXN',
	cplx(name = 'RIBONUCLEOSIDE_DIP_REDUCTI_CPLX', loc = 'cyt') +
	met(name = 'DADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Ox_Thioredoxin', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'RIBONUCLEOSIDE_DIP_REDUCTI_CPLX', loc = 'cyt') +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Red_Thioredoxin', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_ADPREDUCT_RXN', 0.000000), 
	Parameter('rvs_ADPREDUCT_RXN', 1.000000))
Rule('GDPREDUCT_RXN',
	cplx(name = 'RIBONUCLEOSIDE_DIP_REDUCTI_CPLX', loc = 'cyt') +
	met(name = 'DGDP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Ox_Thioredoxin', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'RIBONUCLEOSIDE_DIP_REDUCTI_CPLX', loc = 'cyt') +
	met(name = 'GDP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Red_Thioredoxin', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_GDPREDUCT_RXN', 0.000000), 
	Parameter('rvs_GDPREDUCT_RXN', 1.000000))
Rule('RIBONUCLEOSIDE_DIP_REDUCTII_RXN',
	cplx(name = 'RIBONUCLEOSIDE_DIP_REDUCTII_CPLX', loc = 'cyt') +
	met(name = 'DCDP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Oxidized_NrdH_Proteins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'RIBONUCLEOSIDE_DIP_REDUCTII_CPLX', loc = 'cyt') +
	met(name = 'CDP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Reduced_NrdH_Proteins', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RIBONUCLEOSIDE_DIP_REDUCTII_RXN', 0.000000), 
	Parameter('rvs_RIBONUCLEOSIDE_DIP_REDUCTII_RXN', 1.000000))
Rule('RXN0_748',
	cplx(name = 'RIBONUCLEOSIDE_DIP_REDUCTII_CPLX', loc = 'cyt') +
	met(name = 'DGDP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Oxidized_NrdH_Proteins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'RIBONUCLEOSIDE_DIP_REDUCTII_CPLX', loc = 'cyt') +
	met(name = 'GDP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Reduced_NrdH_Proteins', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_748', 0.000000), 
	Parameter('rvs_RXN0_748', 1.000000))
Rule('RXN0_747',
	cplx(name = 'RIBONUCLEOSIDE_DIP_REDUCTII_CPLX', loc = 'cyt') +
	met(name = 'DADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Oxidized_NrdH_Proteins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'RIBONUCLEOSIDE_DIP_REDUCTII_CPLX', loc = 'cyt') +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Reduced_NrdH_Proteins', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_747', 0.000000), 
	Parameter('rvs_RXN0_747', 1.000000))
Rule('RXN0_722',
	cplx(name = 'RIBONUCLEOSIDE_DIP_REDUCTII_CPLX', loc = 'cyt') +
	met(name = 'DUDP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Oxidized_NrdH_Proteins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'RIBONUCLEOSIDE_DIP_REDUCTII_CPLX', loc = 'cyt') +
	met(name = 'UDP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Reduced_NrdH_Proteins', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_722', 0.000000), 
	Parameter('rvs_RXN0_722', 1.000000))
Rule('RIBONUCLEOSIDE_TRIP_REDUCT_RXN',
	cplx(name = 'RIBONUCLEOSIDE_TRIP_REDUCT_CPLX', loc = 'cyt') +
	met(name = 'FORMATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Ribonucleoside_Triphosphates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'RIBONUCLEOSIDE_TRIP_REDUCT_CPLX', loc = 'cyt') +
	met(name = 'Deoxy_Ribonucleoside_Triphosphates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RIBONUCLEOSIDE_TRIP_REDUCT_RXN', 1.000000), 
	Parameter('rvs_RIBONUCLEOSIDE_TRIP_REDUCT_RXN', 0.000000))
Rule('RXN0_745',
	cplx(name = 'RIBONUCLEOSIDE_TRIP_REDUCT_CPLX', loc = 'cyt') +
	met(name = 'FORMATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'RIBONUCLEOSIDE_TRIP_REDUCT_CPLX', loc = 'cyt') +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_745', 1.000000), 
	Parameter('rvs_RXN0_745', 0.000000))
Rule('RXN0_746',
	cplx(name = 'RIBONUCLEOSIDE_TRIP_REDUCT_CPLX', loc = 'cyt') +
	met(name = 'FORMATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'RIBONUCLEOSIDE_TRIP_REDUCT_CPLX', loc = 'cyt') +
	met(name = 'DGTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_746', 1.000000), 
	Parameter('rvs_RXN0_746', 0.000000))
Rule('RXN0_724',
	cplx(name = 'RIBONUCLEOSIDE_TRIP_REDUCT_CPLX', loc = 'cyt') +
	met(name = 'FORMATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'RIBONUCLEOSIDE_TRIP_REDUCT_CPLX', loc = 'cyt') +
	met(name = 'DUTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_724', 1.000000), 
	Parameter('rvs_RXN0_724', 0.000000))
Rule('RXN0_723',
	cplx(name = 'RIBONUCLEOSIDE_TRIP_REDUCT_CPLX', loc = 'cyt') +
	met(name = 'FORMATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'RIBONUCLEOSIDE_TRIP_REDUCT_CPLX', loc = 'cyt') +
	met(name = 'DCTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_723', 1.000000), 
	Parameter('rvs_RXN0_723', 0.000000))
Rule('RXN0_5116',
	cplx(name = 'RIBULOKIN_CPLX', loc = 'cyt') +
	met(name = 'L_RIBULOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'RIBULOKIN_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_RIBULOSE_5_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5116', 1.000000), 
	Parameter('rvs_RXN0_5116', 0.000000))
Rule('RIBULP3EPIM_RXN',
	prot(name = 'RIBULP3EPIM_MONOMER', loc = 'cyt') +
	met(name = 'RIBULOSE_5P', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'RIBULP3EPIM_MONOMER', loc = 'cyt') +
	met(name = 'XYLULOSE_5_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RIBULP3EPIM_RXN', 1.000000), 
	Parameter('rvs_RIBULP3EPIM_RXN', 1.000000))
Rule('_3dot1dot22dot4_RXN',
	cplx(name = 'RUVABC_CPLX', loc = 'cyt') +
	met(name = 'DNA_Combined_With_Exogenous_DNA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'RUVABC_CPLX', loc = 'cyt') +
	met(name = 'Resolution_of_Recombinational_Junction', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd__3dot1dot22dot4_RXN', 1.000000), 
	Parameter('rvs__3dot1dot22dot4_RXN', 0.000000))
Rule('S_ADENMETSYN_RXN',
	cplx(name = 'S_ADENMETSYN_CPLX', loc = 'cyt') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MET', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'S_ADENMETSYN_CPLX', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_S_ADENMETSYN_RXN', 1.000000), 
	Parameter('rvs_S_ADENMETSYN_RXN', 0.000000))
Rule('SAICARSYN_RXN',
	cplx(name = 'SAICARSYN_CPLX', loc = 'cyt') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PHOSPHORIBOSYL_CARBOXY_AMINOIMIDAZOLE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'L_ASPARTATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'SAICARSYN_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'P_RIBOSYL_4_SUCCCARB_AMINOIMIDAZOLE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_SAICARSYN_RXN', 1.000000), 
	Parameter('rvs_SAICARSYN_RXN', 0.000000))
Rule('SAMDECARB_RXN',
	cplx(name = 'SAMDECARB_CPLX', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'SAMDECARB_CPLX', loc = 'cyt') +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'S_ADENOSYLMETHIONINAMINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_SAMDECARB_RXN', 1.000000), 
	Parameter('rvs_SAMDECARB_RXN', 0.000000))
Rule('RXN0_301',
	prot(name = 'SARCOX_MONOMER', loc = 'cyt') +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'N_METHYLTRYPTOPHAN', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'SARCOX_MONOMER', loc = 'cyt') +
	met(name = 'TRP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HYDROGEN_PEROXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FORMALDEHYDE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_301', 1.000000), 
	Parameter('rvs_RXN0_301', 0.000000))
Rule('SERINE__TRNA_LIGASE_RXN',
	cplx(name = 'SERS_CPLX', loc = 'cyt') +
	met(name = 'SER_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'SERS_CPLX', loc = 'cyt') +
	met(name = 'Charged_SER_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_SERINE__TRNA_LIGASE_RXN', 1.000000), 
	Parameter('rvs_SERINE__TRNA_LIGASE_RXN', 0.000000))
Rule('RXN0_2161',
	cplx(name = 'SERS_CPLX', loc = 'cyt') +
	met(name = 'tRNA_Sec', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'SERS_CPLX', loc = 'cyt') +
	met(name = 'L_seryl_SEC_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_2161', 1.000000), 
	Parameter('rvs_RXN0_2161', 0.000000))
Rule('RXN_13403',
	cplx(name = 'SIROHEMESYN_CPLX', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UROPORPHYRINOGEN_III', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'SIROHEMESYN_CPLX', loc = 'cyt') +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DIHYDROSIROHYDROCHLORIN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_13403', 1.000000), 
	Parameter('rvs_RXN_13403', 0.000000))
Rule('RXN_8675',
	cplx(name = 'SIROHEMESYN_CPLX', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_9038', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'SIROHEMESYN_CPLX', loc = 'cyt') +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DIHYDROSIROHYDROCHLORIN', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_8675', 1.000000), 
	Parameter('rvs_RXN_8675', 0.000000))
Rule('UROPORIIIMETHYLTRANSA_RXN',
	cplx(name = 'SIROHEMESYN_CPLX', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UROPORPHYRINOGEN_III', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'SIROHEMESYN_CPLX', loc = 'cyt') +
	met(name = 'ADENOSYL_HOMO_CYS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_9038', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_UROPORIIIMETHYLTRANSA_RXN', 1.000000), 
	Parameter('rvs_UROPORIIIMETHYLTRANSA_RXN', 0.000000))
Rule('DIMETHUROPORDEHYDROG_RXN',
	cplx(name = 'SIROHEMESYN_CPLX', loc = 'cyt') +
	met(name = 'DIHYDROSIROHYDROCHLORIN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'SIROHEMESYN_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SIROHYDROCHLORIN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DIMETHUROPORDEHYDROG_RXN', 1.000000), 
	Parameter('rvs_DIMETHUROPORDEHYDROG_RXN', 0.000000))
Rule('SIROHEME_FERROCHELAT_RXN',
	cplx(name = 'SIROHEMESYN_CPLX', loc = 'cyt') +
	met(name = 'SIROHYDROCHLORIN', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FEplus2', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'SIROHEMESYN_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SIROHEME', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_SIROHEME_FERROCHELAT_RXN', 1.000000), 
	Parameter('rvs_SIROHEME_FERROCHELAT_RXN', 0.000000))
Rule('SORB6PDEHYDROG_RXN',
	cplx(name = 'SORB6PDEHYDROG_CPLX', loc = 'cyt') +
	met(name = 'D_SORBITOL_6_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'SORB6PDEHYDROG_CPLX', loc = 'cyt') +
	met(name = 'CPD_15709', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_SORB6PDEHYDROG_RXN', 1.000000), 
	Parameter('rvs_SORB6PDEHYDROG_RXN', 1.000000))
Rule('SPERMACTRAN_RXN',
	cplx(name = 'SPERMACTRAN_CPLX', loc = 'cyt') +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SPERMIDINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'SPERMACTRAN_CPLX', loc = 'cyt') +
	met(name = 'CPD_568', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_SPERMACTRAN_RXN', 1.000000), 
	Parameter('rvs_SPERMACTRAN_RXN', 0.000000))
Rule('RXN0_7165',
	cplx(name = 'SPERMACTRAN_CPLX', loc = 'cyt') +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SPERMIDINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'SPERMACTRAN_CPLX', loc = 'cyt') +
	met(name = 'CPD_3462', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_7165', 1.000000), 
	Parameter('rvs_RXN0_7165', 0.000000))
Rule('DIAMACTRANS_RXN',
	cplx(name = 'SPERMACTRAN_CPLX', loc = 'cyt') +
	met(name = 'Aliphatic_Alpha_Omega_Diamines', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'SPERMACTRAN_CPLX', loc = 'cyt') +
	met(name = 'Aliphatic_N_Acetyl_Diamines', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_DIAMACTRANS_RXN', 1.000000), 
	Parameter('rvs_DIAMACTRANS_RXN', 0.000000))
Rule('SPERMIDINESYN_RXN',
	cplx(name = 'SPERMIDINESYN_CPLX', loc = 'cyt') +
	met(name = 'PUTRESCINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'S_ADENOSYLMETHIONINAMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'SPERMIDINESYN_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SPERMIDINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_5_METHYLTHIOADENOSINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_SPERMIDINESYN_RXN', 1.000000), 
	Parameter('rvs_SPERMIDINESYN_RXN', 0.000000))
Rule('RXN0_5217',
	cplx(name = 'SPERMIDINESYN_CPLX', loc = 'cyt') +
	met(name = 'CADAVERINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'S_ADENOSYLMETHIONINAMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'SPERMIDINESYN_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_1065', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_5_METHYLTHIOADENOSINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5217', 1.000000), 
	Parameter('rvs_RXN0_5217', 0.000000))
Rule('RXN0_6427',
	prot(name = 'SPOT_MONOMER', loc = 'imem') +
	met(name = 'GDP_TP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'SPOT_MONOMER', loc = 'imem') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_6427', 1.000000), 
	Parameter('rvs_RXN0_6427', 0.000000))
Rule('PPGPPSYN_RXN',
	prot(name = 'SPOT_MONOMER', loc = 'imem') +
	met(name = 'GUANOSINE_5DP_3DP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'SPOT_MONOMER', loc = 'imem') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GDP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PPGPPSYN_RXN', 1.000000), 
	Parameter('rvs_PPGPPSYN_RXN', 0.000000))
Rule('SUCCCOASYN_RXN',
	prot(name = 'SUCCCOASYN', loc = 'cyt') +
	met(name = 'SUC', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'SUCCCOASYN', loc = 'cyt') +
	met(name = 'SUC_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_SUCCCOASYN_RXN', 1.000000), 
	Parameter('rvs_SUCCCOASYN_RXN', 1.000000))
Rule('SUCCGLUALDDEHYD_RXN',
	prot(name = 'SUCCGLUALDDEHYD_MONOMER', loc = 'cyt') +
	met(name = 'CPD_822', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'SUCCGLUALDDEHYD_MONOMER', loc = 'cyt') +
	met(name = 'N2_SUCCINYLGLUTAMATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_SUCCGLUALDDEHYD_RXN', 1.000000), 
	Parameter('rvs_SUCCGLUALDDEHYD_RXN', 0.000000))
Rule('SUCCGLUDESUCC_RXN',
	prot(name = 'SUCCGLUDESUCC_MONOMER', loc = 'cyt') +
	met(name = 'N2_SUCCINYLGLUTAMATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'SUCCGLUDESUCC_MONOMER', loc = 'cyt') +
	met(name = 'SUC', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_SUCCGLUDESUCC_RXN', 1.000000), 
	Parameter('rvs_SUCCGLUDESUCC_RXN', 0.000000))
Rule('SUCCORNTRANSAM_RXN',
	cplx(name = 'SUCCORNTRANSAM_CPLX', loc = 'cyt') +
	met(name = 'N2_SUCCINYLORNITHINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'SUCCORNTRANSAM_CPLX', loc = 'cyt') +
	met(name = 'CPD_822', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_SUCCORNTRANSAM_RXN', 1.000000), 
	Parameter('rvs_SUCCORNTRANSAM_RXN', 1.000000))
Rule('SULFATE_ADENYLYLTRANS_RXN',
	cplx(name = 'SULFATE_ADENYLYLTRANS_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SULFATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'SULFATE_ADENYLYLTRANS_CPLX', loc = 'cyt') +
	met(name = 'APS', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_SULFATE_ADENYLYLTRANS_RXN', 1.000000), 
	Parameter('rvs_SULFATE_ADENYLYLTRANS_RXN', 0.000000))
Rule('SULFITE_REDUCT_RXN',
	cplx(name = 'SULFITE_REDUCT_CPLX', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'HS', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'SULFITE_REDUCT_CPLX', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SO3', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_SULFITE_REDUCT_RXN', 0.000000), 
	Parameter('rvs_SULFITE_REDUCT_RXN', 1.000000))
Rule('TDPFUCACTRANS_RXN',
	prot(name = 'TDPFUCACTRANS_MONOMER', loc = 'cyt') +
	met(name = 'TDP_D_FUCOSAMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACETYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'TDPFUCACTRANS_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TDP_FUC4NAC', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_TDPFUCACTRANS_RXN', 1.000000), 
	Parameter('rvs_TDPFUCACTRANS_RXN', 0.000000))
Rule('TETRAACYLDISACC4KIN_RXN',
	prot(name = 'TETRAACYLDISACC4KIN_MONOMER', loc = 'cyt') +
	met(name = 'BISOHMYR_GLC', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'TETRAACYLDISACC4KIN_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'LIPID_IV_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_TETRAACYLDISACC4KIN_RXN', 1.000000), 
	Parameter('rvs_TETRAACYLDISACC4KIN_RXN', 0.000000))
Rule('THI_P_KIN_RXN',
	prot(name = 'THI_P_KIN_MONOMER', loc = 'cyt') +
	met(name = 'THIAMINE_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'THI_P_KIN_MONOMER', loc = 'cyt') +
	met(name = 'THIAMINE_PYROPHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_THI_P_KIN_RXN', 1.000000), 
	Parameter('rvs_THI_P_KIN_RXN', 0.000000))
Rule('PYRIMSYN1_RXN',
	prot(name = 'THIC_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_5_PHOSPHORIBOSYL_5_AMINOIMIDAZOLE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None +
	None +
	None | 
	prot(name = 'THIC_MONOMER', loc = 'cyt') +
	met(name = 'AMINO_HYDROXYMETHYL_METHYL_PYR_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CH33ADO', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MET', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'FORMATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_MONOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PYRIMSYN1_RXN', 1.000000), 
	Parameter('rvs_PYRIMSYN1_RXN', 0.000000))
Rule('RXN_12611',
	prot(name = 'THIE_MONOMER', loc = 'cyt') +
	met(name = 'CPD_13575', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMINO_HYDROXYMETHYL_METHYLPYRIMIDINE_PP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'THIE_MONOMER', loc = 'cyt') +
	met(name = 'THIAMINE_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_12611', 1.000000), 
	Parameter('rvs_RXN_12611', 0.000000))
Rule('THI_P_SYN_RXN',
	prot(name = 'THIE_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'THZ_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMINO_HYDROXYMETHYL_METHYLPYRIMIDINE_PP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'THIE_MONOMER', loc = 'cyt') +
	met(name = 'THIAMINE_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_THI_P_SYN_RXN', 1.000000), 
	Parameter('rvs_THI_P_SYN_RXN', 0.000000))
Rule('RXN_9788',
	prot(name = 'THIF_MONOMER', loc = 'cyt') +
	met(name = 'Sulfurylated_ThiI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Adenylated_ThiS_Proteins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Reduced_ferredoxins', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'THIF_MONOMER', loc = 'cyt') +
	met(name = 'Thiocarboxyadenylated_ThiS_Proteins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Sulfur_Carrier_Proteins_ThiI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Oxidized_ferredoxins', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_9788', 1.000000), 
	Parameter('rvs_RXN_9788', 0.000000))
Rule('RXN_9789',
	prot(name = 'THIF_MONOMER', loc = 'cyt') +
	met(name = 'Thi_S', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'THIF_MONOMER', loc = 'cyt') +
	met(name = 'Adenylated_ThiS_Proteins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN_9789', 1.000000), 
	Parameter('rvs_RXN_9789', 0.000000))
Rule('THIAZOLSYN2_RXN',
	prot(name = 'THIG_MONOMER', loc = 'cyt') +
	met(name = 'DEOXYXYLULOSE_5P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_12279', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Thiocarboxyadenylated_ThiS_Proteins', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'THIG_MONOMER', loc = 'cyt') +
	met(name = 'CPD_13575', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Thi_S', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_THIAZOLSYN2_RXN', 1.000000), 
	Parameter('rvs_THIAZOLSYN2_RXN', 0.000000))
Rule('RXN_11319',
	prot(name = 'THIH_MONOMER', loc = 'cyt') +
	met(name = 'S_ADENOSYLMETHIONINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TYR', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None +
	None | 
	prot(name = 'THIH_MONOMER', loc = 'cyt') +
	met(name = 'CPD_12279', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_108', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CH33ADO', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'MET', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_11319', 1.000000), 
	Parameter('rvs_RXN_11319', 0.000000))
Rule('RXN_18388',
	prot(name = 'THII_MONOMER', loc = 'cyt') +
	met(name = 'Sulfurylated_ThiI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Uracil_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Reduced_ferredoxins', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'THII_MONOMER', loc = 'cyt') +
	met(name = 'tRNA_4_thiouridine', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Sulfur_Carrier_Proteins_ThiI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Oxidized_ferredoxins', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_18388', 1.000000), 
	Parameter('rvs_RXN_18388', 0.000000))
Rule('THIKIN_RXN',
	prot(name = 'THIKIN_MONOMER', loc = 'cyt') +
	met(name = 'THIAMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'THIKIN_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'THIAMINE_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_THIKIN_RXN', 1.000000), 
	Parameter('rvs_THIKIN_RXN', 0.000000))
Rule('RXN_14251',
	cplx(name = 'THIOESTERII_CPLX', loc = 'cyt') +
	met(name = 'S_3_HYDROXYBUTANOYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'THIOESTERII_CPLX', loc = 'cyt') +
	met(name = 'CPD_1843', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14251', 1.000000), 
	Parameter('rvs_RXN_14251', 0.000000))
Rule('RXN_14255',
	cplx(name = 'THIOESTERII_CPLX', loc = 'cyt') +
	met(name = 'CPD_650', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'THIOESTERII_CPLX', loc = 'cyt') +
	met(name = 'CPD_335', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_14255', 1.000000), 
	Parameter('rvs_RXN_14255', 0.000000))
Rule('THIOREDOXIN_REDUCT_NADPH_RXN',
	cplx(name = 'THIOREDOXIN_REDUCT_NADPH_CPLX', loc = 'cyt') +
	met(name = 'Red_Thioredoxin', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'THIOREDOXIN_REDUCT_NADPH_CPLX', loc = 'cyt') +
	met(name = 'Ox_Thioredoxin', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_THIOREDOXIN_REDUCT_NADPH_RXN', 0.000000), 
	Parameter('rvs_THIOREDOXIN_REDUCT_NADPH_RXN', 1.000000))
Rule('THREDEHYD_RXN',
	cplx(name = 'THREDEHYDCAT_CPLX', loc = 'cyt') +
	met(name = 'THR', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'THREDEHYDCAT_CPLX', loc = 'cyt') +
	met(name = '_2_OXOBUTANOATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_THREDEHYD_RXN', 1.000000), 
	Parameter('rvs_THREDEHYD_RXN', 0.000000))
Rule('THRESYN_RXN',
	prot(name = 'THRESYN_MONOMER', loc = 'cyt') +
	met(name = 'O_PHOSPHO_L_HOMOSERINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'THRESYN_MONOMER', loc = 'cyt') +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'THR', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_THRESYN_RXN', 1.000000), 
	Parameter('rvs_THRESYN_RXN', 0.000000))
Rule('THREONINE__TRNA_LIGASE_RXN',
	cplx(name = 'THRS_CPLX', loc = 'cyt') +
	met(name = 'THR_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'THR', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'THRS_CPLX', loc = 'cyt') +
	met(name = 'Charged_THR_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_THREONINE__TRNA_LIGASE_RXN', 1.000000), 
	Parameter('rvs_THREONINE__TRNA_LIGASE_RXN', 0.000000))
Rule('THYMIDYLATESYN_RXN',
	cplx(name = 'THYMIDYLATESYN_CPLX', loc = 'cyt') +
	met(name = 'METHYLENE_THF_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DUMP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'THYMIDYLATESYN_CPLX', loc = 'cyt') +
	met(name = 'TMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DIHYDROFOLATE_GLU_N', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_THYMIDYLATESYN_RXN', 1.000000), 
	Parameter('rvs_THYMIDYLATESYN_RXN', 0.000000))
Rule('RXN0_5264',
	cplx(name = 'TMAOREDUCTI_CPLX', loc = 'wall') +
	met(name = 'TRIMETHYLAMINE_N_O', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Menaquinols', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'TMAOREDUCTI_CPLX', loc = 'wall') +
	met(name = 'Menaquinones', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TRIMETHYLAMINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5264', 1.000000), 
	Parameter('rvs_RXN0_5264', 0.000000))
Rule('RXN_19618',
	prot(name = 'TORA_MONOMER', loc = 'per') +
	met(name = 'TRIMETHYLAMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'an_oxidized_TorC_protein', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'TORA_MONOMER', loc = 'per') +
	met(name = 'TRIMETHYLAMINE_N_O', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'a_reduced_TorC_protein', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_19618', 0.000000), 
	Parameter('rvs_RXN_19618', 1.000000))
Rule('TRIOSEPISOMERIZATION_RXN',
	prot(name = 'TPI', loc = 'cyt') +
	met(name = 'GAP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'TPI', loc = 'cyt') +
	met(name = 'DIHYDROXY_ACETONE_PHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_TRIOSEPISOMERIZATION_RXN', 1.000000), 
	Parameter('rvs_TRIOSEPISOMERIZATION_RXN', 1.000000))
Rule('TRANSALDOL_RXN',
	prot(name = 'TRANSALDOLA_MONOMER', loc = 'cyt') +
	met(name = 'D_SEDOHEPTULOSE_7_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GAP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'TRANSALDOLA_MONOMER', loc = 'cyt') +
	met(name = 'FRUCTOSE_6P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ERYTHROSE_4P', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_TRANSALDOL_RXN', 1.000000), 
	Parameter('rvs_TRANSALDOL_RXN', 1.000000))
Rule('TRANSENOYLCOARED_RXN',
	cplx(name = 'TRANSENOYLCOARED_CPLX', loc = 'cyt') +
	met(name = 'Saturated_Fatty_Acyl_CoA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'TRANSENOYLCOARED_CPLX', loc = 'cyt') +
	met(name = 'TRANS_D2_ENOYL_COA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_TRANSENOYLCOARED_RXN', 0.000000), 
	Parameter('rvs_TRANSENOYLCOARED_RXN', 1.000000))
Rule('TRE6PHYDRO_RXN',
	prot(name = 'TRE6PHYDRO_MONOMER', loc = 'cyt') +
	met(name = 'TREHALOSE_6P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'TRE6PHYDRO_MONOMER', loc = 'cyt') +
	met(name = 'D_glucopyranose_6_phosphate', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Glucopyranose', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_TRE6PHYDRO_RXN', 1.000000), 
	Parameter('rvs_TRE6PHYDRO_RXN', 0.000000))
Rule('TREHALA_RXN',
	prot(name = 'TREHALACYTO_MONOMER', loc = 'cyt') +
	met(name = 'TREHALOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'TREHALACYTO_MONOMER', loc = 'cyt') +
	met(name = 'GLC', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ALPHA_GLUCOSE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_TREHALA_RXN', 1.000000), 
	Parameter('rvs_TREHALA_RXN', 0.000000))
Rule('TREHALOSE6PSYN_RXN',
	prot(name = 'TREHALOSE6PSYN_MONOMER', loc = 'cyt') +
	met(name = 'CPD_12575', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'D_glucopyranose_6_phosphate', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'TREHALOSE6PSYN_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UDP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TREHALOSE_6P', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_TREHALOSE6PSYN_RXN', 1.000000), 
	Parameter('rvs_TREHALOSE6PSYN_RXN', 0.000000))
Rule('TREHALOSEPHOSPHA_RXN',
	prot(name = 'TREHALOSEPHOSPHASYN_MONOMER', loc = 'cyt') +
	met(name = 'TREHALOSE_6P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'TREHALOSEPHOSPHASYN_MONOMER', loc = 'cyt') +
	met(name = 'TREHALOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_TREHALOSEPHOSPHA_RXN', 1.000000), 
	Parameter('rvs_TREHALOSEPHOSPHA_RXN', 0.000000))
Rule('TRYPTOPHAN__TRNA_LIGASE_RXN',
	cplx(name = 'TRPS_CPLX', loc = 'cyt') +
	met(name = 'TRP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TRP_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'TRPS_CPLX', loc = 'cyt') +
	met(name = 'Charged_TRP_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_TRYPTOPHAN__TRNA_LIGASE_RXN', 1.000000), 
	Parameter('rvs_TRYPTOPHAN__TRNA_LIGASE_RXN', 0.000000))
Rule('RXN0_2381',
	prot(name = 'TRYPSYN_APROTEIN', loc = 'cyt') +
	met(name = 'INDOLE_3_GLYCEROL_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'TRYPSYN_APROTEIN', loc = 'cyt') +
	met(name = 'INDOLE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GAP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_2381', 1.000000), 
	Parameter('rvs_RXN0_2381', 1.000000))
Rule('TRYPSYN_RXN',
	prot(name = 'TRYPSYN', loc = 'cyt') +
	met(name = 'INDOLE_3_GLYCEROL_P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'SER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'TRYPSYN', loc = 'cyt') +
	met(name = 'TRP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GAP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_TRYPSYN_RXN', 1.000000), 
	Parameter('rvs_TRYPSYN_RXN', 0.000000))
Rule('TRYPTOPHAN_RXN',
	cplx(name = 'TRYPTOPHAN_CPLX', loc = 'cyt') +
	met(name = 'TRP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	cplx(name = 'TRYPTOPHAN_CPLX', loc = 'cyt') +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'INDOLE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_TRYPTOPHAN_RXN', 1.000000), 
	Parameter('rvs_TRYPTOPHAN_RXN', 0.000000))
Rule('TSA_REDUCT_RXN',
	prot(name = 'TSA_REDUCT_MONOMER', loc = 'cyt') +
	met(name = 'NAD_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLYCERATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'TSA_REDUCT_MONOMER', loc = 'cyt') +
	met(name = 'NADH_P_OR_NOP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TARTRONATE_S_ALD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_TSA_REDUCT_RXN', 0.000000), 
	Parameter('rvs_TSA_REDUCT_RXN', 1.000000))
Rule('_2dot6dot1dot57_RXN',
	cplx(name = 'TYRB_DIMER', loc = 'cyt') +
	met(name = 'Aromatic_Amino_Acids', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'TYRB_DIMER', loc = 'cyt') +
	met(name = 'Aromatic_Oxoacids', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLT', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd__2dot6dot1dot57_RXN', 1.000000), 
	Parameter('rvs__2dot6dot1dot57_RXN', 1.000000))
Rule('TYROSINE__TRNA_LIGASE_RXN',
	cplx(name = 'TYRS_CPLX', loc = 'cyt') +
	met(name = 'TYR_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'TYR', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'TYRS_CPLX', loc = 'cyt') +
	met(name = 'Charged_TYR_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_TYROSINE__TRNA_LIGASE_RXN', 1.000000), 
	Parameter('rvs_TYROSINE__TRNA_LIGASE_RXN', 0.000000))
Rule('RXN_16937',
	prot(name = 'UBIX_MONOMER', loc = 'cyt') +
	met(name = 'FMNH2', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD_14332', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'UBIX_MONOMER', loc = 'cyt') +
	met(name = 'CPD_18260', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_16937', 1.000000), 
	Parameter('rvs_RXN_16937', 0.000000))
Rule('PYRNUTRANSHYDROGEN_RXN',
	cplx(name = 'UDHA_CPLX', loc = 'cyt') +
	met(name = 'NAD', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'UDHA_CPLX', loc = 'cyt') +
	met(name = 'NADH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_PYRNUTRANSHYDROGEN_RXN', 1.000000), 
	Parameter('rvs_PYRNUTRANSHYDROGEN_RXN', 0.000000))
Rule('URIDINEKIN_RXN',
	prot(name = 'UDK_MONOMER', loc = 'cyt') +
	met(name = 'URIDINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'UDK_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_URIDINEKIN_RXN', 1.000000), 
	Parameter('rvs_URIDINEKIN_RXN', 0.000000))
Rule('CYTIKIN_RXN',
	prot(name = 'UDK_MONOMER', loc = 'cyt') +
	met(name = 'CYTIDINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'UDK_MONOMER', loc = 'cyt') +
	met(name = 'CMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_CYTIKIN_RXN', 1.000000), 
	Parameter('rvs_CYTIKIN_RXN', 0.000000))
Rule('URKI_RXN',
	prot(name = 'UDK_MONOMER', loc = 'cyt') +
	met(name = 'URIDINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'UDK_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GDP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_URKI_RXN', 1.000000), 
	Parameter('rvs_URKI_RXN', 0.000000))
Rule('CYTIDINEKIN_RXN',
	prot(name = 'UDK_MONOMER', loc = 'cyt') +
	met(name = 'CYTIDINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GTP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'UDK_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GDP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_CYTIDINEKIN_RXN', 1.000000), 
	Parameter('rvs_CYTIDINEKIN_RXN', 0.000000))
Rule('UDP_NACMURALA_GLU_LIG_RXN',
	prot(name = 'UDP_NACMURALA_GLU_LIG_MONOMER', loc = 'cyt') +
	met(name = 'D_GLT', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CPD0_1456', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'UDP_NACMURALA_GLU_LIG_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UDP_AA_GLUTAMATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_UDP_NACMURALA_GLU_LIG_RXN', 1.000000), 
	Parameter('rvs_UDP_NACMURALA_GLU_LIG_RXN', 0.000000))
Rule('UDP_NACMURALGLDAPAALIG_RXN',
	prot(name = 'UDP_NACMURALGLDAPAALIG_MONOMER', loc = 'cyt') +
	met(name = 'D_ALA_D_ALA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UDP_AAGM_DIAMINOHEPTANEDIOATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'UDP_NACMURALGLDAPAALIG_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'C1', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_UDP_NACMURALGLDAPAALIG_RXN', 1.000000), 
	Parameter('rvs_UDP_NACMURALGLDAPAALIG_RXN', 0.000000))
Rule('UDP_NACMURALGLDAPLIG_RXN',
	prot(name = 'UDP_NACMURALGLDAPLIG_MONOMER', loc = 'cyt') +
	met(name = 'MESO_DIAMINOPIMELATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UDP_AA_GLUTAMATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'UDP_NACMURALGLDAPLIG_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UDP_AAGM_DIAMINOHEPTANEDIOATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_UDP_NACMURALGLDAPLIG_RXN', 1.000000), 
	Parameter('rvs_UDP_NACMURALGLDAPLIG_RXN', 0.000000))
Rule('UDPACYLGLCNACDEACETYL_RXN',
	prot(name = 'UDPACYLGLCNACDEACETYL_MONOMER', loc = 'cyt') +
	met(name = 'UDP_OHMYR_ACETYLGLUCOSAMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'UDPACYLGLCNACDEACETYL_MONOMER', loc = 'cyt') +
	met(name = 'UDP_OHMYR_GLUCOSAMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACET', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_UDPACYLGLCNACDEACETYL_RXN', 1.000000), 
	Parameter('rvs_UDPACYLGLCNACDEACETYL_RXN', 0.000000))
Rule('UDPGLUCEPIM_RXN',
	cplx(name = 'UDPGLUCEPIM_CPLX', loc = 'cyt') +
	met(name = 'CPD_12575', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'UDPGLUCEPIM_CPLX', loc = 'cyt') +
	met(name = 'CPD_14553', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_UDPGLUCEPIM_RXN', 1.000000), 
	Parameter('rvs_UDPGLUCEPIM_RXN', 1.000000))
Rule('UDPMANACATRANS_RXN',
	prot(name = 'UDPMANACATRANS_MONOMER', loc = 'cyt') +
	met(name = 'ACETYL_D_GLUCOSAMINYLDIPHOSPHO_UNDECAPRE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UDP_MANNACA', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'UDPMANACATRANS_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'C55_PP_GLCNAC_MANNACA', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UDP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_UDPMANACATRANS_RXN', 1.000000), 
	Parameter('rvs_UDPMANACATRANS_RXN', 0.000000))
Rule('UDPNACETYLGLUCOSAMACYLTRANS_RXN',
	cplx(name = 'UDPNACETYLGLUCOSAMACYLTRANS_CPLX', loc = 'cyt') +
	met(name = 'R_3_hydroxymyristoyl_ACPs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UDP_N_ACETYL_D_GLUCOSAMINE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'UDPNACETYLGLUCOSAMACYLTRANS_CPLX', loc = 'cyt') +
	met(name = 'UDP_OHMYR_ACETYLGLUCOSAMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ACP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_UDPNACETYLGLUCOSAMACYLTRANS_RXN', 1.000000), 
	Parameter('rvs_UDPNACETYLGLUCOSAMACYLTRANS_RXN', 0.000000))
Rule('UDPNACETYLGLUCOSAMENOLPYRTRANS_RXN',
	prot(name = 'UDPNACETYLGLUCOSAMENOLPYRTRANS_MONOMER', loc = 'cyt') +
	met(name = 'UDP_N_ACETYL_D_GLUCOSAMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PHOSPHO_ENOL_PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'UDPNACETYLGLUCOSAMENOLPYRTRANS_MONOMER', loc = 'cyt') +
	met(name = 'UDP_ACETYL_CARBOXYVINYL_GLUCOSAMINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_UDPNACETYLGLUCOSAMENOLPYRTRANS_RXN', 1.000000), 
	Parameter('rvs_UDPNACETYLGLUCOSAMENOLPYRTRANS_RXN', 0.000000))
Rule('UDPNACETYLMURAMATEDEHYDROG_RXN',
	prot(name = 'UDPNACETYLMURAMATEDEHYDROG_MONOMER', loc = 'cyt') +
	met(name = 'NADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UDP_N_ACETYLMURAMATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'UDPNACETYLMURAMATEDEHYDROG_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'NADPH', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UDP_ACETYL_CARBOXYVINYL_GLUCOSAMINE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_UDPNACETYLMURAMATEDEHYDROG_RXN', 0.000000), 
	Parameter('rvs_UDPNACETYLMURAMATEDEHYDROG_RXN', 1.000000))
Rule('RXN_12002',
	cplx(name = 'UMPKI_CPLX', loc = 'cyt') +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UMP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'UMPKI_CPLX', loc = 'cyt') +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UDP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_12002', 1.000000), 
	Parameter('rvs_RXN_12002', 0.000000))
Rule('RXN_8999',
	cplx(name = 'UPPSYN_CPLX', loc = 'cyt') +
	met(name = 'FARNESYL_PP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'DELTA3_ISOPENTENYL_PP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'UPPSYN_CPLX', loc = 'cyt') +
	met(name = 'UNDECAPRENYL_DIPHOSPHATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_8999', 1.000000), 
	Parameter('rvs_RXN_8999', 0.000000))
Rule('URACIL_PRIBOSYLTRANS_RXN',
	cplx(name = 'URACIL_PRIBOSYLTRANS_CPLX', loc = 'cyt') +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UMP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'URACIL_PRIBOSYLTRANS_CPLX', loc = 'cyt') +
	met(name = 'PRPP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'URACIL', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_URACIL_PRIBOSYLTRANS_RXN', 0.000000), 
	Parameter('rvs_URACIL_PRIBOSYLTRANS_RXN', 1.000000))
Rule('UROGENDECARBOX_RXN',
	prot(name = 'UROGENDECARBOX_MONOMER', loc = 'cyt') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UROPORPHYRINOGEN_III', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'UROGENDECARBOX_MONOMER', loc = 'cyt') +
	met(name = 'CARBON_DIOXIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'COPROPORPHYRINOGEN_III', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_UROGENDECARBOX_RXN', 1.000000), 
	Parameter('rvs_UROGENDECARBOX_RXN', 0.000000))
Rule('UROGENIIISYN_RXN',
	prot(name = 'UROGENIIISYN_MONOMER', loc = 'cyt') +
	met(name = 'HYDROXYMETHYLBILANE', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'UROGENIIISYN_MONOMER', loc = 'cyt') +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'UROPORPHYRINOGEN_III', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_UROGENIIISYN_RXN', 1.000000), 
	Parameter('rvs_UROGENIIISYN_RXN', 0.000000))
Rule('UDPSUGARHYDRO_RXN',
	prot(name = 'USHA_MONOMER', loc = 'per') +
	met(name = 'UDP_sugar', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'USHA_MONOMER', loc = 'per') +
	met(name = 'UMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Alpha_D_aldose_1_phosphates', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_UDPSUGARHYDRO_RXN', 1.000000), 
	Parameter('rvs_UDPSUGARHYDRO_RXN', 0.000000))
Rule('BIS5_ADENOSYL_TRIPHOSPHATASE_RXN',
	prot(name = 'USHA_MONOMER', loc = 'per') +
	met(name = 'ADENOSINE5TRIPHOSPHO5ADENOSINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None | 
	prot(name = 'USHA_MONOMER', loc = 'per') +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_BIS5_ADENOSYL_TRIPHOSPHATASE_RXN', 1.000000), 
	Parameter('rvs_BIS5_ADENOSYL_TRIPHOSPHATASE_RXN', 0.000000))
Rule('RXN_18241',
	prot(name = 'USHA_MONOMER', loc = 'per') +
	met(name = 'CPD_606', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) +
	None +
	None | 
	prot(name = 'USHA_MONOMER', loc = 'per') +
	met(name = 'CYTIDINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'GLYCEROL_3P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN_18241', 1.000000), 
	Parameter('rvs_RXN_18241', 0.000000))
Rule('RXN0_2621',
	cplx(name = 'UVRABC_CPLX', loc = 'cyt') +
	met(name = 'CPD_8180', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'UVRABC_CPLX', loc = 'cyt') +
	met(name = 'CPD_8534', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_2621', 1.000000), 
	Parameter('rvs_RXN0_2621', 0.000000))
Rule('GLUCUROISOM_RXN',
	prot(name = 'UXAC_MONOMER', loc = 'cyt') +
	met(name = 'CPD_15530', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'UXAC_MONOMER', loc = 'cyt') +
	met(name = 'FRUCTURONATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GLUCUROISOM_RXN', 1.000000), 
	Parameter('rvs_GLUCUROISOM_RXN', 1.000000))
Rule('GALACTUROISOM_RXN',
	prot(name = 'UXAC_MONOMER', loc = 'cyt') +
	met(name = 'CPD_15633', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'UXAC_MONOMER', loc = 'cyt') +
	met(name = 'D_TAGATURONATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_GALACTUROISOM_RXN', 1.000000), 
	Parameter('rvs_GALACTUROISOM_RXN', 1.000000))
Rule('VALINE_PYRUVATE_AMINOTRANSFER_RXN',
	prot(name = 'VALINE_PYRUVATE_AMINOTRANSFER_MONOMER', loc = 'cyt') +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'VAL', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'VALINE_PYRUVATE_AMINOTRANSFER_MONOMER', loc = 'cyt') +
	met(name = 'L_ALPHA_ALANINE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_KETO_ISOVALERATE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_VALINE_PYRUVATE_AMINOTRANSFER_RXN', 1.000000), 
	Parameter('rvs_VALINE_PYRUVATE_AMINOTRANSFER_RXN', 1.000000))
Rule('RXN0_5200',
	prot(name = 'VALINE_PYRUVATE_AMINOTRANSFER_MONOMER', loc = 'cyt') +
	met(name = 'Aminated_Amine_Donors', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = '_2_OXOBUTANOATE', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'VALINE_PYRUVATE_AMINOTRANSFER_MONOMER', loc = 'cyt') +
	met(name = '_2_Aminobutyrate', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Deaminated_Amine_Donors', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN0_5200', 1.000000), 
	Parameter('rvs_RXN0_5200', 1.000000))
Rule('VALINE__TRNA_LIGASE_RXN',
	prot(name = 'VALS_MONOMER', loc = 'cyt') +
	met(name = 'VAL_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'VAL', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'VALS_MONOMER', loc = 'cyt') +
	met(name = 'Charged_VAL_tRNAs', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PPI', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'AMP', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_VALINE__TRNA_LIGASE_RXN', 1.000000), 
	Parameter('rvs_VALINE__TRNA_LIGASE_RXN', 0.000000))
Rule('RXN0_7092',
	cplx(name = 'XANTHOSINEPHOSPHORY_CPLX', loc = 'cyt') +
	met(name = 'NIACINAMIDE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'RIBOSE_1P', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'XANTHOSINEPHOSPHORY_CPLX', loc = 'cyt') +
	met(name = 'NICOTINAMIDE_RIBOSE', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'ecoli', prot = None) +
	None, 
	Parameter('fwd_RXN0_7092', 0.000000), 
	Parameter('rvs_RXN0_7092', 1.000000))
Rule('XYLISOM_RXN',
	cplx(name = 'XYLISOM_CPLX', loc = 'cyt') +
	met(name = 'D_Xylopyranose', loc = 'cyt', strain = 'ecoli', prot = None) | 
	cplx(name = 'XYLISOM_CPLX', loc = 'cyt') +
	met(name = 'D_XYLULOSE', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_XYLISOM_RXN', 1.000000), 
	Parameter('rvs_XYLISOM_RXN', 1.000000))
Rule('RXN1_42',
	prot(name = 'YDCS_MONOMER', loc = 'per') +
	met(name = 'CPD_650', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'Poly_Hydroxybutyrate', loc = 'cyt', strain = 'ecoli', prot = None) | 
	prot(name = 'YDCS_MONOMER', loc = 'per') +
	met(name = 'Poly_Hydroxybutyrate', loc = 'cyt', strain = 'ecoli', prot = None) +
	met(name = 'CO_A', loc = 'cyt', strain = 'ecoli', prot = None), 
	Parameter('fwd_RXN1_42', 1.000000), 
	Parameter('rvs_RXN1_42', 0.000000))
