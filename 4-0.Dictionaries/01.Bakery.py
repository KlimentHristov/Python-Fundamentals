data = input().split(" ")

my_dict = {}

for element in range(0, len(data),2):
    key = data[element]
    value = int(data[element+1])
    my_dict[key] =value

print( my_dict)