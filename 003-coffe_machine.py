from coffe_data import MENU, machine_resources

profit = 0
CURRENCY = "$"
machine_on = True
def get_menu_items():
    """" get all menu items from MENU """
    menu_items = [ item.capitalize() for item in MENU ]
    return "/".join(menu_items)

def get_machine_resources():
    """" printing the machine resources """
    for k, v in machine_resources.items():
        print(f"{k}: {v}")
    print(f"Profit: {profit}")


def get_flavour_ingredients(choice):
    """ get ingredients for your choice or flavour """
    ingredients = MENU[choice]['ingredients']
    return ingredients

def get_flavour_cost(choice):
    """ return selected flavour cost """
    flavour_cost = MENU[choice]['cost']
    return flavour_cost


def is_sufficient_resource_for_choice(choice, ingredients):
    global machine_on
    for item in machine_resources:
        if machine_resources[item] < ingredients[item]:
            print(f"Insufficient Resource {item} to make your slected flavour {choice}.")
            machine_on = False
            return False
    return True


def insert_coins():
    user_amount = 0
    money = {
        "one": 1,
        "five": 5,
        "ten": 10
    }
    
    for k, v in money.items():
        number = int(input(f"How many {k} Rs {CURRENCY}: "))
        user_amount += number * v
    return user_amount

def is_sufficient_fund_for_choice(choice, user_amount, flavour_cost):
    """ checking inserted amount is sufficient for flavour or not """
    if flavour_cost > user_amount:
        print(f"You inserted insufficient fund {user_amount}. Actual cost of flavour {choice} is Rs {CURRENCY}: {flavour_cost}")
        return False
    else:
        global profit
        balance_amount = 0
        
        if user_amount > flavour_cost:
            balance_amount = user_amount - flavour_cost
            print(f"Please collect your change Rs. {CURRENCY}:  {balance_amount}")
        profit += user_amount
        profit -= balance_amount
        return True

def make_coffe(choice, flavour_ingredients):
    """ making the your choice """
    for k,v in machine_resources.items():
        machine_resources[k] -= flavour_ingredients[k]
    print(f"Your choice {choice} is ready. Enjoy It !!")
             

def main():
    global machine_on
    while machine_on:
        flavours = [ flavour.lower() for flavour in get_menu_items().split("/") ]
        choice = input(f"What would you like to choose {get_menu_items()}: ").lower()
        if choice == 'off':
            machine_on = False
        elif choice == 'report':
            get_machine_resources()
        elif choice in flavours:
            print("Your slected choice is: {}".format(choice))
            flavour_cost = get_flavour_cost(choice)
            flavour_ingredients = get_flavour_ingredients(choice)
            if is_sufficient_resource_for_choice(choice, flavour_ingredients):
                user_amount = insert_coins()
                if is_sufficient_fund_for_choice(choice, user_amount, flavour_cost):
                    make_coffe(choice, flavour_ingredients)
        else:
            print("Invalid choice {}. Select either {} ".format(choice, " or ".join(flavours) ))
            

if __name__ == "__main__":
    main()