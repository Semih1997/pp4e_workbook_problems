def pass_or_fail(input_txt,output_txt):
    notes_lines = open(input_txt,"r")
    pass_or_fail_list = []
    for line in notes_lines.readlines():
        name = line.split()[0]
        sirname = line.split()[1]
        first_exam = int(line.split()[3])
        second_exam = int(line.split()[5])
        last_exam = int(line.split()[7])
        averaged_note = (first_exam*0.3)+(second_exam*0.3)+(last_exam*0.4)
        pass_fail = ""
        if averaged_note >= 60:
            pass_fail = "Pass"
        else:
            pass_fail = "Fail"
        pass_or_fail_list.append((name,sirname,",",pass_fail))
    for i in range(len(pass_or_fail_list)):
        "".join(str(x) for x in pass_or_fail_list[i])
    with open(output_txt,"w") as output:
        for line in pass_or_fail_list:
            output.write(str(line[0])+ " " +str(line[1])+str(line[2])+str(line[3])+"\n")
pass_or_fail("input_5_5.txt","output_5_5.txt")