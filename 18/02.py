def email_blast(name, place = 'Нефтекамск', date, email):
    return (f'To: {email}\nЗдравствуйте, {name}!\nБыли бы рады видеть вас на встрече начинающих программистов в {place},'
    f'\nкоторая пройдет {date}.')

print(email_blast('Ivanov Ivan', 'qwer', 'dd/mm/yyyy', 'Ivanov@ivan.dot'))