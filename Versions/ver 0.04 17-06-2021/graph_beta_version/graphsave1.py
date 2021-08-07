''
from matplotlib import pyplot as plt
import time
plc = [0]
time_x = []
value_y = []
timeperiod = [1, 7, 30, 365]#day,week,month,year
for i in range(10):
    time_x = time_x + plc
    time_x[i] = 1 + time_x[i-1]
    
    value_y = value_y + plc
    value_y[i] = 1000 * 1.3565 / 365 * timeperiod[1] * time_x[i] + value_y[i-1]
time_x = plc + time_x
value_y = plc + value_y
print(time_x)
print(value_y)

plt.plot(time_x, value_y, color='b', linestyle='-', label='All devs')
plt.show()
'''
py_dev_y = [45000, 48000, 53000, 57000, 63000, 65000, 71000, 70000, 75000, 83000, 90033]
plt.plot(ages_x, py_dev_y, 'b', label='Python')

plt.xlabel('Time')
plt.ylabel('Value')
plt.title('DODO Interest Visualiseation')

plt.legend()

plt.show()

time.sleep(3)
'''
