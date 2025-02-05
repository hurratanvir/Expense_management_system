import sqlite3

class connectDB:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
    
    def get_data(self, query):                  # <-- Read the data SELECT
        cursor = self.conn.cursor()
        try:
            data = cursor.execute(query).fetchall()
            cursor.close()
            return data
        except:
            cursor.close()
            return "Error in query probably, recheck it"
    
    def save_data(self, query):                     # <-- writing data to the table INSERT, UPDATE, CREATE
        cursor = self.conn.cursor()
        try:
            cursor.execute(query)
            self.conn.commit()
            cursor.close()
            print("Executed")
            return 1
        except:
            cursor.close()
            return 0
        