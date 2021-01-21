strings = input()
begars = int(input())

mylist = strings.split(", ")
number_list = list(range(begars))

for i in range(0,len(number_list)):
    number_list[i] = 0

counter = 0

for i in range(0, len(mylist)):
    mylist[i] = int(mylist[i])

for element in mylist:
    number_list[counter] += element
    counter += 1
    if counter >= begars:
        counter = 0

print(number_list)




