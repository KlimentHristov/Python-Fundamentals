numbers = list(map(int, input().split(', ')))

indices_for = []

for i in range(len(numbers)):
    number = numbers[i]
    if number % 2 == 0:
        indices_for.append(i)
print(indices_for)
