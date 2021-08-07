from matplotlib import pyplot as plt
import time
from pynput import keyboard
import random

def on_press(key):
    '''
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
    '''
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press)
listener.start()

plt.figure("Compounding Interest & Token Value over time")

year = 365
month = 365/12
week = 365/48
day = 365/336
print(day*7*4*12)
print()
'''
annual_intrest = 1
time_len = 12
init_inv = 1000
'''
annual_intrest = float(input('Interest per annum: ')) / 100
time_len = int(input('Length of time in months: '))
init_inv = int(input('Initial investment: '))
token_val = 1


inv = init_inv
intrest = 0
time_x = []
value_y = []
value_y_ci = []#compound intrest
value_y_tk = []#token value
def reset_plotline():
    global init_inv
    global inv
    global time_x
    global value_y
    global value_y_ci
    global intrest
    
    
    inv = init_inv
    intrest = 0
    time_x = []
    value_y = []
    
    
def plot(plotnum, bonus_round):
    global inv
    global time_x
    global value_y
    global value_y_ci
    global value_y_tk
    global intrest
    #global bonus_round
    
    reset_plotline()

    res = 0
    
    for i in range(time_len + bonus_round):#months
        i = i + 10*0
        print()
        print('BONUS')
        print(bonus_round)
        print(time_len)
        print(i)
        if bonus_round == 0 or i <= time_len - 1:
            time_x = time_x + [0]
            time_x[i] = 1 + time_x[i-1]

        #print('result')
        #print(value_y)
        value_y = value_y + [1]
        intrest = inv*(annual_intrest/12) + intrest
        #print(value_y)
        if plotnum <= 2:
            value_y[i] = inv + intrest
            
            if plotnum == 1:
                value_y_ci = value_y_ci + [0]
                value_y_ci[i] = inv + intrest
                inv = inv + intrest
                
        elif plotnum == 3:
            inv = inv + intrest
            value_y[i] = init_inv / inv

            value_y_tk = value_y_tk + [0]
            value_y_tk[i] = init_inv / inv

        elif plotnum == 4:
            value_y[i] = 1
            
        elif plotnum == 5:
            #print('res')
            #print(value_y)
            #if res == 0:
             #   value_y[i] = value_y_plot1[i] * (token_val * value_y_plot6[i])
              #  res = 1
            #print('THING')
            #print(value_y_plot1)
            #print(token_val)
            #print(value_y_plot6[i])
            value_y[i] = value_y_plot1[i] * (token_val * value_y_plot6[i])
            #print()
            #print(value_y[i])
            #print(value_y)

        
        
        elif plotnum == 6:
            #print('res2')
            #print(value_y)
            #print(value_y)
            #value_y[i] = init_inv
            
            if random.randint(1,2) == 1:
                value_y[i] += random.randint(1,3) / 10
            else:
                value_y[i] -= random.randint(1,3) / 10
            
        print('res3')
        print(value_y)

    print('res4')
    print(value_y)
                
            
    print()
    print('i')
    print(plotnum)
    #if bonus_round != 1:
    time_x = [0] + time_x
    if plotnum == 1:
        value_y = [init_inv] + value_y
        print('res5')
        print(value_y)
    elif plotnum == 2:
        value_y = [init_inv] + value_y
        print('res6')
        print(value_y)
    elif plotnum == 3:
        value_y = [1] + value_y
        print('res7')
        print(value_y)
    
    elif plotnum == 4:
        value_y = [1] + value_y
        print('res8')
        print(value_y)
  
    elif plotnum == 5:
        print('yssnvndsnvdiun')
        print(value_y)
        #value_y = [init_inv * token_val] + value_y
        print('yssnvndsnvdiun')
        print(value_y)
        #value_y_ci = [init_inv] + value_y_ci
        #value_y_tk = [init_inv] + value_y_tk

    elif plotnum == 6:
        value_y = [1] + value_y
        print('res9')
        print(value_y)
    print(plotnum)

plt.subplot(2, 1, 1)

plt.grid(color='grey', linestyle='-', alpha=0.2, linewidth=1)

plot(1, 0)
print(time_x, value_y)
plt.plot(time_x, value_y, color='b', linestyle='-', label='Reinvesting Initial + Compounded Interest')
value_y_plot1 = value_y

plot(2, 0)
print(time_x, value_y)
plt.plot(time_x, value_y, color='k', linestyle=':', label='Reinvesting Initial')
value_y_plot2 = value_y

plt.fill_between(time_x, value_y_plot1, value_y_plot2,
                 where=(value_y_plot1 >= value_y_plot2),
                 interpolate=True, color='blue', alpha=0.1, label='filler')

plt.subplot(2, 1, 2)

plt.grid(color='black', linestyle='-', alpha=0.2, linewidth=1)

plot(3, 0)
print(time_x, value_y)

plt.plot(time_x, value_y, color='r', linestyle='-', alpha=0.1)
value_y_plot3 = value_y

plot(4, 0)
print(time_x, value_y)
plt.plot(time_x, value_y, color='g', linestyle='-')
value_y_plot4 = value_y

plot(6, 0)
print("actual value", time_x, value_y)
plt.plot(time_x, value_y, color='k', linestyle='-', label='Actual value')
value_y_plot6 = value_y

plt.fill_between(time_x, value_y_plot6, value_y_plot4,
                 where=(value_y_plot6 >= value_y_plot4),
                 interpolate=True, color='green', alpha=0.2, label='Increased Profits')
plt.fill_between(time_x, value_y_plot6, value_y_plot4,
                 where=(value_y_plot6 <= value_y_plot4),
                 interpolate=True, color='green', alpha=0.2)

plt.fill_between(time_x, value_y_plot3, value_y_plot4,
                 where=(value_y_plot3 <= value_y_plot4),
                 interpolate=True, color='orange', alpha=0.5, label='Lower Profits')

plt.fill_between(time_x, value_y_plot3, color='red', alpha=0.7, label='Losses')




plt.legend()

plt.figure('P&L')

plt.grid(color='grey', linestyle='-', alpha=0.2, linewidth=1)

plot(5, 1)
print(time_x, value_y)
plt.plot(time_x, value_y, color='b', linestyle='-', label='Investment value')
plt.legend()

plt.show(block=False)
#plt.show(block=False)
running = True

plt.pause(60*10)
    
    

    #print('luyfuyjl')

'''
years = year * int(input('Years: '))
months = month * int(input('Months: '))
weeks = week * int(input('Weeks: '))
days = day * int(input('Days: '))
print()
print(days+weeks+months+years)
print()
print(day*336)
print(day*(week*3+month*11))
print(round(week*4, 1))
print(round(month*12))
x = 365
print()
x = x/365
print(x)
x=round(x*30.41*5)
print(x)
x=round(x+30.41*7)
print(x)
x=x*12+x*0.15
print(x)


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
'''
