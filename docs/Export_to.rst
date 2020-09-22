Export to
=========

The PySB python package could export to different languages
(See more `here <https://pysb.readthedocs.io/en/stable/modules/export/>`_).
Use the following code to export to the supported formats:

.. literalinclude:: ./export.py
   :language: python
   :encoding: latin-1
   :linenos:
..    :emphasize-lines: 7,8

.. note::
    In the case of matlab, mathematica, potterswheel, python, and stochkit, PySB requires to expand
    the rules to determine all mass-balances to write ODE-based models, a proccess
    call network generation and could take excessive time to finish.
