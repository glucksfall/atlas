.. _Simulation-page:

Simulation
==========

Simulation could be done within the PySB python package (See more at `PySB
documentation <https://pysb.readthedocs.io/en/stable/tutorial.html#simulation-and-analysis>`_).
Here is the relevant code that enable the simulation of any PySB model. Step are done internally
by PySB: export of the model, call to the simulator, and import of the results.

.. note::
    See :ref:`Plotting-page` for a simple example on how to plot simulation results.

.. literalinclude:: ./simulation.py
   :language: python
   :encoding: latin-1
   :linenos:
   :emphasize-lines: 2,3,4,5

.. note::
    Please follow the instructions at `BioNetGen <https://github.com/RuleWorld/bionetgen>`_
    and at `KaSim <https://github.com/Kappa-Dev/KaSim>`_ documentations to install
    the stochactic simulators. Also, you could install the simulators from `here <https://anaconda.org/alubbock/repo>`_
    if you have anaconda or conda installed on your system.

    In the case of the cupSODA, modify the `compile.sh <https://github.com/aresio/cupSODA/blob/master/compile.sh>`_ file
    to match the compute architecture of your NVIDIA GPU and compile the executable as ``cupSODA``.

    For network-based simulations (Ordinary Differential
    Equations and Gillespie's algorithm), BioNetGen is required to perform the network
    generation. Change the corresponding paths (lines 2-5) to match the parent folder for
    the BNG2.pl or KaSim executable. If using the pleiades docker instance, there is no
    necessity to set the path.
