card_string = input()
faroshuffle = int(input())

mylist = []
newlist =[]
firstList =[]
secondList = []


# all list
for i in card_string.split():
    mylist.append(i)
firstElement = mylist[0]
lastElement = mylist[-1]

# first List
for y in range(1,len(mylist)//2):
    firstList.append(mylist[y])

# second list
for x in range(len(mylist)//2,len(mylist)-1):
    secondList.append(mylist[x])

for n in range(faroshuffle):
    for m in range(len(firstList)):
        newlist.append(secondList[m])
        newlist.append(firstList[m])
    firstList = newlist[:len(newlist)//2]
    secondList = newlist[len(newlist)//2:]
    newlist.clear()

newlist = firstList + secondList
newlist.insert(0,firstElement)
newlist.append(lastElement)
print(newlist)