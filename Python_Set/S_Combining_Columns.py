import pandas as pd
births = pd.read_csv('https://raw.githubusercontent.com/jakevdp/data-CDCbirths/master/births.csv')

# Potential Error
# 50th Percentile/ .5 Quartile is Median
# There is difference between Mean & Median
# mu should be mean not Median (Statistically)

# Sol 1
births.groupby(['gender'])['births'].sum()

# Sol 2
births.index = pd.to_datetime(10000 * births.year +
                              100 * births.month +
                              births.day, format='%Y%m%d')
# Sol 3
births.column

# Sol 4
births.drop(['year','month','day'],axis=1)

# Sol 5
# Inplace is used to do the operation on the original dataframe
births_1 = births.drop(['year','month','day'],axis=1)
# Can be replaced by
births.drop(['year','month','day'],axis=1,inplace=True)
