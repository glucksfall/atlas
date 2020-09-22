.. _Net-GenomeGraphs:

Genome Graphs
=============

The Genome Graphs have ten columns:

1. The 1st declares the ``UPSTREAM`` and the 2nd declares the ``DOWNSTREAM`` DNA feature.

   The DNA features are five: ``pro`` followed by a number, ``rbs``, ``cds``, ``ter`` followed by a number, and ``BS-`` to define DNA binding sites.

2. The next columns declare rates:

   * ``RNAP_FWD_DOCK_RATE`` and ``RNAP_RVS_DOCK_RATE`` are valid values only for the description of the reversible interaction of the RNA Polymerase to the promoters.
   * ``RNAP_FWD_SLIDE_RATE`` are valid values for the transition of the RNA Polymerase from the ``UPSTREAM`` to the ``DOWNSTREAM`` DNA parts. We describe rules where the RNA Polymerase could not move back.
   * ``RNAP_FWD_FALL_RATE`` are valid values only for the description of the unbinding of the RNA Polymerase and the ``UPSTREAM`` identifiying a DNA terminator.

   * ``RIB_FWD_DOCK_RATE`` and ``RIB_RVS_DOCK_RATE`` are valid values only for the description of the reversible interaction of the bacterial Ribosome to the RBS.
   * ``RIB_FWD_SLIDE_RATE`` are valid values for the transition of the Ribosome from the ``UPSTREAM`` to the ``DOWNSTREAM`` RNA parts. We describe rules where the Ribosome could not move back.
   * ``RIB_FWD_FALL_RATE`` are valid values only for the description of the unbinding of the Ribosome and the ``UPSTREAM`` identifiying a CDS.

Example, and note the use of the prefix ``BS-`` to tell *Atlas* the component is a DNA binding site followed by a name and two coordinates:

.. literalinclude:: ./networks/network-lac-operon-arq.tsv
   :linenos:
   :encoding: latin-1

*OR*

.. literalinclude:: ./networks/network-operon-arq.txt
   :linenos:
   :encoding: latin-1

.. note::
    **Visualization in Cytoscape.** Colors and arrows remains to the user for
    customization. The network could be complemented with a description of
    sigma factor specifity for promoter, as the following network

    .. image:: Fig_GenomeGraphs-crop.png

Finally, execute ``atlas_rbm.construct_model_from_genome_graph(network, verbose = False)`` to obtain the model.

.. note::
    **Simulation**. The model can be simulated only with the instantiation of ``Initials``:

    * ``atlas_rbm.simulation.set_initial.cplx(model, complex_name, location, positive_number)``
    * ``atlas_rbm.simulation.set_initial.dna(model, dna_name, positive_number)``
    * ``atlas_rbm.simulation.set_initial.met(model, metabolite, location, positive_number)``
    * ``atlas_rbm.simulation.set_initial.prot(model, prot_name, location, positive_number)``
    * ``atlas_rbm.simulation.set_initial.rna(model, rna_name, positive_number)``

.. note::
    **Kappa BioBrick Framework.** The *Rules* for transcription and translation
    come from the work of Stewart and Wilson-Kanamori (See more
    `here <https://www.sciencedirect.com/science/article/pii/S1571066111001289>`_).
    A "pure" genome graph uses the originally defined rules, while a genome
    graph + sigma factor specifity uses a modified *rules* to model the release
    of the sigma factor from the RNA Polymerase at the transcription
    initiation.

    .. literalinclude:: ./model_graph_network1.py
       :language: python
       :encoding: latin-1
       :linenos:
