"""
написать функцию которая принимает в качестве аргумента номер месяца, в возвращает строку - время года, этого месяца
"""

user_data: str = input('Fill-up number of month\n')  # user input data


def season_by_month(number_of_month):   # just print data from the dict
    while not number_of_month.isdigit():    # if user data not digital print massage and input again
        number_of_month = input('Only Digit Please!\n')
    else:  # if all is OK convert type on int
        month_number = int(number_of_month)

    list_of_month: list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                           'October', 'November', 'December']   # list of month
    dict_of_month: dict = {'January': 'Winter', 'February': 'Winter',
                           'March': 'Spring', 'April': 'Spring', 'May': 'Spring', 'June': 'Summer', 'July': 'Summer',
                           'August': 'Summer', 'September': 'Autumn', 'October': 'Autumn', 'November': 'Autumn',
                           'December': 'Winter'}  # dict with equal season
    # print formating str
    print(
        f'{list_of_month[month_number - 1]} it\'s a {dict_of_month[list_of_month[month_number - 1]]} !'
    )
    
    return dict_of_month[list_of_month[month_number - 1]]


season_by_month(user_data)
