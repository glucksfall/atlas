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

  * Monomers (*agents*): The complete definition of the characteristics of *agents*;
  * Parameters: The name and value of model parameters. Parameters are used as rule rates and *agent* initial quantities;
  * Rules: The formalized description of transformations involving *agents*;
  * Initials: The complete (*concrete* in terms of pySB) definition of an *agent* and its initial quantity; and
  * Observables: The definition of *agents* that will be quantified throughout a simulation and an alias.

.. note::
    Observables are optionals, but its no inclusion will result in a simulation without tracked entities.

Rationale behind monomers definition in Atlas:

We defined five types of *agents*: metabolites, proteins, DNA, RNA, and complex. The four first types of agents refer to the components of cells while the `Complex` was defined to be aliases of complex of *agents*, e.g., the ``RNAP`` *agent* is a complex that otherwise would be modeled four proteins. Next, because genes, RNA, and proteins share the same name (and normally are written capitalized or italized to differentiate them), we decided to create a ``name`` site that define the name:

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

Moreover, we created a ``type`` site for DNAs and RNAs. Both molecules normally has features that interact specifically with proteins. For instance, promoters interact with the RNA Polymerase and Ribosome Binding Sites interact (obviously) with the ribosome. We defined five types: promoter (PRO), ribosome binding site (RBS), coding DNA sequence (CDS), terminator (TER), and binding site (BS).

.. literalinclude:: ./monomers_types.py
    :language: python
    :encoding: latin-1
    :linenos:
