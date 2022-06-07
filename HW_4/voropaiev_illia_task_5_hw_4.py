"""
Тема приведение типов. Работа со списком. Расчленение строки и ее соединение.
Пользователь вводит через запятую последовательность слов например цвета или продукты.
Программа возвращает уникальные слова отсортированные по алфавиту.
Входные данные: red, white, black, red, green, black
Результат: black, green, red, white
"""

user_list: str = input('Fillup your list, use "," as an separator\n')  # user input the list
user_list: list = user_list.split(', ')  # split str by separator and convert tot the list
user_list = set(sorted(user_list))  # make sorted set from list
print(', '.join(user_list))  # convert to the str format use ', ' like a joint
