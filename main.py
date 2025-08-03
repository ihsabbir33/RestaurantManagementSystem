from restaurant import Restaurant

res = Restaurant("Xenon Restaurant")

# Sample Menu
res.add_menu_item(1, "Burger", 120, "Fast Food")
res.add_menu_item(2, "Pizza", 300, "Fast Food")
res.add_menu_item(3, "Coffee", 80, "Beverage")
res.add_menu_item(4, "Rice & Chicken", 180, "Main Course")

while True:
    print("\n--- Welcome to Xenon Restaurant ---")
    print("1. Show Menu")
    print("2. Show Menu (Sorted High to Low)")
    print("3. Place Order")
    print("4. Show All Orders")
    print("5. Search Order by ID")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        res.show_menu()
    elif choice == '2':
        res.show_menu(sort_by='price_desc')
    elif choice == '3':
        ids = input("Enter item IDs (comma separated): ")
        id_list = [int(i.strip()) for i in ids.split(",") if i.strip().isdigit()]
        res.place_order(id_list)
    elif choice == '4':
        res.show_all_orders()
    elif choice == '5':
        oid = int(input("Enter Order ID: "))
        res.search_order(oid)
    elif choice == '6':
        print("👋 Thanks for visiting!")
        break
    else:
        print("❌ Invalid choice.")
