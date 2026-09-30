class MenuItem:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price


class OrderItem:
    def __init__(self, menu_item: MenuItem, quantity: int):
        self.menu_item = menu_item
        self.quantity = quantity

    def calculate_item_total(self) -> float:
        return self.menu_item.price * self.quantity