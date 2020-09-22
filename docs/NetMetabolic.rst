.. _Net-Metabolic:

Metabolic Networks
==================

Metabolic networks have seven columns:

1. The 1st declares a name for the enzyme, gene, or enzymatic complex. Use *spontaneous* for non-enzymatic reactions.;
2. The 2nd declares the location of the enzyme, gene, or enzymatic complex:
   In the case of enzymatic complexes:

   1. If the number of locations match the number of components of the complex, each location is mapped to the component.
   2. If the number of locations unmatch the number of components, the first location is used for every component
   3. If the number of locations is one, the location is used for every component.

   Valid names are: ``cytosol``, ``inner membrane``, ``periplasmic space``, ``membrane``, ``outer membrane``, ``extracellular space``, ``bacterial nucleoid``, ``cell wall``, ``cell projection`` and ``cytoskeleton``

3. The 3rd declares a name for the reaction. If the name is not unique, Atlas drops the duplicated reaction;
4. The 4th column lists names for substrates using comma (without spaces);
5. The 5th column lists names for products using comma (without spaces);
   To declare metabolites located at a compartment, prefix the name of the metabolite (e.g. "PER-lactose"):

   * 'CYT-' : 'cytosol',
   * 'iMEM-' : 'inner membrane',
   * 'PER-' : 'periplasmic space',
   * 'MEM-' : 'membrane',
   * 'oMEM-' : 'outer membrane',
   * 'EX-' : 'extracellular space',
   * 'bNUC-' : 'bacterial nucleoid',
   * 'WALL-' : 'cell wall',
   * 'cPROJ-' : 'cell projection',
   * 'CYTOSK-' : 'cytoskeleton'

6. The 6th declares the forward reaction rate; and finally
7. The 7th declares the reverse reaction rate.

Examples:

.. literalinclude:: ./networks/network-lac-metabolism-enzymes.tsv
   :linenos:
   :encoding: latin-1

*OR*

.. literalinclude:: ./networks/network-lac-metabolism-genes.tsv
   :linenos:
   :encoding: latin-1

*OR*

.. literalinclude:: ./networks/network-lac-metabolism-complex.tsv
   :linenos:
   :encoding: latin-1

.. note::
    **Visualization in Cytoscape.** Transform the input file into a Cytoscape compatible file with ``atlas_rbm.utils.metabolicNetwork.expand_network(network, 'output.txt')`` and import the network into Cytoscape.

    Colors and arrows remains to the user for customization:
    The following image was prepared from the `lactose-metabolism-cytoscape-v3.txt <github.com/networkbiolab/atlas/tree/master/tutorial/lactose-metabolism-cytoscape-v3.txt>`_ file, and you could reproduce it with Cytoscape:

    1. Click on the ``Import Network from File System`` icon or click on ``File -> Import -> Network from File...``.
    2. Navigate to the file and click on ``Open``.
    3. SOURCE, TARGET, and EDGE ATTRIBUTE are OK, but the 4th columns must be the SOURCE NODE ATTRIBUTE and the 5th column the TARGET NODE ATTRIBUTE. Click on the header and change it to the correct attribute. The attributes will help later to filter and to add format to nodes and edges.
    4. Click on ``Filter`` (on the right), then on the ``+`` icon and finally on ``Column Filter``:

      1. On the selector, click on ``Edge: EDGE_ATTRIBUTE`` and change ``contains`` to ``is``:

         1. Write ``NO_REVERSIBLE`` that will select edges that correspond to irreversible reactions. Click on ``Style``, then ``Edge`` (in the bottom), and click on the 3rd column to bypass the format of the ``Target Arrow Shape`` and select your favorite arrow shape.
         2. Write ``REVERSIBLE`` and bypass the format of the ``Source Arrow Shape`` AND ``Target Arrow Shape``, and select your favorite arrow shape.

      2. On the selector, click on ``Node: SOURCE_NODE_ATTRIBUTE``:

         1. Write ``RXN`` that will select nodes enconding the reactions. Click on ``Style``, then on ``Node`` and bypass the ``Fill Color``. In the new window, you could set-up the color, e.g. #00AA50
         2. Write ``GENE_PROD`` that will select nodes encoding the gene name, protein name, or the enzyme name. Click on ``Style``, then on ``Node`` and bypass the ``Fill Color``. In the new window, you could set-up the color, e.g. #CC0033
         3. Write ``MET`` that will select nodes encoding substrate metabolites. Click on ``Style``, then on ``Node`` and bypass the ``Fill Color``. In the new window, you could set-up the color, e.g. #00ABDD. Also, set a shape for nodes, to differentiate substrates from products.

      3. On the selector, click on ``Node: TARGET_NODE_ATTRIBUTE``:

         1. Write ``MET`` that will select nodes encoding product metabolites. Click on ``Style``, then on ``Node`` and bypass the ``Fill Color``. In the new window, you could set-up the color, e.g. #00ABDD

    .. image:: Fig_Lactose_MetNetwork.png

Finally, execute ``atlas_rbm.construct_model_from_metabolic_network(network, verbose = False)`` to obtain the model.

.. note::
    **Uniqueness of Rule names**. Atlas will write *Rules* for unique
    metabolic reactions. Identical names will be reported for further curation.

.. note::
    **Simulation**. The model can be simulated only with the instantiation of ``Initials``:

    * ``atlas_rbm.simulation.set_initial.cplx(model, complex_name, location, positive_number)``
    * ``atlas_rbm.simulation.set_initial.dna(model, dna_name, positive_number)``
    * ``atlas_rbm.simulation.set_initial.met(model, metabolite, location, positive_number)``
    * ``atlas_rbm.simulation.set_initial.prot(model, prot_name, location, positive_number)``
    * ``atlas_rbm.simulation.set_initial.rna(model, rna_name, positive_number)``

.. note::
    For large models, the ``noObservables`` and the ``noInitials`` will make a faster compilation, while later you could add ``Initials`` and ``Observables`` to the model.

    Use the keyword argument ``toFile = 'name.py'`` to write the model to a file (the function will return ``None``):

    .. literalinclude:: ./model_metabolic_network1.py
       :language: python
       :encoding: latin-1
       :linenos:
