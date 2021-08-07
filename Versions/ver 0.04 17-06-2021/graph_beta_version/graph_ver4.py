from matplotlib import pyplot as plt
import random
import time

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
init_inv = int(input('Initial investment: '))
token_val = 1



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

        value_y = value_y + [1]
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
            value_y[i] = value_y_plot1[i] * (token_val * value_y_plot6[i])

        elif plotnum == 6:
            value_y[i] += random.randint(-3,3) / 10
            
            

    time_x = [0] + time_x
    
    if plotnum == 1:
        value_y = [init_inv] + value_y

    elif plotnum == 2:
        value_y = [init_inv] + value_y
        
    elif plotnum == 3:
        value_y = [1] + value_y
    
    elif plotnum == 4:
        value_y = [1] + value_y
  
    elif plotnum == 5:
        pass
        #value_y = [init_inv * token_val] + value_y

    elif plotnum == 6:
        value_y = [1] + value_y

plot(1, 0)
print(time_x, value_y)
value_y_plot1 = value_y

plot(2, 0)
print(time_x, value_y)
value_y_plot2 = value_y

plot(3, 0)
print(time_x, value_y)
value_y_plot3 = value_y

plot(4, 0)
print(time_x, value_y)
value_y_plot4 = value_y

plot(6, 0)
print("actual value", time_x, value_y)
value_y_plot6 = value_y

plot(5, 1)
print(time_x, value_y)
value_y_plot5 = value_y

plt.figure("Compounding Interest & Token Value over time")

plt.subplot(2, 2, 1)
plt.grid(color='grey', linestyle='-', alpha=0.2, linewidth=1)
plt.plot(time_x, value_y_plot1, color='b', linestyle='-', label='Compounded Interest('+str(round(value_y_plot1[period_num], 2))+')')
plt.plot(time_x, value_y_plot2, color='k', linestyle=':', label='Flat Interest('+str(round(value_y_plot2[period_num], 2))+')')
plt.fill_between(time_x, value_y_plot1, value_y_plot2,
                 where=(value_y_plot1 >= value_y_plot2),
                 interpolate=True, color='blue', alpha=0.1)
plt.legend()

#plt.figure('P&L')
plt.subplot(1, 2, 2)
plt.grid(color='grey', linestyle='-', alpha=0.2, linewidth=1)
plt.plot(time_x, value_y_plot5, color='b', linestyle='-', label='Investment value('+str(round(value_y_plot5[period_num], 2))+')')
plt.legend()

plt.subplot(2, 2, 3)
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

#plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.1, hspace=None)
mng = plt.get_current_fig_manager()
mng.window.state("zoomed")
plt.show(block=False)
plt.pause(60*10)
