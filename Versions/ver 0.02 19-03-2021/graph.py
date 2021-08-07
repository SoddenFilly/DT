# compound interest calculation
print(1000)
print(20)
print(20/100)
print(20/100/12)
print()
print(1000*(20/100/12))
print(1000 + 1000*(20/100/12))
print((1000 + 1000*(20/100/12))+(1000 + 1000*(20/100/12))*(20/100/12))

print()

inv = 1000
print(inv)
intr = 20
print(intr)
intr = intr/100
print(intr)
intr = intr/12
print(intr)
print()
acc = inv * intr
print(acc)
inv = inv + acc
print(inv)
#acc = inv * intr
for i in range(12):
    inv = inv + inv * intr
    print(inv)
print()

from matplotlib import pyplot as plt # render graph
from marketprice import fetch # stock market price fetch script
'''
y_axis = fetch(False,"eth","usd",12)
x_axis = []
for i in range(1,len(y)+1):
    x_axis = x_axis + [i]
y_axis = y[::-1]
#print(x,y)
#plt.plot(x,y)
plt.show(block=False)
'''
#========== Functions ==========#

# Function that generates/collects data
def plot(plotnum):
    global token_count 
    global y_plot 
    global x_axis 
    
    initial_investment = 1000 # $
    token_value = 5 # $ is equivalent to 1 token
    token_count = initial_investment / token_value # Total volume of tokens held
    annual_interest = 20 / 100 / 12 # APY per annum
    x_axis = [] # Timespan
    y_axis = [] # Pricedata
    y_plot = [0] # List that holds all y axis plotline data used by plt.plot
    interest = 0
    
    for i in range(12):
        if plotnum == 1:
            interest = token_count * annual_interest + interest
            y_axis = y_axis + [token_count + interest]
        elif plotnum == 2:
                token_count = token_count + token_count * annual_interest
                y_axis = y_axis + [token_count]
    return y_axis

plot(0) # Pre-defines all variables

# Orders data into a list to be used with plt.plot()
for i in range(2): y_plot = y_plot + [plot(i+1)]
for i in range(len(y_plot[1])): x_axis = x_axis + [i]

'''
interest = inv*(annual_interest/period_len) + interest
        
    if plotnum <= 2:
        value_y[i] = inv + interest
        if plotnum == 1:
            inv = inv + interest
'''

#========== Graph drawing & rendering ==========#

plt.plot(x_axis,y_plot[1], color='k', linestyle=':')
plt.plot(x_axis,y_plot[2], color='b', linestyle='-')

plt.pause(10**10)






