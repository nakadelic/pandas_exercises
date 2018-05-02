import numpy as np
import scipy as sc
import pandas as pd

# pd.set_option('display.max_colwidth', -1)

# import tsv and assign to variable
chipo = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv', sep='\t', header=0)

# STEP 5: What is the price of each item?

chipo2 = chipo.loc[:, ['item_name', 'item_price']]

# was trying to drop duplicates below but there is a native function for that in pandas
chipo3 = chipo.groupby('item_name')

#print chipo3

# http://www.ritchieng.com/pandas-selecting-multiple-rows-and-columns/

# STEP 6: Sort by the name of the item

#print chipo.sort_values(by='item_name')

# STEP 7: What was the quantity of the most expensive item ordered?

expsv = ''
qty = ''

# the below returns a dataframe sorted by the item price (descending)
#
chipo_sorted = chipo.sort_values(by = ['item_price','quantity'], ascending=False)
print chipo_sorted

series = chipo_sorted.iloc[0, :]
type(series)
expsv = str(series['item_name'])
# print expsv

# print 'The most expensive item was ' + expsv + ' and ' + qty + ' were ordered'

