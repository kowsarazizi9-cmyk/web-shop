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
def apply_discount(price, percent):
    """Apply a percentage discount to a price."""
    if not (0 <= percent <= 100):
        raise ValueError("percent must be between 0 and 100")
    return price * (1 - percent / 100)