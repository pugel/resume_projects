#Restaurant Object Oriented Program
meals_dict_global = {"Chicken Salad Sandwich": 3, "Turkey Sandwich": 4, \
                    "Asparagus Soup": 4, "Tortilla Soup": 3, "Harvest Salad": 4}
meals_cost_dict = {"Chicken Salad Sandwich": 7, "Turkey Sandwich": 7, \
                    "Asparagus Soup": 5, "Tortilla Soup": 5, "Harvest Salad": 6}

class Customer():
    """This class lets the customer order and calculates the amount they need to pay
        It will print out what they ordered and how much they owe.
        The code removes what the customer orders from the kitchen inventory."""

    def __init__(self):
        self.food_total_dict = {}

    #This method allows the customer to order food that is on the menu and keeps track of their order
    #If something is typed in wrong, or is not an option, then a message will flash and the user will be prompted again
    def order(self):
        loop = 0
        while loop == 0:
            ki = Kitchen_Inventory()
            loop_2 = 0
            while loop_2 == 0:
                number = input("What would you like to order? Type the number correlating to the dish: ")
                if number not in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
                    print("Please select a number from the available dishes above")
                else:
                    food = ki.link_food_with_number(number)
                    loop_2 = 1
            if ki.check(food) == True:
                self.food_total_dict[food] = 1
                loop = 1
                ki.remove_order(food, 1)
            else:
                print("I'm sorry, we are either out of that or it was typed in wrong, please select something else")
        loop_4 = 0
        keep_going = "yes"
        while keep_going != "quit" and number != "quit" and loop_4 == 0:
            keep_going = input("Would you like to eat anything else? Yes or No? ").lower()
            if keep_going == "yes":
                loop_3 = 0
                while loop_3 == 0:
                    number = input("What would you like to order? ").lower()
                    if number not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "quit"):
                        print("Please select a number from the available dishes above")
                    elif number == "quit":
                        loop_3 = 1
                    else:
                        food = ki.link_food_with_number(number)
                        loop_3 = 1
                food = ki.link_food_with_number(number)
                if ki.check(food) == True and number != "quit":
                    if food in self.food_total_dict:
                        self.food_total_dict[food] += 1
                        ki.remove_order(food, 1)
                    else:
                        self.food_total_dict[food] = 1
                        ki.remove_order(food, 1)
                elif number == "quit" or keep_going == "quit":
                    keep_going = "quit"
                else:
                    print("I'm sorry, we are either out of that or it was typed in wrong, please select something else")
            elif keep_going == "quit":
                loop_4 = 1
            elif keep_going == "no":
                loop_4 = 1
            else:
                print("Please select either Yes or No")
        if keep_going != "quit" or number != "quit":
            print("Your order is: ")
            print(self.food_total_dict)
            return self.food_total_dict

