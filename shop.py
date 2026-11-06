class product:
    def __init__(self, sku, name, price):
        self.sku = sku
        self.name = name
        self.price = price
    
    def finbd_by_name(products, text):
        return [p for p in products if text.lower() in p.name.lower()]
        # note
# wip 1
# wip 2
# A
print("A")# A
