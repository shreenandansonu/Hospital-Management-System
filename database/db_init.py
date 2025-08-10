import sqlite3 as sql3

# one time for creating database
def create_database():
    con = sql3.connect('database/hospital_management.db')
    con.commit()
    con.close()
    print("Database has been created at 'database/hospital_management.db' ")

def create_tables():




if __name__ == "__main__":
    create_database()