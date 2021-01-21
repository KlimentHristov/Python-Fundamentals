n = int(input())
positive_list = []
negative_list = []

for x in range(n):
    current_x = int(input())
    if current_x == 0 or current_x > 0:
        positive_list.append(current_x)
    elif current_x < 0:
        negative_list.append(current_x)
print(positive_list)
print(negative_list)
sum = sum(negative_list)
print(f"Count of positives: {len(positive_list)}. Sum of negatives: {sum}")

