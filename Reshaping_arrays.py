import numpy as np

first_arr = np.arange(1,13)
print(first_arr)

second_arr = np.reshape(first_arr,(3,4))
print(second_arr)

third_arr = np.reshape(first_arr,(6,2))
print(third_arr)

sixth_arr = np.array([[1,2],[3,4],[5,6]])
print(sixth_arr)

seventh_arr_flat = np.reshape(sixth_arr,-1)
print(seventh_arr_flat)

print("")
eighth_arr_flat = sixth_arr.flatten()
print("eighth_arr: ", eighth_arr_flat)
ninth_arr_rav = sixth_arr.ravel()
print("ninth_arr : ", ninth_arr_rav)

eighth_arr_flat[0] = 200
ninth_arr_rav[0] = 200
print("eighth_arr: ", eighth_arr_flat)
print("ninth_arr : ", ninth_arr_rav)
