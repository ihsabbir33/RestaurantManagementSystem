class InventoryManager:
    def __init__(self):
        self.items = {}
        self.threshold = 5  # Default low stock threshold

    def add_item(self, name, quantity, unit, supplier):
        self.items[name.lower()] = {
            'quantity': quantity,
            'unit': unit,
            'supplier': supplier,
            'alert': False
        }

    def update_stock(self, item_name, amount_used):
        item = self.items.get(item_name.lower())
        if item:
            item['quantity'] -= amount_used
            if item['quantity'] < self.threshold:
                item['alert'] = True
                return f"LOW STOCK: {item_name} ({item['quantity']} {item['unit']} left)"
        return None

    def get_low_stock_items(self):
        return [name for name, item in self.items.items() if item['alert']]

    def restock_item(self, item_name, amount):
        if item_name.lower() in self.items:
            self.items[item_name.lower()]['quantity'] += amount
            self.items[item_name.lower()]['alert'] = False
            return True
        return False