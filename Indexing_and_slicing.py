import numpy as np

twodim_arr = np.reshape(np.arange(12),(3,4))
print(twodim_arr)

print(twodim_arr[1,1])

print(twodim_arr[1])


threedim_arr = np.reshape(np.arange(4*4*5),(4,4,5))
print(threedim_arr)

print(threedim_arr[0,2,3])

print(threedim_arr[2,-2, -2])

onedim_arr = np.arange(10)
print(onedim_arr)

print(onedim_arr[2:6])

print(onedim_arr[::3])

print(twodim_arr)

print(twodim_arr[1, :])

print(twodim_arr[:, 2])