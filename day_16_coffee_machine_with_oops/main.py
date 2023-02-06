from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

to_continue = True

while to_continue:
    user = input(f'What would you like? ({my_menu.get_items()}): ')
    drink  = my_menu.find_drink(user)
    if user.lower() == 'report':
        my_coffee_maker.report()
        my_money_machine.report()

    elif user.lower() == 'espresso' or user.lower() == 'latte' or user.lower() == 'cappuccino':
        if my_coffee_maker.is_resource_sufficient(drink):
            enough = my_money_machine.make_payment(drink.cost)
            if enough:
                my_coffee_maker.make_coffee(drink)


    else:
        to_continue = False
