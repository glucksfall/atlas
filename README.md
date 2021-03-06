Atlas RBM
=========

Automatic rule-based modeling of metabolism, protein-protein interactions, and regulation of gene expression
------------------------------------------------------------------------------------------------------------

Authors: Rodrigo Santibáñez[1,2], Daniel Garrido[2], and Alberto Martín[1]

Date: August 2020

[![DOI](https://zenodo.org/badge/226966537.svg)](https://zenodo.org/badge/latestdoi/226966537)

Affiliations:
1. Network Biology Lab, Centro de Genómica y Bioinformática, Facultad de Ciencias, Universidad Mayor, Santiago, 8580745, Chile.
2. Department of Chemical and Bioprocess Engineering, School of Engineering, Pontificia Universidad Católica de Chile, Santiago, 7820436, Chile

![Graphical abstract](https://github.com/glucksfall/atlas/blob/master/graphical_abstract.png)

## Prerequisites

1. PathwayTools must be installed and running to obtain data from the BioCyc databases. Please, run ```pathway-tools -lisp -python-local-only``` before to obtain any data.<br/>
   (Optional) The PathwayTools software could be executed in the background, with help of ```nohup pathway-tools -lisp -python-local-only > /dev/null 2> /dev/null &```.<br/>
   Please follow instructions at http://pathwaytools.org/ to obtain a licensed copy of the software from https://biocyc.org/download-bundle.shtml. However, data could be manually formatted using a text-based editor or a spreadsheet software.

   Note: If you ran into the ```pathway-tools/ptools/24.0/exe/aclssl.so: undefined symbol: CRYPTO_set_locking_callback``` error, please follow instructions here: https://github.com/glucksfall/atlas/tree/master/PTools-Docker. Instructions will guide you to install a docker image that is able to run pathway tools, but does not include it, so you still need to obtain the software with a valid license.<br/>

2. (Highly recommended) Install Docker. Please follow instructions for a supported Operating System https://docs.docker.com/engine/install/:<br/>
   On Ubuntu, install it with ```apt-get install docker.io```.<br/>
   On Win10, install Docker Desktop with WSL2 support https://docs.docker.com/docker-for-windows/wsl/.<br/>
   On MacOS, install Docker Desktop https://docs.docker.com/docker-for-mac/install/.<br/>
   The Docker ```networkbiolab/pleiades```installs the python packages, the jupyter server, and the stochastic simulators.<br/>

3. (Recommended) Jupyter notebook. We recommend the use of Anaconda3 https://www.anaconda.com/products/individual because of the easier installation of the stochastic simulators from https://anaconda.org/alubbock.<br/>

4. (Optional) A stochastic simulator, supported by the pySB python package ([BNG2](https://github.com/RuleWorld/bionetgen), [NFsim](https://github.com/ruleworld/nfsim/tree/9178d44455f6e27a81f398074eeaafb2a1a4b4bd), [KaSim](https://github.com/Kappa-Dev/KappaTools) or [Stochkit](https://github.com/StochSS/StochKit)). pySB requires BNG2 to simulate models with NFsim.<br/>

5. (Optional) Cytoscape to visualize metabolic networks and others.<br/>

6. (Optional) A deterministic simulator: pySB supports ODE integration via scipy.integrate.ode, BioNetGen ODE integration, and CUDA-accelerated ODE integration with Marco S. Nobile's cupSODA software (https://github.com/aresio/cupSODA). If the user feel comfortable with SBML models, pySB could export to SBML and deterministic simulation done with libRoadRunner (http://libroadrunner.org/), Tellurium (http://tellurium.analogmachine.org/), COPASI (http://copasi.org/), etc.

## Installation

To install, please follow one of the following steps:<br/>
   1. Install the docker image "pleiades" using ```docker pull networkbiolab/pleiades```. The container is based on the Anaconda3 software and it installs Atlas, and the stochastic simulators BNG2, NFsim, KaSim, and Stochkit. After building the image, please run the container with ```docker run --detach --publish 10000:8888 networkbiolab/pleiades```, and go to ```localhost:10000``` in your preferred browser. The required password is ```pleiades```.<br/>
   2. Download or clone the Github repository from https://github.com/networkbiolab/pleiades with ```git clone https://github.com/networkbiolab/pleiades foo``` (where ```foo``` is an absolute or relative path). Then, you could build the docker image with ```docker build foo --tag pleiades``` and run it with ```docker run --detach --publish 10000:8888 pleiades```. Finally, go to ```localhost:10000``` in your preferred browser. The required password is ```pleiades```.<br/>
   3. Install with pip3: ```sudo -H python3 -m pip install pleiades``` or ```python3 -m pip install pleiades --user```. Pleiades is a meta-package that install Atlas (the rule-based modeller), Pleione (a genetic algorithm for parameter calibration of RBMs, compatible with SLURM), Alcyone (to perform identifiability analysis of parameters), and Sterope (to perform sensitivity analysis of parameters in kappa RBMs, compatible with SLURM).<br/>
      You should install, configure, and run the jupyter notebook on your own: example ```sudo -H pip3 install jupyter && nohup python3 -m jupyter notebook --port=8888 --no-browser --port-retries=0 > /dev/null 2> /dev/null &```.<br/>
   4. Download or clone the Github repository from https://github.com/networkbiolab/atlas with ```git clone https://github.com/networkbiolab/atlas foo``` (where ```foo``` is an absolute or relative path). Requisites must be fulfilled manually with pip3: ```sudo -H python3 -m pip install pandas pysb pythoncyc jupyter seaborn``` or ```python3 -m pip install pandas pysb pythoncyc jupyter seaborn --user```.

## External resources

* PySB documentation: https://pysb.readthedocs.io/en/stable/
* Kappa and KaSim documentation: https://kappalanguage.org/sites/kappalanguage.org/files/inline-files/Kappa_Manual.pdf
* BioNetGen Language and BNG2 documentation: http://bionetgen.org/
* pyDREAM documentation: https://pydream.readthedocs.io/en/latest/
  * pyDREAM for pySB: https://github.com/LoLab-VU/PyDREAM/tree/master/pydream/examples/corm
  * pyDREAM for pySB: https://github.com/LoLab-VU/PyDREAM/tree/master/pydream/examples/robertson
* pyBioNetFit documentation: https://pybnf.readthedocs.io/en/latest/
  * Examples: https://github.com/lanl/PyBNF/tree/master/examples
* Pleione documentation: https://pleione.readthedocs.io/en/latest/
  * Calibration with BNG2: https://github.com/networkbiolab/pleione/tree/master/examples/bng2
  * Calibration with KaSim: https://github.com/networkbiolab/pleione/tree/master/examples/kasim
  * Calibration with NFsim: https://github.com/networkbiolab/pleione/tree/master/examples/nfsim
  * Calibration with PISKaS: https://github.com/networkbiolab/pleione/tree/master/examples/piskas
* pyViPR documentation: https://pyvipr.readthedocs.io/en/latest/
  * Tutorial: https://github.com/networkbiolab/atlas/blob/master/tutorial/tutorial%20-%202%20-%20Visualization%20of%20models.ipynb
