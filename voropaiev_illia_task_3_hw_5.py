"""
Тема while and else
дан список произвольный с int нужно вывести "all numbers are even" если все четные и NO если нет
Пример входных данных: [11, 23, 65, 44, 76, 533]
Результат: NO
"""

my_list_of_numbers: list = [10, 20, 64, 44, 76, 532]  # for debug [10, 20, 64, 44, 76, 532] [11, 23, 65, 44, 76, 533]
i: int = 0  # iteration in while

while i <= (len(my_list_of_numbers) - 1):
    my_list_of_numbers[i] %= 2  # check the remainder

    if my_list_of_numbers[i] == 1:  # if the remainder == 1 stop code and print "no"
        print('No')
        break

    else:  # if remainder is 0 next iteration (i+1)
        i += 1


else:  # in case when cycle is over successfully print next:
    print('all numbers are even')
