# simulation
bng = '/opt/git-repositories/bionetgen.RuleWorld/bng2/'
kasim = '/opt/git-repositories/KaSim4.Kappa-Dev/'
cupsoda = '/opt/git-repositories/cupSODA.aresio/'
stochkit = '/opt/git-repositories/StochKit.StochSS' # not the bin folder

data0 = simulation.scipy(model, start = 0, finish = 10, points = 2000)
data1 = simulation.cupsoda(model, start = 0, finish = 10, points = 2000, path = cupsoda) # only if you have a GPU NVIDIA; comment if not.
data2 = simulation.bngODE(model, start = 0, finish = 10, points = 2000, path = bng)
data3 = simulation.bngSSA(model, start = 0, finish = 10, points = 2000, n_runs = 20, path = bng)
data4 = simulation.bngPLA(model, start = 0, finish = 10, points = 2000, n_runs = 20, path = bng)
data5 = simulation.bngNF(model, start = 0, finish = 10, points = 2000, n_runs = 20, path = bng)
data6 = simulation.kasim(model, start = 0, finish = 10, points = 2000, n_runs = 20, path = kasim)
data7 = simulation.stochkit(model, start = 0, finish = 10, points = 2000, n_runs = 20, path = stochkit)
