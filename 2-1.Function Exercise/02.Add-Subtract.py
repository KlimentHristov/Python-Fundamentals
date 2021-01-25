def sum_numbers(a, b):
    res = a + b
    return res


def subtract(a, b):
    result = a - b
    return result

n1 = int(input())
n2 = int(input())
n3 = int(input())

sum = sum_numbers(n1,n2)
all = subtract(sum,n3)

print(all)



