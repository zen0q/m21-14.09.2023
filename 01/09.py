line_1 = input('Введите логин:')
line_2 = input('Введите резервный адрес:')
if '@' not in line_1 and '@' in line_2:
    print('OK')
elif '@' in line_1:
    print('Некорректный логин')
elif '@' not in line_2:
    print('Некорректный адрес')
