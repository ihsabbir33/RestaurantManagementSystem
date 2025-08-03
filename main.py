from restaurant import Restaurant

res = Restaurant("Xenon Restaurant")

# Sample Menu: All items under ₹100
res.add_menu_item(1, "Burger", 99, "Fast Food")
res.add_menu_item(2, "Pizza Slice", 95, "Fast Food")
res.add_menu_item(3, "Coffee", 60, "Beverage")
res.add_menu_item(4, "Tea", 30, "Beverage")
res.add_menu_item(5, "French Fries", 70, "Fast Food")
res.add_menu_item(6, "Noodles (Half)", 90, "Main Course")
res.add_menu_item(7, "Pasta Bowl", 85, "Main Course")
res.add_menu_item(8, "Cold Drink", 45, "Beverage")
res.add_menu_item(9, "Ice Cream", 50, "Dessert")
res.add_menu_item(10, "Sandwich", 75, "Fast Food")

def print_boxed_title(title):
    print("╔" + "═" * (len(title) + 4) + "╗")
    print(f"║  {title}  ║")
    print("╚" + "═" * (len(title) + 4) + "╝")

while True:
    print_boxed_title("Welcome to Xenon Restaurant")
    print("1. 🍽️  Show Menu")
    print("2. 🔽 Show Menu (Sorted High to Low)")
    print("3. 🛒 Place Order")
    print("4. 📋 Show All Orders")
    print("5. 🔍 Search Order by ID")
    print("6. 🚪 Exit")

    choice = input("\n👉 Enter your choice: ").strip()

    if choice == '1':
        print_boxed_title("Menu")
        res.show_menu()
    elif choice == '2':
        print_boxed_title("Menu Sorted by Price (High to Low)")
        res.show_menu(sort_by='price_desc')
    elif choice == '3':
        st = input("Your Name:")
        print((st))
        ids = input("🆔 Enter item IDs (comma separated, e.g. 1,1,1,2): ")
        id_list = [int(i.strip()) for i in ids.split(",") if i.strip().isdigit()]
        res.place_order(id_list)
    elif choice == '4':
        print_boxed_title("All Orders")
        res.show_all_orders()
    elif choice == '5':
        try:
            oid = int(input("🔎 Enter Order ID: "))
            res.search_order(oid)
        except ValueError:
            print("❌ Invalid Order ID.")
    elif choice == '6':
        print("👋 Thanks for visiting Xenon Restaurant!")
        break
    else:
        print("❌ Invalid choice. Please try again.")
