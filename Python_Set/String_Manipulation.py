import pandas as pd

s = "1#shyam#datascience#ml,2#robie#physics#economy#daTASCIence#maths," \
    "3#vignesh#robotics#maths#economy,4#preeth#geology#english#maths" \
    "#datascience#timeseries"

# Question

Q1. For the data above, form a tablular Data set and find the area of interest


# Solution 

# Area of interest
values = [j[2:] for j in [x.split('#') for x in s.split(',')]]

# Flattening the List
values_flat = []
for i in range(len(values)):
    for j in range(len(values[i])):
        values_flat.append(values[i][j])
values_flat_1 = map(str.lower,values_flat)

values_DF = pd.DataFrame(values_flat_1,columns=['Interest'])

distribution = values_DF.groupby(['Interest'])['Interest'].count()

distribution.plot()

# Solution 2

# Step 1 : Seperate the main section by (,)
a = s.split(',')
# Step 2 : Seperate the elements by ('#')
b = []
for i in a:
    b.append(i.split('#'))
dict = {}
e = list(dict.keys())

for i in b:
    q = 0
    for j in i:
        k = j.lower()
        if q < 2:
            q += 1
        else:
            if k not in e:
                dict[k] = 1
                e = list(dict.keys())
            else:
                dict[k] += 1