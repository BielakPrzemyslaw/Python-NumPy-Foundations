import numpy as np

print("")
print("copies examples:")
student_ids_number = np.array([1118,1212,2233,2313,1113,1456,3421,2567])
print(student_ids_number)

students_ids_number_reg = student_ids_number
print("id of student_ids_number :",id(student_ids_number))
print("id of students_ids_number_reg :",id(students_ids_number_reg))

students_ids_number_reg[1] = 2222
print(student_ids_number)
print(students_ids_number_reg)

print("")
students_ids_number_cp = student_ids_number.copy()
print(students_ids_number_cp)

print("")
print(students_ids_number_cp == student_ids_number)

print("")
print("id of student_id_number",id(student_ids_number))
print("id of students_ids_number_cp",id(students_ids_number_cp))

print("")
student_ids_number[0] = 1000
print('original: ', student_ids_number)
print('copy: ', students_ids_number_cp)

print("")
print(".view examples:")
student_ids_number_v = student_ids_number.view()
student_ids_number_v[0] = 2000
print('original :', student_ids_number)
print('view: ', student_ids_number_v)
print("")
print(".base")
print(students_ids_number_cp.base)
print(student_ids_number_v.base)