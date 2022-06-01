"""
Написать функцию которая принимает в качестве аргумента строку, и возвращает True,
если строка является полиндромом и False если нет.
"""

user_string: str = input('Input the word\n')    # user fill the word


def is_palindrome(check_word):
    """Function compare user word with reverse user word"""
    return check_word == check_word[::-1]


print(is_palindrome(user_string))  # print the result
