side = [int(input()), int(input()), int(input())]
side = sorted(side)
if side[2] >= side[1] + side[0] or side[0] <= 0:
    print('No Triangle')
elif side[2] ** 2 < side[1] ** 2 + side[0] ** 2:
    print('Acute Triangle')
elif side[2] ** 2 == side[1] ** 2 + side[0] ** 2:
    print('Right Triangle')
else:
    print('Obtuse Triangle')
