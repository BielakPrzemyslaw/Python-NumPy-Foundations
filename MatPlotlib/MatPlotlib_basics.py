
#import numpy as np
import matplotlib.pyplot as plt

average_mounthly_temperatures = [28.3, 32.1, 32.2, 31.1, 31.4, 30.4, 30.8, 30.2, 28.3, 28.2, 26.2, 26.1]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
fig = plt.figure()
plt.plot(months,average_mounthly_temperatures)
plt.title("Average monthly temperatures")
plt.xlabel("months")
plt.ylabel("temperatures")
plt.show()

fig.savefig('average_monthly_temperatures.png')
fig.savefig('average_monthly_temperatures.pdf')

