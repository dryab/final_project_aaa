from random import randint
from typing import Optional
%pip install click
import click

from pizza import Margherita, Pepperoni, Hawaiian
import decorator

pizzas = ['margherita','pepperoni','hawaiin']
@click.group()
def cli():
    pass


@cli.command()
def menu():
    """
    Меню
    """
    print(f"- Margherita 🧀: {', '.join(Margherita.dict().values())}")
    print(f"- Pepperoni 🍕: {', '.join(Pepperoni.dict().values())}")
    print(f"- Hawaiian 🍍: {', '.join(Hawaiian.dict().values())}")


@cli.command()
@click.option("--delivery", default=False, is_flag=True)
@click.argument("pizza", nargs=1)
def order(pizza: str, delivery: bool, size: Optional[str] = None):
    """
    Готовит заказанную пиццу
    Если  значение delivery TRUE, то еще и доставляет заказ
    """

    if pizza not in pizzas:
      raise ValueError("Такой пиццы нет в меню")
    else:
      print(bake(pizza))
      if delivery:
        print(delivery(pizza))
      else:
        print(pickup(pizza))




if __name__ == "__main__":
    cli()
