# CICS 397A Lab 9/29
#
# Complete the following programming exercises using the Pandas framework.  Most of them should
# require no more than one or two lines of code.
#
# Pandas docs that will helpful:
#   read_csv: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
#   DataFrame: https://pandas.pydata.org/pandas-docs/stable/reference/frame.html
#   Series: https://pandas.pydata.org/pandas-docs/stable/reference/series.html
#   Index: https://pandas.pydata.org/pandas-docs/stable/reference/indexing.html


import pandas as pd


# 0. Read in the data file "mtcars.csv" into a DataFrame using pd.read_csv() and print out the 
# resulting DataFrame.

df = pd.read_csv(r"C:\Users\aaron\Downloads\mtcars.csv")
print(df)



# 1. Read it in again, but specify that the 'model' column be used as an index, and print it out.
# (Note the differences with the output from above.)
df2 = pd.read_csv(r"C:\Users\aaron\Downloads\mtcars.csv", index_col="model")
print(df2)

# 2. Print out the values of the model names contained in the Index.
print(df2.to_string(columns=['model']))

# 3. Print out the last 3 rows of the DataFrame.
print(df2.iloc[-3:])

# 4. Print out the sum of the "gear" column.
gearTotal = df2['gear'].sum()
print(gearTotal)

# 5. Print out the median value of the "hp" column.
hpMedian = df2['hp'].median()
print(hpMedian)

# 6. Print out the unique values for the "cyl" column.
cylUnique = df2['cyl'].unique()
print(cylUnique)

# 7. Print out a DataFrame containing only cars with "hp" > 100.  Hint: see
# https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html#boolean-indexing
hpMore100 = df2[df2['hp'] > 100]
print(hpMore100)

# 9. Print out the average "hp" for each group of cars determined by the "cyl" column.  Hint: see
# DataFrame.groupby() in the docs linked above.
avgHPbyCYL = df2.groupby('cyl').mean()
print(avgHPbyCYL)

# 10. Make a new column called "mpq" (miles per quart) that is equal to four times the value in the
# "mpg" column, then print the data frame with the new column.  Hint: see 
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.apply.html#pandas-series-apply

mpq = pd.Series([21,21,22.8,21.4,18.7,18.1,14.3,24.4,22.8,19.2,17.8,16.4,17.3,15.2,10.4,10.4,14.7,32.4,30.4,33.9,21.5,15.5,15.2,13.3,19.2,27.3,26,30.4,15.8,19.7,15,21.4])
df2['mpq'] = mpq.values * 4
print(df2)


