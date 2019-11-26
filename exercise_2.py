#2
def translate(text):
    consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K,' 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Z']
    str = ""
    new_word = ''
    for letter in text.upper():
        if letter in consonants:
            str = str + letter + 'o' + letter
        else:
            str = str + letter
    return(str.lower())

print(translate("this is fun"))
