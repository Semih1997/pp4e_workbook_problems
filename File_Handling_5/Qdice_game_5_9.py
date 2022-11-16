def dice_game(input_txt):
    input_lines = []
    with open(input_txt,"r") as input_text:
        for line in input_text:
            input_lines.append(line.split())
    candidates = {}
    first_person_point = 0
    second_person_point = 0
    last_person_point= 0
    for i in range(len(input_lines)):
        if i != 0:
            if int(input_lines[i][0]) == int(input_lines[i][1]) and int(input_lines[i][1]) == int(input_lines[i][2]):
                first_person_point += 0.33
                second_person_point += 0.33
                last_person_point += 0.33
            elif int(input_lines[i][0]) == int(input_lines[i][1]) and int(input_lines[i][1]) > int(input_lines[i][2]):
                first_person_point += 0.5
                second_person_point += 0.5
            elif int(input_lines[i][1]) == int(input_lines[i][2]) and int(input_lines[i][1]) > int(input_lines[i][0]):
                second_person_point += 0.5
                last_person_point += 0.5
            elif int(input_lines[i][0]) == int(input_lines[i][2]) and int(input_lines[i][2]) > int(input_lines[i][1]):
                first_person_point += 0.5
                last_person_point += 0.5
            elif int(max(input_lines[i])) == int(input_lines[i][0]):
                first_person_point += 1
            elif int(max(input_lines[i])) == int(input_lines[i][1]):
                second_person_point += 1
            elif int(max(input_lines[i])) == int(input_lines[i][2]):
                last_person_point += 1
        else:
            for x in range(len(input_lines[i])):
                candidates[input_lines[i][x]] = 0
    for x in range(len(candidates)):
        if x == 0:
            candidates[list(candidates)[x]] = first_person_point
        elif x == 1:
            candidates[list(candidates)[x]] = second_person_point
        elif x == 2:
            candidates[list(candidates)[x]] = last_person_point
            

    if list(candidates.values())[2] > list(candidates.values())[1] and list(candidates.values())[2] > list(candidates.values())[0]:
        return_tuple = list(candidates)[2] + " " + str(list(candidates.values())[2])
    elif list(candidates.values())[2] == list(candidates.values())[1] and list(candidates.values())[2] > list(candidates.values())[0]:
        return_tuple = list(candidates)[1] + "," + list(candidates)[2] + " " + str(list(candidates.values())[2])
    elif list(candidates.values())[2] == list(candidates.values())[0] and list(candidates.values())[2] > list(candidates.values())[1]:
        return_tuple = list(candidates)[0] + "," + list(candidates)[2] + " " + str(list(candidates.values())[2])
    elif list(candidates.values())[1] > list(candidates.values())[0] and list(candidates.values())[1] > list(candidates.values())[2]:
        return_tuple = list(candidates)[1] + " " + str(list(candidates.values())[1])
    elif list(candidates.values())[1] == list(candidates.values())[0] and list(candidates.values())[1] > list(candidates.values())[2]:
        return_tuple = list(candidates)[0] + "," + list(candidates)[1] + " " + str(list(candidates.values())[1])
    elif list(candidates.values())[0] > list(candidates.values())[1] and list(candidates.values())[0] > list(candidates.values())[2]:
        return_tuple = list(candidates)[0] + " " + str(list(candidates.values())[0])
    elif list(candidates.values())[2] == list(candidates.values())[1] and list(candidates.values())[2] == list(candidates.values())[0]:
        return_tuple = list(candidates)[0] + "," + list(candidates)[1] + list(candidates)[2] + " " + str(list(candidates.values())[1])
    return return_tuple
print(dice_game('input_5_9.txt'))