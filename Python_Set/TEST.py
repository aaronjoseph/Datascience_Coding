a = [-1, 0, 1, 2, 3, 5]

left = 0
right = len(a) - 1

while left <= right:
    mid = (left + right) // 2
    if a[mid] == mid:
        print(f"Fixed point found at index: {mid}")
        break
    elif a[mid] < mid:
        left = mid + 1
    else:
        right = mid - 1
else:
    print("No fixed point found.")