Modeling
========

Atlas is a modular software with each script centered in a specific biological
network

1. **Metabolic Networks**

2. **Interaction Networks**

   1. **Protein-Protein**
   2. **Protein-Small Compounds**
   3. **Protein-DNA binding sites**
   4. **Protein-RNA**
   5. **mRNA-regulatory RNA**
   6. **Sigma Factors-Promoters**

3. **Genome graphs**

1: Metabolic Networks
---------------------

Metabolic networks have four columns. The first declares a unique name for the
enzyme or enzymatic complex; the second declares a unique name for the reaction;
the third column lists using comma unique names for substrates; and the last row
list using comma unique names for products. To declare metabolites located at
the periplasm or extracellular compartments, the user should employ the prefix
“PER-” and “EX-”, respectively. Use *spontaneous* for non-enzymatic reactions.

Examples:

.. code-block:: bash

	spontaneous	LACTOSE-MUTAROTATION	alpha-lactose	beta-lactose
	spontaneous	GALACTOSE-MUTAROTATION	alpha-GALACTOSE	beta-GALACTOSE
	spontaneous	GLUCOSE-MUTAROTATION	alpha-glucose	beta-glucose
	LACY-MONOMER	TRANS-RXN-24	PER-PROTON, PER-alpha-lactose	PROTON, alpha-lactose
	LACY-MONOMER	TRANS-RXN-24-beta	PER-PROTON, PER-beta-lactose	PROTON, beta-lactose
	LACY-MONOMER	TRANS-RXN-94	PER-PROTON, PER-MELIBIOSE	PROTON, MELIBIOSE
	LACY-MONOMER	RXN0-7215	PER-PROTON, PER-CPD-3561	PROTON, CPD-3561
	LACY-MONOMER	RXN0-7217	PER-PROTON, PER-CPD-3785	PROTON, CPD-3785
	LACY-MONOMER	RXN-17755	PER-PROTON, PER-CPD-3801	PROTON, CPD-3801
	BETAGALACTOSID-CPLX	BETAGALACTOSID-RXN	beta-lactose, WATER	beta-GALACTOSE, beta-glucose
	BETAGALACTOSID-CPLX	BETAGALACTOSID-RXN-alpha	alpha-lactose, WATER	alpha-GALACTOSE, alpha-glucose
	BETAGALACTOSID-CPLX	RXN0-5363	alpha-lactose	alpha-ALLOLACTOSE
	BETAGALACTOSID-CPLX	RXN0-5363-beta	beta-lactose	beta-ALLOLACTOSE
	BETAGALACTOSID-CPLX	ALLOLACTOSE-DEG-alpha	alpha-ALLOLACTOSE	alpha-GALACTOSE, alpha-glucose
	BETAGALACTOSID-CPLX	ALLOLACTOSE-DEG-beta	beta-ALLOLACTOSE	beta-GALACTOSE, beta-glucose
	BETAGALACTOSID-CPLX	RXN-17726	CPD-3561, WATER	beta-GALACTOSE, Fructofuranose
	BETAGALACTOSID-CPLX	RXN0-7219	CPD-3785, WATER	beta-GALACTOSE, D-ARABINOSE
	GALACTOACETYLTRAN-CPLX	GALACTOACETYLTRAN-RXN-galactose	beta-GALACTOSE, ACETYL-COA	6-Acetyl-beta-D-Galactose, CO-A

*OR*

