"""
Попробовать посмотреть на написанный код и сделать его более надежным. Любые изменения приветствуются.
просмотреть каждую программу и посмотреть как она может упасть. Попробовать ее зафейлить.
Во время тестирования заметить какие ошибки появляется
используя исключения изменить код. И не только исключения, а и фантазию.
"""



def example1():
    pass
    # for i in range(3):
    #     try:
    #         x = int(input("enter a number: "))
    #         y = int(input("enter another number: "))
    #     except ValueError:
    #         print('Use digital value')
    #     try:
    #         print(x, '/', y, '=', x / y)
    #     except ZeroDivisionError:
    #         print("Devision by zero")


def example2(L):
    print("\n\nExample 2")
    sum = 0
    sumOfPairs = []
    for i in range(len(L)):
        try:
            sumOfPairs.append(L[i] + L[i + 1])
        except IndexError:
            break
        except TypeError:
            sumOfPairs.append(f'{L[i]} + {L[i+1]}')


    print("sumOfPairs = ", sumOfPairs)


def printUpperFile(fileName):
    try:
        file = open(fileName, "r")
    except FileNotFoundError:
        try:
            file = open(fileName, "w")
            file.close()
            file = open(fileName, "r")
            for line in file:
                print(line.upper())
            file.close()
        except FileNotFoundError as e:
            print(f'Sorry, but {e}')



def main():
    example1()
    L = [10, 3, 5, 6, 9, 3]
    example2(L)
    example2([10, 3, 5, 6, "NA", 3])

    printUpperFile("doesNotExistYest.txt")
    printUpperFile("./Dessssktop/misspelled.txt")

main()
