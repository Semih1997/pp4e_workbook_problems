def average_discount(list_of_changes):
    total = 0
    count = 0
    for change in list_of_changes:
        if change < 0:
            total += (- change)     # to make it positive
            count += 1
    return round((total / count), 2)    # rounding 2 digits after decimal point

def calculate_discount_averages(arrays):
    discounts = []
    for array in arrays:
        try:
            discounts.append(average_discount(array))
        except ZeroDivisionError:
            discounts.append(0)
    return discounts

print(calculate_discount_averages([[-3.25, 4.5, 3.5], [-0.25, -2, -1, -1.5], [-4.25, -0.75, -2, 4.5]]))
print(calculate_discount_averages([[2.75, 3.25, -3.25], [2.5, 1.99, 1, 1, 0.5],
                                 [-0.25, -4.5, -2.25, -4, 2, 2], [-3, -2.5, -3, -1.99, -4.5]]))
print(calculate_discount_averages([[-0.75, 4, 2.25, 3.5, -1.25, 4.5],
                                [-1.5, -2.99, 3.99, -0.25, -0.25, -2, 2.99, -4, -3.25],
                                [1.25, 0.75, 0.5, 0.25, 1.5, 0.99],
                                [0.25, 0.25, 0.75, 1.5, 2.75, 3, 2.25],
                                [-3.25, 4.5, 4.99, 4.5, -1.99]]))