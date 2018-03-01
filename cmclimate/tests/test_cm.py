from __future__ import absolute_import, division, print_function
from .. import cm
import matplotlib.pyplot as plt
import numpy as np

def test_cmap_import():
    for name, cmap in vars(cm).items():
        print(name)
        x = np.linspace(0, 10)
        x2d, _ = np.meshgrid(x, x)
        plt.figure()
        plt.pcolor(x2d, cmap=cmap)
        plt.title(name)