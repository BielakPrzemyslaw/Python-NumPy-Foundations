myList = [1,2,3,4,5]
myList[:3]
#print [1,2,3]

myList[0:6:2]
#print [1,3,5]

myList[0:6:3]
#print [1,4]

myList.append(6)
#print [1,2,3,4,5,6]

myList.insert(3, 'a new value')
#print [1,2,a new value,4,5,6]

myList.remove('a new value')
myList
#print [1,2,3,4,5,6]

myList.pop()
#print 6

myList
#print [1,2,3,4,5]

while len(myList):
    print(myList.pop())
#print 5 4 3 2 1


myList
#print []

a = [1,2,3,4,5]
b = a
a.append(6)
print(b)
#print [1,2,3,4,5,6]

a = [1,2,3,4,5]
b = a.copy()
a.append(6)
print(a)
print(b)


