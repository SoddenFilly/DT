from matplotlib import pyplot as plt # render graph
from marketprice import fetch # stock market price fetch script
import pandas as pd
import numpy as np
import json

y_plot = [0] # List that holds all y axis plotline data used by plt.plot
symbol = 'xrp'
symbol = symbol.upper()

#========== Functions ==========#

# Function that generates/collects data
def plot(plotnum):
    global token_count 
    global y_plot 
    global x_axis 
    global y_init
    
    initial_investment = 1000 # $
    investment = initial_investment
    token_value = 5 # $ is equivalent to 1 token
    initial_token_count = 100#initial_investment / token_value # Total volume of tokens held
    token_count = initial_token_count
    annual_interest = 20 / 100 / 12 # APY per annum
    x_axis = [] # Timespan
    y_axis = [] # Pricedata
    interest = 0
    y_init = 0
    
    for i in range(12):
        if plotnum == 1:
            y_init = token_count
            interest = token_count * annual_interest + interest
            y_axis = y_axis + [token_count + interest]
            
        elif plotnum == 2:
            y_init = initial_token_count
            token_count = token_count + token_count * annual_interest
            y_axis = y_axis + [token_count]
            
        elif plotnum == 3:
            y_axis = fetch(False,False,symbol,"usd",12)
            y_axis = y_axis[::-1]
            y_init = y_axis[0]
            break
    
        elif plotnum == 4:
            y_axis = y_axis + [y_plot[3][0]]*12
            y_init = y_axis[0]
            break

        elif plotnum == 5:
            interest = token_count * annual_interest + interest
            investment = investment + interest
            y_axis = y_axis + [initial_investment / investment * y_plot[4][i]]
            y_init = y_axis[0]

        elif plotnum == 6:
            y_axis = y_axis + [y_plot[2][i] * y_plot[3][i]]
            y_init = y_axis[0]
        
        elif plotnum == 7:
            y_axis = y_axis + [y_plot[2][i] * y_plot[4][i]]
            y_init = y_axis[0]

    return [y_init] + y_axis

plot(0) # Pre-defines all variables

# Orders data into a list to be used with plt.plot()

for i in range(7): y_plot = y_plot + [plot(i+1)]
for i in range(len(y_plot[1])): x_axis = x_axis + [i]

#========== Data export/import csv ==========#

dict = {'y_plot1': y_plot[1], 'y_plot2': y_plot[2], 'y_plot3': y_plot[3],
            'y_plot4': y_plot[4], 'y_plot5': y_plot[5], 'y_plot6': y_plot[6], 'y_plot7': y_plot[7]}

with open(r'data.json', 'w') as file:
    json_string = json.dumps(dict)
    file.write(json_string)
with open(r'data.json') as file:
    data = json.load(file)

y_plot1 = np.array(data['y_plot1'])
y_plot2 = np.array(data['y_plot2'])
y_plot3 = np.array(data['y_plot3'])
y_plot4 = np.array(data['y_plot4'])
y_plot5 = np.array(data['y_plot5'])
y_plot6 = np.array(data['y_plot6'])
y_plot7 = np.array(data['y_plot7'])

#========== Graph drawing & rendering ==========#

# Graph window name
plt.figure(symbol + " - Compounding Interest & Token Value over time")

# ---Top left subplot
plt.subplot(2,2,1)
# Gridlines
plt.grid(color='grey', alpha=0.2, linewidth=1)
#2 Compound interest on token volume
plt.plot(x_axis,y_plot2, color='k', label='Compounded Interest('+str(round(y_plot2[0],4)) + ' ' + str(round(y_plot2[len(y_plot2)-1],4)) + ')')
#1 Flat interest on token volume
plt.plot(x_axis,y_plot1, color='grey', linestyle=':', label='Flat Interest(' + str(round(y_plot1[0],4)) + ' ' + str(round(y_plot1[len(y_plot1)-1],4)) + ')')
# Light blue fill
plt.fill_between(x_axis, y_plot1, y_plot2, where=(y_plot1 < y_plot2), interpolate=True, color="blue", alpha=0.1)
                 
# Displays legend
plt.legend()

# ---Bottom left subplot
plt.subplot(2,2,3)
plt.grid(color='grey', linestyle='-', alpha=0.2, linewidth=1)
#4 Uniform token value from start
plt.plot(x_axis,y_plot4, color='g')
#5 Shows where the token value would have to drop to before the total ivestment value becomes less the the original amount
plt.plot(x_axis,y_plot5, alpha=0)
#3 Token value over time
plt.plot(x_axis,y_plot3, color='k', label='Token Value(' + str(round(y_plot3[0],4)) + ' ' + str(round(y_plot3[len(y_plot3)-1],4)) + ')')

plt.fill_between(x_axis, y_plot3, y_plot4,
                 where=(y_plot3 >= y_plot4), interpolate=True, color='green', alpha=0.2, label='Multiplied Profits')
plt.fill_between(x_axis, y_plot3, y_plot4,
                 where=(y_plot3 <= y_plot4), interpolate=True, color='green', alpha=0.2)
plt.fill_between(x_axis, y_plot5, y_plot4,
                 where=(y_plot5 <= y_plot3), interpolate=True, color='orange', alpha=0.5, label='Lower Profits')

# plt.fill_between(x_axis, y_plot3, y_plot4,
#                  interpolate=True, color='green', alpha=0.2, label='Multiplied Profits')
# plt.fill_between(x_axis, y_plot3, y_plot4,
#                  interpolate=True, color='green', alpha=0.2)
# plt.fill_between(x_axis, y_plot5, y_plot4,
#                  interpolate=True, color='orange', alpha=0.5, label='Lower Profits')
plt.fill_between(x_axis, y_plot5, color='red', alpha=0.7, label='Losses(' + str(round(y_plot5[0],4)) + ' ' + str(round(y_plot5[len(y_plot5)-1],4)) + ')')

plt.legend()

# ---Right subplot
plt.subplot(1,2,2)
plt.grid(color='grey', alpha=0.2, linewidth=1)
#6 Total investment value over time

plt.plot(x_axis,y_plot6, color='k', label='Investment Value(' + str(round(y_plot6[0],4)) + ' ' + str(round(y_plot6[len(y_plot6)-1],4)) + ')')
#7
plt.plot(x_axis,y_plot7, alpha=0)

plt.fill_between(x_axis, y_plot6, [y_plot6[0]],
    where=(y_plot6 >= [y_plot6[0]]), interpolate=True, color='orange', alpha=0.4, label='Lower Profits(' + str(round(y_plot7[0],4)) + ' ' + str(round(y_plot7[len(y_plot7)-1],4)) + ')')
plt.fill_between(x_axis, y_plot6, y_plot7,
    where=(y_plot6 >= y_plot7), interpolate=True, color='green', alpha=0.4, label='Multiplied Profits')
plt.fill_between(x_axis, y_plot6, y_plot6[0],
    where=(y_plot6 <= [y_plot6[0]]), interpolate=True, color='red', alpha=0.4, label='Losses')

plt.legend()

# Opens graph window in full-screen mode
plt.get_current_fig_manager().window.state("zoomed")

# Keeps graph window open until program termination
plt.pause(10**10)