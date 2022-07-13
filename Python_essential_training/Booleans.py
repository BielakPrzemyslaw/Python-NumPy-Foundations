print(bool(1))

print(bool(-1))

print(bool(0))

print(bool(0.0))

print(bool(0j))

print('True')

print('False')

print(bool(' '))

print(bool(''))

print(bool([]))

print(bool([1,2]))

print(bool({}))

print(bool({1: 23}))

myList = [2,4,6]
if bool(myList):
    print('Mylist has some values in it!')

#False and nothing to print
a = 5
b = 5
if a - b:
    print('a and b are not equal')

print(a == b)

print('')
print('Boolean Logic:')

weatherIsNice = False
haveUnbrella = True

if not haveUnbrella or weatherIsNice:
    print('Stay inside')
else:
    print('Go for walk')
