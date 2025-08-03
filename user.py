import hashlib


class UserManager:
    def __init__(self):
        self.users = {}
        self.current_user = None

    def register(self, username, password, role='customer'):
        if username in self.users:
            return False, "Username already exists"

        self.users[username] = {
            'password': self._hash_password(password),
            'role': role,
            'order_history': []
        }
        return True, "Registration successful"

    def login(self, username, password):
        user = self.users.get(username)
        if user and user['password'] == self._hash_password(password):
            self.current_user = username
            return True, "Login successful"
        return False, "Invalid credentials"

    def logout(self):
        self.current_user = None
        return True

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def add_order_to_history(self, order_id):
        if self.current_user:
            self.users[self.current_user]['order_history'].append(order_id)