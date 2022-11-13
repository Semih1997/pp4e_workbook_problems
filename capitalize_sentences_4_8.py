def capitalize_sentence(sentence):
    sentence = sentence.capitalize()
    new_sentence = ""
    i = 0
    while i in range(len(sentence)):
        if sentence[i].isalpha():
            word = ""
            i_adding = 0
            for j in range(500):
                if sentence[i:][j].isalpha():
                    word += sentence[i:][j]
                    i_adding += 1
                else:
                    if not(word[len(word) - 1].isalpha()):
                        word = word.capitalize()
                        new_sentence += word
                    else:
                        new_sentence += word
                    i += i_adding
                    break
        else:
            i += 1
    return new_sentence
print(capitalize_sentence('lorem. ipsum? dolor sit amet, consectetur! adipiscing elit.'))
        