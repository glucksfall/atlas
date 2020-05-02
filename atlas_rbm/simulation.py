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
from pysb.simulator import ScipyOdeSimulator, BngSimulator, KappaSimulator
from pysb.util import alias_model_components
from pylab import linspace

import pandas
import seaborn
import matplotlib.pyplot as plt

def set_parameter(model, name, new_value):
	for i in model.parameters._elements:
		if name == i.name:
			i.value = new_value
	return model

class set_initial:
	def monomers(model, name, loc = 'cyt', new_value = 0):
		for i in model.parameters._elements:
			if 't0_' + name + '_' + loc.lower() == i.name:
				i.value = new_value
		return model

	def met(model, name, loc = 'cyt', new_value = 0):
		return set_initial.monomers(model, name, loc, new_value)

	def cplx(model, name, loc = 'cyt', new_value = 0):
		return set_initial.monomers(model, name, loc, new_value)

	def prot(model, name, loc = 'cyt', new_value = 0):
		return set_initial.monomers(model, name, loc, new_value)

	def pattern(model, name, alias = '', new_value = 0):
		model = alias_model_components(model)
		exec('Initial(' + name + ', Parameter(\'t0_' + alias + '\', ' + str(new_value) + '))')
		return model

def ode(model, start = 0, finish = 10, points = 10, path = '/opt/'):
	set_path('bng', path)
	generate_network(model)
	generate_equations(model)

	return BngSimulator(model, linspace(start, finish, points+1)).run(method = 'ode').dataframe

def modes(sims, n_runs):
	data = []
	for i in range(n_runs):
		data.append(sims.xs(i))

	avrg = 0
	for i in range(n_runs):
		avrg += data[i]
	avrg = avrg / n_runs

	stdv = 0
	for i in range(n_runs):
		stdv = (data[i] - avrg)**2
	stdv = (stdv / (n_runs-1))**0.5

	return {'sims' : data, 'avrg' : avrg, 'stdv' : stdv}

def ssa(model, start = 0, finish = 10, points = 10, n_runs = 20, path = '/opt/'):
	set_path('bng', path)
	generate_network(model)
	generate_equations(model)

	sims = BngSimulator(model, linspace(start, finish, points+1)).run(method = 'ssa', n_runs = n_runs).dataframe
	sims = modes(sims, n_runs)
	return {'sims' : sims['sims'], 'avrg' : sims['avrg'], 'stdv' : sims['stdv']}

def kasim(model, start = 0, finish = 10, points = 10, n_runs = 20, path = '/opt/'):
	set_path('kasim', path)
	sims = KappaSimulator(model, linspace(start, finish, points+1)).run(n_runs = n_runs).dataframe
	sims = modes(sims, n_runs)
	return {'sims' : sims['sims'], 'avrg' : sims['avrg'], 'stdv' : sims['stdv']}

def plot(data, observable, loc = 'cyt', *args, **kwargs):
	label = kwargs.get('label', None)
	plt.plot(data.index, data['obs_' + observable + '_' + loc.lower()], label = label)
