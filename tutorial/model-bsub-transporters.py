from pysb import *
Model()

Monomer('met',
	['name', 'loc', 'dna', 'met', 'prot', 'rna'],
	{ 'name' : [ 'ADP', 'AMMONIUM', 'ATP', 'Amino_Acids_20', 'Antibiotics', 'BETA_GLUCOSIDES', 'Beta_Glucoside_6_P', 'CAplus2', 'CHOLINE', 'CPD_1244', 'CPD_15716', 'CPD_543', 'CPD_9956', 'CPD_9985', 'Carboxylates', 'Cytochromes_C_Oxidized', 'Cytochromes_C_Reduced', 'D_GLUCOSAMINE_6_P', 'D_fructose_1_phosphate', 'FEplus3', 'FRU', 'FRUCTOSE_6P', 'GLC', 'GLC_6_P', 'GLN', 'GLT', 'GLUCOSAMINE', 'GLYCEROL', 'GLYCEROL_3P', 'HIS', 'HYPOXANTHINE', 'Hpr_Histidine', 'Hpr_pi_phospho_L_histidines', 'Kplus', 'MAL', 'MALTOSE', 'MANNITOL', 'MANNITOL_1P', 'MANNOSE', 'MANNOSE_6P', 'MGplus2', 'MNplus2', 'MYO_INOSITOL', 'Maltodextrins', 'Menaquinols', 'Menaquinones', 'N_ACETYL_D_GLUCOSAMINE_6_P', 'N_acetyl_D_glucosamine', 'NAplus', 'NITRATE', 'NITRITE', 'OXYGEN_MOLECULE', 'PHOSPHO_ENOL_PYRUVATE', 'PRO', 'PROTON', 'PYRUVATE', 'Pi', 'RIBOFLAVIN', 'SORBITOL', 'SUCROSE', 'Sugar', 'Sugar_Phosphate', 'TREHALOSE', 'TREHALOSE_6P', 'Teichoic_P_Gro_Glc', 'UBIQUINONE_8', 'Ubiquinols', 'Ubiquinones', 'WATER', 'Xenobiotic', '_2_KETOGLUTARATE', '_4_AMINO_BUTYRATE' ],
	'loc' : ['cyt', 'cytosk', 'ex', 'mem', 'per', 'wall', 'bnuc', 'cproj', 'imem', 'omem', 'pmem'],
	'strain' : ['bsubtilis']})
Monomer('prot',
	['name', 'loc', 'dna', 'met', 'prot', 'rna', 'up', 'dw'],
	{ 'name' : [ 'BSU01680_MONOMER', 'BSU02140_MONOMER', 'BSU02170_MONOMER', 'BSU02340_MONOMER', 'BSU02350_MONOMER', 'BSU02400_MONOMER', 'BSU02420_MONOMER', 'BSU03220_MONOMER', 'BSU03330_MONOMER', 'BSU04360_MONOMER', 'BSU05470_MONOMER', 'BSU05800_MONOMER', 'BSU06160_MONOMER', 'BSU06230_MONOMER', 'BSU06310_MONOMER', 'BSU07570_MONOMER', 'BSU07700_MONOMER', 'BSU07800_MONOMER', 'BSU08200_MONOMER', 'BSU09280_MONOMER', 'BSU09850_MONOMER', 'BSU12010_MONOMER', 'BSU13300_MONOMER', 'BSU13890_MONOMER', 'BSU14400_MONOMER', 'BSU16825_MONOMER', 'BSU23050_MONOMER', 'BSU30720_MONOMER', 'BSU31580_MONOMER', 'BSU34820_MONOMER', 'BSU36510_MONOMER', 'BSU37260_MONOMER', 'BSU38050_MONOMER', 'BSU39270_MONOMER', 'BSU39390_MONOMER' ],
	'loc' : ['cyt', 'cytosk', 'ex', 'mem', 'per', 'wall', 'bnuc', 'cproj', 'imem', 'omem', 'pmem'],
	'strain' : ['bsubtilis']})
