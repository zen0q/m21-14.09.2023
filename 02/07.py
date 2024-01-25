fraction = float(input('Введите число:'))
if fraction < 0.000001 or fraction == 0:
    print(1000000)
else:
    print(1/fraction)