from collections import defaultdict


class RestaurantAnalytics:
    def __init__(self, orders, menu):
        self.orders = orders
        self.menu = menu

    def sales_by_category(self):
        category_sales = defaultdict(float)
        for order in self.orders:
            for item in order.items:
                menu_item = next((m for m in self.menu if m.item_id == item.item_id), None)
                if menu_item:
                    category_sales[menu_item.category] += item.price
        return dict(category_sales)

    def peak_hours(self):
        hour_counts = defaultdict(int)
        for order in self.orders:
            hour = order.timestamp.hour
            hour_counts[hour] += 1
        return sorted(hour_counts.items(), key=lambda x: x[1], reverse=True)[:3]

    def average_order_value(self):
        if not self.orders:
            return 0
        total = sum(order.calculate_totals()[1] for order in self.orders)
        return round(total / len(self.orders), 2)