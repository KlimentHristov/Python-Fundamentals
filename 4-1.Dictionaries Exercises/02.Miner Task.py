text = input()

save_list = []

while not text == "stop":
    save_list.append(text)
    quantity = int(input())
    save_list.append(quantity)

    text = input()

my_dict = {}

for i in range(0, len(save_list), 2):
    key = save_list[i]
    value = save_list[i + 1]
    if key in my_dict:
        my_dict[key] += value
    else:
        my_dict[key] = value

for key, value in my_dict.items():
    print(f"{key} -> {value}")
