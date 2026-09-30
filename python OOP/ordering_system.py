from models import MenuItem, OrderItem


class Menu:
    def __init__(self):
        self.items = {}
        self._load_default_menu()

    def _load_default_menu(self):
        default_items = [
            MenuItem("1", "Chickenjoy", 89.00),
            MenuItem("2", "Jolly Spaghetti", 60.00),
            MenuItem("3", "Yumburger", 45.00),
            MenuItem("4", "Burger Steak", 75.00),
            MenuItem("5", "Palabok", 75.00),
            MenuItem("6", "French Fries", 50.00),
            MenuItem("7", "Peach Mango Pie", 45.00),
            MenuItem("8", "Chocolate Sundae", 50.00),
            MenuItem("9", "Coke", 40.00),
            MenuItem("10", "Pineapple Juice", 45.00),
        ]
        for item in default_items:
            self.items[item.code] = item

    def display(self):
        print("\n==============================================")
        print("            JOLLIBEE-STYLE RESTAURANT")
        print("==============================================")
        print("                  FULL MENU")
        print("----------------------------------------------")
        print(f"{'Code':<8}{'Menu Item':<25}{'Price':>10}")
        print("----------------------------------------------")

        for code, item in self.items.items():
            print(f"{code:<8}{item.name:<25}₱{item.price:>8.2f}")

        print("----------------------------------------------")

    def get_item(self, code) -> MenuItem:
        return self.items.get(code.upper())


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, menu_item: MenuItem, quantity: int):
        self.items.append(OrderItem(menu_item, quantity))

    def calculate_subtotal(self) -> float:
        return sum(item.calculate_item_total() for item in self.items)

    def calculate_discount(self) -> float:
        subtotal = self.calculate_subtotal()
        return subtotal * 0.10 if subtotal >= 1000 else 0.0

    def calculate_total(self) -> float:
        return self.calculate_subtotal() - self.calculate_discount()


class RestaurantManager:
    def __init__(self):
        self.menu = Menu()
        self.current_order = Order()

    def display_welcome(self):
        print("\n==============================================")
        print("        WELCOMING YOU TO JOLLIBEE-STYLE!")
        print("==============================================")
        print("       Delicious food at affordable prices!")
        print("==============================================")

    def take_order(self):
        while True:
            self.menu.display()

            # Input code
            while True:
                code = input("\nEnter menu code: ").strip().upper()
                item = self.menu.get_item(code)
                if item:
                    break
                print("Invalid menu code. Please choose from the menu.")

            # Input quantity
            while True:
                try:
                    quantity = int(input("Enter quantity: "))
                    if quantity > 0:
                        break
                    print("Quantity must be greater than 0.")
                except ValueError:
                    print("Please enter a valid number.")

            self.current_order.add_item(item, quantity)
            print(f"\nAdded {quantity} x {item.name} to your order.")

            # Ask to continue
            while True:
                another = input("\nDo you want to order another item? (yes/no): ").strip().lower()
                if another in ["yes", "y"]:
                    break
                elif another in ["no", "n"]:
                    return
                else:
                    print("Please answer only yes or no.")

    def print_receipt(self):
        subtotal = self.current_order.calculate_subtotal()
        discount = self.current_order.calculate_discount()
        total = self.current_order.calculate_total()

        print("\n")
        print("==============================================")
        print("              JOLLIBEE-STYLE")
        print("             OFFICIAL RECEIPT")
        print("==============================================")
        print("              Thank you for dining!")
        print("----------------------------------------------")
        print(f"{'ITEM':<20}{'QTY':>5}{'PRICE':>10}{'TOTAL':>10}")
        print("----------------------------------------------")

        for item in self.current_order.items:
            print(
                f"{item.menu_item.name:<20}"
                f"{item.quantity:>5}"
                f"₱{item.menu_item.price:>9.2f}"
                f"₱{item.calculate_item_total():>9.2f}"
            )

        print("----------------------------------------------")
        print(f"{'Subtotal:':<30}₱{subtotal:>9.2f}")
        print(f"{'Discount:':<30}₱{discount:>9.2f}")
        print(f"{'TOTAL:':<30}₱{total:>9.2f}")
        print("==============================================")
        print("       Thank you! Please come again!")
        print("==============================================")