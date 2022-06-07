"""
1) Программа Выводит экран
Каждый 5й элемент последовательности.
'(etnfづzxfk｡12dt◕`1ad‿6hns‿1zQY◕Cd$y｡FtSq)Ze6?づ#2)$'
Уточнение:
Строка в кавычках, кавычки в данном случае не считаются элементом строки
"""

#  The most beautiful string
String: str = '(etnfづzxfk｡12dt◕`1ad‿6hns‿1zQY◕Cd$y｡FtSq)Ze6?づ#2)$'
i: int = 4  # iteration start

#  Print every 5 symbol
while i < 50:
    print(String[i], i + 1, sep='-')
    i = i + 5
