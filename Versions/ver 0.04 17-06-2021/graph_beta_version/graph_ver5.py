import pandas as pd
from matplotlib import pyplot as plt
import random
import time

6 - 5
9 - 6
5 - 7
7 - 8
8 - 9

year = 365
month = 365/12
week = 365/48
day = 365/336
print(day*7*4*12)
print()

annual_intrest = float(input('%Interest per annum: ')) / 100
#relative = input('Year or day-relative?(y/d): ')
period_len = input('Length of time-periods(y/m/w/d): ')
if 'y' in period_len:
    x = 1
    period_len_name = 'years'
elif 'm' in period_len:
    x = 12
    period_len_name = 'months'
elif 'w' in period_len:
    x = 48
    period_len_name = 'weeks'
elif 'd' in period_len:
    x = 336
    period_len_name = 'days'
    
if 'h' in period_len:
    period_len = x*2
elif 'u' in period_len:
    period_len = x/2
else:
    period_len = x
    
period_num = int(input('Number of '+period_len_name+': '))
token_val = float(input('Token value: '))
init_inv = int(input('Initial token investment: '))
init_value = init_inv * token_val
init_val = []
for i in range(period_num+1):
            init_val = init_val + [init_value]
            
def reset_plotline():
    global init_inv
    global inv
    global time_x
    global value_y
    global intrest
    
    inv = init_inv
    intrest = 0
    time_x = []
    value_y = []
    
def plot(plotnum, bonus_round):
    global inv
    global time_x
    global value_y
    global intrest
    
    reset_plotline()
    
    for i in range(period_num + bonus_round):#months
        i = i + 10*0
        if bonus_round == 0 or i <= period_num - 1:
            time_x = time_x + [0]
            time_x[i] = 1 + time_x[i-1]
        if plotnum != 5:
            value_y = value_y + [1]
        else:
            value_y = value_y + [token_val]
        intrest = inv*(annual_intrest/period_len) + intrest
        
        if plotnum <= 2:
            value_y[i] = inv + intrest
    
            if plotnum == 1:
                inv = inv + intrest
                
        elif plotnum == 3:
            inv = inv + intrest
            value_y[i] = init_inv / inv

        elif plotnum == 4:
            value_y[i] = 1
            
        elif plotnum == 5:
            value_y[i] = value_y_plot1[i] * value_y_plot9[i]

        elif plotnum == 6:
            value_y[i] += random.randint(-3,3) / 10

        elif plotnum == 7:
            value_y[i] = token_val

        elif plotnum == 8:
            inv = inv + intrest
            value_y[i] = init_inv / inv * token_val

        elif plotnum == 9:
            value_y[i] = value_y_plot6[i+1] * token_val
            
            

    time_x = [0] + time_x
    
    if plotnum == 1:
        value_y = [init_inv] + value_y

    elif plotnum == 2:
        value_y = [init_inv] + value_y
        
    elif plotnum == 3 or plotnum == 4 or plotnum == 6:
        value_y = [1] + value_y
        
    elif plotnum == 7 or plotnum == 8 or plotnum == 9:
        value_y = [token_val] + value_y

plot(1, 0)
value_y_plot1 = value_y

plot(2, 0)
value_y_plot2 = value_y

plot(3, 0)
value_y_plot3 = value_y

plot(4, 0)
value_y_plot4 = value_y

plot(6, 0)
value_y_plot6 = value_y

plot(9, 0)
value_y_plot9 = value_y

plot(5, 1)
value_y_plot5 = value_y

plot(7, 0)
value_y_plot7 = value_y

plot(8, 0)
value_y_plot8 = value_y

#plot(10,0)




#WRITE CSV
dict = {'valy_p1': value_y_plot1, 'valy_p2': value_y_plot2, 'valy_p3': value_y_plot3, 'valy_p4': value_y_plot4, 'valy_p5': value_y_plot5, 'valy_p6': value_y_plot6, 'valy_p7': value_y_plot7, 'valy_p8': value_y_plot8, 'valy_p9': value_y_plot9}
df = pd.DataFrame(dict)  
# saving the dataframe  
df.to_csv(r'C:\Users\gabor\apitest\python_graph\data.csv')

#READ CSV
data = pd.read_csv(r'C:\Users\gabor\apitest\python_graph\data.csv')
value_y_plot5 = data['valy_p5']


