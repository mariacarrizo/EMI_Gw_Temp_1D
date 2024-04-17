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
    
def PlotModel(model, depths, ax=None, model_name=None, model_style='k'):
    if ax is None:
        fig, ax = plt.subplots()
    fs=7
    ax.step(model, depths, model_style, label=model_name)
    ax.set_xscale('log')
    ax.set_xlabel('Electrical conductivity [mS/m]')
    ax.set_ylabel('Depth [m]')
    if model_name is not None:
        ax.legend(fontsize=fs)
    plt.tight_layout()
    
def PlotErrorSpace_2Lay(model, model_est, err, models_err, depthmax=10):
      
    fig, ax = plt.subplots()
    
    x = (models_err[:,0])*1000 # conductivities of first layer in mS/m
    y = models_err[:,2]          # thickness of first layer
    z = err
    
    ngridx = 100
    ngridy = 200
    
    # Create grid values first.
    xi = np.linspace(np.min(x), np.max(x), ngridx)
    yi = np.linspace(np.min(y), np.max(y), ngridy)
    
    # Linearly interpolate the data (x, y) on a grid defined by (xi, yi).
    triang = tri.Triangulation(x, y)
    interpolator = tri.LinearTriInterpolator(triang, z)
    Xi, Yi = np.meshgrid(xi, yi)
    zi = interpolator(Xi, Yi)
    
    ax.contour(xi, yi, zi*100, levels=20, linewidths=0.5, colors='k')
    cntr1 = ax.contourf(xi, yi, zi*100, levels=20, cmap="RdBu_r")
    ax.plot(x, y, '.k', ms=1)
    ax.set(xlim=(7,10), ylim=(3.4,4.3))
    ax.scatter(((model_est[0])*1000), model_est[2],
                 marker ='^', c='y', label='Estimated model')
    ax.set_xlabel('$\sigma_1$ [mS/m]', fontsize=8)
    ax.set_ylabel('$h_1$ [m]', fontsize=8)
    ax.legend()
    ax.tick_params(axis='both',labelsize=9)
    #ax[0].tick_params(axis='both',labelsize=9)
    clb = fig.colorbar(cntr1, ax=ax)
    clb.ax.set_title('RMS Error %')
    clb.ax.tick_params(labelsize=9)
    
