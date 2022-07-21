import math

#Slicing

name = 'My name is Przemyslaw'
name[0]
#print M

name[1]
#print y

name[0:7]
#print My name

name[:7]
#print My name

name[11:]
#print Przemyslaw

myList = [1,2,3,4,5]
myList[2:5]
#print[3,4,5]

len(name)
#print 21

len(myList)
#print 5

#Formatting

'My number is: '+str(5)
#print 'My number is: 5'

f'My number is: {5}'
#print 'My number is: 5'

f'My number is: {5} and twice that is {2*5}'
#print My number is: 5 and twice that is 10

f'Pi is: {math.pi: 2f}'
#print Pi is: 3.14

'Pi is: {}'.format(math.pi)
#print Pi is: 3.141592653589793

#Multi-line Strings
myString = '''
Here is a long block of text
I can add new lines!
the text doesn't stop until sees \'\'\'
'''

myString
#print
#Here is a long block of text
#I can add new lines!
#the text doesn't stop until sees '''
#