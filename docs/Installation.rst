Installation
============

There are different ways to install Atlas:

1. **Install the docker Pleiades (Highly recommended).** The docker container is the easiest way to obtain
   the software Atlas, the stochastic simulators BioNetGen and KaSim, and the Jupyter notebook.

   *OR*

2. **Clone the Pleiades GitHub repository.** If you are familiar with git, the docker container could
   be obtained cloning the Pleiades repository. Further details are below.

   *OR*

3. **Install Atlas with pip3.**

   *OR*

4. **Clone the Atlas GitHub repository.** If you are familiar with git, Atlas could
   be obtained cloning the Atlas repository and the respective directory added to `PYTHONPATH`.
   Further details are below.

.. note::
    **Need Help?**
    If you run into any problems with installation, please visit our chat room:
    https://gitter.im/glucksfall/pleiades

Option 1: Install the Pleiades docker container
-----------------------------------------------
Install the docker container is the easiest way to obtain the software Atlas.

Install the docker image "pleiades" using ```docker pull networkbiolab/pleiades```.
The container is based on the Anaconda3 software and
it installs Atlas, and the stochastic simulators BNG2, NFsim, KaSim, and
Stochkit. After building the image, please run the container with
```docker run --detach --publish 10000:8888 networkbiolab/pleiades```, and go to
```localhost:10000``` in your preferred browser. The required password is
```pleiades```.

Option 2: Clone the Pleiades repository
---------------------------------------

Download or clone the Github repository from https://github.com/networkbiolab/pleiades
with ```git clone https://github.com/networkbiolab/pleiades foo``` (where ```foo``` is an absolute
or relative path). Then, you could build the docker image with ```docker build foo --tag pleiades```
and run it with ```docker run --detach --publish 10000:8888 pleiades```.
Finally, go to ```localhost:10000``` in your preferred browser. The required password is ```pleiades```.

Option 3: Install Atlas natively on your computer
-------------------------------------------------

The recommended approach is to use system tools, or install them if
necessary. To install python packages, you could use pip, or download
the package from the `python package index <https://pypi.org/project/atlas-rbm/>`_.

1. **Install with system tools**

   With pip, you need to execute and Atlas will be installed on
   ``$HOME/.local/lib/python3.6/site-packages`` directory or similar.

   .. code-block:: bash

    pip3 install atlas_rbm --user

   If you have system rights, you could install Atlas for all users with

   .. code-block:: bash

    sudo -H pip3 install atlas_rbm

2. **Download from the python package index**

   Alternatively, you could download the package (useful when pip fails to download
   the package because of lack of SSL libraries) and then install with pip. For instance:

   .. code-block:: bash

    wget https://files.pythonhosted.org/packages/ec/ed/8b94e0a29f69a24ddb18ba4a4e6463d3ecede308576774e86baf6a84b998/atlas_rbm-1.0.2-py3-none-any.whl
    pip3 install atlas_rbm-1.0.2-py3-none-any.whl --user

   .. note::
    **Why Python3?**:
    Atlas is intended to be used with >=python3.4 because python2.7 won't receive
    further development past 2020, including security updates.

   .. note::
    **pip, Python, and Anaconda**:
    Be aware which pip you invoque. You could install pip3 with
    ``sudo apt-get install python3-pip`` if you have system rights, or
    install python3 from source, and adding ``<python3 path>/bin/pip3`` to the
    path, or linking it in a directory like ``$HOME/bin`` which is commonly
    added to the path at login. Also be aware that, if you installed
    Anaconda, pip could be linked to the Anaconda specific version of pip, which
    will install Atlas into Anaconda's installation folder.
    Type ``which pip`` or ``which pip3`` to find out the source of pip, and type
    ``python -m site`` or ``python3 -m site`` to find out where is more likely
    Atlas will be installed.

Option 4: Clone the Github repository
-------------------------------------

1. **Clone with git**

   The source code is uploaded and maintained through Github at
   `<https://github.com/networkbiolab/atlas>`_. Therefore, you could clone the
   repository locally, and then add the folder to the ``PYTHONPATH``. Beware
   that you should install the *pysb* package (`pysb`_) and others packages
   by any means, specially the Jupyter Notebook project (`<https://jupyter.org>`_).

   .. code-block:: bash

    path=/opt/atlas
    git clone https://github.com/networkbiolab/atlas $path
    echo export PYTHONPATH="\$PYTHONPATH:\$path" >> $HOME/.profile

   .. note::
    Adding the path to ``$HOME/.profile`` allows python to find the package
    installation folder after each user login. Similarly, adding the path to
    ``$HOME/.bashrc`` allows python to find the package after each terminal
    invocation. Other options include setting the ``PYTHONPATH`` environmental
    variable in a sh file (see the example folder) or invoke ``python3 setup.py clean build install``
    to install Atlas as it was downloaded from the PyPI server.

.. refs
.. _KaSim: https://github.com/Kappa-Dev/KaSim
.. _NFsim: https://github.com/RuleWorld/nfsim
.. _BioNetGen2: https://github.com/RuleWorld/bionetgen
.. _PISKaS: https://github.com/DLab/PISKaS
.. _BioNetFit: https://github.com/RuleWorld/BioNetFit
.. _SLURM: https://slurm.schedmd.com/
.. _pysb: http://pysb.org/

.. _Kappa: https://www.kappalanguage.org/
.. _BioNetGen: http://www.csb.pitt.edu/Faculty/Faeder/?page_id=409
.. _pandas: https://pandas.pydata.org/
