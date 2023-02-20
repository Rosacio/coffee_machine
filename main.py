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


def process_amount(cent1, cent5, cent20, cent50):
    payment = cent1 * 0.01 + cent5 * 0.05 + cent20 * 0.20 + cent50 * 0.50
    return payment


def refilled(wat, mil, cof):
    supplies["water"] += wat
    supplies["coffee"] += mil
    supplies["milk"] += cof


def supplies_used(wat, mil, cof):
    supplies["water"] -= wat
    supplies["coffee"] -= mil
    supplies["milk"] -= cof


supplies = {"water": 300, "milk": 200, "coffee": 100}
coins = {"1cent": 0, "10cent": 0, "20cent": 0, "50cent": 0}
money = 0.0
isOn = True
while isOn:
    question = input("What would you like? (espresso/latte/cappuccino):").lower()
    if question == "off":
        isOn = False
    elif question == "espresso":
        if MENU["espresso"]["ingredients"]["water"] > supplies["water"]:
            print("There isn't enough water, come in later please")
        elif MENU["espresso"]["ingredients"]["coffee"] > supplies["coffee"]:
            print("There isn't enough coffee, come in later please")
        else:
            print(f"Your drink costs {MENU['espresso']['cost']} ")
            print("Please insert your payment")
            cent1 = int(input("Amount of 1 cent coins:"))
            cent5 = int(input("Amount of 5 cent coins:"))
            cent20 = int(input("Amount of 20 cent coins:"))
            cent50 = int(input("Amount of 50 cent coins:"))
            payment = process_amount(cent1,cent5,cent20,cent50)
            if payment == MENU["espresso"]["cost"]:
                money += process_amount(cent1, cent5, cent20, cent50)
                print("Enjoy your drink!")
                supplies_used(MENU["espresso"]["ingredients"]["water"], MENU["espresso"]["ingredients"]["coffee"],
                              MENU["espresso"]["ingredients"]["milk"])
            elif payment > MENU["espresso"]["cost"] and payment - money > 0:
                change = payment - MENU["espresso"]["cost"]
                money += payment
                money -= change
                print(f"Here is your change: {round(change,2)}$")
                print("Enjoy your drink!")
                supplies_used(MENU["espresso"]["ingredients"]["water"], MENU["espresso"]["ingredients"]["coffee"],
                              MENU["espresso"]["ingredients"]["milk"])
            else:
                print("You have not inserted enough money")
    elif question == "latte":
        if MENU["latte"]["ingredients"]["water"] > supplies["water"]:
            print("There isn't enough water, come in later please")
        elif MENU["latte"]["ingredients"]["coffee"] > supplies["coffee"]:
            print("There isn't enough coffee, come in later please")
        elif MENU["latte"]["ingredients"]["milk"] > supplies["milk"]:
            print("There isn't enough milk, come in later please")
        else:
            print(f"Your drink costs {MENU['latte']['cost']} ")
            print("Please insert your payment")
            cent1 = int(input("Amount of 1 cent coins:"))
            cent5 = int(input("Amount of 5 cent coins:"))
            cent20 = int(input("Amount of 20 cent coins:"))
            cent50 = int(input("Amount of 50 cent coins:"))
            payment = process_amount(cent1, cent5, cent20, cent50)
            if payment == MENU["latte"]["cost"]:
                money += process_amount(cent1, cent5, cent20, cent50)
                print("Enjoy your drink!")
                supplies_used(MENU["latte"]["ingredients"]["water"], MENU["latte"]["ingredients"]["coffee"],
                              MENU["latte"]["ingredients"]["milk"])
            elif payment > MENU["latte"]["cost"] and payment - money > 0:
                change = payment - MENU["latte"]["cost"]
                money += payment
                money -= change
                print(f"Here is your change: {round(change, 2)}$")
                print("Enjoy your drink!")
                supplies_used(MENU["latte"]["ingredients"]["water"], MENU["latte"]["ingredients"]["coffee"],
                              MENU["latte"]["ingredients"]["milk"])
            else:
                print("You have not inserted enough money")
    elif question == "cappuccino":
        if MENU["cappuccino"]["ingredients"]["water"] > supplies["water"]:
            print("There isn't enough water, come in later please")
        elif MENU["cappuccino"]["ingredients"]["coffee"] > supplies["coffee"]:
            print("There isn't enough coffee, come in later please")
        elif MENU["cappuccino"]["ingredients"]["milk"] > supplies["milk"]:
            print("There isn't enough milk, come in later please")
        else:
            print(f"Your drink costs {MENU['cappuccino']['cost']} ")
            print("Please insert your payment")
            cent1 = int(input("Amount of 1 cent coins:"))
            cent5 = int(input("Amount of 5 cent coins:"))
            cent20 = int(input("Amount of 20 cent coins:"))
            cent50 = int(input("Amount of 50 cent coins:"))
            payment = process_amount(cent1, cent5, cent20, cent50)
            if payment == MENU["cappuccino"]["cost"]:
                money += process_amount(cent1, cent5, cent20, cent50)
                print("Enjoy your drink!")
                supplies_used(MENU["cappuccino"]["ingredients"]["water"], MENU["cappuccino"]["ingredients"]["coffee"],
                              MENU["cappuccino"]["ingredients"]["milk"])
            elif payment > MENU["cappuccino"]["cost"] and payment - money > 0:
                change = payment - MENU["cappuccino"]["cost"]
                money += payment
                money -= change
                print(f"Here is your change: {round(change, 2)}$")
                print("Enjoy your drink!")
                supplies_used(MENU["cappuccino"]["ingredients"]["water"], MENU["cappuccino"]["ingredients"]["coffee"],
                              MENU["cappuccino"]["ingredients"]["milk"])
            else:
                print("You have not inserted enough money")
    elif question == "report":
        for key in supplies:
            if key != "coffe":
                print(f"{key}:{supplies[key]}mg")
            else:
                print(f"{key}:{supplies[key]}g")
        print(f"Money:{money}$")
    elif question == "refill":
        refill_water = int(input("Water: "))
        refill_coffee = int(input("Coffee: "))
        refill_milk = int(input("Milk: "))
        refilled(refill_water, refill_coffee, refill_milk)

    else:
        print("Please insert a valid option")
