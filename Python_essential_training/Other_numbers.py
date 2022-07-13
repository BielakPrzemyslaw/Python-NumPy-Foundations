from decimal import Decimal, getcontext

int('100')
#print 100

#int('100', 2)
#print 4

#int(100, 2)
#print Error int() can't convert non-string with explicit base

#int('lab', 16)
#print 427

print(getcontext())

getcontext().prec=4
print(getcontext())

print("Change prec on 4")
print(Decimal(1) / Decimal(3))

print("Change prec on 6")
getcontext().prec=6
print(Decimal(1) / Decimal(3))

print(round(1.24 - 1.0, 1))