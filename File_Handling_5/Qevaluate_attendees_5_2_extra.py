attendees_file = open("attendees_5_2.txt","r")
key_file = open("key_5_2.txt","r")
key = key_file.read().split()
key_file.close()
notes = []
for line in attendees_file.readlines():
    correct = 0
    wrong = 0
    name = line.split()[0]
    answers = line.split()[1:]
    for i in range(len(key)):
        if answers[i] == key[i]:
            correct += 1
        else:
            wrong += 1
    notes.append((name,correct - 0.25 * wrong))
attendees_file.close()
sorted_notes = sorted(notes,key=lambda item: item[1],reverse=True)
print(notes)
print(key)