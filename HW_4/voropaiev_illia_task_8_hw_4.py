"""
Тема range
Есть последовательность от -99 до 99. Ее шаг 3. т.е. [-99, -96]
напечатать все элементы последовательности которые делятся на 3 без остатка.
напечатать в формате 'это <<ЧИСЛО>> делится без остатка на 3'
использовать метод редактирования строки f' строки'
"""

# for range from -99 to 99 check the divisible by 3
for i in range(-99, 99):
    if i % 3 == 0:  # if the remainder not exist the results will be 0
        print(f'this number{i} divisible without remainder by 3')  # print the results if true
    else:
        None
