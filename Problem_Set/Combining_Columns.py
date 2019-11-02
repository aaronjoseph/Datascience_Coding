# Importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# The table loaded is the births data
births = pd.read_csv('https://raw.githubusercontent.com/jakevdp/data-CDCbirths/master/births.csv')

# Code Below is trying to acheive something
# Please explain what is being done here
# If there is any potential error, please bring that up as well
quartiles = np.percentile(births['births'], [25, 50, 75])
mu, sig = quartiles[1], 0.74 * (quartiles[2] - quartiles[0])
births = births.query('(births > @mu - 5 * @sig) & (births < @mu + 5 * @sig)')

# Q1 Find the sum of Male and Female Birth


# High difficulty : Feel free to ask for direction from interviewer
# Q2. a) Combine the columns Year, Month and Day to a single column into a single column
# Q2. b) For the new column, convert it to table index
births.index = pd.to_datetime(10000 * births.year +
                              100 * births.month +
                              births.day, format='%Y%m%d')

# Q3. Show the distinct columns in the dataframe

# Q4. Remove the Year, Month & Day column

# Q5. What is your understanding of inplace command in pandas
# Why would you use inplace command ? Cite an example



