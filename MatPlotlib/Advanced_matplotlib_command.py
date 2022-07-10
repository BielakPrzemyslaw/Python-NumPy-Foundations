import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1,  10, 1024)
plt.xscale('log')
plt.yscale('log')

plt.plot(x, x, label = '$f(x)=x$')
plt.plot(x, 10**x, label = '$f(x)=10^x$')
plt.plot(x, np.log(x), label = '$f(x)=log(x)$')

plt.legend()
plt.show()

from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

x = np.arange(0.0, 50.0, 0.1)
y = x**2

fig, ax = plt.subplots()
ax.plot(x,y)

ax.xaxis.set_major_locator(MultipleLocator(10))
ax.xaxis.set_major_formatter('{x: 0f}')

ax.xaxis.set_major_locator(MultipleLocator(2))
plt.show()

x = np.arange(0.0, 50.0, 0.1)
y = x**2
fig, ax = plt.subplot()
ax.plot(x,y)

ax.set_xlim([0, 50])
ax.set_ylim([0, 2500])

plt.show()

x = np.arange(0.0, 50.0, 0.1)
y = x**2

fig, ax = plt.subplots()
ax.plot(x,y)

ax.set_xtricks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
ax.set_ytricks([0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000, 2250, 2500])

plt.show()
