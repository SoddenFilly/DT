'''
from matplotlib import pyplot as plt
import time

ages_x = [25,26,27,28,29,30,31,32,33,34,35]

dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
plt.plot(ages_x, dev_y, color='k', linestyle='--', label='All devs')

py_dev_y = [45000, 48000, 53000, 57000, 63000, 65000, 71000, 70000, 75000, 83000, 90033]
plt.plot(ages_x, py_dev_y, 'b', label='Python')

plt.xlabel('Age')
plt.ylabel('median salery (USD)')
plt.title('median salery (USD) by age')

plt.legend()

plt.show()

time.sleep(3)

plt.close('none')
print("d")
''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
 
x = np.linspace(0, 2*np.pi, 1000)
y = np.sin(2*x)
plt.scatter(x,y, c=cm.hot(np.abs(y)), edgecolor='none')
plt.show()
'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm

x = np.linspace(0, 3 * np.pi, 500)
y = np.sin(x)
dydx = np.cos(0.5 * (x[:-1] + x[1:]))  # first derivative

# Create a set of line segments so that we can color them individually
# This creates the points as a N x 1 x 2 array so that we can stack points
# together easily to get the segments. The segments array for line collection
# needs to be (numlines) x (points per line) x 2 (for x and y)
points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)

# Create a continuous norm to map from data points to colors
norm = plt.Normalize(dydx.min(), dydx.max())
lc = LineCollection(segments, cmap='viridis', norm=norm)
# Set the values used for colormapping
lc.set_array(dydx)
lc.set_linewidth(2)
line = axs[0].add_collection(lc)
fig.colorbar(line, ax=axs[0])

# Use a boundary norm instead
cmap = ListedColormap(['r', 'g', 'b'])
norm = BoundaryNorm([-1, -0.5, 0.5, 1], cmap.N)
lc = LineCollection(segments, cmap=cmap, norm=norm)
lc.set_array(dydx)
lc.set_linewidth(2)
line = axs[1].add_collection(lc)
fig.colorbar(line, ax=axs[1])

axs[0].set_xlim(x.min(), x.max())
axs[0].set_ylim(-1.1, 1.1)
plt.show()
