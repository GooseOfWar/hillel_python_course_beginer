"""
пользователь вводит пароль первый раз система запоминает и просит
повторить пароль проверяет его если нет то просит повторить. А если совпал то сообщение.
"""

user_password: str = input("Please write you Password")  # user write password first time

#  password must be at least 4 sign in length and contain alphabet and numeric sym
short: int = 0  # bypass for "short password" check. They are 0 is it False
dif_symbol: int = 0  # bypass for "only digit\alpha symbols" check. They are 0 is it False

while short * dif_symbol == 0:  # check for short password and only digit\alpha symbols.
    # Run if short and dif_symbols not 1
    if len(user_password) < 4:  # if user password contain less than 4 symbols ask input again
        user_password = input("Too Short Password. Try again")
        short = 0  # return 0 like a False
    else:
        short = 1  # return 1 like a True

    if user_password.isdigit() \
            or user_password.isalpha() == 1:  # if user password contain only digit or alphabet symbols ask input again
        user_password = input("Password must contain digit and number")
        dif_symbol = 0  # return 0 like a False
    else:
        dif_symbol = 1  # return 1 like a True

user_password_repeat: str = input("Repeat your password")  # user repeat the password

while user_password != user_password_repeat:  # if duplicated password is wrong user shall write again
    user_password_repeat = input("Password repeat are wrong. Please write again")
else:
    print("Successful. Welcome!")  # print if all is OK
