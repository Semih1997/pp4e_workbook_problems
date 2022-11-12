def helping_derero(total,height,width):
    if total <= 0:
        return total == 0
    elif helping_derero(total-height,height,width):
        return True
    elif helping_derero(total-width,height,width):
        return True
if helping_derero(19,5,3):
    print("YES")
else:
    print("NO")
if helping_derero(97,12,17):
    print("YES")
else:
    print("NO")
if helping_derero(1000000,30000,50000):
    print("YES")
else:
    print("NO")
if helping_derero(14,3,10):
    print("YES")
else:
    print("NO")

# Input:
# 19
# 5
# 3

# Output:
# YES

# Input:
# 97
# 12
# 17

# Output:
# NO

# Input:
# 1000000
# 3
# 5

# Output:
# NO