"""
написать функцию которая в качестве аргумента принимает размер стороны квадрата, а возвращает кортеж в котором лежат
три значения:
периметр квадрата
диагональ квадрата
площадь квадрата
"""

user_data: str = input("Fillup square side dimension in mm\n")  # data input


def square_parameters(data):  # check data is.digit and calculate square parameters
    while not data.isdigit():  # If data not only digits ask again
        data = input("Incorrect Data. Use only digit.\n")
    else:  # if data is only digit: calculate perimetr diagonal and area of square
        square_side = int(data)  # convert on int type
        perimeter: int = square_side * 4    # perimeter calculation
        diagonal: float = round(square_side / 0.707, 2)  # diagonal calculation
        area: int = square_side ** 2    # area calculation

    # tuple with square parameters
    square_parameters_data: tuple = (perimeter, diagonal, area)
    print(square_parameters_data)

    #  Use f string for calculated data printing
    print((f'Square Perimeter {perimeter} mm', f'Square diagonal {diagonal} mm', f'Square area {area} mm^2'))


square_parameters(user_data)
