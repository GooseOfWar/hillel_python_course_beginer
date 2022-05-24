"""
Посчитать общее количество наименований в списке. И только в списках.

Example:
shedule = {'monday': ['clean house', 'drive car', 'meet with freands'], 'thuesday': None, 'wednesday': ['manicure',
'hammam', 'beer']}
Результат: 6

Найти официальную документацию по Словарям и прикрепить ссылку к домашней работе 5 points
И попробовать прочитать ).
Там много языков и нет Русского 😈
"""

# Given data
my_schedule: dict = {'monday': ['clean house', 'drive car', 'meet with friends'], 'tuesday': None,
                     'wednesday': ['manicure', 'hammam', 'beer']}

number_of_element: int = 0  # Start variable

# for each element in given dict calculate number of elements and add to
# number of element
for key, value in my_schedule.items():

    if value is not None:  # to avoid the None type in dict values
        number_of_element += len(value)

print(number_of_element)  # print the result

print(r'https://docs.python.org/3.10/library/stdtypes.html#dict')  # print link from additional task
