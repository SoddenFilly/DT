import sqlite3
import os
from marketprice import fetch_db

def db_insert(data, db_directory):

    db_connection = sqlite3.connect(db_directory)
    cursor = db_connection.cursor()

    cursor_res = cursor.execute(f"SELECT * FROM crypto WHERE c_symbol = '{data['symbol']}' ") .fetchall()

    if cursor_res == []:

        print("Inserting fetched data into database...\n>Inserted.")
        
    else:

        inp = input(f"{data['slug']}/{data['symbol']} already exists in this database, do you want to update it? (y/n) : ")
        
        if inp != "y":

            print("Abandoning fetched data...\n>Abandoned.\n")
            return

        else:

            print("Inserting fetched data into database...\n>Inserted.\n")

    try:
        delete_id = cursor_res[0][0]

        cursor.execute(f"DELETE FROM crypto WHERE id = '{delete_id}' ")
        cursor.execute(f"DELETE FROM history WHERE c_id = '{delete_id}' ")
    except:
        pass

    sql = "INSERT INTO crypto (c_slug,c_symbol) VALUES (?, ?)"
    insertdata = [ data['slug'], data['symbol'] ]
    
    cursor.execute(sql, insertdata)

    coin_id = cursor.lastrowid

    for i in range(len(data['price'])):

        sql = "INSERT INTO history (c_id,h_price,h_price_high,h_price_low,h_volume,h_date,h_timestamp) VALUES (?,?,?,?,?,?,?)"
        insertdata = [ coin_id, data['price'][i], data['price_high'][i], data['price_low'][i], data['volume'][i], data['date'][i], data['timestamp'][i] ]
        
        cursor.execute(sql, insertdata)
        
    db_connection.commit()

if __name__ == "__main__":

    db_directory = "database.db"

    while True:

        symbol = input("Crypto symbol(s) - if loading multiple seperate each one with a single space ( eg: btc sol xrp eth ).\n! There is a limit of 5 every 20 seconds.\n: ").upper().split(" ")
        
        if len(symbol) > 5:

            print(f"Remember the limit is 5, you tried {len(symbol)}!")

        else:

            print()

            for url_symbol in symbol:

                print("Fetching data for: " + url_symbol)

                data = fetch_db(url_symbol, "USD")

                if data != "failed":
                    
                    db_insert(data, db_directory)

            break