Monomer('cplx',
	['name', 'loc', 'dna', 'met', 'prot', 'rna', 'up', 'dw'],
	{ 'name' : [ 'CPLX8J2_101', 'CPLX8J2_116', 'CPLX8J2_117', 'CPLX8J2_119', 'CPLX8J2_141', 'CPLX8J2_142', 'CPLX8J2_158', 'CPLX8J2_161', 'CPLX8J2_189', 'CPLX8J2_22', 'CPLX8J2_37', 'CPLX8J2_38', 'CPLX8J2_43', 'CPLX8J2_65', 'CPLX8J2_81', 'CPLX8J2_93' ],
	'loc' : ['cyt', 'cytosk', 'ex', 'mem', 'per', 'wall', 'bnuc', 'cproj', 'imem', 'omem', 'pmem'],
	'strain' : ['bsubtilis']})
Rule('_2dot7dot1dot69_RXN',
	prot(name = 'BSU01680_MONOMER', loc = 'pmem') +
	met(name = 'Hpr_pi_phospho_L_histidines', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'Sugar', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	prot(name = 'BSU01680_MONOMER', loc = 'pmem') +
	met(name = 'Hpr_Histidine', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'Sugar_Phosphate', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd__2dot7dot1dot69_RXN', 1.000000), 
	Parameter('rvs__2dot7dot1dot69_RXN', 0.000000))
Rule('TRANS_RXN8J2_6',
	prot(name = 'BSU02140_MONOMER', loc = 'pmem') +
	met(name = 'GLYCEROL_3P', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	prot(name = 'BSU02140_MONOMER', loc = 'pmem') +
	met(name = 'GLYCEROL_3P', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN8J2_6', 1.000000), 
	Parameter('rvs_TRANS_RXN8J2_6', 0.000000))
Rule('TRANS_RXN8J2_7',
	prot(name = 'BSU02170_MONOMER', loc = 'pmem') +
	met(name = 'Carboxylates', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	prot(name = 'BSU02170_MONOMER', loc = 'pmem') +
	met(name = 'Carboxylates', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN8J2_7', 1.000000), 
	Parameter('rvs_TRANS_RXN8J2_7', 0.000000))
Rule('TRANS_RXN8J2_8',
	prot(name = 'BSU02340_MONOMER', loc = 'pmem') +
	met(name = 'GLT', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	prot(name = 'BSU02340_MONOMER', loc = 'pmem') +
	met(name = 'GLT', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN8J2_8', 1.000000), 
	Parameter('rvs_TRANS_RXN8J2_8', 0.000000))
Rule('TRANS_RXN8J2_104',
	prot(name = 'BSU02350_MONOMER', loc = 'pmem') +
	met(name = 'GLUCOSAMINE', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PHOSPHO_ENOL_PYRUVATE', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	prot(name = 'BSU02350_MONOMER', loc = 'pmem') +
	met(name = 'D_GLUCOSAMINE_6_P', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN8J2_104', 1.000000), 
	Parameter('rvs_TRANS_RXN8J2_104', 0.000000))
Rule('TRANS_RXN8J2_5',
	prot(name = 'BSU02400_MONOMER', loc = 'pmem') +
	met(name = 'Amino_Acids_20', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	prot(name = 'BSU02400_MONOMER', loc = 'pmem') +
	met(name = 'Amino_Acids_20', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN8J2_5', 1.000000), 
	Parameter('rvs_TRANS_RXN8J2_5', 0.000000))
Rule('TRANS_RXN8J2_9',
	prot(name = 'BSU02420_MONOMER', loc = 'pmem') +
	met(name = 'GLN', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	prot(name = 'BSU02420_MONOMER', loc = 'pmem') +
	met(name = 'GLN', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN8J2_9', 1.000000), 
	Parameter('rvs_TRANS_RXN8J2_9', 0.000000))
Rule('TRANS_RXN8J2_27',
	prot(name = 'BSU03220_MONOMER', loc = 'pmem') +
	met(name = 'PRO', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'NAplus', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	prot(name = 'BSU03220_MONOMER', loc = 'pmem') +
	met(name = 'PRO', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'NAplus', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN8J2_27', 1.000000), 
	Parameter('rvs_TRANS_RXN8J2_27', 0.000000))
Rule('TRANS_RXN8J2_13',
	prot(name = 'BSU03330_MONOMER', loc = 'pmem') +
	met(name = 'NITRATE', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	prot(name = 'BSU03330_MONOMER', loc = 'pmem') +
	met(name = 'NITRATE', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN8J2_13', 1.000000), 
	Parameter('rvs_TRANS_RXN8J2_13', 0.000000))
Rule('TRANS_RXN8J2_17',
	prot(name = 'BSU04360_MONOMER', loc = 'pmem') +
	met(name = 'MNplus2', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	prot(name = 'BSU04360_MONOMER', loc = 'pmem') +
	met(name = 'MNplus2', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN8J2_17', 1.000000), 
	Parameter('rvs_TRANS_RXN8J2_17', 0.000000))
Rule('TRANS_RXN0_487',
	prot(name = 'BSU05470_MONOMER', loc = 'pmem') +
	met(name = 'MNplus2', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	prot(name = 'BSU05470_MONOMER', loc = 'pmem') +
	met(name = 'MNplus2', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN0_487', 1.000000), 
	Parameter('rvs_TRANS_RXN0_487', 0.000000))
Rule('TRANS_RXN8J2_21',
	prot(name = 'BSU05800_MONOMER', loc = 'pmem') +
	met(name = 'HYPOXANTHINE', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	prot(name = 'BSU05800_MONOMER', loc = 'pmem') +
	met(name = 'HYPOXANTHINE', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN8J2_21', 1.000000), 
	Parameter('rvs_TRANS_RXN8J2_21', 0.000000))
Rule('TRANS_RXN8J2_22',
	prot(name = 'BSU06160_MONOMER', loc = 'pmem') +
	met(name = 'SORBITOL', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	prot(name = 'BSU06160_MONOMER', loc = 'pmem') +
	met(name = 'SORBITOL', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN8J2_22', 1.000000), 
	Parameter('rvs_TRANS_RXN8J2_22', 0.000000))
Rule('TRANS_RXN8J2_24',
	prot(name = 'BSU06230_MONOMER', loc = 'pmem') +
	met(name = 'MYO_INOSITOL', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	prot(name = 'BSU06230_MONOMER', loc = 'pmem') +
	met(name = 'MYO_INOSITOL', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN8J2_24', 1.000000), 
	Parameter('rvs_TRANS_RXN8J2_24', 0.000000))
Rule('TRANS_RXN8J2_115',
	prot(name = 'BSU06310_MONOMER', loc = 'pmem') +
	met(name = '_4_AMINO_BUTYRATE', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	prot(name = 'BSU06310_MONOMER', loc = 'pmem') +
	met(name = '_4_AMINO_BUTYRATE', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN8J2_115', 1.000000), 
	Parameter('rvs_TRANS_RXN8J2_115', 0.000000))
Rule('TRANS_RXN8J2_116',
	prot(name = 'BSU06310_MONOMER', loc = 'pmem') +
	met(name = 'PRO', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	prot(name = 'BSU06310_MONOMER', loc = 'pmem') +
	met(name = 'PRO', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN8J2_116', 1.000000), 
	Parameter('rvs_TRANS_RXN8J2_116', 0.000000))
Rule('TRANS_RXN8J2_28',
	prot(name = 'BSU07570_MONOMER', loc = 'pmem') +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	prot(name = 'BSU07570_MONOMER', loc = 'pmem') +
	met(name = '_2_KETOGLUTARATE', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN8J2_28', 1.000000), 
	Parameter('rvs_TRANS_RXN8J2_28', 0.000000))
Rule('TRANS_RXN8J2_110',
	prot(name = 'BSU07700_MONOMER', loc = 'pmem') +
	met(name = 'N_acetyl_D_glucosamine', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PHOSPHO_ENOL_PYRUVATE', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	prot(name = 'BSU07700_MONOMER', loc = 'pmem') +
	met(name = 'N_ACETYL_D_GLUCOSAMINE_6_P', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN8J2_110', 1.000000), 
	Parameter('rvs_TRANS_RXN8J2_110', 0.000000))
Rule('TRANS_RXN8J2_105',
	prot(name = 'BSU07800_MONOMER', loc = 'pmem') +
	met(name = 'TREHALOSE', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PHOSPHO_ENOL_PYRUVATE', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	prot(name = 'BSU07800_MONOMER', loc = 'pmem') +
	met(name = 'TREHALOSE_6P', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN8J2_105', 1.000000), 
	Parameter('rvs_TRANS_RXN8J2_105', 0.000000))
Rule('TRANS_RXN8J2_111',
	prot(name = 'BSU08200_MONOMER', loc = 'pmem') +
	met(name = 'MALTOSE', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PHOSPHO_ENOL_PYRUVATE', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	prot(name = 'BSU08200_MONOMER', loc = 'pmem') +
	met(name = 'CPD_1244', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN8J2_111', 1.000000), 
	Parameter('rvs_TRANS_RXN8J2_111', 0.000000))
Rule('TRANS_RXN8J2_34',
	prot(name = 'BSU09280_MONOMER', loc = 'pmem') +
	met(name = 'GLYCEROL', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	prot(name = 'BSU09280_MONOMER', loc = 'pmem') +
	met(name = 'GLYCEROL', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN8J2_34', 1.000000), 
	Parameter('rvs_TRANS_RXN8J2_34', 0.000000))
Rule('TRANS_RXN_42',
	prot(name = 'BSU09850_MONOMER', loc = 'pmem') +
	met(name = 'PROTON', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'Kplus', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	prot(name = 'BSU09850_MONOMER', loc = 'pmem') +
	met(name = 'PROTON', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'Kplus', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN_42', 1.000000), 
	Parameter('rvs_TRANS_RXN_42', 0.000000))
Rule('TRANS_RXN8J2_106',
	prot(name = 'BSU12010_MONOMER', loc = 'pmem') +
	met(name = 'MANNOSE', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PHOSPHO_ENOL_PYRUVATE', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	prot(name = 'BSU12010_MONOMER', loc = 'pmem') +
	met(name = 'MANNOSE_6P', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN8J2_106', 1.000000), 
	Parameter('rvs_TRANS_RXN8J2_106', 0.000000))
Rule('TRANS_RXN_141',
	prot(name = 'BSU13300_MONOMER', loc = 'pmem') +
	met(name = 'MGplus2', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	prot(name = 'BSU13300_MONOMER', loc = 'pmem') +
	met(name = 'MGplus2', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN_141', 1.000000), 
	Parameter('rvs_TRANS_RXN_141', 0.000000))
Rule('TRANS_RXN8J2_107',
	prot(name = 'BSU13890_MONOMER', loc = 'pmem') +
	met(name = 'GLC', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PHOSPHO_ENOL_PYRUVATE', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	prot(name = 'BSU13890_MONOMER', loc = 'pmem') +
	met(name = 'GLC_6_P', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN8J2_107', 1.000000), 
	Parameter('rvs_TRANS_RXN8J2_107', 0.000000))
Rule('RXN_15084',
	prot(name = 'BSU14400_MONOMER', loc = 'pmem') +
	met(name = 'Hpr_pi_phospho_L_histidines', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'FRU', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	prot(name = 'BSU14400_MONOMER', loc = 'pmem') +
	met(name = 'D_fructose_1_phosphate', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'Hpr_Histidine', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_RXN_15084', 1.000000), 
	Parameter('rvs_RXN_15084', 0.000000))
Rule('TRANS_RXN8J2_101',
	prot(name = 'BSU16825_MONOMER', loc = 'pmem') +
	met(name = 'Antibiotics', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	prot(name = 'BSU16825_MONOMER', loc = 'pmem') +
	met(name = 'Antibiotics', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN8J2_101', 1.000000), 
	Parameter('rvs_TRANS_RXN8J2_101', 0.000000))
Rule('TRANS_RXN8J2_1',
	prot(name = 'BSU23050_MONOMER', loc = 'pmem') +
	met(name = 'RIBOFLAVIN', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	prot(name = 'BSU23050_MONOMER', loc = 'pmem') +
	met(name = 'RIBOFLAVIN', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN8J2_1', 1.000000), 
	Parameter('rvs_TRANS_RXN8J2_1', 0.000000))
Rule('CYT_UBIQUINOL_OXID_RXN',
	prot(name = 'BSU30720_MONOMER', loc = 'pmem') +
	met(name = 'CPD_9956', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	prot(name = 'BSU30720_MONOMER', loc = 'pmem') +
	met(name = 'UBIQUINONE_8', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_CYT_UBIQUINOL_OXID_RXN', 1.000000), 
	Parameter('rvs_CYT_UBIQUINOL_OXID_RXN', 0.000000))
Rule('RXN0_5266',
	prot(name = 'BSU30720_MONOMER', loc = 'pmem') +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'Ubiquinols', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	prot(name = 'BSU30720_MONOMER', loc = 'pmem') +
	met(name = 'WATER', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'Ubiquinones', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_RXN0_5266', 1.000000), 
	Parameter('rvs_RXN0_5266', 0.000000))
Rule('TRANS_RXN8J2_103',
	prot(name = 'BSU31580_MONOMER', loc = 'pmem') +
	met(name = 'MAL', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'NAplus', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	prot(name = 'BSU31580_MONOMER', loc = 'pmem') +
	met(name = 'MAL', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'NAplus', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN8J2_103', 1.000000), 
	Parameter('rvs_TRANS_RXN8J2_103', 0.000000))
Rule('_3dot6dot3dot44_RXN',
	prot(name = 'BSU34820_MONOMER', loc = 'pmem') +
	met(name = 'Xenobiotic', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	prot(name = 'BSU34820_MONOMER', loc = 'pmem') +
	met(name = 'Xenobiotic', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd__3dot6dot3dot44_RXN', 1.000000), 
	Parameter('rvs__3dot6dot3dot44_RXN', 0.000000))
Rule('RXN_9615',
	prot(name = 'BSU36510_MONOMER', loc = 'pmem') +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	prot(name = 'BSU36510_MONOMER', loc = 'pmem') +
	met(name = 'AMMONIUM', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_RXN_9615', 1.000000), 
	Parameter('rvs_RXN_9615', 0.000000))
Rule('RXN0_3501',
	prot(name = 'BSU37260_MONOMER', loc = 'cyt') +
	met(name = 'NITRATE', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'Menaquinols', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	None | 
	prot(name = 'BSU37260_MONOMER', loc = 'cyt') +
	met(name = 'NITRITE', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'Menaquinones', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_RXN0_3501', 1.000000), 
	Parameter('rvs_RXN0_3501', 0.000000))
Rule('SUCROSEPHOSPHO_RXN',
	prot(name = 'BSU38050_MONOMER', loc = 'pmem') +
	met(name = 'Hpr_pi_phospho_L_histidines', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'SUCROSE', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	prot(name = 'BSU38050_MONOMER', loc = 'pmem') +
	met(name = 'Hpr_Histidine', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'CPD_15716', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_SUCROSEPHOSPHO_RXN', 1.000000), 
	Parameter('rvs_SUCROSEPHOSPHO_RXN', 0.000000))
Rule('TRANS_RXN8J2_109',
	prot(name = 'BSU39270_MONOMER', loc = 'pmem') +
	met(name = 'BETA_GLUCOSIDES', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PHOSPHO_ENOL_PYRUVATE', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	prot(name = 'BSU39270_MONOMER', loc = 'pmem') +
	met(name = 'Beta_Glucoside_6_P', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN8J2_109', 1.000000), 
	Parameter('rvs_TRANS_RXN8J2_109', 0.000000))
Rule('TRANS_RXN8J2_102',
	prot(name = 'BSU39390_MONOMER', loc = 'pmem') +
	met(name = 'HIS', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	prot(name = 'BSU39390_MONOMER', loc = 'pmem') +
	met(name = 'HIS', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN8J2_102', 1.000000), 
	Parameter('rvs_TRANS_RXN8J2_102', 0.000000))
Rule('ATPSYN_RXN',
	cplx(name = 'CPLX8J2_101', loc = 'pmem') +
	met(name = 'ADP', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	cplx(name = 'CPLX8J2_101', loc = 'pmem') +
	met(name = 'ATP', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_ATPSYN_RXN', 1.000000), 
	Parameter('rvs_ATPSYN_RXN', 1.000000))
Rule('TRANS_RXN_156',
	cplx(name = 'CPLX8J2_116', loc = 'pmem') +
	met(name = 'Hpr_pi_phospho_L_histidines', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'MANNITOL', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	cplx(name = 'CPLX8J2_116', loc = 'pmem') +
	met(name = 'MANNITOL_1P', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'Hpr_Histidine', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN_156', 1.000000), 
	Parameter('rvs_TRANS_RXN_156', 0.000000))
Rule('TRANS_RXN8J2_108',
	cplx(name = 'CPLX8J2_117', loc = 'pmem') +
	met(name = 'FRU', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PHOSPHO_ENOL_PYRUVATE', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	cplx(name = 'CPLX8J2_117', loc = 'pmem') +
	met(name = 'FRUCTOSE_6P', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN8J2_108', 1.000000), 
	Parameter('rvs_TRANS_RXN8J2_108', 0.000000))
Rule('TRANS_RXN8J2_112',
	cplx(name = 'CPLX8J2_119', loc = 'pmem') +
	met(name = 'Maltodextrins', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	None | 
	cplx(name = 'CPLX8J2_119', loc = 'pmem') +
	met(name = 'Maltodextrins', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN8J2_112', 1.000000), 
	Parameter('rvs_TRANS_RXN8J2_112', 0.000000))
Rule('TRANS_RXN8J2_113',
	cplx(name = 'CPLX8J2_141', loc = 'pmem') +
	met(name = 'FEplus3', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	cplx(name = 'CPLX8J2_141', loc = 'pmem') +
	met(name = 'FEplus3', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN8J2_113', 1.000000), 
	Parameter('rvs_TRANS_RXN8J2_113', 0.000000))
Rule('TRANS_RXN8J2_114',
	cplx(name = 'CPLX8J2_142', loc = 'pmem') +
	met(name = 'CAplus2', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	cplx(name = 'CPLX8J2_142', loc = 'pmem') +
	met(name = 'CAplus2', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN8J2_114', 1.000000), 
	Parameter('rvs_TRANS_RXN8J2_114', 0.000000))
Rule('TRANS_RXN_101',
	cplx(name = 'CPLX8J2_158', loc = 'pmem') +
	met(name = 'NAplus', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	cplx(name = 'CPLX8J2_158', loc = 'pmem') +
	met(name = 'PROTON', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'NAplus', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN_101', 1.000000), 
	Parameter('rvs_TRANS_RXN_101', 0.000000))
Rule('RXN_18028',
	cplx(name = 'CPLX8J2_161', loc = 'pmem') +
	met(name = 'Teichoic_P_Gro_Glc', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	None | 
	cplx(name = 'CPLX8J2_161', loc = 'pmem') +
	met(name = 'Teichoic_P_Gro_Glc', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_RXN_18028', 1.000000), 
	Parameter('rvs_RXN_18028', 0.000000))
Rule('TRANS_RXN0_506',
	cplx(name = 'CPLX8J2_189', loc = 'pmem') +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	cplx(name = 'CPLX8J2_189', loc = 'pmem') +
	met(name = 'PYRUVATE', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN0_506', 1.000000), 
	Parameter('rvs_TRANS_RXN0_506', 0.000000))
Rule('CYTOCHROME_C_OXIDASE_RXN',
	cplx(name = 'CPLX8J2_22', loc = 'pmem') +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'Cytochromes_C_Reduced', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	cplx(name = 'CPLX8J2_22', loc = 'pmem') +
	met(name = 'PROTON', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'Cytochromes_C_Oxidized', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_CYTOCHROME_C_OXIDASE_RXN', 1.000000), 
	Parameter('rvs_CYTOCHROME_C_OXIDASE_RXN', 0.000000))
Rule('TRANS_RXN8J2_99',
	cplx(name = 'CPLX8J2_37', loc = 'pmem') +
	met(name = 'Antibiotics', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	cplx(name = 'CPLX8J2_37', loc = 'pmem') +
	met(name = 'Antibiotics', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN8J2_99', 1.000000), 
	Parameter('rvs_TRANS_RXN8J2_99', 0.000000))
Rule('TRANS_RXN8J2_98',
	cplx(name = 'CPLX8J2_38', loc = 'ex') +
	met(name = 'CPD_9985', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	None | 
	cplx(name = 'CPLX8J2_38', loc = 'ex') +
	met(name = 'CPD_9985', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN8J2_98', 1.000000), 
	Parameter('rvs_TRANS_RXN8J2_98', 0.000000))
Rule('RXN_12164',
	cplx(name = 'CPLX8J2_43', loc = 'pmem') +
	met(name = 'Menaquinols', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'OXYGEN_MOLECULE', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	cplx(name = 'CPLX8J2_43', loc = 'pmem') +
	met(name = 'Menaquinones', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_RXN_12164', 1.000000), 
	Parameter('rvs_RXN_12164', 0.000000))
Rule('TRANS_RXN8J2_97',
	cplx(name = 'CPLX8J2_65', loc = 'pmem') +
	met(name = 'CHOLINE', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	None | 
	cplx(name = 'CPLX8J2_65', loc = 'pmem') +
	met(name = 'CHOLINE', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN8J2_97', 1.000000), 
	Parameter('rvs_TRANS_RXN8J2_97', 0.000000))
Rule('TRANS_RXN8J2_95',
	cplx(name = 'CPLX8J2_81', loc = 'pmem') +
	met(name = 'Antibiotics', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'bsubtilis', prot = None) | 
	cplx(name = 'CPLX8J2_81', loc = 'pmem') +
	met(name = 'Antibiotics', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN8J2_95', 1.000000), 
	Parameter('rvs_TRANS_RXN8J2_95', 0.000000))
Rule('TRANS_RXN8J2_96',
	cplx(name = 'CPLX8J2_93', loc = 'pmem') +
	met(name = 'CPD_543', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'ATP', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'WATER', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	None | 
	cplx(name = 'CPLX8J2_93', loc = 'pmem') +
	met(name = 'CPD_543', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'ADP', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'Pi', loc = 'cyt', strain = 'bsubtilis', prot = None) +
	met(name = 'PROTON', loc = 'cyt', strain = 'bsubtilis', prot = None), 
	Parameter('fwd_TRANS_RXN8J2_96', 1.000000), 
	Parameter('rvs_TRANS_RXN8J2_96', 0.000000))
