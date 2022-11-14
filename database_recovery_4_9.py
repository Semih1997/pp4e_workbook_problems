def reinstall(db):
    i = 0
    final_data_base_keys = []
    final_data_base_values = []
    final_database = {}
    while i in range(len(db)):

        if db[i].isalpha():
            name = ""
            i_adding = 0
            while i_adding in range(500):
                if db[i:][i_adding].isalpha():
                    name += db[i:][i_adding]
                    i_adding += 1
                    print(name)
                else:
                    name = name.lower()
                    name = name.capitalize()
                    final_data_base_keys.append(name)
                    i += i_adding
                    name = ""
                    break

        elif db[i].isnumeric():
            num = ""
            for j in range(500):
                if db[i:][j].isnumeric():
                    num += db[i:][j]
                else:
                    num = int(num)
                    final_data_base_values.append(num)
                    i += 3
                    break

        else:
            i += 1
    for k in range(len(final_data_base_keys)):
        final_database[final_data_base_keys[k]] = final_data_base_values[k]
    return final_database
print(reinstall("| ahmet : 16 |=| Mehmet : 19 |=| selin : 32 |=| PINAR : 8 |"))