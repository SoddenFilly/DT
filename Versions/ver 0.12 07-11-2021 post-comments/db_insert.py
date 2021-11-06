from marketprice import fetch_db # Gives access to the fetch_db() function in marketprice.py
import sqlite3 # Database handling

def db_insert(data, db_directory): # This function handles everything to do with inserting data into the database, takes in the data to be inserted and the storage location of the desired database

    db_connection = sqlite3.connect(db_directory)
    cursor = db_connection.cursor()

    cursor_res = cursor.execute(f"SELECT * FROM crypto WHERE c_symbol = '{data['symbol']}' ") .fetchall() # Querys the database for any data matching the users given symbol

    if cursor_res == []: # Data returns as [] if no data is found when querying the database, if nothing is found this means that it is safe to inject the data

        print("Inserting fetched data into database...\n>Inserted.")
        
    else: # If data is found then the symbol already exists in the database

        inp = input(f"{data['slug']}/{data['symbol']} already exists in this database, do you want to update it? (y/n) : ") # informative error message
        
        if inp != "y": # if user wants to leave the data as is then the function is cut short and moves on to the next user provided symbol (if any)

            print("Abandoning fetched data...\n>Abandoned.\n")
            return

        else: # if user wants to update the data then the function continues

            print("Inserting fetched data into database...\n>Inserted.\n")

    try: # Purges all data paired with the respective symbol from the database
        delete_id = cursor_res[0][0]

        cursor.execute(f"DELETE FROM crypto WHERE id = '{delete_id}' ")
        cursor.execute(f"DELETE FROM history WHERE c_id = '{delete_id}' ")
    except: # This should theoretically never fire
        print("\nFailed to delete data or data did not exist to be deleted\n")

    sql = "INSERT INTO crypto (c_slug,c_symbol) VALUES (?, ?)"
    insertdata = [ data['slug'], data['symbol'] ]
    
    cursor.execute(sql, insertdata) # Inserts symbol data into the crypto table in the database

    coin_id = cursor.lastrowid # Gets the id of the symbol in the crypto table to act as a pointer for the data in the history table in the database

    for i in range(len(data['price'])): # loops through all the available prices for the last 33 months

        sql = "INSERT INTO history (c_id,h_price,h_price_high,h_price_low,h_volume,h_date,h_timestamp) VALUES (?,?,?,?,?,?,?)"
        insertdata = [ coin_id, data['price'][i], data['price_high'][i], data['price_low'][i], data['volume'][i], data['date'][i], data['timestamp'][i] ]
        
        cursor.execute(sql, insertdata) # Inserts the symbols history data into the history table with a reference to the relevant symbol in the crypto table in the database
        
    db_connection.commit()

if __name__ == "__main__": # Only fires if this file was executed independantly

    db_directory = "database.db" # Where the database is stored locally

    symbol = input("Crypto symbol(s) - if loading multiple seperate each one with a single space ( eg: btc sol xrp eth ).\n! There is a limit of 5 every 20 seconds.\n: ").upper().split(" ") # Receives one or more symbols from the user to search and insert into the database
    
    if len(symbol) > 5: # Stops the user from going over the request-limit enforced by Alpha-vantage as each seperate symbol is a request in itself

        print(f"Remember the limit is 5, you tried {len(symbol)}!")

    else:

        print() # Visual formatting

        for url_symbol in symbol: # Loops through each of the provided crypto symbols provided by the user

            print("Fetching data for: " + url_symbol)

            data = fetch_db(url_symbol, "USD") # Gets the actual data for the current symbol from marketprice.py

            if data != "failed": # If all went well:
                
                db_insert(data, db_directory) # This injects the returned data into the database

            