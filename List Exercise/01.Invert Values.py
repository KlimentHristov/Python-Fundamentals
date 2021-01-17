random_string = input()
mylist = []
for i in random_string.split():
    mylist.append(i)
for i in range(0, len(mylist)):
    mylist[i] = int(mylist[i])
for i in range(0, len(mylist)):
    if mylist[i] >= 0:
        mylist[i] *= -1
    else:
        mylist[i] = abs(mylist[i])
print(mylist)