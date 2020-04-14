# For the lists below, print the combination of two lists
color_list1 = ['green', 'red', 'blue', 'yellow']
color_list2 = ['dark', 'bright', 'tinted', 'glowing']

""" 
Similar to the output below
['dark green', 'dark red', 'dark blue', 'dark yellow'],
['bright green', 'bright red', 'bright blue', 'bright yellow'], 
['tinted green', 'tinted red', 'tinted blue', 'tinted yellow'], 
['glowing green', 'glowing red', 'glowing blue', 'glowing yellow']
"""



# Solutions
[[color2 + ' ' + color1 for color1 in color_list1] for color2 in color_list2]

# Solution
for i in color_list1:
    for j in color_list2:
        print(i,j)

