n = int(input())
text = input()
alllist = []

for i in range(n):
    current_text = input()
    alllist.append(current_text)
print(alllist)

for i in range(len(alllist)-1,-1,-1):
    element = alllist[i]
    if text not in element:
        alllist.remove(element)
print(alllist)