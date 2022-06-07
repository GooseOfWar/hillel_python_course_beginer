"""
Пользователь водит свое имя.
Возвращается тектс в БОЛЬШОМ и маленьком регистре. Использовать ' '.format().
Для вставки аргументов в текст.
Входные данные: Apollo
Результат: APPOLLO apollo
"""
user_name: str = input('Fillup your name\n')  # user input the name
print('{} {}'.format(user_name.upper(), user_name.lower()))  # modify name to upper and LWR case
