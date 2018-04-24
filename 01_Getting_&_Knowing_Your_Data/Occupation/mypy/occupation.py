import numpy as np
import scipy as sc
import pandas as pd

# pd.set_option('display.max_colwidth', -1)

# import psv from the web and assign to variable
# use double quotes as opposed to single quotes (often used with /t)
occ = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user', sep="|", header=0)

# EXERCISE: See the first 25 entries
occ.head(25)

# EXERCISE: See last 10 entries
occ.tail(10)

# EXERCISE: num of observations in dataset

# did not remember the first time
occ.shape[0]

# EXERCISE: num of columns in dataset
str(len(occ.columns))

# EXERCISE: name of all columns
occ.columns

# EXERCISE: how is the dataset indexed?
# .index returns the start, stop value, and the 'steps' from one value to the next (re: indexing)
occ.index

# EXERCISE: datatype of each column
occ.info()

# EXERCISE: Print only the occupation column
# how to print only a certain column?
# .iloc allows you to select a row, column, or both. row first, column second.
# https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
# occ.iloc[:,3]

# EXERCISE: How many different occupations there are in this dataset
# IDK
# formula --> data_frame.col_name.unique() returns a series of each unique value in the column
# len(occ.occupation.unique())

# EXERCISE 13: What is the most frequent occupation
# IDK...REVIEW THIS ONE
# print occ.occupation.value_counts()

# EXERCISE 14: Summarize the DataFrame
print 'SUMMARY BELOW'
print occ.describe()

# EXERCISE 15: Summarize all the columns
print 'The Column Summary will be printed below: \n---Column Summary---'

# look into the function below (the DataFrame.describe)
col_sum = occ.describe(include = 'all')
print col_sum

# EXERCISE 16: Summarize only the occupation column
# The following is wrong --> print occ.groupby('occupation').describe()
print '\nSUMMARY OF OCCUPATION COLUMN BELOW \n'
print occ.occupation.describe()

# EXERCISE 17: What is the mean age of users?
mean = occ.age.mean()
print 'The mean age of users is: ' + str(mean)

# also consider the round() function to round the value of the 'mean'

# EXERCISE 18: What is the age with least occurrence?
# What is the difference between Series.value_counts and Series.value_counts() ?
# What is different when value_counts has parentheses?
