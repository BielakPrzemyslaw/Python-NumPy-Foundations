import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
x = np.arange(3)
y = 2 * x
plt.subplot(2,2,1)
plt.plot(x, y, 'b')

plt.subplot(2,2,2)
plt.plot(x, 1 - y, 'r')

plt.subplot(2,2,3)
plt.plot(x, 2 - y, 'g')

plt.subplot(2,2,4)
plt.plot(x, y, 'y')

plt.show()

fig, axs = plt.subplots(2,2, figsize = (6,6))
axs[0,0].plot(x, y, 'b')
axs[0,1].plot(x, 1-y, 'r')
axs[1,0].plot(x, 2-y, 'g')
axs[1,1].plot(x, y, 'y')
plt.show()