''
from matplotlib import pyplot as plt
import time

#defaults
inv = 0
day_range = 30
per_range = 12
time_x = []
value_y = []
intrest = 0
pers_year = 35
pers_year_len = 100
r_inv = 1000
r_day = 30
r_per = 12

try:
    pers_year = float(input('Annual percentage(default 35 = 35% yearly intrest): '))
    if pers_year > 0: pass
    r_inv = int(input('Initial Investment(default 1000: '))
    if r_inv > 0: pass
    r_day = int(input('Number of days in a period(default 30 = 1 month): '))
    if r_day > 0: pass
    r_per = int(input('Number of periods(default 12 = 1 year): '))
    if r_per > 0: pass

except:
    pass
if len(str(pers_year)) == 1:
    pers_year_len = 10
elif len(str(pers_year)) == 2:
    pers_year_len = 100
elif len(str(pers_year)) == 3:
    pers_year_len = 1000
    
print(pers_year)
print(r_inv)
print(r_day)
print(r_per)
print()
#print("Investment: "+str(round(r_inv, 2)))


def reset(r_inv, r_day, r_per):
    global inv
    global time_x
    global value_y
    global intrest
    inv = r_inv #default 1000

    time_x = []
    value_y = []
    intrest = 0
    
def d90(second):
    global inv
    global time_x
    global value_y
    global intrest
    global pers_year_len
    reset(r_inv, r_day, r_per)
    print("Investment: "+str(round(inv, 2)))
    for s in range(r_per):
        for i in range(r_day):#days
            i = i + r_day*s
            time_x = time_x + [0]
            time_x[i] = 1 + time_x[i-1]

            value_y = value_y + [0]
            intrest = inv*(pers_year/pers_year_len+1)/365 + intrest
            value_y[i] = intrest + inv
            
        if second == 0:
            inv = inv + intrest
            intrest = 0
            print("Period "+str(s+1)+": "+str(round(inv, 2)))
        else:
            print(round(intrest + inv, 2))
            
    time_x = [0] + time_x
    value_y = [0] + value_y
#while
d90(0)
plt.plot(time_x, value_y, color='b', linestyle='-', label='Reinvesing Initial + Accumulated Intrest')
d90(1)
plt.plot(time_x, value_y, color='k', linestyle=':', label='Reinvesing Initial')

plt.legend()
#print(time_x)
#print(value_y)

plt.show()
