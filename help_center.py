import db_connector

DATABASE_NAME = "cost_management.db"
mysql_db1 = db_connector.connectDB(DATABASE_NAME)

def help_menu():
    print("")
    print("What do you need help with? \n1. Contact \n2. How does it work? \n3. Data processing details")
    try:
        user_input = int(input("Please enter a number: "))
    except:
        while not user_input.isdigit():
            print("You screwed it bro, use a number.")
            help_menu()
    if user_input == 1:
        print("going to contact details...")
    elif user_input == 2:
        print("How does it work?...")
    elif user_input == 3:
        print("Data processing details...")

