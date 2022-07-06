import numpy as np

first_arr = np.arange(10,110,10)
print(first_arr)

second_arr = np.arange(10,100,10).reshape(3,3)
print(second_arr)

third_arr = np.arange(10,110,10).reshape(2,5)
print(third_arr)

print(" ")
print(".sum")
print(first_arr.sum())
print(second_arr.sum())
print(third_arr.sum())

print("axis = 0 columns, 1 rows")
print(second_arr.sum(axis = 1))

print(second_arr.prod())

print(third_arr.prod(axis = 0))

print(" ")
print(".average")
print(np.average(first_arr))

print(np.min(first_arr))

print(np.max(second_arr))

print(np.mean(first_arr))

print(np.std(first_arr))