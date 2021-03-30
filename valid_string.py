def valid_word(seq, word):
    s2 = ''.join(seq)
    word = ''.join(word)
    if len(s2) == 0:
        return False
    s2 = s2.replace(word, '')
    if len(word)!= 0:
        word = word.replace(s2, '')
        if word in seq:
            return True
        for i in seq:
            if i in word:
                word = word.replace(i, '')
        if len(word) ==0:
            return True
    if len(s2) == 0 or s2 in seq:
        return True
    else:
        return False