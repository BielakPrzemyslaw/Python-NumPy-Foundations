import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10)

y1 = x
y2 = 8-x

fig, ax = plt.subplots()
plt.plot(x, y1, label = 'supply')
plt.plot(x, y2, label = 'demnad')

ax.annotate("Equilibrium", xy=(4,4), xytext=(3,2), \
            fontsize=12, fontweight='semibold', \
            arrowprops=dict(linewidth=2, arrowstyle= "->"))

plt.xlabel('quantity', fontsize=12)
plt.ylabel('price', fontsize=12)

plt.legend()
plt.show()

x = np.linspace(0, 10)

y1 = x
y2 = 8-x

fig, ax = plt.subplots()
plt.plot(x, y1, label='supply')
plt.plot(x, y2, label='demnad')

bbox_props = dict(boxstyle='rarrow', fc=(0.8, 0.9, 0.9), lw=2)
t = ax.text(2,4, 'equailibrium', ha="center", va="center", rotation=0,
            size=10, bbox=bbox_props)

plt.xlabel('quantity', fontsize=12)
plt.ylabel('price', fontsize=12)

plt.legend()
plt.show()

from matplotlib.patches import Circle, Polygon
from matplotlib.collections import PathCollection

fig, ax = plt.subplot()
patches = []

circle = Circle((.42, .75),0.12)
triangle = Polygon([[.1, .5],[.2,.7],[.3,.54]], True)

patches += [circle, triangle]

colors = 100*np.random.rand(len(patches))
p = PathCollection(patches)
p.set_array(np.array(colors))
ax.add_collection(p)

plt.show()
