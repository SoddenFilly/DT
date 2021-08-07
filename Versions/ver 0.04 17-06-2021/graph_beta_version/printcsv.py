import pandas as pd
from matplotlib import pyplot as plt

line = 'migimong'
#WRITE CSV
dict = {'line': line}
df = pd.DataFrame(dict)  
# saving the dataframe  
df.to_csv(r'C:\Users\gabor\apitest\python_game\data1.csv')



data = pd.read_csv(r'C:\Users\gabor\apitest\python_game\data1.csv')
csvline = data['line']

print(csvline)
