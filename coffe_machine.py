MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def is_sufficient_resource(order_ingredient):
    """To check the resource is sufficient"""
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def total_money():
    """To calculate the total money"""
    print("Please insert coins. ")
    total = 0
    total += int(input("How many pennies?: ")) * 0.01
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many quarters?: ")) * 0.25
    return total


def transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} dollars in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"Sorry that's not enough money. You need ${drink_cost}. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} 🧋. Enjoy!")


is_on = True
while is_on:
    # Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    #  Turn off the Coffee Machine by entering “off” to the prompt.
    if choice == "off":
        is_on = False
    # Print report.
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_sufficient_resource(drink["ingredients"]):
            money = total_money()
            if transaction_successful(money, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
