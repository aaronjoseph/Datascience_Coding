# Reduce : Used to compress the list to a single value
# Lambda : Used to create a function
from functools import reduce

# Define Lambda sum_val, which adds two values x1 & x2
sum_val = lambda x1,x2: x1+x2

list_1 = [1,2,3,4]
# Reduce list_1 to sum of all values
print(reduce(sum_val,list_1))

# Map Function : The Map function will be applied to all the elements
# Apply the map function to the list and find the length of each element

list_2 = ['Tina', 'Raj', 'Tom']
print(list(map(len, list_2)))



