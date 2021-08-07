# imports the main functions from the two used scripts
import os
from marketprice import fetch_db
from graph import graph
# from db_structure import db_structure
# import db_structure

while True:
    print("\nwhat do you want to do?")
    try: i = int(input("(1): New database\n(2): Add to database\n(3): Load data\n(4): Graph data\n(5): Quit\n: "))
    except:
        i = 0
        print("Please input a singular number within range 1-5")
    if i == 1:
        os.system('python db_structure.py')
    elif i == 2:
        pass
    elif i == 3:
        i = input("(1): Raw\n(2): Database\n: ")
        if i == "1":
            # allows user to select a range of data to graph (eg, what currency and the time period in months)
            symbol = input("Crypto symbol: ").upper()
            months = int(input("Whole months: "))

            # returns all available data along with a flag that if changed then contains the new time period that corresponds to the available data
            data, flag = fetch_db(True, symbol, "usd", months)
            print(data,flag)
        elif i == "2":
            pass
    elif i == 4:
        try:
            if flag != -1: # Checks if the flag was changed, if the flag was changed then do as if unchanged except use the new time period (flag) instead of the old (months)
                print(f"Graphing results using new paramters: {symbol}, {flag}")
                graph(symbol, flag, data)
            else:
                print(f"Graphing results using paramters: {symbol}, {months}")
                graph(symbol, months, data)
        except Exception as err: print("invalid graphing data", err)
    elif i == 5:
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