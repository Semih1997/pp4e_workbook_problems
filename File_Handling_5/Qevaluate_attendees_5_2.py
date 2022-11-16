attendees_file = open('attendees_5_2.txt','r')
answers_file = open('key_5_2.txt','r')
all_lines = []
student_dict = {}
notes = []
for line in attendees_file:
    all_lines.append(line.split())
    for i in range(len(all_lines)):
        key_list = []
        for j in range(len(all_lines[i])):
            if j != 0:
                key_list.append(all_lines[i][j])
        student_dict[all_lines[i][0]] = key_list
answers_line = []
for line in answers_file:
    answers_line.append(line.split())
for i in range(len(answers_line)):
    correct = 0
    wrong = 0
    total = 0
    if student_dict.values()[i][j] == answers_line[j]:
        correct += 1
    elif student_dict.values()[i] != answers_line[i]:
        wrong += 1
    notes.append((student_dict.keys()[i],correct - 0.25 * wrong))
print(notes)

"""
    
    UNFINISH
    
"""