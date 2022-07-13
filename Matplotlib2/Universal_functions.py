from __future__ import print_function
import numpy as np

numbers = np.arange(1,11)
print(numbers)

np.sin(numbers)
print(numbers)

np.log(numbers)
print(numbers)

integers = np.arange(1,101)
print("integers" , *integers)

def modulo(val):
    return (val % 10)
mod_10 = np.frompyfunc(modulo, 1, 1)

mod_integers = mod_10(integers)
print("mod_integers" , *mod_integers)