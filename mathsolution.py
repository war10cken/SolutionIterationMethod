import math
import decimal

x = decimal.Decimal((input('Enter x: ')))
eps = decimal.Decimal((input('Enter eps: ')))
q = decimal.Decimal((input('Enter q: ')))
a = eps * (1 - q) / q
a = a.quantize(decimal.Decimal('1.0000000'))
while True:
    x1 = decimal.Decimal(math.log10(x)).quantize(decimal.Decimal('1.0000000'))
    if x1 > 1:
        print('Logarithm > 1')
        break
    res = decimal.Decimal(math.asin(x1)).quantize(decimal.Decimal('1.0000000'))
    pi = decimal.Decimal(math.pi).quantize(decimal.Decimal('1.0000000'))
    if -1 <= res <= 1:
        y = decimal.Decimal(((pi - res) / 2)).quantize(decimal.Decimal('1.0000000'))
        p = x - y
        x = y
        if abs(p) > a:
            break
    else:
        print('arcsin out of range!')
        break
x = x.quantize(decimal.Decimal('1.0000000'))
print('x =', format(x))
input()
