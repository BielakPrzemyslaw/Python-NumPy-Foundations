import numpy as np

first_arr = np.arange(1,10)
second_arr = np.arange(11,21)
print(first_arr)
print(second_arr)

con_arr = np.concatenate((first_arr,second_arr))
print(con_arr)

third_2darr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(third_2darr)

fourth_2darr = np.array([[11,12,13,14,15],[16,17,18,19,20]])
print(fourth_2darr)

con2d_arr = np.concatenate((third_2darr,fourth_2darr),axis=1)
print(con2d_arr)


print("")
print(".hstack")
hst_arr = np.hstack((first_arr,second_arr))
print(hst_arr)

print("")
print(".split")
fifth_arr = np.arange(1,13)
print(fifth_arr)

sp_arr = np.array_split(fifth_arr,4)
print(sp_arr)

print(sp_arr[1])

sp_arr = np.array_split(fifth_arr,8)
print(sp_arr)


