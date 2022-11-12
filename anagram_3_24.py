def anagram(x,y):
    control = 0
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] == y[j]:
                x.replace(x[i],"")
                y.replace(y[j],"")
                control += 1
    if control == len(x) and (len(x) == len(y)):
        return True
    else:
        return False
print(anagram("palm","lamp"))
print(anagram('hello', 'olla'))