import sqlite3
from database import name_db
import pandas as pd

def login_user(login, password, interface):
    connect = sqlite3.connect(name_db)
    cursor = connect.cursor()

    sql_command = """SELECT * FROM {} WHERE email = ? and password = ?""".format('clients')

    cursor.execute(sql_command, (login, password))
    registers = cursor.fetchall()
    registers = pd.DataFrame(columns=['ID', 'name', 'email', 'password', 'age'], data= registers)
    if registers.shape[0] == 0:
        print('This user not exists')
    else:
        interface.destroy()
        print('Acess!')

    connect.commit()
    connect.close()