"""
Приветствует пользователя в произвольном виде.
Принимает на ввод его никнейм, пол, возраст.
Если никнейм содержит admin, выводит: "Привет, повелитель!", не прекращая работу.
Если возраст больше 10 и меньше 14 и пол М или больше 30 и пол М: Выводит "Советую Вам посмотреть "StarWars" или 'Мандалорец'"
Если возраст больше 22 и меньше 32 и пол Ж: Рекомендация "Советую Вам посмотреть "Трансформеры""
Если возраст меньше 16 и пол Ж: Рекомендация "Советую Вам посмотреть "Инсургент""
Если никнейм 'Женя': Рекомендация "Советую Вам посмотреть 'TENET'"
Если возраст до 11 и пол М: Рекомендация "Советую Вам посмотреть "TMNT""
Если никнейм Guido: Кроме рекомендации, выводит "Огромное спасибо!
"""
print('Welcome friend!')  # Welcome user

# Fillup user data: nickname, age, sex
user_name: str = input('Fillup your nickname\n')
user_age: str = input('Fillup your age\n')
# If answer has letters the loop asks again until winning result
while not user_age.isdigit():  # Letter content check
    user_age: str = input('Please, use only digits\n')  # Ask again
user_sex: str = input('Fillup your sex M - for male, F - for female\n')

user_sex = user_sex.upper()  # convert to upper case
good_buy: str = ' Watch you later ' + user_name + '!'  # Good buy words


#  Advice function for some age and sex
def advice_tree(user_age, user_sex):
    user_age = int(user_age)

    if (10 < user_age < 14 and user_sex == 'M') or (user_age > 30 and user_sex == 'M'):
        print(user_name, 'I advise you to watch "Star Wars" or "The Mandalorian".', sep='! ', end=good_buy)
    elif 22 < user_age < 32 and user_sex == 'F':
        print(user_name, 'I advise you to watch "Transformers".', sep='! ', end=good_buy)
    elif user_age < 16 and user_sex == 'F':
        print(user_name, 'I advise you to watch "Insurgent".', sep='! ', end=good_buy)
    elif user_age > 11 and user_sex == 'M':
        print(user_name, 'Советую Вам посмотреть "TMNT".', sep='! ', end=good_buy)
    else:
        print(user_name, 'I recommend watching "Rick and Morty".', sep='! ', end=good_buy)


#  additional functions named Zhenya, admin, Guido
if user_name == 'Женя':
    print(user_name, "I advise you to watch 'TENET'.", sep='! ', end=good_buy)
elif user_name == 'admin':
    print("Hello master!", ), advice_tree(user_age, user_sex)
elif user_name == 'Guido':
    advice_tree(user_age, user_sex), print("Thanks a lot!")
else:
    advice_tree(user_age, user_sex)
