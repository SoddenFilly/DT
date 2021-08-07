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
plt.plot(time_x, value_y_plot1, color='b', linestyle='-', label='Compounded Interest('+str(round(value_y_plot1[time_len], 2))+')')
plt.plot(time_x, value_y_plot2, color='k', linestyle=':', label='Flat Intrest('+str(round(value_y_plot2[time_len], 2))+')')
plt.fill_between(time_x, value_y_plot1, value_y_plot2,
                 where=(value_y_plot1 >= value_y_plot2),
                 interpolate=True, color='blue', alpha=0.1)
plt.legend()


#plt.figure('P&L')
plt.subplot(1, 2, 2)
plt.grid(color='grey', linestyle='-', alpha=0.2, linewidth=1)
plt.plot(time_x, value_y_plot5, color='b', linestyle='-', label='Investment value('+str(round(value_y_plot5[time_len], 2))+')')
plt.legend()


plt.subplot(2, 2, 3)
plt.grid(color='black', linestyle='-', alpha=0.2, linewidth=1)
plt.plot(time_x, value_y_plot3, color='r', linestyle='-', alpha=0.1)
plt.plot(time_x, value_y_plot4, color='g', linestyle='-')
plt.plot(time_x, value_y_plot6, color='k', linestyle='-', label='Token value('+str(round(value_y_plot6[time_len], 2))+')')
plt.fill_between(time_x, value_y_plot6, value_y_plot4,
                 where=(value_y_plot6 >= value_y_plot4),
                 interpolate=True, color='green', alpha=0.2, label='Multiplied Profits')
plt.fill_between(time_x, value_y_plot6, value_y_plot4,
                 where=(value_y_plot6 <= value_y_plot4),
                 interpolate=True, color='green', alpha=0.2)
plt.fill_between(time_x, value_y_plot3, value_y_plot4,
                 where=(value_y_plot3 <= value_y_plot4),
                 interpolate=True, color='orange', alpha=0.5, label='Lower Profits')
plt.fill_between(time_x, value_y_plot3, color='red', alpha=0.7, label='Losses')
plt.legend()


mng = plt.get_current_fig_manager()
mng.window.state("zoomed")
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.1, hspace=None)
plt.show(block=False)
#plt.show(block=False)
running = True

plt.pause(60*10)
    
    

    #print('luyfuyjl')
