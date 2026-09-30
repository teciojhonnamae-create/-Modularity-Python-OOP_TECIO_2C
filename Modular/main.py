from menu import get_default_menu
from order import calculate_total, calculate_discount
from ui import display_welcome, display_menu, get_order, display_receipt


def main():
    menu = get_default_menu()
    display_welcome()
    display_menu(menu)

    while True:
        start_order = input("\nWould you like to order? (yes/no): ").strip().lower()

        if start_order in ["yes", "y"]:
            break
        elif start_order in ["no", "n"]:
            print("\nThank you for visiting! Goodbye!")
            return
        else:
            print("Please answer only yes or no.")

    orders = get_order(menu)
    subtotal = calculate_total(orders)
    discount = calculate_discount(subtotal)
    total = subtotal - discount

    display_receipt(orders, subtotal, discount, total)


if __name__ == "__main__":
    main()