import db_connector
import read_expenses
import manage_expenses
import sharing_the_expenses
import help_center
import project_settings
import expense_statistics

DATABASE_NAME = "cost_management.db"
mysql_db1 = db_connector.connectDB(DATABASE_NAME)
query1 = "CREATE TABLE expense_records (item VARCHAR(50), cost INT, date_time DATE)"
try:
    mysql_db1.save_data(query1)
except:
    print("The table is already in existance.")



def expense_record_menu():
    print("What would you like to do?\n1. Check total expenses \n2. Manage expenses \n3. Share expenses \n4. Help \n5. Settings\n6. Expense statistics")
    
    expense_rec_dict = {1:read_expenses.check_all_expenses, 2: manage_expenses.expense_management_menu, 3: sharing_the_expenses.sharing_the_expenses, 4: help_center.help_menu, 5: project_settings.setting_menu, 6: expense_statistics.statistics_menu}

    try:
        user_input = int(input("Enter your choice (input must be a number): "))
    except:
        user_input = 0
    if user_input == 0:
        print("Please enter a valid choice.")
        expense_record_menu()
    expense_rec_dict[user_input]()
    print("")
    print("Would you like to see the menu again or to exit the application?\n1. Back to main menu\n2. Quit")
    try:
        user_input = int(input("Enter a number please: "))
    except:
        user_input = 0
    if user_input == 1:
        expense_record_menu()
    
        




expense_record_menu()