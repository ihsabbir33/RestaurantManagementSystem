class PaymentProcessor:
    def __init__(self):
        self.transactions = []

    def process_payment(self, order, method, details=None):
        _, amount = order.calculate_totals()
        transaction = {
            'order_id': order.order_id,
            'amount': amount,
            'method': method,
            'status': 'pending'
        }

        if method.lower() == 'cash':
            transaction['status'] = 'completed'
            self.transactions.append(transaction)
            return True, "Cash payment received"

        elif method.lower() == 'card':
            if details and self.validate_card(details):
                transaction['status'] = 'completed'
                self.transactions.append(transaction)
                return True, f"Card payment processed (₹{amount})"
            return False, "Invalid card details"

        return False, "Unsupported payment method"

    def validate_card(self, details):
        return (len(details.get('number', '')) == 16 and
                details.get('expiry') and
                details.get('cvv', '').isdigit() and len(details['cvv']) == 3)

    def get_transaction_history(self):
        return self.transactions