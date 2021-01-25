random = input()

def odd_even(num_word):
    num_word = str(num_word)
    sum_even = 0
    sum_odd = 0
    for element in num_word:
        if int(element) % 2 == 0:
            sum_even += int(element)
        else:
            sum_odd += int(element)
    return f"Odd sum = {sum_odd}, Even sum = {sum_even}"
print(odd_even(random))