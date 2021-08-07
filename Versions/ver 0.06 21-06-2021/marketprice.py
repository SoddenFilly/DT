import requests # For api
import json     # For converting raw json data
import datetime # For getting current year
import time
from progress.bar import ShadyBar

def fetch(url_local_input, native, url_symbol, url_market, month_cap):
    timestamp = []
    stamp = -1
    itr = 100
    
    url_symbol = url_symbol.upper()
    url_market = url_market.upper()
    
    # Gets my personal api key from a txt doc in the current working directory
    with open(r"api_key.txt") as file:
        for line in file:
            key = line.split(";")
            api_key = key[1]
    #exit()
    # print('uyksfbS')
    if len(timestamp) == 5:
        # wait = round(timestamp[4] - timestamp[0])
        # print(wait)
        if timestamp[4] - timestamp[0] <= 60:
            timestamp = []
            # print('waiting')
            bar = ShadyBar('Processing', max=60)
            for i in range(60):
                i = i
                time.sleep(0.8)
                bar.next()
                #print()
            bar.finish()
                
    
            
    url = True
    while url:
        try:
            if url_local_input == True:
                # Concatination of required queries to form fetch url
                url_symbol = input("Symbol: ").upper()
                url_market = input("Market: ").upper()
                url = "https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_MONTHLY&symbol=" + url_symbol + "&market=" + url_market + "&apikey=" + api_key
                #url = "https://www.alphavantage.co/query?function=" + input("Function: ") + "&symbol=" + input("Symbol: ") + "&market=" + input("Market: ") + "&apikey=" + api_key
                # print(url)
            else:
                url = "https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_MONTHLY&symbol=" + url_symbol + "&market=" + url_market + "&apikey=" + api_key
                # print(url)
                
                # print(timestamp)
                # if len(timestamp) == 5: timestamp.pop(0)
                # timestamp = timestamp + [time.time()]
                # print(timestamp)
                
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
    run = True
    while run:
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
            if native == True:
                # print(str(year)+"-"+zero+str(month)+"-"+str(day)+":")
                # print(value,"\n")
                pass
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

if __name__ == "__main__":

    print(fetch(False,True,'sol','usd',47))