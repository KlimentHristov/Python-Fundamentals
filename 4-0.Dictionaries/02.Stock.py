stocks = input().split(" ")

products = {}

for element in range(0, len(stocks),2):
    key = stocks[element]
    value = int(stocks[element+1])
    products[key] =value

products_to_search = input().split(" ")

for product in products_to_search:
    if product in products:
        print(f"We have {products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")