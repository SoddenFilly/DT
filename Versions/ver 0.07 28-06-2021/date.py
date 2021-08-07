import datetime
print(datetime.datetime.now())
now_day = datetime.datetime.now().day
now_month = datetime.datetime.now().month
now_year = datetime.datetime.now().year
start_day = now_day
start_month = now_month
i = int(input("year span from now: "))
for year in range (now_year-i, now_year+1):
    for month in range (start_month,13):
        for day in range (start_day,32):
            print(year, month, day)
            start_day = 1
            if day == now_day and year == now_year: break
        start_month = 1
        if month == now_month and year == now_year: break
print(year, month, day)