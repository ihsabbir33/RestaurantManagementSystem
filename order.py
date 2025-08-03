import datetime

class Order:
    order_counter = 1

    def __init__(self, items):
        self.order_id = Order.order_counter
        Order.order_counter += 1
        self.items = items
        self.timestamp = datetime.datetime.now()

    def total_price(self):
        return sum(item.price if not hasattr(item, 'get_discounted_price') else item.get_discounted_price() for item in self.items)

    def __str__(self):
        item_list = "\n".join([
            f"- {item.name}: {item.get_discounted_price() if hasattr(item, 'get_discounted_price') else item.price} TK"
            for item in self.items
        ])
        return f"Order ID: {self.order_id}\nTime: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}\nItems:\n{item_list}\nTotal: {self.total_price():.2f} TK"

