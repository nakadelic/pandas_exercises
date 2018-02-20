import numpy as np
import scipy as sc
import pandas as pd

# pd.set_option('display.max_colwidth', -1)

# import tsv and assign to variable
chipo = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv', sep='\t', header=0)

# print first ten records
print(chipo.head(10))

# .info prints a dataframe of the columns (with names), the number of records in each column, and the data type of each column
print(chipo.info())
print('\n')

# print num of observations in dataset
print(chipo.shape[0])
print('\n')

# num of columns in dataset
c = str(len(chipo.columns))
col = 'This dataset has ' + c + ' columns'

print(col)

# prints list of column names (headers)
# print(chipo.columns)

print(chipo.apply(pd.value_counts))

# what item was ordered the most?
# organizes the data
melted_chipo = pd.melt(chipo, ['item_name'])

# gets the count of how many times a value occurred in the 'item name' column
# most = melted_chipo['item_name'].value_counts()
# the above gave the incorrect response...why?

# solution
c = chipo.groupby('item_name')
c = c.sum()
c = c.sort_values(['quantity'], ascending=False)
print(c.head(1))

# print(c)
print('\n')
print(chipo.quantity.sum())

# Turn the item price into a float (what is this?)
dollarizer = lambda x: float(x[1:-1])
chipo.item_price = chipo.item_price.apply(dollarizer)

# total revenue!
total_rev = (chipo['item_price'] * chipo['quantity']).sum()
print 'Revenue was $' + str(total_rev)

# how many orders were made?

# returns the order ids and how many times they appeared
total_orders = chipo['order_id'].value_counts().count()

print str(total_orders) + " total orders were made. Nice!"

# What is the average amount per order
# Total revenue / total orders = average amount per order
# the below is actually wrong
avg_per_order = total_rev / total_orders

print '\n'
# print 'Average amount per order was $' + str((np.round(avg_per_order, 2))) + ". No it's not."

order_grouped = chipo.groupby(by=['order_id']).sum()

print order_grouped.mean().item_price

# How many different items are sold?

# items = chipo.groupby(by=['item_name']).values_count()

items = chipo['item_name'].value_counts().count()

print items









