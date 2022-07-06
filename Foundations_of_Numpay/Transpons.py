import numpy as np

first_2d_arr = np.arange(12).reshape(3,4)
print(first_2d_arr)

print(" ")
print(".transpose")
print(np.transpose(first_2d_arr))

second_2d_arr = np.arange(6).reshape(3,2)
print(second_2d_arr)

print(np.transpose(second_2d_arr,(1,0)))

first_3d_arr = np.arange(24).reshape(2,3,4)
print(first_3d_arr)

print(np.swapaxes(first_3d_arr, 0,2))