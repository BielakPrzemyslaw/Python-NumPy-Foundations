import numpy as np
import matplotlib.pyplot as plt

x = np.arange(3)
plt.plot(x,x)
plt.plot(x,2*x)
plt.plot(x,3*x)
plt.grid(True)
plt.show()

x = np.linspace(0,5,5)
y = 2 * x
plt.plot(x,y)
plt.show()

fig = plt.figure()
axes = fig.add.axes([0.1, 0.1, 0.8, 0.8])
axes.plt(x,y)
plt.show()