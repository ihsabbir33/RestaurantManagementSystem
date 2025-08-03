class MenuItem:
    def __init__(self, item_id, name, price, category):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"[{self.item_id}] {self.name} - {self.price} TK ({self.category})"
