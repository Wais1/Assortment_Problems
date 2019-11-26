#7
def maps_list(lst):
    new_list = []
    for word in lst:
        new_list.append(len(word))
    return new_list

print(maps_list(['hello','dog','cat']))
