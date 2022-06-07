"""
Спросить у пользователя год рождения.
Спомощью if -elif-else
Проверить встроенным строковым методом, состоит ли возраст из числа или текста.
если текст то по попросить ввести число.
Если 21 год вывести “You should visit Holland.”
Если больше 21 вывести “You should visit Vietnam.”
Все остальные варианты. Вывести “Travell everywhere”
"""

# it is the package of answers
answer_for_er_age: str = ('Only digit, please\n')
answer_for_21: str = ('You should visit Holland.')
answer_for_more_then_21: str = ('You should visit Vietnam.')
answer_for_else: str = ('Travell everywhere')

# user age input
user_age: str = input('Fillup your age\n')


# function for advice tree
def advice_tree(user_age):
    user_age = int(user_age)  # converting a variable to int

    if user_age == 21:  # user age = 21
        print(answer_for_21)
    elif user_age > 21:  # user age more then 21
        print(answer_for_more_then_21)
    else:
        print(answer_for_else)  # for another answers


# If answer has letters the loop asks again until winning result
while not user_age.isdigit():  # Letter content check
    user_age: str = input(answer_for_er_age)  # Ask again
else:
    advice_tree(user_age)  # if all is OK use the function "advice_tree" above
