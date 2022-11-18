def exercise_memento(text_file):
    try:
        password_file = open(text_file,"r")
        for line in password_file.readlines():
            all_numeric = True
            for i in range(len(line)-1):
                if not(line[i].isnumeric()):
                    all_numeric = False
            if all_numeric:
                print("Finally you found the correct one! The password is: ",line)
            else:
                print("Wrong file, try again!")
    except FileNotFoundError:
        print("File not found, try again!")
exercise_memento("test.txt")
exercise_memento("text_1.txt")
exercise_memento("test_2.txt")