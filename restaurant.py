from menu_item import MenuItem
from order import Order

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = []
        self.orders = []

    def add_menu_item(self, item_id, name, price, category):
        item = MenuItem(item_id, name, price, category)
        self.menu.append(item)

    def show_menu(self, sort_by=None):
        items = self.menu
        if sort_by == 'price_asc':
            items = sorted(self.menu, key=lambda x: x.price)
        elif sort_by == 'price_desc':
            items = sorted(self.menu, key=lambda x: x.price, reverse=True)

        for item in items:
            print(item)

    def place_order(self, item_ids):
        items = [item for item in self.menu if item.item_id in item_ids]
        if not items:
            print("❌ Invalid item IDs.")
            return None
        order = Order(items)
        self.orders.append(order)
        print("\n✅ Order Confirmed:")
        print(order)

    def search_order(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                print("\n📦 Order Found:")
                print(order)
                return
        print("❌ Order not found.")

    def show_all_orders(self):
        print("\n🧾 All Orders:")
        for order in self.orders:
            print(order)
            print("-"*30)