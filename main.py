from restaurant import Restaurant
from payment import PaymentProcessor
from feedback import FeedbackManager
from user import UserManager
from reservation import ReservationSystem
from analytics import RestaurantAnalytics

# Initialize systems
res = Restaurant("Xenon Restaurant")
payment_processor = PaymentProcessor()
feedback_manager = FeedbackManager()
user_manager = UserManager()
reservation_system = ReservationSystem()

# Sample Menu
menu_items = [
    (1, "Burger", 99, "Fast Food"),
    (2, "Pizza Slice", 95, "Fast Food"),
    (3, "Coffee", 60, "Beverage"),
    (4, "Tea", 30, "Beverage"),
    (5, "French Fries", 70, "Fast Food"),
    (6, "Noodles (Half)", 90, "Main Course"),
    (7, "Pasta Bowl", 85, "Main Course"),
    (8, "Cold Drink", 45, "Beverage"),
    (9, "Ice Cream", 50, "Dessert"),
    (10, "Sandwich", 75, "Fast Food")
]

for item in menu_items:
    res.add_menu_item(*item)


def print_boxed_title(title):
    border = "═" * (len(title) + 4)
    print(f"╔{border}╗")
    print(f"║  {title}  ║")
    print(f"╚{border}╝")


def handle_payment(order):
    print("\n💳 Payment Options:")
    print("1. Cash")
    print("2. Credit Card")
    payment_choice = input("Select payment method: ").strip()

    if payment_choice == '1':
        success, message = payment_processor.process_payment(order, 'cash')
        print(f"\n{message}")
    elif payment_choice == '2':
        card_number = input("Enter card number (16 digits): ")
        expiry = input("Enter expiry (MM/YY): ")
        cvv = input("Enter CVV: ")
        details = {'number': card_number, 'expiry': expiry, 'cvv': cvv}
        success, message = payment_processor.process_payment(order, 'card', details)
        print(f"\n{message}")
    else:
        print("❌ Invalid payment method")


def handle_feedback():
    try:
        oid = int(input("Enter Order ID for feedback: "))
        rating = int(input("Rating (1-5 stars): "))
        comments = input("Comments (optional): ")
        feedback_manager.add_feedback(oid, rating, comments)
        print("✅ Thank you for your feedback!")
    except ValueError:
        print("❌ Invalid input")


def show_analytics():
    analytics = RestaurantAnalytics(res.orders, res.menu)
    print_boxed_title("Restaurant Analytics")
    print("\n📊 Sales by Category:")
    for category, amount in analytics.sales_by_category().items():
        print(f"- {category}: ₹{amount:.2f}")
    print("\n⏰ Peak Hours:")
    for hour, count in analytics.peak_hours():
        print(f"- {hour}:00 - {hour + 1}:00: {count} orders")
    print(f"\n💰 Average Order Value: ₹{analytics.average_order_value()}")


def auth_required():
    if not user_manager.current_user:
        print("🔒 Please login first")
        return False
    return True


