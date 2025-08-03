from datetime import datetime


class FeedbackManager:
    def __init__(self):
        self.feedbacks = []

    def add_feedback(self, order_id, rating, comments=""):
        feedback = {
            'order_id': order_id,
            'rating': min(5, max(1, rating)),  # Clamp between 1-5
            'comments': comments,
            'timestamp': datetime.now()
        }
 rn sorted(self.feedbacks, key=lambda x: x['timestamp'], reverse=True)[:count]