import time
from menu import MENU
from menu import resources
from art import logo


profit = 0

def format_data(resource):
    """This function formats the dictionary to a readable format"""
    resource_water = resource["water"]
    resource_milk = resource["milk"]
    resource_coffee = resource["coffee"]
    return f"The machine's storage tanks filled with:\n{resource_water} ml water\n{resource_milk} ml milk\n{resource_coffee} g coffee"

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def coins():
    """This function stores the inserted coins"""
    print("Please insert your coins!")
    total = int(input("How many quarters?:\n")) * 0.25
    total += int(input("How many dimes?:\n")) * 0.1
    total += int(input("How many nickles?:\n")) * 0.05
    total += int(input("How many pennies?:\n")) * 0.01
    return total

def is_transaction_successful(money, cost):
    """Checks if the inserted money is enough"""
    if money >= cost:
        change = round(money - cost, 2)
        print(f"Here is ${change} in change:")
        global profit
        profit += cost
        return True
    else:
        print("!!! SORRY, THE INSERTED MONEY IS NOT ENOUGH !!!\nREFUND IN PROGRESS...")
        time.sleep(3)
        print("\n" * 50)
        return False

def operation():
    """Defines the complete operation of the machine"""
    is_operation_active = True
    is_turn_on = False
    program_finish = False
    # The first while loop last as long as the machine "plugged in"
    while not program_finish:
        # The 2nd while loop last as long as the machine "operation function called"
        while is_operation_active:
            machine_status = input("Machine is currently turned off... \n(Type 'ON' to turn it on)\n").lower()
            if machine_status == "on":
                is_turn_on = True
                print("\n" * 50)
            elif machine_status == "unplug":
                is_turn_on = False
                is_operation_active = False
                program_finish = True
            # The 3rd while loop lasts as long as the machine turned on
            while is_turn_on:
                print(logo)
                user_prompt = input("Welcome! What would you like to drink? (Espresso/Latte/Cappuccino): ").lower()
                # Here the service mode is defined:
                if user_prompt == "service":
                    is_service_active = True
                    while is_service_active:
                        print("\nWelcome to service mode!")
                        create_report = input("Do you want to create a report? 'Y' or 'N'\n").lower()
                        if create_report == "y":
                            print("Printing report...")
                            time.sleep(5)
                            print(format_data(resources))
                            print(f"Money in the machine: ${profit}")
                        else:
                            print("Service mode closing...")
                            time.sleep(5)
                            print("Service mode closed!")
                            is_service_active = False
                # Making of the espresso:
                elif user_prompt == "espresso":
                    can_make = True
                    for ingredient, amount in MENU["espresso"]["ingredients"].items():
                        if resources.get(ingredient, 0) < amount:
                            can_make = False
                            print(f"!!!ERROR!!! Not enough {ingredient}")
                    if can_make:
                        print(f"Espresso's price: ${MENU["espresso"]["cost"]}")
                        payment = coins()
                        if is_transaction_successful(payment, MENU["espresso"]["cost"]):
                            print("Preparing a warm espresso for you! Please be patient...")
                            for ingredient, amount in MENU["espresso"]["ingredients"].items():
                                if ingredient in resources:
                                    resources[ingredient] -= amount
                            time.sleep(10)
                            print("Your Espresso is ready. Enjoy!")
                            print("For next customer hit Enter...")
                            input()
                            print("\n" * 50)
                    else:
                        print("!!! SERVICE REQUIRED !!!")
                # Making of the latte:
                elif user_prompt == "latte":
                    can_make = True
                    for ingredient, amount in MENU["latte"]["ingredients"].items():
                        if resources.get(ingredient, 0) < amount:
                            can_make = False
                            print(f"!!!ERROR!!! Not enough {ingredient}")
                    if can_make:
                        print(f"Latte's price: ${MENU["latte"]["cost"]}")
                        payment = coins()
                        if is_transaction_successful(payment, MENU["latte"]["cost"]):
                            print("Preparing a warm milky Latte for you! Please be patient...")
                            for ingredient, amount in MENU["latte"]["ingredients"].items():
                                if ingredient in resources:
                                    resources[ingredient] -= amount
                            time.sleep(10)
                            print("Your Latte is ready. Enjoy!")
                            print("For next customer hit Enter...")
                            input()
                            print("\n" * 50)
                    else:
                        print("!!! SERVICE REQUIRED !!!")
                # Making of the cappucino:
                elif user_prompt == "cappuccino":
                    can_make = True
                    for ingredient, amount in MENU["cappuccino"]["ingredients"].items():
                        if resources.get(ingredient, 0) < amount:
                            can_make = False
                            print(f"!!!ERROR!!! Not enough {ingredient}")
                    if can_make:
                        print(f"Cappuccino's price: ${MENU["cappuccino"]["cost"]}")
                        payment = coins()
                        if is_transaction_successful(payment, MENU["cappuccino"]["cost"]):
                            print("Preparing a warm foamy Cappuccino for you! Please be patient...")
                            for ingredient, amount in MENU["cappuccino"]["ingredients"].items():
                                if ingredient in resources:
                                    resources[ingredient] -= amount
                            time.sleep(10)
                            print("Your Cappuccino is ready. Enjoy!")
                            print("For next customer hit Enter...")
                            input()
                            print("\n" * 50)
                    else:
                        print("!!! SERVICE REQUIRED !!!")
                # Turn off:
                elif user_prompt == "turn off":
                    is_turn_on = False
                    print("Turning OFF...")
                    time.sleep(10)
                    print("\n" * 50)
                # Unplug:
                elif user_prompt == "unplug":
                    is_turn_on = False
                    is_operation_active = False
                    program_finish = True

operation()
