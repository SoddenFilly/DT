import requests # Data request handling
import json     # Json data handling
import datetime # Time handling
import math     # Advanced math handling

def fetch(url_symbol, url_market, month_cap): # This function gets and formats crypto data, takes in the requested symbol, the market the symbol is paired with(USD/NZD) and the total amount of months of data to go look back for NOTE: This function is only for reference within the scope of this script

    stamp = -1 # Acts as a check for if fetched data runs out later on
    itr = 100 # Acts as a delay in the same area as 'stamp'
    
    url_symbol = url_symbol.upper() # ensures that given symbol is in all uppercase
    url_market = url_market.upper() # ensures that given market is in all uppercase
    
    with open(r"Resources/api_key.txt") as file: # Gets my api key from a txt doc in the current working directory

        for line in file: api_key = line
    
    while True:

        try: # Gets the raw history data for the provided currency using the api key from just above

            url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_MONTHLY&symbol={url_symbol}&market={url_market}&apikey={api_key}"
                
            try:
                api_response = requests.get(url).text # Sends a request to www.alphavantage.co using the concatinated url and then converts the response to string format
                dict_json = json.loads(api_response) # Converts string into a dictionary
            except:
                print("!!! Remember! You need an internet connection for this feature to function correctly!\n")
                return "failed"
            
        except KeyError: print("You may have misspelt somthing or that currency is not available,\nPlease try again.") # prog will loop infinitly untill a valid symbol is provided(BTC/ETH,etc) or the internet fails
        
        else: break # If all goes well, break while loop

    now_day = datetime.datetime.now().day # Current day
    now_month = datetime.datetime.now().month # Current month

    zero = "" # For formatting the dictionary key correctly
    day = 32 # Max amount of days possible in a month
    month = 12 # Max possible months in a year
    year = datetime.datetime.now().year # Current year

    month_current = 0
    y_axis = []

    # Runs through all existing dates until there is a match(starting at most recent), Collects price of the relevant match, Stops when a certain number of matches have occured(month_cap) or the data runs out
    while True:

        if month == 1: # detects when the year should be deincremented

            day = 32
            month = 12
            year -= 1

        elif day == 1: # detects when each month should be deincremented

            day = 32
            month -= 1
        
        day -= 1 # deincrements once every loop

        if month <= 9: zero = "0" # Makes sure that even if the month number is below 10, it is still formatted as a double-digit
        else: zero = ""
        
        try: # Tests whether the relevant date is in the dictionary, if yes then update the month and add the value to y_axis, if not then pass

            value = float(dict_json["Time Series (Digital Currency Monthly)"][f"{ str(year) }-{ zero }{ str(month) }-{ str(day) }"][f"4a. close ({url_market})"])
            month_current += 1
            y_axis = y_axis + [value]

        except: pass

        if month_current < month_cap and itr == 0: # If program has not got the amount of data the use said there 'should be' and the delay(itr) has stopped occuring

            stamp1 = stamp
            stamp = month_current
            if stamp == stamp1: # If (old == new) then this must mean that the data has run out, return all up untill this point

                print(f"\nThere are only {month_current} months of data available, you asked for {month_cap}")
                return y_axis

            itr = 100 # Resets delay

        else: itr -= 1 # Deincrements delay

        if month_current == month_cap: break # Stops loop once the set number of matches have occured(month_cap)

    return y_axis

def fetch_db(url_symbol, url_market): # This function gets and formats crypto data, takes in the requested symbol and the market the symbol is paired with(USD/NZD)

    url_symbol.upper() # ensures that given symbol is in all uppercase
    url_market.upper() # ensures that given market is in all uppercase
    
    with open(r"Resources/api_key.txt") as file: # Gets my api key from a txt doc in the current working directory

        for key in file: api_key = key

    try: # Gets the raw history data for the provided currency using the api key from just above

        url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_MONTHLY&symbol={url_symbol}&market={url_market}&apikey={api_key}"
            
        try:
            api_response = requests.get(url).text # Sends a request to www.alphavantage.co using the concatinated url and then converts the response to string format
            dict_json = json.loads(api_response) # Converts string into a dictionary
        except:
            print("!!! Remember! You need an internet connection for this feature to function correctly!\n")
            return "failed"
        
    except KeyError: quit("You may have misspelt somthing or that currency is not available,\nPlease try again.") # prog will loop infinitly untill a valid symbol is provided(BTC/ETH,etc) or the internet fails

    data = { # Dictionary structure to store received data in, following comments show examples of what each pair could hold (all hypothetical)
        "slug":"",       # Bitcoin
        "symbol":"",     # BTC
        "price":[],      # 61438.92
        "price_high":[], # 61924.35
        "price_low":[],  # 60899.28
        "volume":[],     # 1378.73
        "date":[],       # 31-2-2014
        "timestamp":[]   # 1239829838
    }

    try:

        for date in dict_json["Time Series (Digital Currency Monthly)"]: # Organizes all data to be utilised later much easier
            
            data["slug"]       = dict_json["Meta Data"] ["3. Digital Currency Name"]
            data["symbol"]     = url_symbol
            data["price"]      = data["price"]      + [float(dict_json["Time Series (Digital Currency Monthly)"] [date] [f"4a. close ({url_market})"] ) ]
            data["price_high"] = data["price_high"] + [float(dict_json["Time Series (Digital Currency Monthly)"] [date] [f"2a. high ({url_market})"]  ) ]
            data["price_low"]  = data["price_low"]  + [float(dict_json["Time Series (Digital Currency Monthly)"] [date] [f"3a. low ({url_market})"]   ) ]
            data["volume"]     = data["volume"]     + [float(dict_json["Time Series (Digital Currency Monthly)"] [date] [f"5. volume"]                ) ]
            data["date"]       = data["date"]       + [date]
            data["timestamp"]  = data["timestamp"]  + [datetime.datetime.strptime(date, "%Y-%m-%d").timestamp()]
    
    except: # If anything goes wrong it will be one of the scenarios mentioned in the print statement below

        print(f"data for {url_symbol} is not available or the currency does not exist,\nOR these calls have been made too quickly,\nplease make calls of more than one a minimum of 60 second apart\n - skipping>>\n")
        
        return "failed"
            
    return data # Returns the final organised product

if __name__ == "__main__": # Only fires if this file was executed via command line or by similar means

    symbol = input("\nCrypto symbol: ").upper()
    months = int(input("Whole months: ")) # Quantity of months into the past to look for crypto data

    print("\nResulting values:",fetch(symbol, "usd", months), "\n") # Runs function fetch() and prints the returned data