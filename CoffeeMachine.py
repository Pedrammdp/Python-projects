MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 19,
        },
        "cost": 1.5,
    },
    "latte" : {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 200,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water" : 1000,
    "milk" : 400,
    "coffee" : 250,
    "money": 0.0
}

COIN_VALUES = {
    "quarters" : 0.25,
    "dimes" : 0.10,
    "nickles" : 0.05,
    "pennies" : 0.01
}

def print_report():
    """Prints a report of all current resources and profit."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")
    print("----------------\n")

def check_resources(order_ingredients):
    """
    Checks if there are enough ingredients (resources) in the machine
    to make the requested drink.
    Returns True if sufficient, otherwise prints an error and returns False.
    """
    for ingredient, amount_needed in order_ingredients.items():
        if resources.get(ingredient, 0) < amount_needed:
            print(f"Sorry, there is not enough {ingredient} to make your drink.")
            return False
    return True

def process_coins():
    """
    Prompts the user to insert coins and calculates the total value.
    Returns the total monetary value inserted.
    """
    print("\nPlease insert coins.")
    try:
        quarters =  int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int((input("How many nickles?: ")))
        pennies = int(input("How many pennies?: "))
    except ValueError:
        print("Invalid input for coins. Please enter whole numbers.")
        return 0.0
    
    total = (quarters * COIN_VALUES["quarters"] +
             dimes * COIN_VALUES["dimes"] +
             nickles * COIN_VALUES["nickles"] +
             pennies * COIN_VALUES["pennies"])
    
    return round(total, 2)

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"Here is ${change:.2f} in change.")

        resources["money"] += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):

    for ingredient, amount in order_ingredients.items():
        if ingredient in resources:
            resources[ingredient] -= amount
    print(f"Here is your {drink_name}. Enjoy!")

def run_coffee_machine():
    """The main function to run the coffee machine program loop."""
    is_on = True
    print("Welcome to the Coffee Machine Simulator!")

    while is_on:
        prompt = "What would you like? (espresso/latte/cappuccino/report/off): "
        choice = input(prompt).lower().strip()

        if choice == "off":
            is_on = False
            print("Shutting down the coffee machine for maintenance. Goodbye!")
        
        elif choice == "report":
            print_report()
        
        elif choice in MENU:
            drink = MENU[choice]
            
            if check_resources(drink["ingredients"]):
                payment = process_coins()
                cost = drink["cost"]
                
                if is_transaction_successful(payment, cost):
                    make_coffee(choice, drink["ingredients"])
        
        else:
            print("Invalid selection. Please choose a valid drink or command.")
        
run_coffee_machine()