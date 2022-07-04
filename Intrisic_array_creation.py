import numpy as np
print("")
print(".arange examples:")
integers_array = np.arange(10)
print(integers_array)

integers_second_array = np.arange(100, 130)
print(integers_second_array)

integers_third_array = np.arange(20, 60, 5)
print(integers_third_array)

print("")
print(".linspace examples:")
first_floats_array = np.linspace(10,20)
print(first_floats_array)

second_floats_array = np.linspace(10,20,4)
print(second_floats_array)

print("")
print(".random.rand examples:")
first_rand_arr = np.random.rand(10)
print(first_rand_arr)

second_rand_arr = np.random.rand(4,4)
print(second_rand_arr)

print("")
print(".random.randint examples:")
third_rand_arr = np.random.randint(0, 100, 20)
print(third_rand_arr)