Requirements
============

1. PathwayTools must be installed and running to obtain data from the BioCyc databases. Please, run ```pathway-tools -lisp -python-local-only``` before to obtain any data.

   (Optional) The PathwayTools software could be executed in the background, with help of ```nohup pathway-tools -lisp -python-local-only > /dev/null 2> /dev/null &```.
   Please follow instructions at http://pathwaytools.org/ to obtain a licensed copy of the software from https://biocyc.org/download-bundle.shtml. However, data could be manually formatted using a text-based editor or a spreadsheet software.

   Note: If you ran into the ```pathway-tools/ptools/24.0/exe/aclssl.so: undefined symbol: CRYPTO_set_locking_callback``` error, please follow instructions here: https://github.com/networkbiolab/atlas/tree/master/PTools-Docker. Instructions will guide you to install a docker image that is able to run pathway tools, but does not include it, so you still need to obtain the software with a valid license.

2. (Highly recommended) Install Docker. Please follow instructions for a supported Operating System https://docs.docker.com/engine/install/:

   On Ubuntu, install it with ```apt-get install docker.io```.

   On Win10, install Docker Desktop with WSL2 support https://docs.docker.com/docker-for-windows/wsl/.

   On MacOS, install Docker Desktop https://docs.docker.com/docker-for-mac/install/.

   The Docker ```networkbiolab/pleiades``` installs the python packages, the jupyter server, and the stochastic simulators.

3. (Recommended) Jupyter notebook. We recommend the use of Anaconda3 https://www.anaconda.com/products/individual because of the easier installation of the stochastic simulators from https://anaconda.org/alubbock.

4. (Optional) A stochastic simulator, supported by the pySB python package (`BNG2 <https://github.com/RuleWorld/bionetgen>`_, `NFsim <https://github.com/ruleworld/nfsim/tree/9178d44455f6e27a81f398074eeaafb2a1a4b4bd>`_, `KaSim <https://github.com/Kappa-Dev/KappaTools>`_ or `Stochkit <https://github.com/StochSS/StochKit>`_). pySB requires BNG2 to simulate models with NFsim.

5. (Optional) Cytoscape to visualize metabolic networks and others.

6. (Optional) A deterministic simulator: pySB supports ODE integration via scipy.integrate.ode, BioNetGen ODE integration, and CUDA-accelerated ODE integration with Marco S. Nobile's cupSODA software (https://github.com/aresio/cupSODA). If the user feel comfortable with SBML models, pySB could export to SBML and deterministic simulation done with libRoadRunner (http://libroadrunner.org/), Tellurium (http://tellurium.analogmachine.org/), COPASI (http://copasi.org/), etc.
