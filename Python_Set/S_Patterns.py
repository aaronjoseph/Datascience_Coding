# Pattern Problem

# Print the patterns as below using loops
"""
*
**
***
****
"""

for i in range(5):
    print('*'*i)


# Q2. Find the code for the next pattern
"""
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
"""
a = [i for i in range(6)]

for i in range(0, 6):
    for j in range(0,i):
        print(a[i]),
    print("\n")
