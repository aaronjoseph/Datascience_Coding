import numpy as np

generate_random_array = lambda size: np.random.choice(range(0,6), size, replace=True)

generate_random_array(4)



def can_reach_end(A):
    furthest_reach_so_far, last_index = 0, len(A) - 1
    i = 0
    while i <= furthest_reach_so_far and furthest_reach_so_far < last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, A[i] + i)
        i += 1
    return furthest_reach_so_far >= last_index

# Test examples
A1 = [3, 3, 1, 0, 2, 0, 1]
A2 = [3, 2, 0, 0, 2, 0, 1]

print(can_reach_end(A1))  # Output: True
print(can_reach_end(A2))