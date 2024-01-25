height_1 = input('Введите первый рост: ')
height_2 = input('Введите второй рост: ')
height_3 = input('Введите третий рост: ')
if height_3 < height_2 < height_1:
    print(height_1, height_2, height_3)
elif height_2 < height_1 < height_3:
    print(height_3, height_1, height_2)
elif height_1 < height_3 < height_2:
    print(height_2, height_3, height_1)
else:
    print(height_3, height_2, height_1)
