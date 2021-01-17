strings = input()
n = int(input())

mylist = []

# convert strings in list
for i in strings.split():
    mylist.append(int(i))

for x in range(n):
    mylist.remove(min(mylist))

print(mylist)



