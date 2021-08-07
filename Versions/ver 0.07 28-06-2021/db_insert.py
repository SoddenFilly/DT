import sqlite3
import os
from marketprice import fetch

db_file = "database.db"

def db_insert (cursor):
    # st = f"INSERT INTO history (h_price, h_price_high, h_price_low, h_volume, h_timestamp') VALUES ('{}')"
    st = f"INSERT INTO history (h_price) VALUES ('{price}')"
    print(st)
    cursor.execute(st)


if __name__ == "__main__":

    if os.path.isfile(db_file) == False:
        quit("no db here")
    
    db_connection = sqlite3.connect(db_file)

    cursor = db_connection.cursor()

    db_insert(cursor)

    fetch()



    
    