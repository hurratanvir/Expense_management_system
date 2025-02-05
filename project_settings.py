import db_connector
# import expense_management_system

DATABASE_NAME = "cost_management.db"
mysql_db1 = db_connector.connectDB(DATABASE_NAME)

def setting_menu():
    print( "What settings would you like to change?\n1. Background color\n2. Text color\n3. Fond size" )
    user_input = input("Please enter a number: ")
    while not user_input.isdigit():
        print("Enter only numbers please: ")
        setting_menu()
    user_input = int(user_input)
    if user_input == 1:
        print("going to background color options...")
    elif user_input == 2:
        print("Going to text colors...")
    elif user_input == 3:
        print("going to fond sizes...")
    else:
        print( "You should enter a number of 1,2 or 3.\nWould you like to try it again?\n""\nEnter 'yes' to try it again\nEnter 'no' to turn back to the main menu.")
        user_input = input("Enter your choice please: ")
        user_input.lower()
        if user_input == "yes":
            setting_menu()
        elif user_input == "no":
            expense_management_system.expense_record_menu()
        else:
            print("It is not a valid input. You will be redirected to the main menu.")
            expense_management_system.expense_record_menu()


              

    
    