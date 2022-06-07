"""
Программа принимает список продуктов и принтит самое длинное слово и его длинну.
Ипользовать ''.format() для вывода строки и аргументов.
Входные данные: ['bread', 'milk', 'kolbasa']
Результат: 'Самое длинное название продукта kolbasa длинна 7 символов'
"""
user_list: str = input('Fillup your list, use a space as a separator\n')  # user input the grocery list
user_list: list = user_list.split(' ')  # Convert from str to list

# for the task solving words must be compared one by one for to start use first index word

word: str = user_list[0]  # first index word
word_length: int = len(user_list[0])  # length of the first index word

for i in user_list:  # if length index 'i' bigger than length of the first index word replace the value on 'i'

    if len(i) > word_length:
        word = i
        word_length = int(len(i))

    else:  # if length index 'i' smaller than length of the first index word leave the last option
        word = word
        word_length = word_length

print('Самое длинное название продукта {} длинна {} символов'.format(word, word_length))  # print the results
