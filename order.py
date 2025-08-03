import datetime
from collections import Counter

class Order:
    order_counter = 1

    def __init__(self, items):
        self.order_id = Order.order_counter
        Order.order_counter += 1
        self.items = items
        self.timestamp = datetime.datetime.now()

    def calculate_totals(self):
        original_total = sum(item.price for item in self.items)
        discounted_total = original_total

        # Rule 1: Same item 5+ times → 15% discount
        item_counts = Counter(item.name for item in self.items)
        for name, count in item_counts.items():
            if count >= 5:
                item_price = next(item.price for item in self.items if item.name == name)
                discounted_total -= (item_price * count) * 0.15

        # Rule 2: Total > 500 → 10% overall discount
        if discounted_total > 500:
            discounted_total *= 0.90

        return original_total, discounted_total

    def __str__(self):
        item_list = "\n".join([
            f"- {item.name}: {item.price} TK" for item in self.items
        ])
        original_total, discounted_total = self.calculate_totals()
        return (
            f"Order ID: {self.order_id}\n"
            f"Time: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Items:\n{item_list}\n"
            f"Total (before discount): {original_total:.2f} TK\n"
            f"Total (after discount): {discounted_total:.2f} TK"
        )
