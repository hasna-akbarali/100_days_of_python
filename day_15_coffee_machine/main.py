import menu


def get_report():
    print('Water: ', menu.resources["Water"], 'ml', sep='')
    print('Milk: ', menu.resources["Milk"], 'ml', sep='')
    print('Coffee: ', menu.resources["Coffee"], 'g', sep='')
    print('Money: $', menu.resources["Money"], sep='')


def total_coins():
    print("Please insert coins.")
    quart = eval(input("how many quarters?: "))
    dimes = eval(input("how many dimes?: "))
    nickles = eval(input("how many nickles?: "))
    pennies = eval(input("how many pennies?: "))
    total = menu.conv["quart"] * quart + menu.conv["dime"] * dimes + menu.conv["nickel"] * nickles + menu.conv["penny"] * pennies
    return total


def update_menu():
    menu.resources["Money"] += menu.MENU[user]["cost"]
    menu.resources["Water"] -= menu.MENU[user]["ingredients"]["water"]
    menu.resources["Milk"] -= menu.MENU[user]["ingredients"]["milk"]
    menu.resources["Coffee"] -= menu.MENU[user]["ingredients"]["coffee"]


def check_if_possible():
    if (menu.resources["Water"] > menu.MENU[user]["ingredients"]["water"]
            and menu.resources["Milk"] > menu.MENU[user]["ingredients"]["milk"]
            and menu.resources["Coffee"] > menu.MENU[user]["ingredients"]["coffee"]):
        totalMoney = total_coins()
        if totalMoney > menu.MENU[user]["cost"]:
            change = round(totalMoney - menu.MENU[user]["cost"], 2)
            print(f"Here is ${change} in change.")
            print("Here is your espresso ☕️. Enjoy!")
            update_menu()
        elif totalMoney == menu.MENU[user]["cost"]:
            print("Here is your espresso ☕️. Enjoy!")
            update_menu()
        else:
            print("Sorry that's not enough money. Money refunded.")
    else:
        if menu.resources["Water"] < menu.MENU[user]["ingredients"]["water"]:
            print("There is not enough Water.")
        elif menu.resources["Milk"] < menu.MENU[user]["ingredients"]["milk"]:
            print("There is not enough Milk.")
        elif menu.resources["Coffee"] < menu.MENU[user]["ingredients"]["coffee"]:
            print("There is not enough Coffee.")


to_continue = True

while to_continue:
    user = input('What would you like? (espresso/latte/cappuccino): ')

    if user.lower() == 'report':
        get_report()

    elif user.lower() == 'espresso' or user.lower() == 'latte' or user.lower() == 'cappuccino':
        check_if_possible()

    else:
        to_continue = False
