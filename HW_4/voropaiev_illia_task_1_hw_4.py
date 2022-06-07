"""
написать программку которая будет состоять из первых двух и последних символов предоставленной строки.
Если длинна строки меньше двух символов напечатать строку типа.
'Ваша строка слишком короткая - СТРОКА ' . Через метод форматирования строк с %.
Входная строка : 'Hillel school'
Результат1 : 'Hiol'
или
Результат2 : 'Ваша строка слишком короткая - и ваша строка'
"""

user_text: str = input('Fillup your text\n')  # User fillup text

while len(user_text) < 4:  # if user text less than 4 symbols print error message
    user_text: str = input('Your text "%s" is too short! Please write more than 4 symbols!\n' % user_text)
else:  # if user text is OK print first and last two symbols
    print(user_text[0:2] + user_text[-2:])






