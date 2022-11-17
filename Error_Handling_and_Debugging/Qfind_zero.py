def find_zero(arr):
    zero_place = -1
    counter = -1
    try:
        for i in arr:
            counter += 1
            error_control = 1/i
    except ZeroDivisionError:
        zero_place = counter
    return zero_place
print(find_zero([1,2,3,4,5]))
print(find_zero([123,35,0,46,2567]))
print(find_zero([0,1,0,1,1,0]))