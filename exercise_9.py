
#9
def filter_long_words(lwords, n):
    new_words = []
    for word in lwords:
        if(len(word) > n):
            new_words.append(word)
    return(new_words)
