"""
Написать функцию которая будет добовлять код страны
к номеру телефона с помощью замыкания
внешний вид вызова функции.
my_number = user_telephone('+044')
my_number('838372893')
+044838372893 результат.
"""
# user_input: str = input('Fillup your number')
user_input: str = '0978768982'


def add_country_code(tel_num: str) -> str:
    """ Function add Ukrainian country code to user phone"""
    ua_tel_code: str = "+38"

    def code_append() -> str:
        """UA code +38 adding to user input number"""
        return ua_tel_code + tel_num

    return code_append()


print(add_country_code(user_input))
