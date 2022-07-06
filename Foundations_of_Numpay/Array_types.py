import numpy as np

#Array types and conversions between types
integers = np.array([10,20,30,40,50])
print(integers)

print(integers[0])

integers[0] = 15
print(f"New array", integers)

integers[0] = 15.5
print(integers)
print(integers.dtype)

smallerIntegers = np.array(integers, dtype = np.int8)
print(smallerIntegers)

print(integers.nbytes)

print(smallerIntegers.nbytes)

overflow = np.array([127,128,129], dtype = np.int8)
print(overflow)

floats = np.array([1.2,2.3,3.5,4.2,5.4,9.4])
print(floats)
print(floats.dtype)