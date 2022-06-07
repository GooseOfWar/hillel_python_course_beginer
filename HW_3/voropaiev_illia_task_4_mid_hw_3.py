"""
Программа получает пользователский ввод:
"количество_земных_дней, количество_часов", (за один input)
Обратите внимание на формат ввода.
Это всегда будут два числа разделенных запятой и одним пробелом после.
Программа переводит земные дни в марсианские солы.
Программа должна вывести на экран число солов, соответствующих пользовательскому вводу.
Результат округлять до 2-х знаков после запятой
"""
sol: float = 1.02595675  # Sol coefficient

#  User input days and hours in special format
earth_day_hours: str = input('Input numbers of earth days and hours. Use format: days:hours - without gap\n')

#  Checking user input for compatibility
#  Checking the right separator
while earth_day_hours.find(':') == -1:
    earth_day_hours: str = input('Please use only digits in format: days:hours - without gap\n')
else:
    earth_day: str = earth_day_hours.split(':')[0]
    earth_hours: str = earth_day_hours.split(':')[1]
#  Checking for data compatibility. Data shall be only digit
while earth_day.isalpha() or earth_hours.isalpha():
    earth_day_hours: str = input('Please use only digits in format: days:hours - without gap\n')
    earth_day: str = earth_day_hours.split(':')[0]
    earth_hours: str = earth_day_hours.split(':')[1]

#  Translate data from str to int
earth_day = int(earth_day)
earth_hours = int(earth_hours)

#  Main solution: (D+H/24)*Sol coefficient
translation_in_sol: float = round((earth_day + earth_hours / 24) * sol, 2)

print("That's ", translation_in_sol, " sols on Mars!")  # Print the results
