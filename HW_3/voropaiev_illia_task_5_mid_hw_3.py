"""
Программа получает пользовательский ввод: большой_текст

В тексте будут встречаться ругательства: "черт". При этом, ругательства могут быть написаны с использованием любого
регистра или с использованием двоих сразу.
Пример: 'черт его возьми, черт его знает, Чертополох, иди к черту, черт ногу сломит, Чертеж здания в разрезе'
Результат: #### его возьми, #### его знает, Чертополох, иди к черту, #### ногу сломит, Чертеж здания в разрезе
и тд.
Вывести текст, заменив все отдельные слова "черт" на "####". Не беспокойтесь о регистре букв выводимого текста.
Так же текст будет без знаков припенания.
Учитывайте что в словах текста может встречаться последовательность "черт", которая является частью другого слова
и такие последовательности за ругательства не считаются.
"""

large_user_text: str = input('Please write your text\n')  # Input text


large_user_text = large_user_text.replace('черт ', '#### ')  # Replace the bad words
large_user_text = large_user_text.replace('Черт ', '#### ')

print(large_user_text)  # Print results
