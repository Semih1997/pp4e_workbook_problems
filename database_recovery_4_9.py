def reinstall(db):
    i = 0
    final_data_base_keys = []
    final_data_base_values = []
    
    while i in range(len(db)):
        
        if db[i].isalpha():
            name = ""
            i_adding = 0
            while i_adding in range(500):
                if db[i:][i_adding].isalpha():
                    name += db[i:][i_adding]
                    i_adding += 1
                else:
                    name = name.lower()
                    name = name[0].upper()
                    final_data_base_keys.append(name)
                    i += i_adding
                    break
                    
        # elif db[i].isnumeric():
        #     for j in range(len(db[i:])-1):
        #         if db[i:][j].isnumeric():
        #             final_data_base_values += db[i][j]
        #         else:
        #             i += 1

        else:
            i += 1
    return final_data_base_keys
print(reinstall("| ahmet : 16 |=| Mehmet : 19 |=| selin : 32 |=| PINAR : 8 |"))