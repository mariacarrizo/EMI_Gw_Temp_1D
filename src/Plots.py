import numpy as np
import matplotlib.pyplot as plt
from utils import rel_diff

def PlotModelData(model, depths, data, ax=None, model_name='', model_style='k', data_style='.', data_name=''):
    if ax is None:
        fig, ax = plt.subplots(1,2)
    fs=7
    ax[0].step(model, depths, model_style, label=model_name)
    ax[0].set_xscale('log')
    ax[0].set_xlabel('Electrical conductivity [mS/m]')
    ax[0].set_ylabel('Depth [m]')
    ax[0].legend(fontsize=fs)
    ax[0].set_title('1D model')

    ax[1].plot(data[:9]*1000, '.',c=data_style, label='Q '+data_name)
    ax[1].set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8])
    ax[1].set_xticklabels(['H2', 'H4', 'H8', 'V2', 'V4', 'V8', 'P2', 'P4', 'P8'])
    ax[1].plot(data[9:]*1000, 'x', c=data_style, label = 'IP '+data_name)
    ax[1].set_xlabel('Coil geometry')
    ax[1].legend(fontsize=fs, bbox_to_anchor=(1.05, 1.05))
    ax[1].set_title('EMI measurements')
    ax[1].set_ylabel('[ppt]')

    plt.tight_layout()
    
