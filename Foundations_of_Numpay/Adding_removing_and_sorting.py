import numpy as np

print("")
print(".insert examples:")
first_arr = np.array([1,2,3,5])
print(first_arr)

new_first_arr = np.insert(first_arr, 3,4)
print(new_first_arr)

print("")
print(".append examples:")
second_arr = np.array([1,2,3,4])
print(second_arr)

new_second_arr = np.append(second_arr, 5)
print(new_second_arr)

print("")
print(".delete examples:")
third_arr = np.array([1,2,3,4,5])
print(third_arr)

del_element = 1
del_third_arr = np.delete(third_arr, del_element)
print(del_third_arr)

print("")
print(".integers examples:")
integers_arr = np.random.randint(0,20,20)
print(integers_arr)
print("")
print(".sort examples:")
print(np.sort(integers_arr))

integers_2dim_arr = np.array([[3,2,5,4],[5,0,7,1]])
print(integers_2dim_arr)

print(np.sort(integers_2dim_arr))

colors = np.array(['blue' , 'green', 'white', 'orange', 'pink', 'red'])
print(colors)

print(np.sort(colors))

