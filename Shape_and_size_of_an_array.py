import numpy as np

print("")
print(".arange examples:")
first_arr = np.arange(20)
print(first_arr)

print("")
print(".linspace examples:")
second_arr = np.linspace((1,2),(10,20),10)
print(second_arr)

print(" ")
third_arr = np.full((2,3,3),13)
print(third_arr)

np.shape(first_arr)
print(first_arr.shape)

np.shape(second_arr)
print(second_arr.shape)

np.size(first_arr)
print(first_arr.size)

