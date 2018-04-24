import numpy as np
import scipy as sc
import pandas as pd

# pd.set_option('display.max_colwidth', -1)

# import tsv and assign to variable
chipo = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv', sep='\t', header=0)

# EXERCISE: print first ten records
print(chipo.head(10))

# .info prints a dataframe of the columns (with names), the number of records in each column, and the data type of each column
print(chipo.info())
print('\n')

# EXERCISE: print num of observations in dataset
# .shape gets a tuple of the number of rows and the number of columns (in that order, so [0] will get the num of rows)
print(chipo.shape[0])
print('\n')

# EXERCISE: num of columns in dataset
# .columns returns a series (aka an array) of the column names
# len() gets the length of the series
# str() converts the value in the parameter to a string
c = str(len(chipo.columns))
col = 'This dataset has ' + c + ' columns'

print(col)

# can also do 
# print chipo.shape[1] to get the second value from the tuple (which returns (#rows, #cols))

# EXERCISE: what item was ordered the most?

# gets the count of how many times a value occurred in the 'item name' column
# melted_chipo = pd.melt(chipo, ['item_name'])
# most = melted_chipo['item_name'].value_counts()
# the above gave the incorrect response...why?

# SOLUTION
c = chipo.groupby('item_name')
c = c.sum()
c = c.sort_values(['quantity'], ascending=False)
print(c.head(1))

# EXERCISE: How many total items were ordered?
# .quantity returns a dataframe of the each rows and *the num of values in each row?*
# .sum() sums up the values from the second column from the previous data frame
print(chipo.quantity.sum())

# EXERCISE: Turn the item price into a float (LOOK INTO THIS DEEPLY)
dollarizer = lambda x: float(x[1:-1])
chipo.item_price = chipo.item_price.apply(dollarizer)

# EXERCISE: total revenue!
total_rev = (chipo['item_price'] * chipo['quantity']).sum()
print 'Revenue was $' + str(total_rev)

# EXERCISE: how many orders were made?
# .count() returns Series with number of non-NA/null observations over requested axis
# value_count() returns object containing counts of unique values
total_orders = chipo['order_id'].value_counts().count()

print str(total_orders) + " total orders were made. Nice!"

# EXERCISE: What is the average amount per order
# Total revenue / total orders = average amount per order
# avg_per_order = total_rev / total_orders
# print 'Average amount per order was $' + str((np.round(avg_per_order, 2)))
# the above is actually wrong because 

# SOLUTION
order_grouped = chipo.groupby(by=['order_id']).sum()
print order_grouped.mean().item_price

# EXERCISE: How many different items are sold?

# items = chipo.groupby(by=['item_name']).values_count()
# Why does the above not work?
# The above returns

items = chipo['item_name'].value_counts().count()
print items









