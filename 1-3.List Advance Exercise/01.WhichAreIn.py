substrings = input().split(", ")
strings = input().split(", ")

save_list = []

for substring in substrings:
    for string in strings:
        if substring in string and substring not in save_list:
            save_list.append(substring)
print(save_list)