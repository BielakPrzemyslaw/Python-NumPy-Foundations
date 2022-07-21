from decimal import Decimal, getcontext

#Integ

int('100')
#print 100

int('1ab', 16)
#print 427

1.2 - 1.0
#print 0.19999999999999996

#Decimals
getcontext()
#print Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999,
# Emax=999999, capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])

getcontext().prec=4
getcontext()
#print Context(prec=4, rounding=ROUND_HALF_EVEN, Emin=-999999,
# Emax=999999, capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])

Decimal(1) / Decimal(3)
#print 0.3333

getcontext().prec=2
Decimal(1) / Decimal(3)
#print 0.33

Decimal(3.14)
#print 3.140000000000000124344978758017532527446746826171875

Decimal('3.14')
#print 3.14

