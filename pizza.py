from typing import List, Dict
class Pizza:

  """
    Базовый класс для всех остальных классов пиццы.
    

    Реализует методы
        - __eq__() для сравнения пицц
        - dict() выводит рецепт в виде словаря
  """

  pizza_sizes = ["L", "XL"]
  def __init__(self, size: str = "L"):
        if size in self.pizza_sizes:
            self.size = size
        else:
            raise ValueError(f"Размера пиццы {size} не существует ")
        self.sauces = []
        self.cheese = []
        self.main_ingredients = []


  def dict(self) -> Dict[str, str]:
        """
        Функция выводит рецепт пиццу в виде словаря со строками

        """
        receipt_dict = {'Соус': ', '.join(self.sauces), 'Сыр':', '.join(self.cheese),'Основные ингредиенты':', '.join(self.main_ingredients)  }
        return receipt_dict


  def __eq__(self, other) -> str:
    """
    Функция сравнивает две пиццы по составу и размеру и выводит строку с результами сравнения

    """
    compare_result = ''
    if sorted(self.sauces) != sorted(other.sauces):
      compare_result = compare_result + 'разный соус'
    else: 
      compare_result = compare_result + 'одинаковый соус' 
    if sorted(self.cheese) != sorted(other.cheese):
      compare_result = compare_result +', '+'разный сыр'
    else: 
      compare_result = compare_result +', '+ 'одинаковый сыр'    
    if sorted(self.main_ingredients) != sorted(other.main_ingredients):
      compare_result = compare_result +', ' +'разная начинка'
    else: 
      compare_result = compare_result +', '+ 'одинаковая начинка' 
    if self.size != other.size:
      compare_result = compare_result +', ' +'разный размер'
    else: compare_result = compare_result +', '+ 'одинаковый размер' 
    return compare_result
 


class Margherita(Pizza):
    """
    Пицца Маргарита
    """

    def __init__(self, size: str = "L"):
        super().__init__(size=size)
        self.sauces = ["tomato sauce"]
        self.cheese = ["mozzarella"]
        self.main_ingredients = ["tomatoes"]


class Pepperoni(Pizza):
    """
    Пицца Пеппорони
    """

    def __init__(self, size: str = "L"):
        super().__init__(size=size)
        self.sauces = ["tomato sauce"]
        self.cheese = ["mozzarella"]
        self.main_ingredients = ["pepperoni"]


class Hawaiian(Pizza): 
    """
    Гавайская пицца
    """

    def __init__(self, size: str = "L"):
        super().__init__(size=size)
        self.sauces = ["tomato sauce"]
        self.cheese = ["mozzarella"]
        self.main_ingredients = ["chicken", "pineapples"]



