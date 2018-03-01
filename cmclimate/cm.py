from __future__ import absolute_import

import numpy as np
import json
import pkg_resources
from matplotlib.colors import ListedColormap

# Open NCL colormaps from a JSON file
filename = pkg_resources.resource_filename(__name__,
                                           'data/ncl_colormaps.json')
with open(filename) as file:
    ncl_colortables = json.load(file)

# Dictionary to store colormaps
cmaps = dict()

# Add colormaps and reversed to dictionary
for cmapname in ncl_colortables:
    data = np.array(ncl_colortables[cmapname])
    data /= data.max()
    cmaps[cmapname] = ListedColormap(data, cmapname)
    # Reversed colormap
    cmapname_r = cmapname + '_r'
    data_r = data[::-1, :]
    cmaps[cmapname_r] = ListedColormap(data_r, cmapname_r)

# Make colormaps available to call
locals().update(cmaps)