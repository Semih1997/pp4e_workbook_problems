def calculate_expenses(shopping_lists):
    total_list = []
    for shopping_list in shopping_lists:
        try:
            def sum_prices(shopping_list):
                total = 0
                for (item, price) in shopping_list:
                    total += price
                return round(total, 2)
            total = 0
            total = sum_prices(shopping_list)
            total_list.append(total)
        except TypeError:
            total = 'Incoplete'
            total_list.append(total)
    return total_list
print(calculate_expenses([[("chocolate", 4.25), ("jambonbutter", 4.75), ("ice cream", 3.5), ("milk", 3.25)], [("coffee", 4.75), ("olive", 2.25), ("ice cream", 2.99)]]))
print(calculate_expenses([[("coffee", 2.5), ("milk", "dunno"), ("ice cream", 2.75)],
                        [("candy", 2.99), ("chocolate", 3.99), ("tea", 3.5), ("coffee", 2.99), ("olive", 2.99)],
                        [("tea", 3.99), ("coffee", 2.5), ("olive", 2.25), ("chocolate", 4.25), ("jambonbutter", 4.25), ("egg", 2.25)]]))
print(calculate_expenses([[("tea", 4.99), ("olive", 3.5), ("chocolate", 4.75), ("coffee", 3.99),
                         ("milk", 2.99), ("egg", 3.99), ("jambonbutter", "not sure")],
                         [("jambonbutter", 3.5), ("egg", 3.75), ("tea", 3.99), ("coffee", 4.5), ("olive", 3.75)],
                         [("jambonbutter", 3.99), ("milk", 3.5), ("chocolate", 4.25), ("ice cream", 3.5),
                          ("cheese", 2.75), ("candy", 2.75), ("tea", 4.5), ("olive", "unknown")],
                          [("ice cream", 3.99), ("olive", 3.75), ("chocolate", 2.99), ("coffee", 4.5),
                          ("milk", 3.25), ("tea", 2.25), ("candy", 4.25), ("cheese", 4.75)],
                          [("ice cream", 3.75), ("coffee", 3.25), ("candy", "unknown"),
                          ("chocolate", 3.99), ("egg", 4.99), ("olive", 3.25), ("milk", 2.5)]]))
