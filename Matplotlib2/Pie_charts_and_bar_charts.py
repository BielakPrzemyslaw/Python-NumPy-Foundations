import numpy as np
import matplotlib.pyplot as plt

preffered_workoption = [10.7, 47.6, 38.6, 2.9]

colors = ['b', 'g', 'r', 'c']

labels = ['Collocated', 'Hybrid', 'Fully remote', 'Not applicable']

explode = (0, 0.2, 0, 0)

plt.pie(preffered_workoption, colors=colors, labels=labels, explode=explode, autopct='%1.1f%%', counterclock=False, shadow=True)

plt.title('Prefered workoption')

plt.show()

preffered_workoption = [10.7, 47.6, 38.6, 2.9]

colors = ['b', 'g', 'r', 'c']

labels = ['Collocated', 'Hybrid', 'Fully remote', 'Not applicable']

widths = [0.7, 0.7, 0.7, 0.7]

plt.bar(range(0, 4), preffered_workoption, width=widths, color=colors, align='center')

plt.title('Preffered workoption')

plt.show()