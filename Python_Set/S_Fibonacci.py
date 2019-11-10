# Given below is the fibonacci function which gives the nth fibonacci values

# Correct the function such that it provides the right output
def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b

"""
The optimal output needs to be
Input : 0 Output : 0
Input : 1 Output : 1
Input : 2 Output : 1
Input : 3 Output : 2
Input : 4 Output : 3
"""
print(fibonacci(9))

