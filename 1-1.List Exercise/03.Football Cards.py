cards = input()

list1 = cards.split(" ")
list2 = []

a_team = 11
b_team = 11

for i in range(len(list1)):
    if a_team < 7 or b_team < 7:
        break
    else:
        if "A" in list1[i] and list1[i] not in list2:
            a_team -= 1
            list2.append(list1[i])
        elif "B" in list1[i] and list1[i] not in list2:
            b_team -= 1
            list2.append(list1[i])

print(f"Team A - {a_team}; Team B - {b_team}")

if a_team < 7 or b_team < 7:
    print("Game was terminated")
