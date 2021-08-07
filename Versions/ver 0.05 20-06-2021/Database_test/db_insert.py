import sqlite3
import os

# hardcoded name of the database file
database_file = "database.db"
schema_file = "database.sql"

# -----------------------------------------------------------------------
# this function connects to the database
# if the database.db file doesn't exist then it creates the database 
# it returns the connection object if successful
def connect_db(database_file):
    
    db_connection = sqlite3.connect(database_file)

    return db_connection

# -----------------------------------------------------------------------
# this function creates the data schema (tables and columns) in the database. 
# It accepts the DB connection as a parameter
def structure_db(db_connection,schema_file):

    # going to default to success. if there's an issue then we'll change the message
    message = "Database successfully structured."
    successFlag = True

    try:
        # your database schema must live in a file in the same directory
        with open(schema_file) as schema:
            db_connection.executescript(schema.read())

    except sqlite3.Error as error:
        message = "Database failed to be structured.",error
        successFlag = False
    
    return message, successFlag

# -----------------------------------------------------------------------
# this function iterates through 
def populate_db(cursor):

    # going to default to success. if there's an issue then we'll change the message
    message = "Database successfully populated."
    successFlag = True

    # iterate through the entire datastore by key,value
    print(positions_c.items())
    for key, table_it in positions_c.items():

        print(table_it)

        print(key)

        # try to populate each row with a dictionary 'position'
        try:
            # cursor.execute(f"INSERT INTO crypto VALUES (c_slug, c_symbol)", [table_it["c_slug"], table_it["c_symbol"], ])
            # cursor.execute("INSERT INTO crypto (c_slug, c_symbol) VALUES ("+ table_it["c_slug"] +","+ table_it["c_symbol"] +")")
            st = "INSERT INTO crypto (c_slug, c_symbol) VALUES ('"+ table_it["c_slug"] +"','"+ table_it["c_symbol"] +"')"
            print(st)
            cursor.execute(st)

        # if something fails then change the message so we don't assume it worked
        except sqlite3.Error as error:
            message = "Database failed to populate.", error
            successFlag = False

    for key, table_it in positions_h.items():

        # print(position)

        # try to populate each row with a dictionary 'position'
        try:
            # cursor.execute(f"INSERT INTO history (c_id, h_price_usd, h_timestamp) VALUES ({table_it["c_id"]},{table_it["h_price"]},{table_it["h_timestamp"]})")
            cursor.execute("INSERT INTO history (c_id, h_price_usd, h_timestamp) VALUES ("+ table_it["c_id"] +","+ table_it["h_price"] +","+ table_it["h_timestamp"] +")")

        # if something fails then change the message so we don't assume it worked
        except sqlite3.Error as error:
            message = "Database failed to populate.", error
            successFlag = False
    
    return message, successFlag


# -----------------------------------------------------------------------
# procedural code belongs beneath this line
if __name__ == "__main__":


    # check if database already exists
    if os.path.isfile(database_file):

        # file = open(database_file)

        # if the database file is there then prompt to overwrite it
        # confirm = input("The database '"+database_file+"' already exists. Do you want to overwrite? (y/n): ")
        confirm = "y"

        if confirm == "y":

            try:
                # delete existing database file
                os.remove(database_file)
            except:
                print("Failed to delete the old database file. \nCheck that it isn't connected in another app (eg. SQLiteStudio) then run this script again.")
                quit()

            # call the function to either connect to or create the database
            db_connection = connect_db(database_file)

        else:
            print("Ok, then. Goodbye.")
            quit() 

    else:

        # if the database file doesn't exist then 
        # call the function to either connect to or create the database
        db_connection = connect_db(database_file)




    # create a cursor object to hold our place as we work within the database
    cursor = db_connection.cursor()
    
    # call the function to structure the database with schema (tables and columns)
    # we return two variables (message and successFlag)
    message, successFlag = structure_db(db_connection,schema_file)

    print(message)




    # only proceed if structuring was successful
    if successFlag == True:
        # send the cursor we just created and the datastore dictionary off to populate the database
        from datastore_str import positions_c # from a seperate file called data.py
        from datastore_str import positions_h # from a seperate file called data.py
        message, successFlag = populate_db(cursor)

        # visibility of system status
        print(message)

        # only commit to database if populating was successful
        # if successFlag == True and successFlag_h == True:

        db_connection.commit()
        print("Done!")


