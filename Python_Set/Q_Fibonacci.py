# Given below is the fibonacci function which gives the nth fibonacci values

# Find the potential flaw with the program
def fibonacci(n):
    a = NULL
    b = NULL
    if n < 0:
        pass
    elif n == 0:
        return False
    elif n == 1:
        return False
    else:

        return True

"""
The optimal output needs to be
Input : 0 Output : 0
Input : 1 Output : 1
Input : 2 Output : 1
Input : 3 Output : 2
Input : 4 Output : 3
"""
print(fibonacci(9))

