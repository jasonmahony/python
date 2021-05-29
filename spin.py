def spin_words(sentence):
    new_sentence = ""
    for word in sentence.split():
        if len(word) >= 5:
            new_sentence += "".join(reversed(word)) + " "
        else:
            new_sentence += word + " "
    return new_sentence.strip()


print(spin_words("Welcome to the jungle"))