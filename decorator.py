from typing import  Optional
from random import randint



def log(pattern: Optional[str] = None):
    """
    Функция декоратора, которая выводит название функции и затраченное время

    """
    def decorator(func):
        def wrapper(*args):
            time = randint(1, 20)
            name = func.__name__
            if pattern:
                    print(pattern.format(time))
            else:
                print(f"{name} - {time} seconds!")
            return func(*args)
        return wrapper
    return decorator


@log()
def bake(pizza) -> int:
    """
    Готовит пиццу
    """


@log("🛵 Доставили за  {} секунд!")
def delivery(pizza) -> int:
    """
    Доставляет пиццу
    """


@log("🏡 Забрали за {} секунд!")
def pickup(pizza) -> int:
    """
    Самовывоз
    """
