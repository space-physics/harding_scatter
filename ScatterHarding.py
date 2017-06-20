#!/usr/bin/env python
import numpy as np
from matplotlib.pyplot import figure,show
#
from harding_scatter import scatter_along_los

def dhf(x:np.ndarray, y:np.ndarray):
    """
    x,y: meshgrid arrays of locations
    f: array of brightness at each (x,y)

    dhf(x,y) is a function takes a location in meters and returns the brightness
      that an observer at (x,y,ground) would see looking straight up.
    The instrument is at (x=0, y=0).
    The assumption is a thin shell of emission at altitude h.
    """
    f = np.ones(x.shape) # background glow
    f[y > 300e3] = 2. # twice as bright, a bright region in the North.

    return f

def P_rayleigh(u0,u1,phi0,phi1):
    '''
    Scattering phase function, defined so it integrates to 4*pi over the sphere.
    '''
    u = u0*u1 + np.sqrt((1-u0**2)*(1-u1**2)) * np.cos(phi0-phi1) # cos (scattering angle)
    return 0.75 * (1 + u**2)


if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser()
    p = p.parse_args()

    zenang = np.arange(60., 5.)
    az = np.arange(360., 10.)
    h = 150e3

    optdepth = 0.05 # per B. Harding for minimal aerosol

    g_sc,g_dir,s_sc,s_dir = scatter_along_los(dhf, optdepth, P_rayleigh, h, zenang, az)