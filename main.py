from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Definition of objects
# Can print the items and can select the item into a new object
menu = Menu()
# manages the money, gives the change and prints the revenue
moneymachine = MoneyMachine()
# makes the coffee given the selected item, consumes resources and handles lack of such
coffeemaker = CoffeeMaker()

# Initializing variables for while loop
keep_ordering = True


print(f"Welcome to the coffee machine. We serve: {menu.get_items()}")
while keep_ordering:
    start_order = input("Would you like to make an order (Y/N)? ")
    if start_order == 'N':
        break
    else:
        product = menu.find_drink(input("What kind of coffee do you want? "))
        if product is None:
            continue
        if coffeemaker.is_resource_sufficient(product):
            successfull_payment = moneymachine.make_payment(product.cost)
            if successfull_payment:
                coffeemaker.make_coffee(product)
check_report = input("Do you want to see the report of this session (Y/N)? ")
if check_report == 'Y':
    moneymachine.report()
    coffeemaker.report()
print("Bye bye!")

    
