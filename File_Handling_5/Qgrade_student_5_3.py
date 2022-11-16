def grade_student(answer_txt,student_txt):
    answer_lines = open(answer_txt,"r")
    students_lines = open(student_txt,"r")
    answer_list =[]
    student_ans_list = []
    point_list = []
    
    for line in answer_lines.readlines(): #answer key and points
        answer = line.split()[1]
        answer_list.append(answer)
        question_point = line.split()[2]
        point_list.append(question_point)
        
    for line in students_lines.readlines(): #students answers
        student_ans = line.split()[1]
        student_ans_list.append(student_ans)
    total = 0
    for i in range(len(answer_list)):
        if answer_list[i] == student_ans_list[i]:
            total += int(point_list[i])
    return total
print(grade_student('answer_key_5_3.txt','student_5_3.txt'))