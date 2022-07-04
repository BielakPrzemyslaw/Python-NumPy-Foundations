import numpy as np

first_list = [1,2,3,4,5,6,7,8,9,10]
print(first_list)

first_array = np.array(first_list)
print(first_array)

second_list = [1,2,3,-1,33,60, 2456.13,34.1]
print(second_list)

second_array = np.array(second_list)
print(second_array)
print(second_array.dtype)

third_list = ['Ann', 11111, 'Peter', 111112, 'Tom', 111113]
third_array = np.array(third_list)
print(third_array)

first_tuple = (5,10,15,20,25,30)
array_from_tuple = np.array(first_tuple)
print(array_from_tuple)
print(array_from_tuple.dtype)

multi_dim_list = [[[0,1,2], [3,4,5], [6,7,8], [9,10,11]]]
array_from_multi_dim_list = np.array(multi_dim_list)
print(array_from_multi_dim_list)
