from ordering_system import RestaurantManager


def main():
    restaurant = RestaurantManager()
    restaurant.display_welcome()
    restaurant.menu.display()

    while True:
        start_order = input("\nWould you like to order? (yes/no): ").strip().lower()
        if start_order in ["yes", "y"]:
            break
        elif start_order in ["no", "n"]:
            print("\nThank you for visiting! Goodbye!")
            return
        else:
            print("Please answer only yes or no.")

    restaurant.take_order()
    restaurant.print_receipt()


if __name__ == "__main__":
    main()