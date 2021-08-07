#year-relative
year = 365
month = year/12
week = year/48 #12*4
day = year/336 #12*4*7
print(year, month, week, day)
print(day*7*4*12, day*336)
print()
#day-relative
day = 1
week = day*7
month = day*28 #7*4
year = day*336 #7*4*12
print(year, month, week, day)
print(day*year)
print()

annual_intrest = 100
period_len = 15
#period_num = 6

num = 360 / period_len
#period_num = period_num * num
print(num)
print(period_len * num)
print(annual_intrest / num)
print(annual_intrest / num * num)
print()
#print(annual_intrest / num * period_num)
print(365/(12*2))
