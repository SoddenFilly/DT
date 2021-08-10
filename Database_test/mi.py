import sqlite3
import os

# hardcoded name of the database file
database_file = "database.db"
schema_file = "database.sql"

def connect_db(database_file):
    
    db_connection = sqlite3.connect(database_file)

    return db_connection

def populate_db(cursor,positions):

    # going to default to success. if there's an issue then we'll change the message
    message = "Database successfully populated."
    successFlag = True

    for key, table_it in positions_h.items():

        try:
            # cursor.execute(f"INSERT INTO history VALUES ('c_id', 'h_price', 'h_timestamp')", [5,  85000, 3827382738723])
            st = "INSERT INTO history (c_id, h_price_usd, h_timestamp) VALUES (4,3,8)"
            cursor.execute(st)

        except sqlite3.Error as error:
            message = "Database failed to populate.", error
            successFlag = False

    return message, successFlag

if __name__ == "__main__":
    
    db_connection = connect_db(database_file)
    cursor = db_connection.cursor()

    from datastore import positions_h # from a seperate file called data.py
    message_h, successFlag_h = populate_db(cursor,positions_h)

    # visibility of system status
    print(message_h)


    db_connection.commit()
    print("Done!") 