plt.figure("Compounding Interest & Token Value over time")

plt.subplot(3, 2, 1)#verti, horiz, index
plt.grid(color='grey', linestyle='-', alpha=0.2, linewidth=1)
plt.plot(time_x, value_y_plot1, color='b', linestyle='-', label='Compounded Interest('+str(round(value_y_plot1[period_num], 2))+')')
plt.plot(time_x, value_y_plot2, color='k', linestyle=':', label='Flat Interest('+str(round(value_y_plot2[period_num], 2))+')')
plt.fill_between(time_x, value_y_plot1, value_y_plot2,
                 where=(value_y_plot1 >= value_y_plot2),
                 interpolate=True, color='blue', alpha=0.1)
plt.legend()
''
plt.subplot(3, 2, 5)
plt.grid(color='black', linestyle='-', alpha=0.2, linewidth=1)
plt.plot(time_x, value_y_plot3, color='r', linestyle='-', alpha=0.1)
plt.plot(time_x, value_y_plot4, color='g', linestyle='-')
plt.plot(time_x, value_y_plot6, color='k', linestyle='-', label='Token value('+str(round(value_y_plot6[period_num], 2))+')')
plt.fill_between(time_x, value_y_plot6, value_y_plot4,
                 where=(value_y_plot6 >= value_y_plot4),
                 interpolate=True, color='green', alpha=0.2, label='Multiplied Profits')
plt.fill_between(time_x, value_y_plot6, value_y_plot4,
                 where=(value_y_plot6 <= value_y_plot4),
                 interpolate=True, color='green', alpha=0.2)
plt.fill_between(time_x, value_y_plot3, value_y_plot4,
                 where=(value_y_plot3 <= value_y_plot4),
                 interpolate=True, color='orange', alpha=0.5, label='Lower Profits')
plt.fill_between(time_x, value_y_plot3, color='red', alpha=0.7, label='Losses('+str(round(value_y_plot3[period_num], 2))+'='+str(1-round(value_y_plot3[period_num], 2))+')')
plt.legend()
''
plt.subplot(3, 2, 3)
plt.grid(color='black', linestyle='-', alpha=0.2, linewidth=1)
plt.plot(time_x, value_y_plot7, color='g', linestyle='-')
plt.plot(time_x, value_y_plot8, color='r', linestyle='-', alpha=0.1)
plt.plot(time_x, value_y_plot9, color='k', linestyle='-', label='Token value('+str(round(value_y_plot9[period_num], 2))+')')
plt.fill_between(time_x, value_y_plot9, value_y_plot7,
                 where=(value_y_plot9 >= value_y_plot7),
                 interpolate=True, color='green', alpha=0.2, label='Multiplied Profits')
plt.fill_between(time_x, value_y_plot9, value_y_plot7,
                 where=(value_y_plot9 <= value_y_plot7),
                 interpolate=True, color='green', alpha=0.2)
plt.fill_between(time_x, value_y_plot8, value_y_plot7,
                 where=(value_y_plot8 <= value_y_plot7),
                 interpolate=True, color='orange', alpha=0.5, label='Lower Profits')
plt.fill_between(time_x, value_y_plot8, color='red', alpha=0.7, label='Losses('+str(round(value_y_plot3[period_num], 2))+'='+str(1-round(value_y_plot3[period_num], 2))+')')
plt.legend()
''
#plt.figure('P&L')
plt.subplot(1, 2, 2)
plt.grid(color='grey', linestyle='-', alpha=0.2, linewidth=1)
plt.plot(time_x, value_y_plot5, color='black', linestyle='-', label='Investment value('+str(round(value_y_plot5[period_num], 2))+')')
plt.fill_between(time_x, value_y_plot5, init_val,
                 where=(value_y_plot5 >= init_val),
                 interpolate=True, color='green', alpha=0.4, label='Multiplied Profits')
plt.fill_between(time_x, value_y_plot5, init_val,
                 where=(value_y_plot5 <= init_val),
                 interpolate=True, color='red', alpha=0.4)

plt.legend()
''
print()
print(init_val)
print(init_value)

#plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.1, hspace=None)
mng = plt.get_current_fig_manager()
mng.window.state("zoomed")
plt.show(block=False)
plt.pause(60*10)
