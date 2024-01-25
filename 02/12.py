line = input('Введите сообщение:')
length = len(line)
length *= 40
print(length//100, 'р.', length % 100, 'коп.')
