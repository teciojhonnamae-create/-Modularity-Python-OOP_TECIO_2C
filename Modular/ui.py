def display_welcome():
    print("\n==============================================")
    print("        WELCOMING YOU TO JOLLIBEE-STYLE!")
    print("==============================================")
    print("       Delicious food at affordable prices!")
    print("==============================================")


def display_menu(menu):
    print("\n==============================================")
    print("            JOLLIBEE-STYLE RESTAURANT")
    print("==============================================")
    print("                  FULL MENU")
    print("----------------------------------------------")
    print(f"{'Code':<8}{'Menu Item':<25}{'Price':>10}")
    print("----------------------------------------------")

    for code, item in menu.items():
        print(f"{code:<8}{item['name']:<25}₱{item['price']:>8.2f}")

    print("----------------------------------------------")


def get_order(menu):
    orders = []

    while True:
        display_menu(menu)

        # Validate menu code
        while True:
            item_code = input("\nEnter menu code: ").strip().upper()
            if item_code in menu:
                break
            print("Invalid menu code. Please choose from the menu.")

        # Validate quantity
        while True:
            try:
                quantity = int(input("Enter quantity: "))
                if quantity > 0:
                    break
                print("Quantity must be greater than 0.")
            except ValueError:
                print("Please enter a valid number.")

        orders.append({
            "code": item_code,
            "name": menu[item_code]["name"],
            "price": menu[item_code]["price"],
            "quantity": quantity,
            "total": menu[item_code]["price"] * quantity
        })

        print(f"\nAdded {quantity} x {menu[item_code]['name']} to your order.")

        # Ask to continue
        while True:
            another_order = input(
                "\nDo you want to order another item? (yes/no): "
            ).strip().lower()

            if another_order in ["yes", "y"]:
                break
            elif another_order in ["no", "n"]:
                return orders
            else:
                print("Please answer only yes or no.")


def display_receipt(orders, subtotal, discount, total):
    print("\n")
    print("==============================================")
    print("              JOLLIBEE-STYLE")
    print("             OFFICIAL RECEIPT")
    print("==============================================")
    print("              Thank you for dining!")
    print("----------------------------------------------")
    print(f"{'ITEM':<20}{'QTY':>5}{'PRICE':>10}{'TOTAL':>10}")
    print("----------------------------------------------")

    for order in orders:
        print(
            f"{order['name']:<20}"
            f"{order['quantity']:>5}"
            f"₱{order['price']:>9.2f}"
            f"₱{order['total']:>9.2f}"
        )

    print("----------------------------------------------")
    print(f"{'Subtotal:':<30}₱{subtotal:>9.2f}")
    print(f"{'Discount:':<30}₱{discount:>9.2f}")
    print(f"{'TOTAL:':<30}₱{total:>9.2f}")
    print("==============================================")
    print("       Thank you! Please come again!")
    print("==============================================")