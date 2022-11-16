def delete_exams_from_exam(questions_txt,exam_txt):
    questions_line = open(questions_txt,"r")
    questions = []
    for line in questions_line:
        if line.split()[0] != "Answer":
            questions_exam = line
            questions.append(questions_exam)
    print(questions)
    with open(exam_txt,"w") as exam_sheet:
        for line in questions:
            exam_sheet.write(line)
delete_exams_from_exam('questions_5_6.txt','exam_5_6.txt')