import random
# arr1 = sorted([random.randint(1, 100) for i in range(10)])
# arr2 = sorted([random.randint(1, 100) for i in range(10)])
arr1 = [11, 30, 31, 39, 42, 58, 64, 68, 87, 98]
arr2 = [17, 41, 41, 42, 49, 68, 72, 73, 78, 94]

p1=0
p2=0

res = [float('inf')]

while p1 < len(arr1) and p2 < len(arr2):
    n1 = arr1[p1] if p1 < len(arr1) else float("inf")
    n2 = arr2[p2] if p2 < len(arr2) else float("inf")

    x = min(n1, n2)
    print(x)

    if res[-1] != x:
        res.append(x)

    if p1 < len(arr1) and arr1[p1] == x: p1+=1
    if p2 < len(arr2) and arr2[p2] == x: p2+=1

res = res[1:]
print(res)

