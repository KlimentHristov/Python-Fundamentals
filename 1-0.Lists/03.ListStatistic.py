n = int(input())
positive_list = []
negative_list = []

for x in range(n):
    current_x = float(input())
    if current_x == 0 or current_x > 0:
        positive_list.append(current_x)
    elif current_x < 0:
        negative_list.append(current_x)
print(f"Count of positves: {len(positive_list)}.")
sum = sum(negative_list)
print(f"Sum of negatives: {sum:.0f}")
