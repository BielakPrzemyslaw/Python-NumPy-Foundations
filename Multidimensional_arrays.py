import numpy as np

nums = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(nums)
print(nums[0,2])
#ndim = number arrays
print(nums.ndim)

multi_arr = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
print(multi_arr)
print(multi_arr.ndim)
print(multi_arr[0,3,1])
