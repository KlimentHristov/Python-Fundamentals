command = input()
dect = {}


def add_user(dect, force_Side, force_User):
    if force_Side not in dect:
        dect[force_Side] = []


    for side, members in dect.items():
        if force_User in members:
            return dect

    if force_User not in dect[force_Side]:
        dect[force_Side].append(force_User)

    return dect


def transfer_user(dect, force_Side, force_User):
    is_new = True
    for side, user in dect.items():
        if force_User in user:
            dect[side].remove(force_User)
            is_new = False
            return add_user(dect, force_Side, force_User)

    if is_new:
       return add_user(dect, force_Side, force_User)


while command != "Lumpawaroo":
    data_list = command.split(" | ")
    if len(data_list) > 1:
        force_Side, force_User = command.split(" | ")
        dect = add_user(dect, force_Side, force_User)
    else:
        force_User, force_Side = command.split(" -> ")
        dect = transfer_user(dect, force_Side, force_User)
        print(f"{force_User} joins the {force_Side} side!")
    command = input()

finally_dect = sorted(dect.items(), key=lambda x: (-len(x[1]), x[0]))

for side, members in finally_dect:
    if len(members) > 0:
        print(f"Side: {side}, Members: {len(members)}")
        for member in sorted(members):
            print(f"! {member}")