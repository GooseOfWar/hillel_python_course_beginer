"""
Написать программу, которая подсчитывает количество символов в строке
и формирует dict в котором key = буква, value= количество их в слове:
Входная строка : 'Hillel school'
Результат :  {'H': 1, 'i': 1, 'l': 4, 'e': 1, ' ': 1, 's': 1, 'c': 1, 'h': 1, 'o': 2}
"""
user_text: str = input('Fillup you text\n')  # User input the text
text_list: list = list(user_text)  # convert string to the list to get the string letter by letter
new_dictionary: dict = {}  # create new empty dictionary


for i in text_list:  # add to the dictionary every 'key' and 'value' element
    key: str = i
    value: int = text_list.count(i)
    new_dictionary[key] = value
print(new_dictionary)

# provide check - compare the dictionary
check: dict = {'H': 1, 'i': 1, 'l': 4, 'e': 1, ' ': 1, 's': 1, 'c': 1, 'h': 1, 'o': 2}
if new_dictionary == check:
    print('It\'s OK')
else:
    print('no no no, try again')

