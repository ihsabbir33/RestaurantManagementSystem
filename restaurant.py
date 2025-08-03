from menu_item import MenuItem
from order import Order
from payment import PaymentProcessor
from feedback import FeedbackManager
from inventory import InventoryManager
from user import UserManager
from reservation import ReservationSystem
from analytics import RestaurantAnalytics


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = []
        self.orders = []
        self.payment_processor = PaymentProcessor()
        self.feedback_manager = FeedbackManager()
        self.inventory_manager = InventoryManager()
        self.user_manager = UserManager()
        self.reservation_system = ReservationSystem()
        self.analytics = RestaurantAnalytics(self.orders, self.menu)

    def add_menu_item(self, item_id, name, price, category):
        item = MenuItem(item_id, name, price, category)
        self.menu.append(item)

    def show_menu(self, sort_by=None):
        items = self.menu
        if sort_by == 'price_asc':
            items = sorted(self.menu, key=lambda x: x.price)
        elif sort_by == 'price_desc':
            items = sorted(self.menu, key=lambda x: x.price, reverse=True)
        elif sort_by == 'category':
            items = sorted(self.menu, key=lambda x: x.category)

        for item in items:
            print(item)

    def place_order(self, item_ids, customer_name="", delivery_address=None):
        items = []
        for item_id in item_ids:
            item = next((item for item in self.menu if item.item_id == item_id), None)
            if item:
                items.append(item)

        if not items:
            print("❌ Invalid item IDs.")
            return None

        order = Order(items, customer_name)
        if delivery_address:
            order.add_delivery_info(delivery_address)

        self.orders.append(order)
        return order

    def search_order(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                return order
        return None

    def show_all_orders(self):
        if not self.orders:
            print("No orders yet.")
            return
        for order in self.orders:
            print(order)
            print("-" * 40)

    def add_reservation(self, name, guests, time):
        self.reservations.append({
            'name': name,
            'guests': guests,
            'time': time
        })
        print(f"✅ Table reserved for {name} ({guests} guests) at {time}")

    def show_reservations(self):
        if not self.reservations:
            print("No reservations yet.")
            return
        for res in self.reservations:
            print(f"{res['time']}: {res['name']} ({res['guests']} guests)")
