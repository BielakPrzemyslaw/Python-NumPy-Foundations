from timeit import timeit

import numpy as np

numbers = np.arange(10, dtype = np.int8)
print(numbers)

print(numbers.strides)

numbers.shape = 2,5
print(numbers)

print(numbers.strides)

first_array = np.zeros((100000,))
print(first_array)

second_array = np.zeros((100000 * 100,))[::100]
print(second_array)

print(first_array.shape)

print(second_array.shape)

print(first_array.strides)

print(second_array.strides)

