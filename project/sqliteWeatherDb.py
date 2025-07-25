import sqlite3
from datetime import datetime
def createDb(dbName:str)->None:
    conn = sqlite3.connect(dbName+'.db')

    cursor = conn.cursor()
    try :
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS weather (
                city varchar(20) PRIMARY KEY,
                temp float NOT NULL,
                time date
            )
        ''')
    except Exception as e:
        print(f"error{e}")
    conn.commit()

def insertWeatherData(dbName:str,weatherData)->None:
    conn = sqlite3.connect(dbName+'.db')
    cursor = conn.cursor()
    try:
        for city in weatherData:
            print(city,weatherData[city])
            cursor.execute("INSERT INTO weather  VALUES (?, ?,?)", (city, weatherData[city],datetime.now()))
    except Exception as e:
        print(f"error occurred in db {e}")
    finally:
        #conn.commit()
        rows = cursor.execute('select * from weather')
        print(list(rows))
        conn.close()
        

