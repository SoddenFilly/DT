from matplotlib import pyplot as plt # render graph
import os
import sqlite3
from marketprice import fetch_db
from graph import graph
# from db_structure import db_structure
# import db_structure

loaded_data_status = "empty"

def data_status():

    # database_total_currencies = 0
    # database_status = f"populated with {database_total_currencies} currencies"

    db_connection = sqlite3.connect("database.db")
    cursor = db_connection.cursor()

    cursor.execute("SELECT * FROM crypto")

    database_total_currencies = len(cursor.fetchall())
    database_status = f"populated with {database_total_currencies} currencies"

    db_connection.close()

    return f"\nDatabase status: {database_status}\nLoaded data status: {loaded_data_status}"

while True:
    
    # print(f"\nDatabase status: {database_status}\nLoaded data status: {loaded_data_status} \n\nwhat do you want to do?")

    print(data_status())
    
    try: i = int(input("\nWhat do you want to do?\n (1): New database\n (2): Add to database\n (3): Remove from database\n (4): List all currently stored coins\n (5): Load database data\n (6): Graph loaded data\n (7): Quit program\n: "))
    except:
        i = 0
        print("Please input a singular number within range 1-5")

    if i == 1:

        os.system('python db_structure.py')

    elif i == 2:

        os.system('python db_insert.py')

    elif i == 3:

        db_connection = sqlite3.connect("database.db")
        cursor = db_connection.cursor()

        i = input("symbol: ").upper()

        cursor.execute(f"SELECT * FROM crypto WHERE c_symbol = '{i}' ")

        cursor_res = cursor.fetchall()
        delete_id = cursor_res[0][0]
        print("cr", cursor_res, delete_id)
        cursor.execute(f"DELETE FROM crypto WHERE id = '{delete_id}' ")
        cursor.execute(f"DELETE FROM history WHERE c_id = '{delete_id}' ")

        db_connection.commit()

    elif i == 4:
        
        db_connection = sqlite3.connect("database.db")
        cursor = db_connection.cursor()

        cursor.execute(f"SELECT * FROM crypto")
        # print(cursor.fetchall())
        coins = cursor.fetchall()

        print()
        increment = 0
        for coin in coins:
            increment += 1
            print(str(increment) + ":", coin[2], "|", coin[1])
        
        input("\n>>Press enter to continue ")


        pass

    elif i == 5:

        db_connection = sqlite3.connect("database.db")
        cursor = db_connection.cursor()

        i = input("symbol: ").upper()

        cursor.execute(f"SELECT * FROM crypto WHERE c_symbol = '{i}' ")
        # print("cur", cursor.fetchall()[0][0])
        currency_data = cursor.fetchall()
        

        cursor.execute(f"SELECT * FROM history WHERE c_id = '{currency_data[0][0]}' ")
        # print("cur", cursor.fetchall())
        raw_data = cursor.fetchall()
        print(raw_data)

        graph_data_x = []
        graph_data_y = []
        for value in raw_data:
            graph_data_x.append(value[6])
            graph_data_y.append(value[2])

        loaded_data_status = currency_data[0][1]

        print()
        print(graph_data_x)
        print()
        print(graph_data_y)

    elif i == 6:
        # try:
        #     if flag != -1: # Checks if the flag was changed, if the flag was changed then do as if unchanged except use the new time period (flag) instead of the old (months)
        #         print(f"Graphing results using new paramters: {symbol}, {flag}")
        #         graph(symbol, flag, data)
        #     else:
        #         print(f"Graphing results using paramters: {symbol}, {months}")
        #         graph(symbol, months, data)
        # except Exception as err: print("invalid graphing data", err)


        # plt.figure( i, " - Compounding Interest & Token Value over time" )

        plt.grid(color='grey', alpha=0.2, linewidth=1)

        plt.plot(graph_data_x, graph_data_y)

        plt.get_current_fig_manager().window.state("zoomed")

        plt.show()


        pass

    elif i == 7:
        quit("\n>Program terminated")

    else:
        pass


# # allows user to select a range of data to graph (eg, what currency and the time period in months)
# symbol = input("Crypto symbol: ").upper()
# months = int(input("Whole months: "))

# # returns all available data along with a flag that if changed then contains the new time period that corresponds to the available data
# data, flag = fetch(False, symbol, "usd", months)

# if flag != -1: # Checks if the flag was changed, if the flag was changed then do as if unchanged except use the new time period (flag) instead of the old (months)
#     print(f"Graphing results using new paramters: {symbol}, {flag}")
#     graph(symbol, flag, data)
# else:
#     print(f"Graphing results using paramters: {symbol}, {months}")
#     graph(symbol, months, data)

# This prints when the matplotlib graph window is closed
# print("\n>Program terminated")