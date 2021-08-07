import sqlite3
import os
from marketprice import fetch_all

def db_insert(data):

    db_connection = sqlite3.connect("database.db")
    cursor = db_connection.cursor()

    cursor.execute(f"SELECT * FROM crypto WHERE c_symbol = '{data['symbol']}' ")
    cursor_res = cursor.fetchall()
    if cursor_res != []:
        inp = input(f"{data['slug']}/{data['symbol']} already exists in this database, do you want to update it? (y/n) : ")
        if inp != "y":
            return


    try:
        delete_id = cursor_res[0][0]
        print("cur", cursor_res, delete_id)
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

    if os.path.isfile("database.db") == False:
        quit("no db here")

    while True:
        symbol = input("Crypto symbol(s) - if loading multiple seperate each one with a single space ( eg: btc sol xrp eth ) there is a limit of 5 every 20 seconds : ").upper().split(" ")
        if len(symbol) > 5:
            print(f"Remember the limit is 5, you tried {len(symbol)}!")

        else:
            for url_symbol in symbol:
                print(url_symbol)
                data = fetch_all(url_symbol, "USD")
                # pprint(data)
                if data != "failed":
                    db_insert(data)
            break