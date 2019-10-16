import math
import decimal
import numpy as np

x = decimal.Decimal((input('Введите x: ')))
eps = decimal.Decimal((input('Введите eps: ')))
q = decimal.Decimal((input('Введите q: ')))
a = eps * (1 - q) / q
a = a.quantize(decimal.Decimal('1.0000000'))
while True:
    x1 = decimal.Decimal(math.log10(x)).quantize(decimal.Decimal('1.0000000'))
    if x1 > 1:
        print('Логорифм > 1')
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
        print('arcsin вышел за предел!')
        break
x = x.quantize(decimal.Decimal('1.0000000'))
print('x =', format(x))
# def Variant2():
#     x = decimal.Decimal(input('Введите x: '))
#     eps = decimal.Decimal((input('Введите eps: ')))
#     q = decimal.Decimal((input('Введите q: ')))
#     a = eps * (1 - q) / q
#     a = a.quantize(decimal.Decimal('1.0000000'))
#     while True:
#         y = decimal.Decimal(x) + decimal.Decimal(0.37) * decimal.Decimal((math.sin(2 * x))
#         - decimal.Decimal(math.log(x)))
#         p = x - y
#         x = y
#         if abs(p) > a:
#             break
#     x = x.quantize(decimal.Decimal('1.0000000'))
#     print('x =', format(x))


# answer = int(input('Выберите вариант(1 или 2): '))
# l = True
# while l:
#     if answer == 1:
#         Variant1()
#     elif answer == 2:
#         Variant2()
#     else:
#         print('Выбери из списка, дубина!')
#         continue
input()
