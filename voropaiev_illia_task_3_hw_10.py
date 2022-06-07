"""
дописать декоратор, чтобы он принимал аргумент, например текст.
и выводил его тоже.
@methods_amount('need to learn')
[count, index]
'need to learn 2'
"""


def methods_amount(fun):    # Just example function
    """what are they wanting"""
    def wrapper():
        my_fun = fun()
        do_some_things = ' won shrewder'
        return my_fun + do_some_things
    return wrapper


@methods_amount
def some_str():
    """Ninja turtles"""
    return "ninja turtles"


print(some_str())