def main_menu():
    while True:
        print_boxed_title(f"Welcome {user_manager.current_user}")
        print("1. 🍽️  Show Menu")
        print("2. 🔽 Show Menu (Sorted)")
        print("3. 🛒 Place Order")
        print("4. 📋 Order Management")
        print("5. 💳 Payment System")
        print("6. 🌟 Feedback System")
        print("7. 🪑 Reservations")
        print("8. 📊 Analytics Dashboard")
        print("9. 👋 Logout")

        choice = input("\n👉 Enter your choice: ").strip()

        if choice == '1':
            print_boxed_title("Menu")
            res.show_menu()
        elif choice == '2':
            print_boxed_title("Menu Sorting")
            print("1. Price High to Low")
            print("2. Price Low to High")
            print("3. By Category")
            sort_choice = input("Select sorting: ").strip()
            if sort_choice == '1':
                res.show_menu(sort_by='price_desc')
            elif sort_choice == '2':
                res.show_menu(sort_by='price_asc')
            elif sort_choice == '3':
                res.show_menu(sort_by='category')
            else:
                print("❌ Invalid choice")
        elif choice == '3':
            print_boxed_title("Order Type")
            print("1. Dine-in")
            print("2. Delivery")
            order_type = input("Select order type: ").strip()
            name = input("Your Name: ")
            ids = input("Enter item IDs (comma separated): ")
            id_list = [int(i.strip()) for i in ids.split(",") if i.strip().isdigit()]

            if order_type == '1':
                order = res.place_order(id_list, name)
            elif order_type == '2':
                address = input("Delivery Address: ")
                order = res.place_order(id_list, name, address)
            else:
                print("❌ Invalid choice")
                continue

            if order:
                print("\n✅ Order Placed:")
                print(order)
        elif choice == '4':
            print_boxed_title("Order Management")
            print("1. View All Orders")
            print("2. Search Order")
            mgmt_choice = input("Select option: ").strip()

            if mgmt_choice == '1':
                res.show_all_orders()
            elif mgmt_choice == '2':
                try:
                    oid = int(input("Enter Order ID: "))
                    order = res.search_order(oid)
                    if order:
                        print("\n📦 Order Found:")
                        print(order)
                    else:
                        print("❌ Order not found.")
                except ValueError:
                    print("❌ Invalid Order ID.")
        elif choice == '5':
            print_boxed_title("Payment System")
            try:
                oid = int(input("Enter Order ID for payment: "))
                order = res.search_order(oid)
                if order:
                    handle_payment(order)
                else:
                    print("❌ Order not found")
            except ValueError:
                print("❌ Invalid Order ID")
        elif choice == '6':
            print_boxed_title("Feedback System")
            print("1. Submit Feedback")
            print("2. View Recent Feedback")
            fb_choice = input("Select option: ").strip()

            if fb_choice == '1':
                handle_feedback()
            elif fb_choice == '2':
                print("\n🌟 Recent Feedback:")
                for fb in feedback_manager.get_recent_feedbacks():
                    print(f"Order {fb['order_id']}: {fb['rating']}★ - {fb['comments']}")
        elif choice == '7':
            print_boxed_title("Reservations")
            print("1. Make Reservation")
            print("2. View Reservations")
            res_choice = input("Select option: ").strip()

            if res_choice == '1':
                name = input("Your Name: ")
                guests = int(input("Number of Guests: "))
                time = input("Reservation Time (HH:MM): ")
                reservation_system.make_reservation(name, guests, time)
            elif res_choice == '2':
                print("\n📅 Current Reservations:")
                for res_id, res_details in reservation_system.get_reservations().items():
                    print(f"{res_id}: {res_details['name']} - {res_details['guests']} guests at {res_details['time']}")
        elif choice == '8':
            show_analytics()
        elif choice == '9':
            user_manager.logout()
            print("👋 Logged out successfully")
            break
        else:
            print("❌ Invalid choice. Please try again.")
        input("\nPress Enter to continue...")


# Authentication flow
while True:
    print_boxed_title("Xenon Restaurant")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    auth_choice = input("\n👉 Enter your choice: ").strip()

    if auth_choice == '1':
        print_boxed_title("Registration")
        username = input("Choose username: ")
        password = input("Choose password: ")
        success, message = user_manager.register(username, password)
        print(message)
        if success:
            user_manager.login(username, password)
            main_menu()
    elif auth_choice == '2':
        print_boxed_title("Login")
        username = input("Username: ")
        password = input("Password: ")
        success, message = user_manager.login(username, password)
        print(message)
        if success:
            main_menu()
    elif auth_choice == '3':
        print("👋 Thank you for visiting!")
        break
    else:
        print("❌ Invalid choice. Please try again.")
    input("\nPress Enter to continue...")