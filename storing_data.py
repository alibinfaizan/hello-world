import pandas as pd
import numpy as np

t = int(input('How many items you purchased? \n'))

d1 = {}
item_list = []
price_list = []

for i in range(0,t):
    item = input(f"Item {i+1} : ").upper()
    price = int(input('Item Price :'))
    item_list.append(item)
    price_list.append(price)
    print('\n')
item_list.append('Total')
s = sum(price_list)
price_list.append(s)

d1['Items'], d1['Price'] = item_list, price_list

df = pd.DataFrame(d1)
df.to_csv('bill.csv')
print('Data has stored is the database.')
