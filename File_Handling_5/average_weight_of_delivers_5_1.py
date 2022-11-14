def average_weight(file):
    file = open(file,'r')
    all_lines = []
    one_one_all_list = []
    for line in file.readlines():
        all_lines.append(line.split())
    for i in range(len(all_lines)):
        for j in all_lines[i]:
            if int(j) < 125 and int(j) > 45:
                one_one_all_list.append(int(j))
    average = sum(one_one_all_list) / len(one_one_all_list)
    return average
print(average_weight("inputs_5_1.txt"))