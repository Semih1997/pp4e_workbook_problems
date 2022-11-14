def cheapest_flour(input_txt_5_4,output_txt_5_4):
    
    flour_lines = open(input_txt_5_4,"r")
    price_per_kilo_list = []
    
    for line in flour_lines.readlines():
        price = int(line.split()[0])
        kilo = int(line.split()[1])
        price_per_kilo = price / kilo
        price_per_kilo_list.append(price_per_kilo)
        
    price_per_kilo_list.sort(reverse=True)

    with open(output_txt_5_4,"w") as output_lines:
        for lines in price_per_kilo_list:
            output_lines.write(str(lines)+"\n")

print(cheapest_flour('input_5_4.txt','output_5_4.txt'))