class Kitchen_Inventory():
    """This class keeps track of the Kitchen Inventory, it lets the owner remove
        and add dishes to the menu. This class also have functions to remove and
        check food based on what it ordered/stolen. This class also has a
        function to update the printed menu with what is in stock.
        Lastly, this class turns all the food items into a number to order"""

    def __init__(self):
        pass

    #this method removes one from a certain item that was either purchased or stolen
    def remove_order(self, bought_item, amount_item):
        meals_dict_global[bought_item] -= amount_item

    #This method lets the owner remove item from the kitchen inventory
    def remove(self):
        ki = Kitchen_Inventory()
        print("Your current menu is below:")
        ki.print_menu()
        loop_1 = 0
        while loop_1 == 0:
            loop_2 = 0
            while loop_2 == 0:
                number = input("What item would you like to remove?: Type the number correlating to the dish: ")
                if number not in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
                    print("Please select a number from the available dishes above")
                else:
                    remove_item = ki.link_food_with_number(number)
                    loop_2 = 1
            if ki.check(remove_item) == False:
                print("That item is not in the inventory or is already at 0")
            elif ki.check(remove_item) == True:
                loop_1 = 1
                loop_2 = 0
                while loop_2 == 0:
                    remove_amount = input("How much of this item would you like to remove?: ")
                    if remove_amount not in ("1", "2", "3", "4", "5", "6", "7",\
                                                "8", "9", "0"):
                        print("Please enter a number")
                    elif remove_amount in ("1", "2", "3", "4", "5", "6", "7", \
                                            "8", "9", "0"):
                        loop_2 = 1
                        if meals_dict_global[remove_item] < int(remove_amount):
                            print("There is not that much in inventory for " + \
                                    remove_item)
                        else:
                            meals_dict_global[remove_item] -= int(remove_amount)
        keep_going = "yes"
        while keep_going != "no":
            keep_going = input("Would you like to remove something else? Yes or No?")
            if keep_going == "yes":
                loop_2 = 0
                while loop_2 == 0:
                    number = input("What item would you like to remove?: Type the number correlating to the dish: ")
                    if number not in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
                        print("Please select a number from the available dishes above")
                    else:
                        remove_item = ki.link_food_with_number(number)
                        loop_2 = 1
                if ki.check(remove_item) == False:
                    print("That item is not in the inventory")
                elif ki.check(remove_item) == True:
                    loop_2 = 0
                    while loop_2 == 0:
                        remove_amount = input("How much of this item would you like to remove?: ")
                        if remove_amount not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
                            print("Please enter a number")
                        elif remove_amount in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
                            loop_2 = 1
                            if meals_dict_global[remove_item] < int(remove_amount):
                                print("There is not that much in inventory for " + remove_item)
                            else:
                                meals_dict_global[remove_item] -= int(remove_amount)
            elif keep_going == "no":
                keep_going = "no"
            else:
                print("Please select either yes or no")
        print("Your Inventory is now: ")
        print(meals_dict_global)

    #This method lets the owner add items to the kitchen inventory
    def add(self):
        ki = Kitchen_Inventory()
        print("Your current menu is below:")
        ki.print_menu()
        add_item = input("What item would you like to add?: ")
        if ki.check(add_item) == False:
            loop_1 = 0
            while loop_1 == 0:
                amount_item = input("What is the amount of this item?: ")
                if amount_item not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
                    print("Please enter a number")
                elif amount_item in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
                    meals_dict_global[add_item] = int(amount_item)
                    loop_1 = 1
                    if add_item not in meals_cost_dict:
                        loop_2 = 0
                        while loop_2 == 0:
                            cost_item = input("What will be the cost of this item?")
                            if cost_item not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
                                print("Please enter a number")
                            elif cost_item in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
                                meals_cost_dict[add_item] = int(cost_item)
                                loop_2 = 1
        elif ki.check(add_item) == True:
            loop_2 = 0
            while loop_2 == 0:
                amount_item = input("What is the amount of this item?: ")
                if amount_item not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
                    print("Please enter a number")
                elif amount_item in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
                    loop_2 = 1
                    previous_amount = meals_dict_global[add_item]
                    meals_dict_global[add_item] = int(amount_item) + previous_amount
        keep_going = "yes"
        while keep_going == "yes":
            loop = 0
            while loop == 0:
                keep_going = input("Would you like to add something else? Yes or No?: ").lower()
                if keep_going == "yes":
                    loop = 1
                    add_item = input("what item would you like to add?: ").lower()
                    if ki.check(add_item) == False:
                        loop_3 = 0
                        while loop_3 == 0:
                            amount_item = input("What is the amount of this item?: ")
                            if amount_item not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
                                print("Please enter a number")
                            elif amount_item in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
                                meals_dict_global[add_item] = int(amount_item)
                                loop_3 = 1
                                if add_item not in meals_cost_dict:
                                    loop_4 = 0
                                    while loop_4 == 0:
                                        cost_item = input("What will be the cost of this item?")
                                        if cost_item not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
                                            print("Please enter a number")
                                        elif cost_item in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
                                            meals_cost_dict[add_item] = int(cost_item)
                                            loop_4 = 1
                    elif ki.check(add_item) == True:
                        loop_5 = 0
                        while loop_5 == 0:
                            amount_item = input("What is the amount of this item?: ")
                            if amount_item not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
                                print("Please enter a number")
                            elif amount_item in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):
                                previous_amount = meals_dict_global[add_item]
                                meals_dict_global[add_item] = int(amount_item) + previous_amount
                elif keep_going == "no":
                    loop = 1
                    print("Your Inventory is now: ")
                    print(meals_dict_global)
                else:
                    print("Please type either yes or no: ")

    #This method prints all the food items that are available for purchase from the customer
    def print_menu(self):
        print('          ')
        print("----Welcome To Mikayla's Cusine----")
        print("The food we have available for lunch is listed below:")
        print("                    ")
        count = 1
        while count < len(meals_dict_global):
            for item in meals_dict_global:
                if int(meals_dict_global[item]) > 0:
                    print("[" + str(count) + "]" + item)
                    count += 1
                elif int(meals_dict_global[item]) == 0:
                    print("[" + str(count) + "]" + item + " - Temporarily Sold Out")
                    count += 1
        print("   ")

    #This method checks if a food item is currently on the menu
    def check(self, check_food):
        all_food_items = meals_dict_global.keys()
        if check_food in all_food_items:
            if meals_dict_global[check_food] > 0:
                return True
            else:
                return False
        else:
            return False

    #The method lets the owner check their inventory to see how much of which items they have
    def check_answer_owner(self):
        ki = Kitchen_Inventory()
        print("Your current menu is below:")
        ki.print_menu()
        loop_1 = 0
        while loop_1 == 0:
            check_item_number = input("What item would you like to check? Please select a number: ")
            if check_item_number not in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
                print("Please select a number from the available dishes above")
            else:
                check_item = ki.link_food_with_number(check_item_number)
                loop_1 = 1
        all_food_items = meals_dict_global.keys()
        if check_item in all_food_items:
            if meals_dict_global[check_item] == 0:
                print("You have zero of that food in inventory")
            elif meals_dict_global[check_item] >= 1:
                print("You have " + str(meals_dict_global[check_item]) + " of  " + check_item + " in the inventory")
        else:
            print(check_item + "is not a dish your restaurant makes")
        keep_going = "yes"
        while keep_going != "no":
            keep_going = input("Would you like to check something else? Yes or No? ").lower()
            if keep_going == "yes":
                loop_2 = 0
                while loop_2 == 0:
                    check_item_number = input("What item would you like to check? Please select a number: ")
                    if check_item_number not in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
                        print("Please select a number from the available dishes above")
                    else:
                        check_item = ki.link_food_with_number(check_item_number)
                        loop_2 = 1
                if check_item in all_food_items:
                    if meals_dict_global[check_item] == 0:
                        print("You have zero of that food in inventory")
                    elif meals_dict_global[check_item] >= 1:
                        print("You have " + str(meals_dict_global[check_item]) + " of " + check_item + " in the inventory")
                else:
                    print(check_item + " is not a dish your restaurant makes")
            elif keep_going == "no":
                keep_going = "no"
            else:
                print("Please select either yes or no")

    #This method links the food item with a number when ordering
    def link_food_with_number(self, food_order):
        count = 1
        while count <= len(meals_dict_global.keys()):
            for item in meals_dict_global.keys():
                if count == int(food_order):
                    return item
                    break
                else:
                    count += 1

