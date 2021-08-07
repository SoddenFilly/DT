from matplotlib import pyplot as plt # render graph
from marketprice import fetch # stock market price fetch script

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
    token_count = initial_investment / token_value # Total volume of tokens held
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
            y_init = token_count
            token_count = token_count + token_count * annual_interest
            y_axis = y_axis + [token_count]
        elif plotnum == 3:
            y_axis = fetch(False,"eth","usd",12)
            y_axis = y_axis[::-1]
            y_init = y_axis[0]
            break
        elif plotnum == 4:
            #print(y_plot[3])
            y_axis = y_axis + [y_plot[3]]*12
            y_init = y_axis[0]
            break
        elif plotnum == 5:
            interest = token_count * annual_interest + interest
            investment = investment + interest
            print(initial_investment / investment)
            print(y_plot[4][i])
            y_axis = y_axis + [initial_investment / investment * y_plot[4][1][i]]
            y_init = 0
            #print(y_axis)
    return y_axis

plot(0) # Pre-defines all variables

# Orders data into a list to be used with plt.plot()
print("yyy",y_plot)
for i in range(5): y_plot = y_plot + [y_init] + [plot(i+1)]
print("ddd",y_plot[1])
for i in range(len(y_plot[1])+1): x_axis = x_axis + [i]

#========== Graph drawing & rendering ==========#

# Top left subplot
plt.subplot(2,2,1)

#2 Compound interest on token volume
plt.plot(x_axis,y_plot[2], color='b', linestyle='-', label='Compounded Interest('+str(round(y_plot[2][0],2)) + ' ' + str(round(y_plot[2][len(y_plot[2])-1],2)) + ')')
#1 Flat interest on token volume
print("hbjhb")
plt.plot(x_axis,y_plot[1], color='k', linestyle=':', label='Flat Interest(' + str(round(y_plot[1][0],2)) + ' ' + str(round(y_plot[1][len(y_plot[1])-1],2)) + ')')

plt.legend()

# Bottom left subplot
plt.subplot(2,2,3)
#3 Token value over time
plt.plot(x_axis,y_plot[3], color='k', linestyle='-')
#4 Uniform token value from start
plt.plot(x_axis,y_plot[4], color='g', linestyle='-')
#5 
plt.plot(x_axis,y_plot[5], color='r', linestyle='-')

# Right subplot
plt.subplot(1,2,2)

# Opens graph window in full-screen mode
plt.get_current_fig_manager().window.state("zoomed")

# Keeps graph window open until close
plt.pause(10**10)






