"""
Создать файл (модуль) с примерами всех методов строк. +
Создать по 3 варинта всех уже изученных объектов в Пайтоне.
    строки. +
    числа(с плавающей точкой, целочисленные)
    Списки
    Словари
    Кортежи
Написать 3 примера использования max(), min(),
выучить какие не изменяемые объекты, а какие изменяемые.
Написать 3 примера различных с оператором in
написать 3 примера условия if elif else.
"""



"""
Used methods
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'find', 'format', 'index', 'join',
'lower',  'partition', 'replace', 'rsplit', 'split', 'strip', 'swapcase', 'title', 'upper',]
"""
# modifying word
word: str = 'kOmaTozz {}'
# examples (not all methods)
print(
    '\nTask 1.1\n'.center(140, '-'),
    word.capitalize(), word.casefold(), word.center(30, '~'), word.count('z'),
    word.encode(encoding='utf-8', errors='ignore'), word.find('z'), word.format('aaaaa'), word.index('a'),
    '.'.join(word), word.lower(), word.upper(), word.partition('a'), word.replace('a', 'A'), word.split('a'),
    word.rsplit('a'), word.strip('{} kz'), word.swapcase(), word.title(), sep="\n")


(example_a_1, example_a_2, example_a_) = ('konieyasher',
                                          "r'https://docs.python.org/3.10/library/stdtypes.html#str.strip",
                                          bytes([50, 100, 76, 72, 41]))
print('\nTask 1.2.1\n'.center(140, '-'), example_a_1, example_a_2, example_a_, sep='\n')