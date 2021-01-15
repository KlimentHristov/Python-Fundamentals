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
            filtered.append(numbers[x])
elif command == 'odd':
    for x in range(len(numbers)):
        element = int(numbers[x])
        if element % 2 != 0:
            filtered.append(numbers[x])
elif command == 'positive':
    for x in range(len(numbers)):
        element = int(numbers[x])
        if element > 0:
            filtered.append(numbers[x])
elif command == 'negative':
    for x in range(len(numbers)):
        element = int(numbers[x])
        if element < 0:
            filtered.append(numbers[x])
print(filtered)


