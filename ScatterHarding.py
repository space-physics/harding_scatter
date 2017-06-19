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


if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser()
    p = p.parse_args()

    xv = np.arange(-500e3, 500e3,5e3)
    yv = np.arange(-500e3, 500e3,5e3)

    x,y = np.meshgrid(xv,yv)

    I = dhf(x,y)

    zenang = 30
    az = 45
    h = 150e3

    optdepth = 0.
    P = 4 * np.pi

    g_sc = scatter_along_los(I, optdepth, P, h, zenang, az)[0]