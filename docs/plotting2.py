import seaborn
import matplotlib.pyplot as plt

palette = seaborn.color_palette('colorblind')

# first plot, periplasmic concentration
fig, ax = plt.subplots(1, 2, figsize = (4*2, 3*1), dpi = 100)
simulation.plot.metabolite(data3, 'Alpha_lactose', 'per', ax = ax[0], **{'kind' : 'fill_between', 'weight' : .5},
   plt_kws = {'s' : 2, 'color' : palette[0], 'label' : r'$\alpha$-lactose [PER]', 'alpha' : .5})

# second plot, cytoplasmic concentration
simulation.plot.metabolite(data3, 'Alpha_lactose', 'cyt', ax = ax[1], **{'kind' : 'fill_between', 'weight' : .5},
   plt_kws = {'s' : 2, 'color' : palette[1], 'label' : r'$\alpha$-lactose [CYT]', 'alpha' : .5})

# second plot, cytoplasmic concentration
simulation.plot.metabolite(data3, 'ALLOLACTOSE', 'cyt', ax = ax[1], **{'kind' : 'fill_between', 'weight' : .5},
   plt_kws = {'s' : 2, 'color' : palette[2], 'label' : r'allolactose [CYT]', 'alpha' : .5})

# first plot, periplasmic concentration
simulation.plot.metabolite(data0, 'Alpha_lactose', 'per', ax = ax[0], **{'kind' : 'plot'},
   plt_kws = {'s' : 2, 'color' : palette[0], 'label' : r'ODE'})

# second plot, cytoplasmic concentration
simulation.plot.metabolite(data0, 'Alpha_lactose', 'cyt', ax = ax[1], **{'kind' : 'plot'},
   plt_kws = {'s' : 2, 'color' : palette[1], 'label' : r'ODE'})

# second plot, cytoplasmic concentration
simulation.plot.metabolite(data0, 'ALLOLACTOSE', 'cyt', ax = ax[1], **{'kind' : 'plot'},
   plt_kws = {'s' : 2, 'color' : palette[2], 'label' : r'ODE'})

ax[0].set_xlim((0,.25))
ax[1].set_xlim((0,2.5))
ax[0].set_ylim((0,100))
ax[1].set_ylim((0,100))

seaborn.despine()
