from matplotlib import pyplot as plt # render graph
from marketprice import fetch # stock market price fetch script
import pandas as pd

y_plot = [0] # List that holds all y axis plotline data used by plt.plot

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
    initial_token_count = initial_investment / token_value # Total volume of tokens held
    token_count = initial_token_count
    annual_interest = 20 / 100 / 12 # APY per annum
    x_axis = [] # Timespan
    y_axis = [] # Pricedata
    interest = 0
    y_init = 0
    
    for i in range(12):
        if plotnum == 1:
            y_init = token_count
            #print("siis", y_init)
            interest = token_count * annual_interest + interest
            y_axis = y_axis + [token_count + interest]
        elif plotnum == 2:
            #print(token_count)
            y_init = initial_token_count
            token_count = token_count + token_count * annual_interest
            y_axis = y_axis + [token_count]
        elif plotnum == 3:
            y_axis = fetch(False,"xrp","usd",12)
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
            #print(y_axis)

        elif plotnum == 6:
            y_axis = y_axis + [y_plot[2][i] * y_plot[3][i]]
            y_init = y_axis[0]
        
        elif plotnum == 7:
            y_axis = y_axis + [y_plot[2][i] * y_plot[4][i]]
            y_init = y_axis[0]

        '''
        elif plotnum == 7:
            y_axis = y_axis + [y_plot[6][0]]*12
            y_init = y_axis[0]
            break
        '''
        '''
        elif plotnum == 4:
            print(y_plot[4])
            y_axis = y_axis + [y_plot[3]]*12
            y_init = y_axis[0]
            break
        '''
            
    #print([y_init] + y_axis)
    return [y_init] + y_axis

plot(0) # Pre-defines all variables

# Orders data into a list to be used with plt.plot()

for i in range(7): y_plot = y_plot + [plot(i+1)]
for i in range(len(y_plot[1])): x_axis = x_axis + [i]

#========== Data export/import csv ==========#

path = r'C:\Users\gabor\.python_DT\python'
'''
dict = {'valy_p1': value_y_plot1, 'valy_p2': value_y_plot2, 'valy_p3': value_y_plot3, 'valy_p4': value_y_plot4, 'valy_p5': value_y_plot5,
        'valy_p6': value_y_plot6, 'valy_p7': value_y_plot7, 'valy_p8': value_y_plot8, 'valy_p9': value_y_plot9}
df = pd.DataFrame(dict)  

df.to_csv()

data = pd.read_csv()
value_y_plot7 = data['valy_p7']

csv_dict = {'y_plot1': y_plot[1], 'y_plot2': y_plot[2], 'y_plot3': y_plot[3],
            'y_plot4': y_plot[4], 'y_plot5': y_plot[5], 'y_plot6': y_plot[6], 'y_plot7': y_plot[7]}

df = pd.DataFrame(csv_dict)

df.to_csv(path+'\data.csv')

data = pd.read_csv(path+'\data.csv')
print()
print(y_plot[6])
y_plot[6] = data[['y_plot6']]
print()
print(y_plot[6])
'''

#========== Graph drawing & rendering ==========#

# Graph window name
plt.figure("Compounding Interest & Token Value over time")

# ---Top left subplot
plt.subplot(2,2,1)
# Gridlines
plt.grid(color='k', alpha=0.2, linewidth=1)
#2 Compound interest on token volume
plt.plot(x_axis,y_plot[2], color='k', label='Compounded Interest('+str(round(y_plot[2][0],2)) + ' ' + str(round(y_plot[2][len(y_plot[2])-1],2)) + ')')
#1 Flat interest on token volume
plt.plot(x_axis,y_plot[1], color='grey', linestyle=':', label='Flat Interest(' + str(round(y_plot[1][0],2)) + ' ' + str(round(y_plot[1][len(y_plot[1])-1],2)) + ')')
# Light blue fill
plt.fill_between(x_axis, y_plot[1], y_plot[2],
                 where=(y_plot[1] >= y_plot[2]), interpolate=True, color='blue', alpha=0.1)
# Displays legend
plt.legend()

# ---Bottom left subplot
plt.subplot(2,2,3)
plt.grid(color='k', linestyle='-', alpha=0.2, linewidth=1)
#3 Token value over time
plt.plot(x_axis,y_plot[3], color='k', label='Token Value(' + str(round(y_plot[3][0],2)) + ' ' + str(round(y_plot[3][len(y_plot[3])-1],2)) + ')')
#4 Uniform token value from start
plt.plot(x_axis,y_plot[4], color='g')
#5 Shows where the token value would have to drop to before the total ivestment value becomes less the the original amount
plt.plot(x_axis,y_plot[5], alpha=0)

plt.fill_between(x_axis, y_plot[3], y_plot[4],
                 where=(y_plot[3] >= y_plot[4]), interpolate=True, color='green', alpha=0.2, label='Multiplied Profits')
plt.fill_between(x_axis, y_plot[3], y_plot[4],
                 where=(y_plot[3] <= y_plot[4]), interpolate=True, color='green', alpha=0.2)
plt.fill_between(x_axis, y_plot[5], y_plot[4],
                 where=(y_plot[5] <= y_plot[4]), interpolate=True, color='orange', alpha=0.5, label='Lower Profits')
plt.fill_between(x_axis, y_plot[5], color='red', alpha=0.7, label='Losses(' + str(round(y_plot[5][0],2)) + ' ' + str(round(y_plot[5][len(y_plot[5])-1],2)) + ')')

plt.legend()

# ---Right subplot
plt.subplot(1,2,2)
plt.grid(color='k', alpha=0.2, linewidth=1)
#6 Total investment value over time
plt.plot(x_axis,y_plot[6], color='k', label='Investment Value(' + str(round(y_plot[6][0],2)) + ' ' + str(round(y_plot[6][len(y_plot[6])-1],2)) + ')')
#7
plt.plot(x_axis,y_plot[7], alpha=1)

plt.fill_between(x_axis, y_plot[6], [y_plot[6][0]],
                 where=(y_plot[6] >= [y_plot[6][0]]),
                 interpolate=True, color='orange', alpha=0.4, label='Lower Profits')
plt.fill_between(x_axis, y_plot[6], [y_plot[6][0]],
                 where=(y_plot[6] <= [y_plot[6][0]]),
                 interpolate=True, color='red', alpha=0.4)
plt.fill_between(x_axis, y_plot[6], y_plot[7],
                 where=(y_plot[6] >= y_plot[7]),
                 interpolate=True, color='green', alpha=0.4)    
plt.legend()

# Opens graph window in full-screen mode
plt.get_current_fig_manager().window.state("zoomed")

# Keeps graph window open until close
plt.pause(10**10)
    
