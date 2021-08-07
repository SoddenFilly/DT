import requests # For api
import json     # For converting raw json data
import datetime # For getting current year

def fetch(url_local_input, url_symbol, url_market, month_cap):
    url_symbol = url_symbol.upper()
    url_market = url_market.upper()
    
    # Gets my personal api key from a txt doc in the current working directory
    f = open(r"C:\Users\gabor\.python_DT\python\api_key.txt", "r")
    api_key = f.read()

    url = True
    while url:
        try:
            if url_local_input == True:
                # Concatination of required queries to form fetch url
                url_symbol = input("Symbol: ").upper()
                url_market = input("Market: ").upper()
                url = "https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_MONTHLY&symbol=" + url_symbol + "&market=" + url_market + "&apikey=" + api_key
                #url = "https://www.alphavantage.co/query?function=" + input("Function: ") + "&symbol=" + input("Symbol: ") + "&market=" + input("Market: ") + "&apikey=" + api_key
                #print(url)
            else:
                url = "https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_MONTHLY&symbol=" + url_symbol + "&market=" + url_market + "&apikey=" + api_key
                #print(url)
                
            # Sends a request to www.alphavantage.co using concatinated url and then converts the response to string format
            api_response = requests.get(url).text
            #print(api_response)

            # Converts string into a dictionary
            dict_json = json.loads(api_response)
            #print(dict_json)

            # This is needed to trigger the except block if somthing went wrong
            meta_data = "\nMeta Data:\n" + str(dict_json["Meta Data"]) + "\n"
            #print(meta_data)
            
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
            value = dict_json["Time Series (Digital Currency Monthly)"][str(year)+"-"+zero+str(month)+"-"+str(day)]["4a. close (" + url_market + ")"]
            value = round(float(value),2)
            if url_local_input == True:
                print(str(year)+"-"+zero+str(month)+"-"+str(day)+":")
                print(value,"\n")
            month_current += 1
            y_axis = y_axis + [value]
        except: pass

        # Stops script once the set number of matches have occured(month_cap)
        if month_current == month_cap: break
    return y_axis

if __name__ == "__main__":
    fetch(True,'','',10)
