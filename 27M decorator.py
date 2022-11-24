from typing import Callable


def bread(func: Callable):
    def wrapped():
        print('</----------\>')
        func()
        print('<\______/>')
    return wrapped


def salat(func: Callable):
    def wrapped():
        print('#помидоры#')
        func()
        print('~салат~')
    return wrapped


@bread
@salat
def topping():
    print('--ветчина--')


topping()
