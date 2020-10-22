import seaborn
import matplotlib.pyplot as plt

palette = seaborn.color_palette('colorblind')

for kind in ['scatter', 'plot']:
    # first plot, periplasmic concentration
    fig, ax = plt.subplots(1, 2, figsize = (4*2, 3*1), dpi = 100)

    simulation.plot.metabolite(data3['avrg'], 'Alpha_lactose', 'per', ax = ax[0], **{'kind' : kind},
        plt_kws = {'s' : 2, 'color' : palette[0], 'label' : r'$\alpha$-lactose [PER]', 'alpha' : .5})

    simulation.plot.metabolite(data3['avrg'], 'Alpha_lactose', 'cyt', ax = ax[1], **{'kind' : kind},
        plt_kws = {'s' : 2, 'color' : palette[1], 'label' : r'$\alpha$-lactose [CYT]', 'alpha' : .5})

    simulation.plot.metabolite(data3['avrg'], 'ALLOLACTOSE', 'cyt', ax = ax[1], **{'kind' : kind},
        plt_kws = {'s' : 2, 'color' : palette[2], 'label' : r'allolactose [CYT]', 'alpha' : .5})

    ax[0].set_xlim((0,.25))
    ax[1].set_xlim((0,2.5))
    ax[0].set_ylim((0,100))
    ax[1].set_ylim((0,100))

    seaborn.despine()
