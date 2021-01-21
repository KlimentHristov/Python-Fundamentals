n = int(input())
numbers = []
filtered = []

for i in range(n):
    current_num = input()
    numbers.append(current_num)
command = input()
if command == 'even':
    for x in range(len(numbers)):
        element = int(numbers[x])
        if element % 2 == 0:
            filtered.append(element)
elif command == 'odd':
    for x in range(len(numbers)):
        element = int(numbers[x])
        if element % 2 != 0:
            filtered.append(element)
elif command == 'positive':
    for x in range(len(numbers)):
        element = int(numbers[x])
        if element >= 0:
            filtered.append(element)
elif command == 'negative':
    for x in range(len(numbers)):
        element = int(numbers[x])
        if element < 0:
            filtered.append(element)
for y in range(0,len(filtered)):
    filtered[y] = int(filtered[y])
print(filtered)


