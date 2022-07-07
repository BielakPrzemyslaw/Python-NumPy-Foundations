import numpy as np
import matplotlib.pyplot as plt

x = np.linspace[1,10]
first_line = plt.plot(x, x+1, label= 'y=x+1')
plt.legend()

second_line = plt.plot(x, x+2, linestyle= 'solid')
second_line.set_label('y=x+2')
third_line = plt.plot(x, x+3, linestyle= 'dashed')
third_line.set_label('y=x+3')
plt.legend()