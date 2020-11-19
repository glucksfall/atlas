Rule Based Modeling Basics
==========================

Rule-based models (RBM) are characterized by the utilization of a formal
language. The language defines basic transformations:

  * Addition: two *agents* join together;
  * Separation: a complex of *agents* split into components;
  * Creation: An *agent* or a complex of *agents* appears in the system;
  * Deletion: An *agent* or a complex of *agents* is removed from the system; and
  * State change: A property of the *agent* is modified.

However, a rule-based model requires additional elements that shape the final form of rules
and this note is intended as an introduction to modeling with pySB. For more
information, please visit `<https://pysb.readthedocs.io/en/stable/tutorial.html>`_.
Rule-based models are defined by:

  * Monomers (*agents*): The complete definition of the possible characteristics of *agents*;
  * Parameters: The name and value of model parameters. Parameters are used as rule rates and *agent* initial quantities;
  * Rules: The formalized description of transformations involving *agents*;
  * Initials: The complete (*concrete* in terms of pySB) definition of an *agent* and its initial quantity; and
  * Observables: The complete or partial definition of *agents* that will be quantified throughout a simulation and an alias.

.. note::
    Observables are optionals, but its no inclusion will result in a simulation without trackable entities.

Rationale behind monomers definition in Atlas:

We defined five types of *agents*: metabolites, proteins, DNA, RNA, and Complex. The four first types of agents refer to the components of cells while the `Complex` was defined to be aliases of complex of *agents*, e.g., the ``RNAP_CPLX`` *agent* is an alias of the real protein complex that otherwise would be modeled by four interacting proteins. Next, because genes, RNA, and proteins share the same name (and normally are written capitalized or italized to differentiate them), we decided to create a ``name`` site that define the name:

.. literalinclude:: ./monomers_names.py
    :language: python
    :encoding: latin-1
    :linenos:

.. note::
    Monomers define the complete set of sites and site states that *agents* could adopt in the system. If a component of a rule, initial or observable do not match the monomer definition, pySB will raise an error. In addition, an initial must be concrete, meaning that all sites must be included and defined with a value.

Next, we created a ``loc`` site that define the location of the monomer. Bacterial cells has many compartments (see :ref:`Net-Metabolic` for a complete list of valid names) and monomers could exist on them:

.. literalinclude:: ./monomers_loc.py
    :language: python
    :encoding: latin-1
    :linenos:

Moreover, we created a ``type`` site for DNAs and RNAs. Both molecules normally has features that interact specifically with proteins. For instance, promoters interact with the RNA Polymerase and Ribosome Binding Sites interact (obviously) with the ribosome. We defined five types: promoter (PRO), ribosome binding site (RBS), coding DNA sequence (CDS), terminator (TER), and binding site (BS). The DNA binding sites interact with Transcription Factors and other proteins, while RNA binding sites interact with RNA-binding proteins (e.g., RNase E):

.. literalinclude:: ./monomers_types.py
    :language: python
    :encoding: latin-1
    :linenos:

After we solved how to describe concisely *agents* without creating single monomers for each one, we defined interaction sites. All five types of monomers has four interactions sites to interact with another *agent* of the type of the site: ``met`` to interact with a Metabolite, ``prot`` to interact with a protein, ``dna`` to interact with a DNA feature or part, and ``rna`` to interact with a RNA feature or part. However and as anticipated, a single site constraints the number of partners to one (of the type of the interaction site). To overcome the limit, we used the ``up`` and ``dw`` sites that Stewart & Wilson-Kanamori used for the description of DNA and RNA features in `Kappa BioBrick Framework <https://www.sciencedirect.com/science/article/pii/S1571066111001289>`_ to make polymers of proteins:

.. literalinclude:: ./monomers_updw.py
    :language: python
    :encoding: latin-1
    :linenos:

Now that we have a suitable definition of *agents* with purporsely created interaction sites, complex of *agents* are defined by unique numbered bonds that are shared by the interactions sites:

    For instance, the dimer ``[lacI,lacI]`` (see :ref:`Net-ProteinProtein` for details of the notation) is converted to:

    .. literalinclude:: ./dimer.py
        :language: python
        :encoding: latin-1
        :linenos:

    And a more complicated complex ``[lacI,lacI,SMALL-beta-ALLOLACTOSE]`` (see :ref:`Net-Protein-SmallCompounds` for details of the notation) is converted to:

    .. literalinclude:: ./dimer_lacI_allolactose.py
        :language: python
        :encoding: latin-1
        :linenos:

.. note::
    Valid site values are: ``None`` defines the site is empty, not bonded to any other agent; ``ANY`` defines the site is linked to an agent without explicitly write which it is; ``WILD`` defines the site could be linked or not, again without explicit mention to which agent; and a ``string`` that defines the state of the site (in the case of Atlas: name, location or type).

    PySB requires agents that are components of a complex must be separated by the ``%`` symbol.

    The same number must be repeated only twice. If a bond appears one time means that an *agent* has a dangling bond while three or more times mean the bond is ambiguous.

    In the case of *kappa* language, the bond number must be unique in the rule, even if it describes a link that appear in different complexes:

        .. literalinclude:: ./dimer_dimer.py
            :language: python
            :encoding: latin-1
            :linenos:

Finally, the notation of rules:

    Unidireccional rules employ the ``>>`` symbols to separate substrates (Left-hand side) and products (Right-hand side):

    .. literalinclude:: ./dimer_uni.py
        :language: python
        :encoding: latin-1
        :linenos:

    While bidireccional rules employ the ``|`` symbol:

    .. literalinclude:: ./dimer_bi.py
        :language: python
        :encoding: latin-1
        :linenos:
