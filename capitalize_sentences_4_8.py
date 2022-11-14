def capitalize_sentence(sentence):
    capital_sign = ["!",".","?"]
    sentence_list = list(sentence)
    for i in range(len(sentence)):
        if i == 0:
            sentence_list[i] = str(sentence[i].upper())
        elif sentence[i] == " ":
            if sentence[i-1] in capital_sign:
                sentence_list[i+1] = str(sentence[i+1].upper())
    return "".join(sentence_list)
print(capitalize_sentence('string methods are really useful in Python! you need to know them to succeed in CENG240.'))
print(capitalize_sentence('lorem. ipsum? dolor sit amet, consectetur! adipiscing elit.'))