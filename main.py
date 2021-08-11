from matplotlib import pyplot as plt # For graphing
import sqlite3 # Database handling
import os # For accessing other files

def Data_status(loaded_data_status):

    cursor, db_connection = DB_connect(db_directory)

    cursor.execute("SELECT * FROM crypto")
    
    database_total_currencies = len(cursor.fetchall())
    database_status = f"populated with {database_total_currencies} currencies"

    db_connection.close()

    return f"\nDatabase status: {database_status}\nCurrency selected for graphing: {loaded_data_status}", database_total_currencies

def DB_connect(db_directory):

    db_connection = sqlite3.connect(db_directory)
    cursor = db_connection.cursor()

    return cursor, db_connection

def Main(db_directory, loaded_data_status):

    while True:

        try:
            message, database_total_currencies = Data_status(loaded_data_status)
            print(message)
        except Exception as err:
            print(err)
        
        try:
            task = int(input("\nWhat do you want to do?\n (1): New database\n (2): Add to database\n (3): Remove from database\n (4): List all currently stored coins\n (5): Load database data\n (6): Graph loaded data\n (7): Quit program\n: "))
            print()
        except:
            task = 0
            input("\n!!! Please input an integer within the range 1-7 (Press 'enter' to continue)\n")

        if task == 1:

            os.system('python db_structure.py')

        elif task == 2:

            os.system('python db_insert.py')

        elif task == 3 and database_total_currencies > 0:

            cursor, db_connection = DB_connect(db_directory)

            symbol = input("symbol: ") .upper()
            data = cursor.execute(f"SELECT * FROM crypto WHERE c_symbol = '{symbol}' ") .fetchall()
            
            if data == []:

                input(f"\n!!! Currency {symbol} does not currently exit within the database. (Press 'enter' to continue) ")

            else:

                delete_id = data[0][0]
            
                cursor.execute(f"DELETE FROM crypto WHERE id = '{delete_id}' ")
                cursor.execute(f"DELETE FROM history WHERE c_id = '{delete_id}' ")

                db_connection.commit()

                print(f"\nCurrency {symbol} has been purged from database.")

        elif task == 4:
            
            cursor, db_connection = DB_connect(db_directory)

            coins = cursor.execute(f"SELECT * FROM crypto") .fetchall()

            increment = 0
            for coin in coins:

                increment += 1
                print(str(increment) + ":", coin[2], "|", coin[1])
            
            input("\n>>Press enter to continue ")

        elif task == 5:

            cursor, db_connection = DB_connect(db_directory)

            symbol = input("symbol: ") .upper()

            currency_data = cursor.execute(f"SELECT * FROM crypto WHERE c_symbol = '{symbol}' ") .fetchall()

            if currency_data == []:

                input(f"\n!!! Currency {symbol} does not currently exit within the database. (Press 'enter' to continue) ")
            
            else:
                raw_data = cursor.execute(f"SELECT * FROM history WHERE c_id = '{currency_data[0][0]}' ") .fetchall()

                graph_data_x, graph_data_y = [], []
                for value in raw_data:

                    graph_data_x.append(value[6])
                    graph_data_y.append(value[2])

                loaded_data_status = currency_data[0][1]

                print(f"Currency {symbol} loaded and ready to graph.")

        elif task == 6:

            print("! Note that the graph window needs to be closed before proceeding with the program.")

            plt.figure(f"Price of {symbol} in USD over {len(graph_data_x)} months")

            plt.plot(graph_data_x, graph_data_y, label=f"Price of {symbol} in USD")

            plt.setp(plt.gca().get_xticklabels(), rotation=30, horizontalalignment='right')
            plt.get_current_fig_manager() .window.state("zoomed")
            plt.grid(color='grey', alpha=0.5, linewidth=1)
            plt.subplots_adjust(bottom=0.15)
            plt.ylabel("Prices Ascending")
            plt.xlabel("Dates Acending")
            plt.gca().invert_xaxis()
            plt.legend()

            plt.show()

        elif task == 7:

            quit(">Program terminated\n")


if __name__ == "__main__":

    db_directory = "database.db"

    loaded_data_status = "empty"
    
    Main(db_directory, loaded_data_status)