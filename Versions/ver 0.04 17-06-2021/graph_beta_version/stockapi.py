import requests
import json

# ------------- hard coded values ----------------------
api_key = "UY46D7M5TNA70QSX"

#url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=eth&to_currency=NZD&apikey="
url = "https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=IBM&apikey="

request_url = url+api_key

# ------------- fetch ----------------------

response_API = requests.get(request_url)

# convert response into a string
data = response_API.text

# convert string into a dictionary
parse_json = json.loads(data)

# look at all the data
print(parse_json)

# find bits in the dictionary
#rate = parse_json["Realtime Currency Exchange Rate"]#["2000-07-31"]["4. close"]
rate = parse_json["Meta Data"]
rate = parse_json["Monthly Time Series"]
print('\n Rate:',rate)

for id, info in parse_json.items():
    print("\nDates:", id)
    for key in info:
        print(key + ':', info[key])
'''
rate = parse_json["Monthly Time Series"]["2021-03-15"]
print('\n Rate:',rate)
'''
day = 31
month = 12
year = 2021
zero = ""
monthnum = 10
monthnum1 = 0
run = True
while run:
    if day == 1:
        day = 32
        month -= 1
    if month == 1:
        month = 12
        year -= 1
    day -= 1
    if month <= 9:
        zero = "0"
    else:
        zero = ""
    #print(year,zero+str(month))
    #print("date = month: ",month," , day: ",day)
    
    try:
        #print("date = month:",zero+str(month),",day:",day)
        rate = parse_json["Monthly Time Series"][str(year)+"-"+zero+str(month)+"-"+str(day)]["4. close"]
        print(str(year)+"-"+zero+str(month)+"-"+str(day)+":")
        print(rate)
        print()
        monthnum1 += 1
    except:
        pass
    if monthnum1 == monthnum:
        break


 
