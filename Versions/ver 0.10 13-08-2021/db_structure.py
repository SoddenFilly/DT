import sqlite3
import os

def db_structure (db_struct, db_connection):

    try:
        with open(db_struct) as struct: db_connection.executescript(struct.read())
        print("\n>>Database successfully structured")
    except sqlite3.Error as err: print("Database failed to be structured.\n",err)
    
if __name__ == "__main__":

    db_file = "database.db"
    db_struct = "Resources/database_struct.sql"

    if os.path.isfile(db_file):
        
        msg = input("\nThe database file already exists in this directory, if you intend to re-initialise this database, then proceed to input 'y'\nWARNING: This will permanently erase the current database, are you sure you want to proceed? (y/n): ").lower()
        if msg == "y" or msg =="yes":

            try: os.remove(db_file)
            except: quit("\n>>Database file failed to be deleted\nSome other operation may be blocking this programs access to the file.\nPlease close out of any and all programs that may be interfering before proceeding with initialisation.\n\n>>Program terminated")
        
            db_connection = sqlite3.connect(db_file)
        
        else:

            quit("\n>>Database deletion abort\n")
    
    else: db_connection = sqlite3.connect(db_file)

    db_structure(db_struct,db_connection)

    db_connection.commit()

    print("\n>>Database structurization complete")