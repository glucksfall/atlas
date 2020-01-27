Simulation
==========

.. code-block:: python3

	from pysb.bng import generate_network, generate_equations
	from pysb.simulator import ScipyOdeSimulator, BngSimulator, KappaSimulator

	from pysb.pathfinder import set_path
	set_path('bng', '/opt/git-repositories/bionetgen.RuleWorld/bng2/')
	set_path('kasim', '/opt/git-repositories/KaSim4.Kappa-Dev/')

	import seaborn
	import matplotlib.pyplot as plt

	palette = seaborn.color_palette('colorblind')

	# generate_network(model)
	# generate_equations(model)

	runs = 100
	# data1 = ScipyOdeSimulator(model, linspace(0, 100, 200)).run().dataframe
	# data1 = BngSimulator(model, linspace(0, 200, 201)).run(method = 'ode').dataframe
	# data2 = BngSimulator(model, linspace(0, 200, 201)).run(method = 'ssa', n_runs = runs).dataframe
	data2 = KappaSimulator(model, linspace(0, 100, 101)).run(n_runs = runs).dataframe

	data = []
	for i in range(0,runs):
		data.append(data2.xs(i))

	avrg = 0
	for i in range(0,runs):
		avrg += data[i]
	avrg = avrg / runs

	stdv = []
	for i in range(0,runs):
		stdv = (data[i] - avrg)**2
	stdv = (stdv / (runs-1))**0.5

	data2 = data[0]
