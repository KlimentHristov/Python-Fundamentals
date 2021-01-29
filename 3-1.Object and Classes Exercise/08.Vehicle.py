class Vehicle:
    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money, name):
        if self.price > money:
            return "Sorry, not enough money"
        elif self.owner:
            return 'Car already sold'
        else:
            self.owner = name
            change = money - self.price
            return f"Successfully bought a {self.type}. Change: {change:.2f}"

    def sell(self):
        if self.owner:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"