class Profits():
    """This class helps the owner calculate the total amount of money they made.
        Also this class calculates what the customer owes when they order."""

    def __init__(self):
        self.total = 0

    #This method lets the owner calculate total income from different meals sold
    def total_meals(self):
        print(" ")
        print("Your inventory is printed below")
        print(meals_dict_global)
        loop_1 = 0
        while loop_1 == 0:
            item_sold = input("What item did you sell?: ")
            if item_sold not in meals_dict_global:
                print("That item is not in your inventory")
            else:
                self.total += meals_cost_dict[item_sold]
                loop_1 = 1
        keep_going = "yes"
        while keep_going != "no":
            keep_going = input("Did you sell anything else? Yes or No? ")
            if keep_going == "yes":
                loop_2 = 0
                while loop_2 == 0:
                    another_item_sold = input("What other item did you sell? ")
                    if another_item_sold not in meals_dict_global:
                        print("That item is not in your inventory")
                    else:
                        self.total += meals_cost_dict[another_item_sold]
                        loop_2 = 1
            elif keep_going == "no":
                keep_going = "no"
            else:
                print("Please select either yes or no")
        print("your total is " + "$" + str(self.total))

    #The method calculates how much the customer owes for the food they are buying
    def calculate_customer_cost(self, full_order_list_dict):
        total_cost = 0
        for key in full_order_list_dict.keys():
            total_cost += meals_cost_dict[key]*full_order_list_dict[key]
        print("and your total comes to $" + str(total_cost))