.. code-block:: bash

	spontaneous	LACTOSE-MUTAROTATION	alpha-lactose	beta-lactose
	spontaneous	GALACTOSE-MUTAROTATION	alpha-GALACTOSE	beta-GALACTOSE
	spontaneous	GLUCOSE-MUTAROTATION	alpha-glucose	beta-glucose
	lacY	TRANS-RXN-24	PER-PROTON, PER-alpha-lactose	PROTON, alpha-lactose
	lacY	TRANS-RXN-24-beta	PER-PROTON, PER-beta-lactose	PROTON, beta-lactose
	lacY	TRANS-RXN-94	PER-PROTON, PER-MELIBIOSE	PROTON, MELIBIOSE
	lacY	RXN0-7215	PER-PROTON, PER-CPD-3561	PROTON, CPD-3561
	lacY	RXN0-7217	PER-PROTON, PER-CPD-3785	PROTON, CPD-3785
	lacY	RXN-17755	PER-PROTON, PER-CPD-3801	PROTON, CPD-3801
	[lacZ,lacZ,lacZ,lacZ]	BETAGALACTOSID-RXN	beta-lactose, WATER	beta-GALACTOSE, beta-glucose
	[lacZ,lacZ,lacZ,lacZ]	BETAGALACTOSID-RXN-alpha	alpha-lactose, WATER	alpha-GALACTOSE, alpha-glucose
	[lacZ,lacZ,lacZ,lacZ]	RXN0-5363	alpha-lactose	alpha-ALLOLACTOSE
	[lacZ,lacZ,lacZ,lacZ]	RXN0-5363-beta	beta-lactose	beta-ALLOLACTOSE
	[lacZ,lacZ,lacZ,lacZ]	ALLOLACTOSE-DEG-alpha	alpha-ALLOLACTOSE, WATER	alpha-GALACTOSE, alpha-glucose
	[lacZ,lacZ,lacZ,lacZ]	ALLOLACTOSE-DEG-beta	beta-ALLOLACTOSE, WATER	beta-GALACTOSE, beta-glucose
	[lacZ,lacZ,lacZ,lacZ]	RXN-17726	CPD-3561, WATER	beta-GALACTOSE, Fructofuranose
	[lacZ,lacZ,lacZ,lacZ]	RXN0-7219	CPD-3785, WATER	beta-GALACTOSE, D-ARABINOSE
	[lacA,lacA,lacA]	GALACTOACETYLTRAN-RXN-galactose	beta-GALACTOSE, ACETYL-COA	6-Acetyl-beta-D-Galactose, CO-A

*OR*

.. code-block:: bash

	spontaneous	LACTOSE-MUTAROTATION	alpha-lactose	beta-lactose
	spontaneous	GALACTOSE-MUTAROTATION	alpha-GALACTOSE	beta-GALACTOSE
	spontaneous	GLUCOSE-MUTAROTATION	alpha-glucose	beta-glucose
	lacY	TRANS-RXN-24	PER-PROTON, PER-alpha-lactose	PROTON, alpha-lactose
	lacY	TRANS-RXN-24-beta	PER-PROTON, PER-beta-lactose	PROTON, beta-lactose
	lacY	TRANS-RXN-94	PER-PROTON, PER-MELIBIOSE	PROTON, MELIBIOSE
	lacY	RXN0-7215	PER-PROTON, PER-CPD-3561	PROTON, CPD-3561
	lacY	RXN0-7217	PER-PROTON, PER-CPD-3785	PROTON, CPD-3785
	lacY	RXN-17755	PER-PROTON, PER-CPD-3801	PROTON, CPD-3801
	lacZ	BETAGALACTOSID-RXN	beta-lactose, WATER	beta-GALACTOSE, beta-glucose
	lacZ	BETAGALACTOSID-RXN-alpha	alpha-lactose, WATER	alpha-GALACTOSE, alpha-glucose
	lacZ	RXN0-5363	alpha-lactose	alpha-ALLOLACTOSE
	lacZ	RXN0-5363-beta	beta-lactose	beta-ALLOLACTOSE
	lacZ	ALLOLACTOSE-DEG-alpha	alpha-ALLOLACTOSE, WATER	alpha-GALACTOSE, alpha-glucose
	lacZ	ALLOLACTOSE-DEG-beta	beta-ALLOLACTOSE, WATER	beta-GALACTOSE, beta-glucose
	lacZ	RXN-17726	CPD-3561, WATER	beta-GALACTOSE, Fructofuranose
	lacZ	RXN0-7219	CPD-3785, WATER	beta-GALACTOSE, D-ARABINOSE
	lacA	GALACTOACETYLTRAN-RXN-galactose	beta-GALACTOSE, ACETYL-COA	6-Acetyl-beta-D-Galactose, CO-A
