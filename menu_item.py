class MenuItem:
    def __init__(self, item_id, name, price, category):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"[{self.item_id}] {self.name} - {self.price} TK ({self.category})"

# Child class: DiscountedItem → Demonstrates Inheritance and Polymorphism
class DiscountedItem(MenuItem):
    def __init__(self, item_id, name, price, category, discount_percent):
        super().__init__(item_id, name, price, category)
        self.discount_percent = discount_percent

    def get_discounted_price(self):
        return self.price * (1 - self.discount_percent / 100)

    # Overriding __str__ → Polymorphism
    def __str__(self):
        return f"[{self.item_id}] {self.name} - {self.get_discounted_price():.2f} TK after {self.discount_percent}% OFF ({self.category})"

