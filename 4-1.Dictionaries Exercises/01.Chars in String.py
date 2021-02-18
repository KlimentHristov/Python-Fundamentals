text = input()

filter_text = [w for w in text if len(text) > 1]

for el in filter_text:
    if el == " ":
        filter_text.remove(el)

text_dict = {i:filter_text.count(i) for i in filter_text}

for key, value in text_dict.items():
    print(f"{key} -> {value}")








