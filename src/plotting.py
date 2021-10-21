import matplotlib.pyplot as plt
import numpy as np

from src.options import Colors


def custom_plot(x, y,
                color=Colors.wisteria,
                title=r'Title',
                xlabel=r'xaxis label',
                ylabel=r'yaxis label',
                use_latex=True, 
                save_fig=False,
                fig_size=(12, 5),
                
    
    ):
    
    plt.close('all')

    # Enable latex text edit
    if use_latex:
        plt.rc('text', usetex=True)
        plt.rc('font', family='serif')
    fontSize = 15 

    # Plot
    fig = plt.figure()

    # Plot size
    h, w = fig_size
    fig.set_size_inches(h, w)
    ax = fig.add_subplot(1, 1, 1)

    # Labels and Title
    ax.set_title(title, fontsize=fontSize)
    ax.set_xlabel(xlabel, fontsize=fontSize)
    ax.set_ylabel(ylabel, fontsize=fontSize)

    # Limits to plot, uncomment to use
    # ax.set_xlim(,)
    # ax.set_ylim(,)

    # Tick size
    ax.xaxis.set_tick_params(labelsize=fontSize)
    ax.yaxis.set_tick_params(labelsize=fontSize)  

    # Thicknes and axis colors
    for axis in ['top','bottom','left','right']:
        ax.spines[axis].set_linewidth(1.0)
    ax.tick_params(direction='out', length=6, width=1, colors='k')

    # Plotting 
    x = np.array([1, 2, 3, 4])
    y = x**2
    
    ax.plot(x, y, color=color, linewidth=2.5,
            label=r'Label')

    # Text over plots
    ax.legend(shadow=False, loc=(0.71, 0.12), handlelength=1.5,
            fontsize=fontSize, framealpha=0.9)

    # Save figure as PDF
    if save_fig:
        fig.tight_layout()  # remove empty layout spaces
        fig.savefig('./plot_name.pdf')

    plt.show()
