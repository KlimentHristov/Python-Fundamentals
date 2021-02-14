words = input().split(", ")
new_words = []

for word in words:
    is_wrong = False
    for char in word:
        if 3 < len(word) < 16:
            if not char.isdigit() and not char.isalpha():
                if char != "-" and char != "_":
                    is_wrong = True
        else:
            is_wrong = True
    if not is_wrong:
        new_words.append(word)
for name in new_words:
    print(name)