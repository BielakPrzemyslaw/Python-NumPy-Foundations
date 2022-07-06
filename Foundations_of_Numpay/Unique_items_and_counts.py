import numpy as np


first_arr = np.array([1,2,3,4,5,1,4,5,6,8,10])
print(first_arr)

print(".unique")
print(np.unique(first_arr))

print("second_arr")
second_arr = np.array([[1,2,3,1],[1,2,3,1],[1,4,2,1],[1,8,12,11]])
print(second_arr)
print(np.unique(second_arr))

print(" ")
print(np.unique(second_arr, axis = 0))

print(" ")
print(".unique .return_index=True")
print(np.unique(first_arr, return_index= True))