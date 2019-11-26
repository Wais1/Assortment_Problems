#8
def find_longest_word(lwords):
    max_length = 0
    for word in lwords:
        if len(word) > max_length:
            max_length = len(word)
    return(max_length)
