def word_split(txt1):
    with open(txt1, 'r') as reader:
        words = reader.read().split()
        reader.close()
        new_words = []
    for word in words:
        word = word.strip(',.?')
        new_words.append(word)
    return new_words

def word_count(txt1):
    words = word_split(txt1)
    words = [word.lower() if isinstance(word, str) else word for word in words]
    word_dict = {}
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict