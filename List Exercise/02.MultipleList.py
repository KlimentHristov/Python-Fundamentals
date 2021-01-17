factor = int(input())
count = int(input())

empty = []

for i in range(1,count+1):
    i *=factor
    empty.append(i)
print(empty)