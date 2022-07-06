import numpy as np

a = np.arange(1,11)
b = np.arange(21,31)
print("a",a)
print("b",b)

print(a + b)
print(b - a)
print(a * b)
print(b / a)

c = np.arange(2,12)
print("c",c)

print(a ** c )

d = np.array([[[1,34,45],[23,12,14],[2,5,6]]])
print(d)

print(a * 2)

print(" ")
print(".add")
print(np.add(a,b))

print(" ")
print(".subtract")
print(np.subtract(b,a))

print(" ")
print(".multiply")
print(np.multiply(a,b))

print(" ")
print(".divide")
print(np.divide(b,a))

print(" ")
print(".mod")
print(np.mod(b,a))

print(" ")
print(".power")
print(np.power(a,c))

print(" ")
print(".sqrt")
print(np.sqrt(a))
