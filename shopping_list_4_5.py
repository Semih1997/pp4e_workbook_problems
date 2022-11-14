def readable(str):
    i = 0
    last_list = []
    while i in range(len(str)):
        
        if str[i].isalpha():
            name = ""
            i_adding = 0
            while i_adding in range(len(str[i:])):
                if str[i:][i_adding].isalpha():
                    name += str[i:][i_adding]
                    i_adding += 1
                else:
                    name = name.lower()
                    last_list.append(name)
                    i += i_adding
                    name = ""
                    break
        else:
            i += 1
    return "\n".join(last_list)
print(readable("LemOn,   gaRlic, PASta "),"\n")
print(readable("CheeSe, cHeesE,    CHEESE "))