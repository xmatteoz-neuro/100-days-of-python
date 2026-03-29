# Coffee Machine

# Initial Data

menu = {
    "espresso": {
        "ingredients": {
            "water": 50,  # amount in milliliters
            "coffee": 18,  # amount in grams
            "milk": 0
        },
        "cost": 1.5,  # cost in currency
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
    "water": 300,  # amount in milliliters
    "milk": 200,   # amount in milliliters
    "coffee": 100, # amount in grams
}

machine_on = True
earnings = 0
change = 0

# Functions

def report(resources):
    '''
    This function takes the available resources and updates after each 
    purchase the ingredients and checks the earnings of the machine
    '''
    print(f"Water: {resources['water']} mL")
    print(f"Milk: {resources['milk']} mL")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Earnings: $ {earnings}")

def coins():
    '''
    This function asks the user for coins and calculates how much money 
    has been inserted into the machine.
    No input variable required.
    '''
    cents = int(input("Add cents: "))*0.01
    tens = int(input("Add tens: "))*0.1
    twenty = int(input("Add twenty: "))*0.2
    quarters = int(input("Add quarters: "))*0.25
    return cents + tens + twenty + quarters

def check_ingredients(user_choice, resources, menu):
    '''
    This function checks that the resources are sufficient for the machine to run.
    '''
    ingredients = menu[user_choice]['ingredients']
    for item, amount in ingredients.items():
        if resources.get(item, 0) < amount:
            return False
    return True
        
def make_coffee(user_choice, menu, resources):
    '''
    This function executes the purchase of coffee.
    '''
    if check_ingredients(user_choice, resources, menu) == False:
            print("Not enough resources")
            return 0
    else:
        budget = coins()
        if budget < menu[user_choice]['cost']:
            print("Not enough funds")
            return 0
        else:
            print(f"Your {user_choice} is ready!")
            change = budget - menu[user_choice]['cost']
            print(f"You change is: ${change}")
            resources["water"] -= menu[user_choice]['ingredients']["water"] 
            resources["milk"] -= menu[user_choice]['ingredients']["milk"]  
            resources["coffee"] -= menu[user_choice]['ingredients']["coffee"]
            return menu[user_choice]['cost']
        
        
# Body of the code

while machine_on:
    print("Welcome to the coffee machine project.")
    user_input = input("Do you want to turn on the machine? (Y/N): ")
    if user_input in ('y', 'Y'):
        keep_going = True
        while keep_going:
            user_choice = input("What kind of coffee would you like (espresso/latte/cappuccino): ")
            if user_choice == 'report':
                report(resources)
            else:
                # since the coffee function generates earnings the earning is updated everytime it is used.
                # and also handles failed purchases
                earnings += make_coffee(user_choice, menu, resources)
                user_input = input("Do you want to continue using the coffee machine? (Y/N): ")
                if user_input in ('n', 'N'):
                    keep_going = False
                    report(resources)
                    print("Turning off coffee machine...")
                    machine_on = False
    else:
        machine_on = False