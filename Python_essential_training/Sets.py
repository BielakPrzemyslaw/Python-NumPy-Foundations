mySet = {'a', 'b', 'c'}
mySet
#print {'a', 'b', 'c'}

mySet = set(('a', 'b', 'c'))
mySet
#print {'a', 'b', 'c'}

myList = ['a', 'b', 'c']
#mySet[0]
#print TypeError: 'set' object does not support indexing

mySet.add('d')
mySet
#print {'a', 'b', 'c', 'd'}

'a' in mySet
#print True

'z' in mySet
#print False

len(mySet)
#print 4

while len(mySet):
    print(mySet.pop())

#print a,b,c,d

mySet
#print ()

mySet = {'a', 'b', 'c'}
mySet.discard('a')
mySet
#print {'b', 'c'}

#TUPLES
myTuple = ('a', 'b', 'c')
myTuple
#print ('a', 'b', 'c')

myTuple[0]
#print 'a'

def returnMultipleValue():
    return 1,2,3
type(returnMultipleValue())
#print tuple

myTuple = 1,2,3
type(myTuple)
#print tuple

a, b, c = returnMultipleValue()
print(a)
print(b)
print(c)