import db_connector
import read_expenses

DATABASE_NAME = "cost_management.db"
mysql_db1 = db_connector.connectDB(DATABASE_NAME)

def add_new_expense():
    user_input_item = input("Name of the expense: ")
    user_input_item = user_input_item.lower()
    user_input_cost = input("Enter the cost: ")
    while user_input_cost.isdigit() == False:           # .isdigit() works only on strings. it checks whether a given input is turnable into an integer or not.
        print("Your input is based on lies. Try over again, this time with a number.")
        user_input_cost = input("Enter the cost: ")
    user_input_date = input("Enter the date of purchase: ")
    query2 = f"INSERT INTO expense_records (item, cost, date_time) VALUES ('{user_input_item}', {user_input_cost}, '{user_input_date}')"
    mysql_db1.save_data(query2)
    print("Your data has been safed. Would you like to add another expense? (Yes or No) ")
    user_input = input("")
    user_input = user_input.lower()
    if user_input == "yes":
        add_new_expense()
    elif user_input == "no":
        print("Would you like to turn back to the menu? (yes/no) ")
        user_input = input("")
        user_input = user_input.lower()
        if user_input == "yes":
            expense_management_menu()
        elif user_input == "no":
            print("Would you like to exit the application? (yes/no) ")
            user_input = input("")
            user_input = user_input.lower()
    else:
        print("......")



def delete_an_expense():
    user_input_item = input("What item would you like to delete?: ")
    user_input_item = user_input_item.lower()
    fetched_items = [x[0].lower() for x in read_expenses.check_all_expenses()]
    print(fetched_items)
    if user_input_item in fetched_items:
        query4 = f"DELETE FROM expense_records WHERE item='{user_input_item}'"
        status = mysql_db1.save_data(query4)
        if status == 1:
            print("The item has been deleted")
        else:
            print("no success")
    else:
        print("The item is not in the record.")
    user_input = input("Would you like to delete another item? \nEnter yes or no: ")
    user_input = user_input.lower()
    if user_input == "yes":
        delete_an_expense()
    elif user_input == "no":
        user_input = input("Do you want to go back to the menu? (yes or no): ")
        user_input = user_input.lower()
        if user_input == "yes":
            read_expenses.expense_record_menu()
        else:
            return
    if user_input == "yes":
        delete_an_expense()



def expense_management_menu():
        print("")
        print("What would you like to do?\n1. Add a new expense \n2. Delete an existing expense \n3. Update an existing expense\n4. Back to main menu")
        try:
            user_input = int(input("Enter your choice (input must be a number): "))
        except:
            user_input = 0
        if user_input == 1:
            add_new_expense()
        elif user_input == 2:
            delete_an_expense()
        elif user_input == 3:
            update_expense()
        # elif user_input == 4:
        #     # expense_record_menu() ???????????????????????????????????????????????????????
        # else:
        #     print("Please enter a valid input.")



def update_expense():
    print("")
    user_input = input("Enter the name of the item you wanna bring changes to: ")
    user_input = user_input.lower()
    fetch_the_items = [x[0].lower() for x in read_expenses.check_all_expenses()]
    if user_input in fetch_the_items:
        choice_of_update()
    else:
        print("The entered item does not excist in the list.")
        user_input = input("Do you want to have a look at it again? (yes or no): ")
        user_input = user_input.lower()
        if user_input == "yes":
            update_expense()
        elif user_input == "no":
            user_input = input("Would you like to go back to the expense record menu? (yes or no): ")
            user_input = user_input.lower()
            if user_input == "yes":
                read_expenses.expense_record_menu()
            


def choice_of_update():
    print("")
    print("What would you exactly like to change?\n1.The item itself \n2. The cost of the item \n3. The date of the item")
    try:
        user_input = int(input("Enter your choice (input must be a number): "))
    except:
        user_input = 0
    if user_input == 1:
        user_input = input("To what would you like to change the current item?: ")
        updating_an_item()
    elif user_input == 2:
        print("Let the user change the cost")
    elif user_input == 3:
        print("let the user change the date")
    else:
        choice_of_update()



def updating_an_item():
    query5 = "UPDATE expense_records SET ..."
    return mysql_db1.save_data(query5)