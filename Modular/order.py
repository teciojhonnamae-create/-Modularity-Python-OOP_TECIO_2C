def calculate_total(orders):
    """Calculates subtotal across all ordered items."""
    return sum(order["total"] for order in orders)


def calculate_discount(subtotal):
    """Calculates discount (10% off for subtotal >= ₱1000)."""
    if subtotal >= 1000:
        return subtotal * 0.10
    return 0.0