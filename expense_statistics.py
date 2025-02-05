import db_connector
import read_expenses

DATABASE_NAME = "cost_management.db"
mysql_db1 = db_connector.connectDB(DATABASE_NAME)

def statistics_menu():
    print("Welcome to the statistic menu. What statistics would you like to see?\n1. Cheapest/most expensive item\n2. Total average/median spent\n3. spent in 1 month / 3 months / 1 year")
    user_input = input("Please enter a number: ")
    while not user_input.isdigit():
        print("Please, enter a digit.")
    user_input = int(user_input)
    if user_input not in (1,2,3):
        print("Ur input was invalid. Please make a choice over again in the menu.")
        statistics_menu()
    elif user_input == 1:
        get_cheapest_most_expensive_item()
    elif user_input == 2:
        print("This is the average/median")
    elif user_input == 3:
        print("This is what you spent in a timeframe of 1 month,3months,1year.")



def get_cheapest_most_expensive_item():
    print("")
    print("Are you searching for the cheapest or most expensive item? (please enter a number)\n1. Cheapest\n2. Most expensive")
    try:
        user_input = int(input(""))
    except:
        user_input = 0
    if user_input == 1:
        print("")
        cheapest_item()
    if user_input == 2:
        print("")
        most_expensive_item()

def most_expensive_item():
    dict1 = {tpl[0] : tpl[1] for tpl in read_expenses.check_all_expenses(print_results=False)}
    highest_value = 0
    the_item = ""
    for k,v in dict1.items():
        if v > highest_value:
            highest_value = v
            the_item = k
    print(f"Your most expensive item is '{the_item}', with a price tag of: € {highest_value},-")
    return the_item, highest_value



def cheapest_item():
    dict2 = {tpl[0] : tpl[1] for tpl in read_expenses.check_all_expenses(print_results= False)}
    lowest_number = 700
    the_item = ""
    for k,v in dict2.items():
        if v < lowest_number:
            lowest_number = v
            the_item = k
    print(f"item: {the_item}, cost: € {lowest_number},-")
    return the_item ,lowest_number



statistics_menu()
    





# statistics of: cheapest/most expensive item, item-cost average, how much spent per month, how much spent in 3 months, how much spent per year
# median spent
# how much % spent for school/work, how much for groceries, how much for household goods etc. #v2
