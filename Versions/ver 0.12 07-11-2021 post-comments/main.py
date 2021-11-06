from matplotlib import pyplot as plt # For graphing
import sqlite3                       # Database handling
import os                            # File handling (executing/deleting/etc other files)

def DB_connect(db_directory): # Connects program to the database, takes in the location of where the database is stored as its only paramater

    db_connection = sqlite3.connect(db_directory)
    cursor = db_connection.cursor()

    return cursor, db_connection

def DB_status(loaded_data_status): # Creates a simple overview of what state the program and database are in, takes in the param (loaded_data_status), this stores what currency has been selected from the database to be graphed, if none are selected it has a default of "empty"

    if os.path.isfile(db_directory): # Checks if database file exists

        cursor, db_connection = DB_connect(db_directory)

        cursor.execute("SELECT * FROM crypto") # Gets list of all currency symbols from database
        
        database_total_currencies = len(cursor.fetchall()) # gets the list length of all currency symbols from database
        database_status = f"populated with {database_total_currencies} currencies"

        db_connection.close()

        return f"--------------------------------------------------.\nDatabase status: {database_status}\nCurrency selected for graphing: {loaded_data_status}", loaded_data_status, True # This returns data on what is stored in the database and what is stored locally in the program

    return "No existing database file. Please initialise a new database (1).", "empty", False # returns if database file does not exist. The bool gets assigned to db_exist in Main() (for further error prevention)

def Data_graph(symbol, graph_data_x, graph_data_y): # Matplotlib module function, this handles everything to do with the graphing and takes in the symbol(BTC,ETH,etc) and the x(Dates)/y(Prices) axis datalists as parameters

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

    try: # Graph fullscreen method + alternate (window does not show whole graph correctly if not in fullscreen)
        figManager = plt.get_current_fig_manager().window # gets the ability to alter advanced options eg. wether the window opens in fullscreen
        figManager.state("zoomed") # Makes the graphing window open in fullscreen
    except: # If first '("zoomed")' method fails
        try:
            figManager.showMaximized()
        except:
            print("\nProgram failed to open graph window in fullscreen mode, opened in the smaller windowed mode instead")

    plt.show() # Commits configurations and opens the graphing window

def Main(db_directory, loaded_data_status): # The main function used to run the "main menu" of the program, the access point to every other aspect of the program, takes in the params db_directory (directory where the database resides)

    while True: # Main program loop, everything else in this program is accessible from this root loop acting as a menu section.
 
        try: # Gets and prints database status data
            message, loaded_data_status, db_exist = DB_status(loaded_data_status)
            print(message)
        except Exception as err: # This should never have to fire
            print(err)
        
        try: # Prints out a blurb on what the user has access to do
            task = int(input("\nWhat do you want to do?\n (1): New database\n (2): Add to database\n (3): Remove from database\n (4): List all currently stored coins\n (5): Load database data\n (6): Graph loaded data\n (7): Quit program\n: "))
            
            if task > 7 or task < 1: # Error prevention
                input("\n!!! Please input an integer within the range 1-7 (Press 'enter' to continue)\n")
            
        except: # Error prevention
            task = 0 # Makes sure nothing further is triggered with task
            input("\n!!! Please input an integer within the range 1-7 (Press 'enter' to continue)\n")

        if task == 1: # (1) New database

            os.system('python db_structure.py') # This runs db_structure.py then returns here once it terminates

        elif task == 2 and db_exist == True: # (2) Add to database

            os.system('python db_insert.py') # This runs db_insert.py then returns here once it terminates

        elif task == 3 and db_exist == True: # (3) Delete from database

            cursor, db_connection = DB_connect(db_directory)

            symbol = input("symbol: ") .upper()
            data = cursor.execute(f"SELECT * FROM crypto WHERE c_symbol = '{symbol}' ") .fetchall() # Querys the database for all data paired with the symbol the user chose
            
            if data == []: # Data returns as [] if no data is found when querying the database

                input(f"\n!!! Currency {symbol} does not currently exit within the database. (Press 'enter' to continue)\n")

            else:

                delete_id = data[0][0] # The '[0][0]' is needed to select the required value from the returned data == '([1, ?, ?])' to '1'
            
                cursor.execute(f"DELETE FROM crypto WHERE id = '{delete_id}' ") # purges all data paired with the user chosen symbol
                cursor.execute(f"DELETE FROM history WHERE c_id = '{delete_id}' ") # purges all data paired with the user chosen symbol

                db_connection.commit()

                print(f"\nCurrency {symbol} has been purged from database.")
            
            db_connection.close()

        elif task == 4 and db_exist == True: # (4) List all currently stored coins
            
            cursor, db_connection = DB_connect(db_directory)

            coins = cursor.execute(f"SELECT * FROM crypto") .fetchall() # Querys the database for every unique currency in the 'crypto' table

            increment = 0
            for coin in coins: # Iterates through all the currency's in database and prints them out with some additional information

                increment += 1
                print(str(increment) + ":", coin[2], "|", coin[1])
            
            db_connection.close()
            
            input("\n>>Press enter to continue ")

        elif task == 5 and db_exist == True: # (5) Load database data (Selects all the historic data for the provided currency)

            cursor, db_connection = DB_connect(db_directory)

            symbol = input("symbol: ") .upper()

            currency_data = cursor.execute(f"SELECT * FROM crypto WHERE c_symbol = '{symbol}' ") .fetchall() # Querys the database for if the users selected symbol exists in the database

            if currency_data == []: # Data returns as [] if no data is found when querying the database

                input(f"\n!!! Currency {symbol} does not currently exit within the database. (Press 'enter' to continue)\n")
            
            else:
                raw_data = cursor.execute(f"SELECT * FROM history WHERE c_id = '{currency_data[0][0]}' ") .fetchall() # If the previous query finds the symbol then this querys the database for all the raw price data associated with said symbol

                graph_data_x, graph_data_y = [], [] # These are the x/y axis used when graphing
                for valueList in raw_data:
                    # A Single "valueList" from raw_data looks like this: (34, 2, 2.079, 2.144, 1.911, 615717925.6, '2021-11-04', 1635937200)
                    graph_data_x.append(valueList[6]) # This isolates no.6 (the "date")
                    graph_data_y.append(valueList[2]) # This isolates no.2 (the "closing value" is the final currency value at the end of the respective time period (1h,2h,4h,1day,1month,etc))

                loaded_data_status = currency_data[0][1] # Currency_data looks like this [(2, 'Cardano', 'ADA')] and with [0][1] 'Cardano' gets isolated, sidenote: loaded_data_status is what is displayed next to "Currency selected for graphing: "

                print(f"\nCurrency {symbol} loaded and ready to graph.") # Symbol == BTC, ETH or DOGE etc
            
            db_connection.close()

        elif task == 6 and db_exist == True: # Graphs locally stored/selected data (task 6)

            if loaded_data_status == "empty": # Won't graph if no historic data is selected

                input("\n!!! No data is currently selected for graphing. (Press 'enter' to continue)\n")
            
            else:

                Data_graph(symbol, graph_data_x, graph_data_y)

        elif task == 7: # Quits program (wow!)

            quit(">Program terminated\n")

if __name__ == "__main__": # Only fires if this file was executed via command line or by similar means

    db_directory = "database.db" # Where the database is stored

    loaded_data_status = "empty" # Selected graphing data/ this is referred to as "the programs local storage" by me in other comments
    
    Main(db_directory, loaded_data_status) # Gets the ball rolling :O