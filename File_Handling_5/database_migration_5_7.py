def database_migration(old_database,new_database):
    def seperator(a):
        words = []
        word = ""
        for i in range(len(a)):
            if a[i].isalpha() or a[i].isnumeric():
                word += a[i]
            else:
                words.append(word)
                word = ""
        return words
    data_list = []
    with open(old_database,"r") as database:
        for line in database:
            data_list.append(seperator(line))
    data_names_list = data_list[0]
    data_list.pop(0)
    for i in range(len(data_names_list)):
        data_names_list[i] = data_names_list[i] + ":"
    with open(new_database,"w") as last_database:
        for line in data_list:
            last_database.write(data_names_list[0] + line[0]+" "+line[1]+","+data_names_list[1]+line[2]+","+data_names_list[2]+line[3]+"\n")
print(database_migration("old_database_5_7.txt","new_database_5_7.txt"))
            