a = input()
b = input()
def character(a, b):
    mylist = []
    for i in range(ord(a)+1, ord(b)):
        mylist.append(i)
    for x in range(0, len(mylist)):
        mylist[x] = chr(mylist[x])
    characters = " "
    return (characters.join(mylist))

print(character(a,b))
