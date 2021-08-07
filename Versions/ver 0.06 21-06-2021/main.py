# imports the main functions from the two used scripts
from marketprice import fetch
from graph import graph

# allows user to select a range of data to graph (eg, what currency and the time period in months)
symbol = input("Crypto symbol: ").upper()
months = int(input("Whole months: "))

# returns all available data along with a flag that if changed then contains the new time period that corresponds to the available data
y_ax, flag = fetch(False, False, symbol, "usd", months)

if flag != -1: # Checks if the flag was changed, if the flag was changed then do as if unchanged except use the new time period (flag) instead of the old (months)
    print(f"Graphing results using new paramters: {symbol}, {flag}")
    graph(symbol, flag, y_ax)
else:
    print(f"Graphing results using paramters: {symbol}, {months}")
    graph(symbol, months, y_ax)

# This prints when the matplotlib graph window is closed
print("\nProgram terminated")