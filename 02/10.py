number_1 = float(input('Введите первое дробное число:'))
number_2 = float(input('Введите второе дробное число:'))
line = input('Введите одну из четырех основных математических операций:')
if line == '+':
    print(number_1+number_2)
elif line == '-':
    print(number_1-number_2)
elif line == '*':
    print(number_1*number_2)
elif line == '/':
    if number_2 != 0:
        print(number_1/number_2)
    else:
        print(888888)
else:
    print(888888)