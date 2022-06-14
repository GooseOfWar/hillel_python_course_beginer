"""
Скинуть файлик с примерами всех конструкций КРОМЕ менеджера контекста. With/as.
"""


def catcher(word: str, index: int) -> str:
    try:
        return word[index]
    except IndexError:
        return "Word has no that index"


def catcher2(word: str, index: int) -> str:
    try:
        return word[index]
    finally:
        return "always will be print"


class MyError(Exception):
    pass


def catcher3(word: str, index: int) -> str:
    try:
        raise MyError
        return word[index]
    except MyError as e:
        return "My Error"


print(catcher('sd;lmflk', 50))
print(catcher2('milk', 50))
print(catcher3('astanavites', 50))

assert False, "any things"
