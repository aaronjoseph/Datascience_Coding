from typing import  List
def generate(numRows: int) -> List[List[int]]:
    # Result list to store all rows of Pascal's triangle
    res = []
    # Loop through each row index from 0 to numRows-1
    for i in range(numRows):
        # Initialize the current row with all 1's (we will update it later)
        row = [1] * (i + 1)
        # Update the middle elements (if any), which are the sum of the two elements from the previous row
        for j in range(1, i):
            row[j] = res[i - 1][j - 1] + res[i - 1][j]
        # Append the current row to the result
        res.append(row)
    return res

generate(4)


n = 6

# Initialize the results list with each row having (i+1) elements, all set to 'i'
results = [[1] * (i + 1) for i in range(n)]

# Print initial triangle structure
print("\nInitial structure of Pascal's Triangle:")
for row in results:
    print(row)

# Generate Pascal's Triangle
for i in range(n):
    for j in range(1, i):
        results[i][j] = results[i - 1][j - 1] + results[i - 1][j]
        print(f"\nUpdating results[{i}][{j}] = results[{i-1}][{j-1}] ({results[i-1][j-1]}) + results[{i-1}][{j}] ({results[i-1][j]}) = {results[i][j]}")

# Print final Pascal's Triangle
print("\nFinal Pascal's Triangle:")
for row in results:
    print(row)