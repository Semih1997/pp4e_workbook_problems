def buy_hats(arr,int):
    arr.sort()
    i = 0
    spend_money = 0
    while i in range(len(arr)) and spend_money < int:
        spend_money += arr[i]
        i += 1
    return i
print(buy_hats([12, 3, 7, 5, 4, 8], 12))
print(buy_hats([4, 3, 6, 2, 5, 5], 27))