class Product:
    def __init__(self, sku, name, price):
        if not sku:
            raise ValueError("sku is required")
        self.sku = sku
        self.name = name
        self.price = price
# wip 1
# wip 2
# A
print("A")# A
def apply_discount(price, percent):
    return price * (100 - percent) / 100
def add_tax(price, rate=0.2):
    return price * (1+rate)