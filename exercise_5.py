
#5
def overlapping(lst1,lst2):
    for i in lst1:
        for k in lst2:
            if(i == k):
                return True
    return False
