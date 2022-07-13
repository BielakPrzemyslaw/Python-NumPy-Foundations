import numpy as np

first_array = np.arange(16).reshape(4,4)
print(first_array)

first_matrix = np.matrix(first_array)
print(first_matrix)

second_matrix = np.matrix(np.identity(4))
print(second_matrix)

print(" ")
print('Matrix a')
matrix_a = np.random.randint(5, size=(2,3))
print(matrix_a)

print(" ")
print('Matrix b')
matrix_b = np.random.randint(5, size=(3,2))
print(matrix_b)

print(" ")
print(".matmul")
print(np.matmul(matrix_a, matrix_b))

print(" ")
matrix_c = np.matrix("0 1 2; 1 0 3; 4 -3 8")
print(matrix_c)

print(".linalg ")
inverse = np.linalg.inv(matrix_c)
print(inverse)

print(" ")
print(matrix_c * inverse)


