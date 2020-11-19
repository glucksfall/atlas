.. _Net-SFsPromoters:

Sigma Factor-Promoter Interaction Networks
==========================================

The Sigma Factor-Promoter network have five columns:

1. The 1st declares the ``SOURCE`` and the 2nd declares the ``TARGET``.

   It does not matter the order, as the two columns defines a bimolecular reaction which product is the merge of all components into one complex.
   *Atlas* understand components inside brackets (e.g. ``[rpoA,rpoA,rpoB,rpoC,rpoD]``) as a complex, therefore, the components are internally linked.

2. The 3rd, 4th, and 5th columns declare rate values:

   * The ``FWD_DOCK_RATE`` and the ``RVS_DOCK_RATE`` define the rates of the binding of the RNAP to the promoter and its separation, respectively.
   * The ``FWD_SLIDE_RATE`` defines the rate of the transition from the promoter to the following DNA feature declared in the genome graph (see :ref:`Net-GenomeGraphs`).

   Note the name of the promoter: name of the gene followed by ``pro`` and a number.

Examples:

.. literalinclude:: ./networks/network-lac-sigma-specificity.tsv
   :linenos:
   :encoding: latin-1

Finally, execute ``atlas_rbm.construct_model_from_sigma_specificity_network(interaction_network, genome_graph, verbose = False)`` to obtain the model.

.. note::
    **Simulation**. The model can be simulated only with the instantiation of ``Initials``:

    * ``atlas_rbm.simulation.set_initial.cplx(model, complex_name, location, positive_number)``
    * ``atlas_rbm.simulation.set_initial.dna(model, dna_name, positive_number)``
    * ``atlas_rbm.simulation.set_initial.met(model, metabolite, location, positive_number)``
    * ``atlas_rbm.simulation.set_initial.prot(model, prot_name, location, positive_number)``
    * ``atlas_rbm.simulation.set_initial.rna(model, rna_name, positive_number)``

.. note::
    Use the keyword argument ``toFile = 'name.py'`` to write the model to a file (the function will return ``None``):

    .. literalinclude:: ./model_sigma_network1.py
       :language: python
       :encoding: latin-1
       :linenos:
