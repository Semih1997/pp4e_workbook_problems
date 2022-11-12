def single_sorted_copy(arr):
    last_list = []
    for i in range(len(arr)):
        if not(arr[i] in last_list):
            last_list.append(arr[i])
    last_list.sort()
    return last_list
print(single_sorted_copy([3, 3, 2, 2, 1, 1]))
# [1, 2, 3]

print(single_sorted_copy([1, 3, 2, 2, 1, 1, 4]))
# [1, 2, 3, 4]