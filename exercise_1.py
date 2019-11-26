#1
def example():
    values = input("Enter a sequence of comma-separated numbers")
    temp = values.split(",")
    xlist = list(temp)
    xtuple = tuple(temp)
    print("List: " + str(xlist))
    print("Tuple: " + str(xtuple))

example()