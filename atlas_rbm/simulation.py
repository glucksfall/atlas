# -*- coding: utf-8 -*-

'''
Project "Reconstruction of RBM from biological networks", Rodrigo Santibáñez, 2019-2020 @ NBL, UMayor
Citation:
DOI:
'''

__author__  = 'Rodrigo Santibáñez'
__license__ = 'gpl-3.0'

from pysb import *
from pysb.bng import generate_network, generate_equations
from pysb.pathfinder import set_path
from pysb.simulator import ScipyOdeSimulator, BngSimulator
from pylab import linspace

import pandas
import seaborn
import matplotlib.pyplot as plt

def set_initial(model, name, loc, new_value):
	for i in model.parameters._elements:
		if 't0_' + name + '_' + loc in i.name:
			i.value = new_value

	return model

def ode(model, start = 0, finish = 10, points = 10, path = '/opt/'):
	set_path('bng', path)
	generate_network(model)
	generate_equations(model)

	return BngSimulator(model, linspace(start, finish, points+1)).run(method = 'ode').dataframe

def ssa(model, start = 0, finish = 10, points = 10, n_runs = 20, path = '/opt/'):
	set_path('bng', path)
	generate_network(model)
	generate_equations(model)

	return BngSimulator(model, linspace(start, finish, points)).run(method = 'ssa', n_runs = n_runs).dataframe

def plot(data, observable, loc, *args, **kwargs):
	label = kwargs.get('label', None)
	plt.plot(data.index, data['obs_' + observable + '_' + loc], label = label)
