def append_reverse(input_txt):
    name_list = []
    with open(input_txt,"r") as input_text:
        for line in input_text:
            name = line.split()[0]
            sir_name = line.split()[1]
            names = (name,sir_name)
            name_list.append(names)
    with open(input_txt,"a") as input_text:
        for line in name_list:
            input_text.write("\n"+line[1]+" "+line[0])
    return name_list
print(append_reverse("input_5_8.txt"))