import requests # For api
import json     # For converting raw json data
import datetime # For getting current year
import math

def fetch(url_symbol, url_market, month_cap):
    global url
    stamp = -1
    itr = 100
    
    url_symbol = url_symbol.upper()
    url_market = url_market.upper()
    
    # Gets my personal api key from a txt doc in the current working directory
    with open(r"resources/api_key.txt") as file:
        for line in file:
            key = line.split(";")
            api_key = key[1]
                
    url = True
    while url:
        try:
            url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_MONTHLY&symbol={url_symbol}&market={url_market}&apikey={api_key}"
                
            # Sends a request to www.alphavantage.co using concatinated url and then converts the response to string format
            api_response = requests.get(url).text

            # Converts string into a dictionary
            dict_json = json.loads(api_response)
            # print(dict_json)

            # This is needed to trigger the except block if somthing went wrong
            # meta_data = "\nMeta Data:\n" + str(dict_json["Meta Data"]) + "\n"
            # print(meta_data)
            
        except KeyError: print("You may have misspelt somthing or that currency is not available,\nPlease try again.")
        else: break


    print(datetime.datetime.now())

    now_day = datetime.datetime.now().day
    now_month = datetime.datetime.now().month
    now_year = datetime.datetime.now().year
    start_day = now_day
    start_month = now_month

    # months = start_month-(i%12)
    print("strt")
    for year in range (now_year-math.floor(month_cap/12), now_year +1):

        for month in range (start_month-(month_cap%12),start_month+1):
            
            print(start_month-(month_cap%12))
            if month == 0:
                month += 12
            # print(month)

            for day in range (start_day,32):
                print(year, month, day)
                # start_day = 28

                # if month <= 9: zero = "0" # Makes sure that even if the month number is below 10, it is still a double-digit
                # else: zero = ""
    print("enid")
    
    
    #meta_data = "\nMeta Data:\n" + str(dict_json["Meta Data"]) + "\n"
    zero = "" # For formatting the dictionary key correctly
    day = 32
    month = 12
    year = datetime.datetime.now().year # current year
    #month_cap = 30 # over how many months to collect data total
    month_current = 0
    y_axis = []

    # Runs through all existing dates until there is a match(starting at most recent),
    # Collects price of the relevant match,
    # Stops when a certain number of matches have occured(month_cap)or the data runs out
    
    while True:
        if month == 1:
            day = 32
            month = 12
            year -= 1
        elif day == 1:
            day = 32
            month -= 1
        
        if month <= 9: zero = "0" # Makes sure that even if the month number is below 10, it is still a double-digit
        else: zero = ""
            
        day -= 1
        
        # Tests whether the relevant date is in the dictionary
        try:
            value = float(dict_json["Time Series (Digital Currency Monthly)"][str(year)+"-"+zero+str(month)+"-"+str(day)]["4a. close (" + url_market + ")"])
            # value = round(float(value),2)
            month_current += 1
            y_axis = y_axis + [value]
        except: pass
            # print(f"there are only {month_current} months of data available, you asked for {month_cap}")
            # month_cap = month_current

        if month_current < month_cap and itr == 0:
            stamp1 = stamp
            stamp = month_current
            if stamp == stamp1:
                print(f"\nThere are only {month_current} months of data available, you asked for {month_cap}")
                return y_axis, month_current
            itr = 100

        else: itr -= 1

        # Stops script once the set number of matches have occured(month_cap)
        # print(month_current, month_cap)
        if month_current == month_cap: break
    return y_axis, -1

def fetch_db(url_symbol, url_market):

    url_symbol = url_symbol.upper()
    url_market = url_market.upper()
    
    # Gets my personal api key from a txt doc in the current working directory
    with open(r"resources/api_key.txt") as file:
        for line in file:
            key = line.split(";")
            api_key = key[1]

    try:
        url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_MONTHLY&symbol={url_symbol}&market={url_market}&apikey={api_key}"
            
        # Sends a request to www.alphavantage.co using concatinated url and then converts the response to string format
        api_response = requests.get(url).text

        # Converts string into a dictionary
        dict_json = json.loads(api_response)
        
    except KeyError: quit("You may have misspelt somthing or that currency is not available,\nPlease try again.")

    data = {
        "slug":"",
        "symbol":"",
        "price":[],
        "price_high":[],
        "price_low":[],
        "volume":[],
        "date":[],
        "timestamp":[]
    }
    # print(dict_json)
    try:
        for date in dict_json["Time Series (Digital Currency Monthly)"]:
            
            data["slug"]      = dict_json["Meta Data"]["3. Digital Currency Name"]
            data["symbol"]     = url_symbol
            data["price"]      = data["price"]      + [float(dict_json["Time Series (Digital Currency Monthly)"][date][f"4a. close ({url_market})"])]
            data["price_high"] = data["price_high"] + [float(dict_json["Time Series (Digital Currency Monthly)"][date][f"2a. high ({url_market})"])]
            data["price_low"]  = data["price_low"]  + [float(dict_json["Time Series (Digital Currency Monthly)"][date][f"3a. low ({url_market})"])]
            data["volume"]     = data["volume"]     + [float(dict_json["Time Series (Digital Currency Monthly)"][date][f"5. volume"])]
            data["date"]       = data["date"]       + [date]
            data["timestamp"]  = data["timestamp"]  + [datetime.datetime.strptime(date, "%Y-%m-%d").timestamp()]
    except:
        print(f"data for {url_symbol} is not available or the currency does not exist,\nOR these calls have been made too quickly,\nplease make calls of more than one a minimum of 60 second apart\n - skipping>>\n")
        return "failed"
            
    return data

if __name__ == "__main__":

    symbol = input("Crypto symbol: ").upper()
    months = int(input("Whole months: "))

    print("Resulting values:",fetch(symbol, "usd", months)[0])