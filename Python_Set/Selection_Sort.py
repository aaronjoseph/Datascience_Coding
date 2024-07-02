
my_list = [64, 25, 12, 22, 11]

l = len(my_list)

for i in range(l):
    primary_index = i
    for j in range(i+1, l):
        if my_list[j] < my_list[primary_index]:
            primary_index = j
    my_list[i], my_list[primary_index] = my_list[primary_index], my_list[i]