class Thief():
    """This method allows a theif to come into the store and steal any food in the inventory"""

    def __init__(self):
        self.stolen_goods_dict = {}

    #This method lets the thief steal items from the menu that are in inventory
    def steal(self):
        ki = Kitchen_Inventory()
        loop_2 = 0
        while loop_2 == 0:
            steal_number = input("You can steal anything on the menu, what would you like to steal? Please select a number: ")
            if steal_number not in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
                print("Please select a number from the available dishes above")
            else:
                steal_item = ki.link_food_with_number(steal_number)
                loop_2 = 1
        if ki.check(steal_item) == True:
            self.stolen_goods_dict[steal_item] = 1
            ki.remove_order(steal_item, 1)
        elif steal_item != "quit":
            print("That is not available to steal")
        keep_going = "yes"
        while keep_going != "no" and keep_going != "quit" and steal_item != "quit":
            keep_going = input("Would you like to try to steal something else? Yes or No? ").lower()
            if keep_going == "yes":
                loop_2 = 0
                while loop_2 == 0:
                    steal_number = input("What would you like to steal? Please select a number ")
                    if steal_number not in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
                        print("Please select a number from the available dishes above")
                    else:
                        steal_item = ki.link_food_with_number(steal_number)
                        loop_2 = 1
                if ki.check(steal_item) == True:
                    self.stolen_goods_dict[steal_item] = 1
                    ki.remove_order(steal_item, 1)
                elif steal_item == "quit" or keep_going == "quit":
                    keep_going = "quit"
                else:
                    print("That is not available to steal")
            elif keep_going != "no" and keep_going != "yes" and keep_going != "quit":
                print("Please select yes or no or type quit to quit")
        if keep_going == "no" and keep_going != "quit" and steal_item != "quit":
            print("You successfully stole ")
            print(self.stolen_goods_dict)

class User_Inputs():
    """This class runs the store and takes in different user inputs"""

    def __init__(self):
        pass

    #This method runs the user input:
        #There are 3 types of people the user can choose from: Owner, Customer, Thief
        #The Owner can add, check or remove items from the inventory as well as calculate total income
        #The customer can order food and check out
        #The Thief can steal items from the menu
    def run_store(self):
        ki = Kitchen_Inventory()
        loop_1 = 0
        while loop_1 == 0:
            person = input("Owner, Customer, or Thief? Type quit to end: ").lower()
            if person == "owner":
                loop_2 = 0
                while loop_2 == 0:
                    action = input("Would you like to see the inventory or calculate profits? Type i for inventory or c for calculate: ").lower()
                    if action == "i":
                        loop_3 = 0
                        loop_2 = 1
                        while loop_3 == 0:
                            action_inv = input("would you like to add, check, or remove inventory? ")
                            if action_inv == "add":
                                ki.add()
                                loop_3 = 1
                            elif action_inv == "check":
                                ki.check_answer_owner()
                                loop_3 = 1
                            elif action_inv == "remove":
                                ki.remove()
                                loop_3 = 1
                            elif action_inv == "quit":
                                loop_1 = 1
                                loop_2 = 1
                                loop_3 = 1
                            else:
                                print("Please choose either add, check, or remove")
                    elif action == "c":
                        loop_2 = 1
                        p = Profits()
                        p.total_meals()
                    elif action == "quit":
                        loop_1 = 1
                    else:
                        print("Please type in either inventory or calculate profits")
            elif person == "customer":
                ki.print_menu()
                c = Customer()
                person_order = c.order()
                p = Profits()
                p.calculate_customer_cost(person_order)
            elif person == "thief":
                ki.print_menu()
                t = Thief()
                t.steal()
            elif person == "quit":
                loop_1 = 1
            else:
                print("Please input either Owner, Customer or Thief")
                print("If you would like to quit, type in quit")

ui = User_Inputs()
ui.run_store()
