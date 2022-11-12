def leggo(arr,start,stop):
    i = start - 1
    while i <= stop - 1:
        arr[i] = 0
        i += 1
    return arr
print(leggo([1, 2, 3, 4, 5, 6],1,3))
print(leggo([2, 2, 7, 4, 9, 6, 1, 9, 2],3,7))

# Input:
# [1, 2, 3, 4, 5, 6]
# 1
# 3

# Output:
# [0, 0, 0, 4, 5, 6]

# Input:
# [2, 2, 7, 4, 9, 6, 1, 9, 2]
# 3
# 7

# Output:
# [2, 2, 0, 0, 0, 0, 0, 9, 2]