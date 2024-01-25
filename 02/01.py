city_1 = input('Введите первый город: ')
city_2 = input('Введите первый город: ')
if city_1 != city_2 and (city_1 == 'Тула' or city_2 == 'Пенза') and not (city_1 == 'Тула' and city_2 == 'Пенза'):
    print('Да')
else:
    print('Нет')
