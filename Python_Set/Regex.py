import re 

Data = "133-01.txt and 133-21.txt and 133-91.txt and 133-100.txt and 133-79"

# Q1. For the question above, usinig regex, filter for all text files with the number ending 91,79 
# Incase if the text doesn't happen to be there, it should operate in OR condition



# Solution 
# S1. 
m = re.searchall(r'(133)(:?\-)(79|99|100)',a)
print(m)