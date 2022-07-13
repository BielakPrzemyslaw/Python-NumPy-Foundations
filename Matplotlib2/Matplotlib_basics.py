import matplotlib.pyplot as plt
import numpy as np
import smtplib

average_monthly_temperatures = [31.3, 29.4, 28.5, 27.5, 28.9, 30.2, 25.3, 27.8, 32.3]
fig=plt.figure()
plt.plot(average_monthly_temperatures)
plt.title("Average monthly temperatures")
plt.xlabel("month")
plt.ylabel("temperature")
plt.show()
