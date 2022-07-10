import numpy as np
import matplotlib.pyplot as plt

first_figure = plt.figure()
x = np.linspace(1,10)
y = np.linspace(1,10)
ax = first_figure.add_axes([0,0,1,1])
ax.plot(x,y, color='red')
plt.show()

second_figure = plt.figure()
x = np.linspace(1,10)
y = np.linspace(1,10)
ax = second_figure.add_axes([0,0,1,1])
ax.plot(x,y, color='g')
plt.show()

third_figure = plt.figure()
ax = third_figure.add_axes([0,0,1,1])
ax.plot(x,y, color='#FF00FF')
plt.show()

plt.plot(x, 2*x, linestyle = 'solid')
plt.plot(x, 3*x, linestyle = "dashed")
plt.plot(x, 4*x, linestyle = 'dashdot')
plt.plot(x, 5*x, linestyle = 'dotted')
plt.show()

