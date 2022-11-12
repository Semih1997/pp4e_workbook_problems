def min_to_max(x,y,z):
    num_list=[x,y,z]
    summing = sum(num_list)
    mid_num = summing - min(x,y,z) - max(x,y,z)
    last_order = str(min(x,y,z)) + " " + str(mid_num) + " " + str(max(x,y,z))
    return last_order
print(min_to_max(20,10,15))
print(min_to_max(8,13,1))



# Input:
# 20
# 10
# 15

# Output:
# 10 15 20

# Input:
# 8
# 13
# 1

# Output:
# 1 8 13