import numpy as np

arr_ldim = [10,2,4,7,12,3,7,5]
print(arr_ldim)

print(arr_ldim[::-1])

print(np.flip(arr_ldim))

arr_2dim = np.arange(9).reshape(3,3)
print(arr_2dim)

print(np.flip(arr_2dim))