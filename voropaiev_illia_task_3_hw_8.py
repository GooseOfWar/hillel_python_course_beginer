"""
Lambda function. с помощью Анонимной функции остортировать список кортежей по цифре.
Пример(Example)
Input: [('bread', 5), ('milk', 2), ('eggs', 30), ('cola', 1)]
Otput: [('cola', 1), ('milk', 2), ('bread', 5), ('eggs', 30)]
"""

input_list: list = [('bread', 5), ('milk', 2), ('eggs', 30), ('cola', 1)]
print(sorted(input_list, key=lambda i: i[1]))

