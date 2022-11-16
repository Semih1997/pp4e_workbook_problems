def fix_operation_file(input_text,output_text):
    line_list = []
    with open(input_text,"r") as inputs:
        for line in inputs:
            line_list.append(line.split())
    return line_list
print(fix_operation_file("inputs_5_10.txt", "output_5_10.txt"))