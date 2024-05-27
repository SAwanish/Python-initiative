# Coins Operated
# Penny = $0.01
# Nickel = $0.05
# Dime = $0.10
# Quarter = $0.25

# Ingredient
water = 300
Milk = 200
Coffee = 100
Money = 0


# Functions
def report():
    print(f"Water: {water}ml")
    print(f"Milk: {Milk}ml")
    print(f"Coffee: {Coffee}g")
    print(f"Money: ${Money}")


def espresso():
    Price = 1.50
    global water
    global Milk
    global Coffee
    global Money
    if water < 50:
        print("Sorry, there is not enough water!")
    elif Coffee < 18:
        print("Sorry, there is not enough coffee!")
    else:
        print("Please insert coins.")
        Quarters = int(input("How many quarters?:"))
        Dimes = int(input("How many dimes?:"))
        Nickels = int(input("How many nickels?:"))
        Pennies = int(input("How many pennies?:"))
        user_income = (Quarters / 4) + (Dimes / 10) + (Nickels / 20) + (Pennies / 100)
        if user_income < Price:
            print(f"insufficient Balance!! Kindly take back your money : {user_income}")
        else:
            print(f"Here is {user_income - Price} in change.")
            print("Here is your espresso ☕ Enjoy!")
            water -= 50
            Coffee -= 18
            Money += Price


def latte():
    Price = 2.50
    global water
    global Milk
    global Coffee
    global Money
    if water < 200:
        print("Sorry, there is not enough water!")
    elif Coffee < 24:
        print("Sorry, there is not enough coffee!")
    elif Milk < 150:
        print("Sorry, there is not enough Milk!")
    else:
        print("Please insert coins.")
        Quarters = int(input("How many quarters?:"))
        Dimes = int(input("How many dimes?:"))
        Nickels = int(input("How many nickels?:"))
        Pennies = int(input("How many pennies?:"))
        user_income = (Quarters / 4) + (Dimes / 10) + (Nickels / 20) + (Pennies / 100)
        if user_income < Price:
            print(f"insufficient Balance!! Kindly take back your money : {user_income}")
        else:
            print(f"Here is {user_income - Price} in change.")
            print("Here is your espresso ☕ Enjoy!")
            water -= 200
            Coffee -= 24
            Milk -= 150
            Money += Price


def cappuccino():
    Price = 3.00
    global water
    global Milk
    global Coffee
    global Money
    if water < 250:
        print("Sorry, there is not enough water!")
    elif Coffee < 24:
        print("Sorry, there is not enough coffee!")
    elif Milk < 100:
        print("Sorry, there is not enough Milk!")
    else:
        print("Please insert coins.")
        Quarters = int(input("How many quarters?:"))
        Dimes = int(input("How many dimes?:"))
        Nickels = int(input("How many nickels?:"))
        Pennies = int(input("How many pennies?:"))
        user_income = (Quarters / 4) + (Dimes / 10) + (Nickels / 20) + (Pennies / 100)
        if user_income < Price:
            print(f"insufficient Balance!! Kindly take back your money : {user_income}")
        else:
            print(f"Here is {user_income - Price} in change.")
            print("Here is your espresso ☕ Enjoy!")
            water -= 250
            Coffee -= 24
            Milk -= 100
            Money += Price


machine = True
while machine:
    user = input("what would you like? (espresso/latte/cappuccino): ")

    if user == 'off':
        machine = False
    elif user == 'report':
        report()
    elif user == 'espresso':
        espresso()
    elif user == 'latte':
        latte()
    elif user == 'cappuccino':
        cappuccino()
    else:
        print("Invalid Input!")