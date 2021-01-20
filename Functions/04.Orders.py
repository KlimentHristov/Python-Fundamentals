product = input()
quality = int(input())


def orders(product_name, quantity):
    result = 0
    if product_name == 'coffee':
        result = quantity * 1.50
    elif product_name == 'water':
        result = quantity * 1.00
    elif product_name == 'coke':
        result = quantity * 1.40
    elif product_name == 'snacks':
        result = quantity * 2.00
    return f"{result:.2f}"


print(orders(product, quality))
