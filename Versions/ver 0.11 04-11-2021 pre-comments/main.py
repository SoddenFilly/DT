from matplotlib import pyplot as plt # For graphing
import sqlite3 # Database handling
import os # For accessing other files

def DB_connect(db_directory): # Connects program to the database

    db_connection = sqlite3.connect(db_directory)
    cursor = db_connection.cursor()

    return cursor, db_connection

# Creates a simple overview of what state the program and database are in, takes in the param (loaded_data_status), this stores what currency has been selected from the database to be graphed, if none are selected it has a default of "empty"
def DB_status(loaded_data_status):

    if os.path.isfile(db_directory): # Checks if database file exists

        cursor, db_connection = DB_connect(db_directory)

        cursor.execute("SELECT * FROM crypto") # Gets list of all currency symbols from database
        
        database_total_currencies = len(cursor.fetchall()) # gets the list length of all currency symbols from database
        database_status = f"populated with {database_total_currencies} currencies"

        db_connection.close()

        return f"--------------------------------------------------.\nDatabase status: {database_status}\nCurrency selected for graphing: {loaded_data_status}", loaded_data_status, True

    return "No existing database file. Please initialise a new database (1).", "empty", False # returns if database file does not exist, the bool gets assigned to db_exist in Main() for further error prevention

# The main function used to run the "main menu" of the program, the access point to every other aspect of the program, takes in the params db_directory (directory where the database resides)
def Main(db_directory, loaded_data_status):

    while True:
 
        try:
            message, loaded_data_status, db_exist = DB_status(loaded_data_status)
            print(message)
        except Exception as err: # This should never have to fire
            print(err)
        
        try:
            task = int(input("\nWhat do you want to do?\n (1): New database\n (2): Add to database\n (3): Remove from database\n (4): List all currently stored coins\n (5): Load database data\n (6): Graph loaded data\n (7): Quit program\n: "))
            
            if task > 7 or task < 1:
                input("\n!!! Please input an integer within the range 1-7 (Press 'enter' to continue)\n")
            
        except:
            task = 0
            input("\n!!! Please input an integer within the range 1-7 (Press 'enter' to continue)\n")

        if task == 1: # New database

            os.system('python db_structure.py')

        elif task == 2 and db_exist == True: # Add to database

            os.system('python db_insert.py')

        elif task == 3 and db_exist == True: # Delete from database

            cursor, db_connection = DB_connect(db_directory)

            symbol = input("symbol: ") .upper()
            data = cursor.execute(f"SELECT * FROM crypto WHERE c_symbol = '{symbol}' ") .fetchall()
            
            if data == []: # Data returns as [] if no data is found when querying the database

                input(f"\n!!! Currency {symbol} does not currently exit within the database. (Press 'enter' to continue)\n")

            else:

                delete_id = data[0][0] # The '[0][0]' is needed to go from the returned data '([1, ?, ?])' to '1'
            
                cursor.execute(f"DELETE FROM crypto WHERE id = '{delete_id}' ")
                cursor.execute(f"DELETE FROM history WHERE c_id = '{delete_id}' ")

                db_connection.commit()

                print(f"\nCurrency {symbol} has been purged from database.")
            
            db_connection.close()

        elif task == 4 and db_exist == True: # List all currency's in database
            
            cursor, db_connection = DB_connect(db_directory)

            coins = cursor.execute(f"SELECT * FROM crypto") .fetchall()

            increment = 0
            for coin in coins: # Iterates through all currency's in database and prints them out with some additional information

                increment += 1
                print(str(increment) + ":", coin[2], "|", coin[1])
            
            db_connection.close()
            
            input("\n>>Press enter to continue ")

        elif task == 5 and db_exist == True: # Selects all the historic data for the provided currency

            cursor, db_connection = DB_connect(db_directory)

            symbol = input("symbol: ") .upper()

            currency_data = cursor.execute(f"SELECT * FROM crypto WHERE c_symbol = '{symbol}' ") .fetchall()

            if currency_data == []:

                input(f"\n!!! Currency {symbol} does not currently exit within the database. (Press 'enter' to continue)\n")
            
            else:
                raw_data = cursor.execute(f"SELECT * FROM history WHERE c_id = '{currency_data[0][0]}' ") .fetchall()

                graph_data_x, graph_data_y = [], [] # These are the x,y axis used when graphing
                for value in raw_data:

                    graph_data_x.append(value[6])
                    graph_data_y.append(value[2])

                loaded_data_status = currency_data[0][1]

                print(f"\nCurrency {symbol} loaded and ready to graph.")
            
            db_connection.close()

        elif task == 6 and db_exist == True: # Graphs selected data ( task 6 )

            if loaded_data_status == "empty": # Wont graph if no historic data is selected

                input("\n!!! No data is currently selected for graphing. (Press 'enter' to continue)\n")
            
            else:

                print("! Note that the graph window needs to be closed before proceeding with the program.")

                plt.figure(f"Price of {symbol} in USD over {len(graph_data_x)} months") # Name of graphing window

                plt.plot(graph_data_x, graph_data_y, label=f"Price of {symbol} in USD") # Injects selected data into graph and sets arbitrary values specific to this plotline
                # Graph settings
                plt.setp(plt.gca().get_xticklabels(), rotation=30, horizontalalignment='right') # Rotates dates on x-axis so they don't overlap
                plt.grid(color='grey', alpha=0.5, linewidth=1) # Adds a semi-visible grid to better see where values line up on the graph
                plt.subplots_adjust(bottom=0.15) # Fixes the bottom border of the graph slightly higher than default
                plt.ylabel("Prices Ascending") # Y-axis title
                plt.xlabel("Dates Acending") # X-axis title
                plt.gca().invert_xaxis() # Matplotlib atomatically inverts the x-axis based on the data, this reverses that
                plt.legend() # displays legend on graph

                try:
                    figManager = plt.get_current_fig_manager().window
                    figManager.state("zoomed") # Makes the graphing window always open in fullscreen
                except: # If first '("zoomed")' method fails
                    try:
                        figManager.showMaximized()
                    except:
                        print("\nProgram failed to open graph window in fullscreen mode, opened in the smaller windowed mode instead")

                plt.show() # Opens graphing window

        elif task == 7: # Quits program

            quit(">Program terminated\n")


if __name__ == "__main__":

    db_directory = "database.db"

    loaded_data_status = "empty" # Selected data
    
    Main(db_directory, loaded_data_status)