import numpy as np

print("")
print(".zeros examples:")
first_z_array = np.zeros(5)
print(first_z_array)
print("")
second_z_array = np.zeros((4,5))
print(second_z_array)

print("")
print(".ones examples:")
first_one_array = np.ones(6)
print(first_one_array)
print("")
second_ones_array = np.ones((7,8))
print(second_ones_array)
third_ones_array = np.ones((4,5),dtype=int)
print(third_ones_array)

print("")
print(".empty examples:")
first_fill_array = np.empty(10,dtype=int)
first_fill_array.fill(12)
print(first_fill_array)

first_full_array = np.full(3,10)
print(first_full_array)

second_full_array = np.full((4,5),8)
print(second_full_array)