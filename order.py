import datetime
from collections import Counter


class Order:
    order_counter = 1

    def __init__(self, items, customer_name=""):
        self.order_id = Order.order_counter
        Order.order_counter += 1
        self.items = items
        self.customer_name = customer_name
        self.timestamp = datetime.datetime.now()
        self.status = "received"
        self.payment_method = None
        self.delivery_address = None
        self.special_instructions = ""

    def add_delivery_info(self, address):
        self.delivery_address = address
        self.is_delivery = True

    def set_payment_method(self, method):
        self.payment_method = method

    def calculate_totals(self):
        original_total = sum(item.price for item in self.items)
        discounted_total = original_total

        # Discount rules
        item_counts = Counter(item.name for item in self.items)
        for name, count in item_counts.items():
            if count >= 5:
                item_price = next(item.price for item in self.items if item.name == name)
                discounted_total -= (item_price * count) * 0.15

        if discounted_total > 500:
            discounted_total *= 0.90

        # Add delivery fee if applicable
        if hasattr(self, 'is_delivery') and self.is_delivery:
            discounted_total += 50  # Flat delivery fee

        return original_total, round(discounted_total, 2)

    def __str__(self):
        item_list = "\n".join([f"- {item.name}: ₹{item.price}" for item in self.items])
        original_total, discounted_total = self.calculate_totals()

        delivery_info = ""
        if hasattr(self, 'is_delivery') and self.is_delivery:
            delivery_info = f"\nDelivery Address: {self.delivery_address}"

        return (
            f"Order ID: {self.order_id}\n"
            f"Customer: {self.customer_name}\n"
            f"Time: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Status: {self.status}\n"
            f"Items:\n{item_list}\n"
            f"Subtotal: ₹{original_total:.2f}\n"
            f"Total: ₹{discounted_total:.2f}"
            f"{delivery_info}\n"
            f"Payment Method: {self.payment_method or 'Not specified'}"
        )