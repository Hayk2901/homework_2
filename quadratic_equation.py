from math import sqrt
a = float(input())
b = float(input())
c = float(input())

if a == 0:
    print('Non-quadratic equation')
    if b == 0 and c == 0:
        print('Infinite solutions')
    elif b == 0:
        print('No Solutions')
    else:
        print('One solution:', c / b)
else:
    print('Quadratic equation')
    d = b * b - 4 * a * c
    print('Discriminant:', d)
    if d > 0:
        print('Two solutions:', (- b + sqrt(d)) / 2 / a, (- b - sqrt(d)) / 2 / a)
    if d == 0:
        print('One solution:', - b / 2 / a)
    if d < 0:
        print('No Solutions')
