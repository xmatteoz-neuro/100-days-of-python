# ☕ Coffee Machine — Day 16

A terminal-based coffee machine simulator built in Python as part of Angela Yu's *100 Days of Code* bootcamp.

## Features

- Interactive menu with multiple drink options
- Resource management (water, milk, coffee)
- Coin-based payment system with change
- Session report with revenue and remaining ingredients

## Project structure

```
day-16/
├── main.py           # Entry point and main loop
├── menu.py           # Menu and MenuItem classes
├── coffee_maker.py   # CoffeeMaker class (resources & brewing)
└── money_machine.py  # MoneyMachine class (payments & revenue)
```

## How to run

```bash
python main.py
```

No external dependencies — standard library only.

## How it works

1. The machine displays the available drinks on startup
2. The user chooses whether to place an order
3. If resources are sufficient, the machine prompts for coins
4. On successful payment, the drink is prepared and change is returned
5. On exit, the user can optionally view a session report

## Example session

```
Welcome to the coffee machine. We serve: latte/espresso/cappuccino
Would you like to make an order (Y/N)? Y
What kind of coffee do you want? latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0
Here is $0.5 in change.
Here is your latte ☕. Enjoy!
Would you like to make an order (Y/N)? N
Do you want to see the report of this session (Y/N)? Y
Water: 200ml
Milk: 100ml
Coffee: 76g
Money: $2.5
```

## Course context

Built on Day 16 of [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/) by Dr. Angela Yu. Focuses on OOP principles: class design, encapsulation, and object interaction.
