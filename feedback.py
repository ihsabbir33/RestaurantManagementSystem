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
        self.feedbacks.append(feedback)
        return feedback

    def get_average_rating(self):
        if not self.feedbacks:
            return 0
        return sum(f['rating'] for f in self.feedbacks) / len(self.feedbacks)

    def get_recent_feedbacks(self, count=5):
        return sorted(self.feedbacks, key=lambda x: x['timestamp'], reverse=True)[:count]