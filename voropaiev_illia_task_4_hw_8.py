"""
познакомиться с модулем datetime и написать программу с помощью lambda для возвращение текущего года, месяца , дня
например результат должен быть таким
import datetime
now = datetime.datetime.now()
.....ваш код))
print(year(now))
print(month(now))
print(day(now))

скинуть мне ссылку на документациюю по datetime.
"""

import datetime

#  import now
now = datetime.datetime.now()  # 2022-05-31 14:40:40.502384

year: any = lambda i: i.year  # use lambda expression to call attribute year
month: any = lambda i: i.month  # use lambda expression to call attribute month
day: any = lambda i: i.day  # use lambda expression to call attribute day

# print the result
print(f'It\'s {year(now)} now')
print(f'{month(now)}th month')
print(f'And day {day(now)}')

print(r'https://docs.python.org/3.10/library/datetime.html')
print(r'https://www.w3resource.com/python-exercises/lambda/python-lambda-exercise-8.php')
