.. _Net-ProteinProtein:

Protein-Protein Interaction Networks
====================================

Protein-protein interaction (PPI) networks have five columns:

1. The 1st declares the ``SOURCE`` and the 2nd declares the ``TARGET``.

   It does not matter the order, as the two columns defines a bimolecular reaction which product is the merge of all components into one complex.
   *Atlas* understand components inside brackets (e.g., ``[lacZ,lacZ]``) as a complex, therefore, the components are internally linked. For non-symmetrical complexes
   (e.g., ``[araF,araH,araH,araG,araG]``), the user must be aware that the order in ``SOURCE`` and ``TARGET`` defines the order in the product: ``[SOURCE,TARGET]``.

2. The 3rd and 4th columns declare the forward and the reverse reaction rate values, respectively.
3. The 5th column declares the location of the complex components:

   1. If the number of locations match the number of components of the complex, each location is mapped in the same order to each component.
   2. If the number of locations unmatch the number of components, the first location is used for every component. The remaining locations are disregarded.
   3. If the number of locations is one, the location is used for every component.

   Valid location names are: ``cytosol``, ``inner membrane``, ``periplasmic space``, ``membrane``, ``outer membrane``, ``extracellular space``, ``bacterial nucleoid``, ``cell wall``, ``cell projection`` and ``cytoskeleton``

Examples:

.. literalinclude:: ./networks/network-lac-ProtProt.tsv
   :linenos:
   :encoding: latin-1

.. note::
    **Visualization in Cytoscape.** Cytoscape cannot import hyper-graphs. To do so,
    Create simple networks and right-click to embed a subnetwork in the corresponding node.

    .. image:: Fig_Lactose_PPINetwork.png

Finally, execute ``atlas_rbm.construct_model_from_interaction_network(network, verbose = False)`` to obtain the model.

.. note::
    **Uniqueness of Rule names**. Atlas will write *Rules* with numbered
    names. Merge into one ``DataFrame`` the networks (employing ``pandas.concat(list)``) or
    concatenate externally and employ a single file to model interactions.

.. note::
    **Simulation**. The model can be simulated only with the instantiation of ``Initials``:

    * ``atlas_rbm.simulation.set_initial.cplx(model, complex_name, location, positive_number)``
    * ``atlas_rbm.simulation.set_initial.dna(model, dna_name, positive_number)``
    * ``atlas_rbm.simulation.set_initial.met(model, metabolite, location, positive_number)``
    * ``atlas_rbm.simulation.set_initial.prot(model, prot_name, location, positive_number)``
    * ``atlas_rbm.simulation.set_initial.rna(model, rna_name, positive_number)``

.. note::
    Use the keyword argument ``toFile = 'name.py'`` to write the model to a file (the function will return ``None``):

    .. literalinclude:: ./model_ppi_network1.py
       :language: python
       :encoding: latin-1
       :linenos:
