import db_connector

DATABASE_NAME = "cost_management.db"
mysql_db1 = db_connector.connectDB(DATABASE_NAME)

def check_all_expenses(print_results = True):           # we use a default argument within the parenticesis
    query3 = "SELECT * FROM expense_records"
    a = mysql_db1.get_data(query3)
    if(print_results == True):
        print(a)
    return a
