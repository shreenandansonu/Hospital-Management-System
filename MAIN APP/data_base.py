import sqlite3 as sq3

def create_user_db(name, password, email):
    
    con=sq3.connect('MAIN APP/user.db')
    cur=con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users (
                

                )''')
    cur.commit()
    cur.close()