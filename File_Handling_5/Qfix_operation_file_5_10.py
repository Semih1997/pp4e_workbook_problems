def fix_operation_file(input_text,output_text):
    input_txt = open(input_text,"r")
    output_txt = open(output_text,"w")
    seperator = 0
    process = ""
    results = []
    for line in input_txt:
        process += line.rstrip()
        seperator += 1
        if seperator == 3:
            output_txt.write(process)
            output_txt.write("\n")
            results.append(eval(process))
            seperator = 0
            process = ""
    return results
print(fix_operation_file("inputs_5_10.txt", "output_5_10.txt"))