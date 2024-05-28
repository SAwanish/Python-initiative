from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

Coffee = CoffeeMaker()
Money = MoneyMachine()
menu = Menu()

machine = True
while machine:
    choice = input(f"What would you like to order: {menu.get_items()}?:")
    if choice == 'off':
        machine = False
    elif choice == 'report':
        Coffee.report()
        Money.report()
    else:
        drink = menu.find_drink(choice)
        if Coffee.is_resource_sufficient(drink) and Money.make_payment(drink.cost):
            Coffee.make_coffee(drink)