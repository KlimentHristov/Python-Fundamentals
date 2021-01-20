command = input()
a = int(input())
b = int(input())

def solve(operator,x,y):
    result = None
    if operator == 'multiply':
        result = x * y
    elif operator == 'divide':
        result = int(x/y)
    elif operator == 'add':
        result = x + y
    elif operator == 'subtract':
        result = x - y
    return result

print(solve(command,a,b))
