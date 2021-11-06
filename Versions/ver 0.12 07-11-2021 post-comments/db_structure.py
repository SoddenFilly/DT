import sqlite3 # Database handling
import os # File handling (executing/deleting/etc other files)

def db_structure(db_struct, db_connection): # This function formats/structures an existant database file, takes in the location of the structure file and connection to the database file as parameters

    try:
        with open(db_struct) as struct: db_connection.executescript( struct.read() ) # This opens the database file and reads the structure from the structure file to it
        print("\n>>Database successfully structured") # Only fires if no errors occured

    except sqlite3.Error as err: print("Database failed to be structured.\n",err) # Error prevention
    
if __name__ == "__main__": # Only fires if this file was executed via command line or by similar means

    db_file = "database.db" # Database filename
    db_struct = "Resources/database_struct.sql" # File location of the sql file containing the database structure

    if os.path.isfile(db_file): # Checks if the database file already exists
        
        msg = input("\nThe database file already exists in this directory, if you intend to re-initialise this database, then proceed to input 'y'\nWARNING: This will permanently erase the current database, are you sure you want to proceed? (y/n): ").lower()
        if msg == "y" or msg =="yes": # User wants to replace current database file

            try: os.remove(db_file) # Deletes the current database file
            except: quit("\n>>Database file failed to be deleted\nSome other operation may be blocking this programs access to the file.\nPlease close out of any and all programs that may be interfering before proceeding with initialisation.\n\n>>Program terminated") # Error prevention, quits script
        
            db_connection = sqlite3.connect(db_file)
        
        else: # User doesnt actually want to replace current database file

            quit("\n>>Database deletion abort\n") # Quits script (if executed by another script then the other script will resume)
    
    else: db_connection = sqlite3.connect(db_file) # If database file does not already exist one is created immediately

    db_structure(db_struct,db_connection) # Structures database

    db_connection.commit() # Commits any changes made to the database

    print("\n>>Database structurization complete") # Final script endpoint