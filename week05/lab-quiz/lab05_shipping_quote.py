"""Lab 05 - Shipping Quote

Each function does ONE job, takes parameters and RETURNS a value.
"""

DISCOUNT_THRESHOLD = 100   # subtotal >= 100 gets a discount
DISCOUNT_RATE = 0.10       # 10% discount
FREE_SHIPPING_THRESHOLD = 50  # amount >= 50 ships free
SHIPPING_FEE = 5.99


def calculate_subtotal(items):
    """items is a list of (price, quantity). Returns the sum of price * quantity."""
    subtotal = 0
    for price, quantity in items:
        subtotal += price * quantity
    return subtotal


def calculate_discount_rate(subtotal):
    """Returns 0.10 if subtotal is 100 or more, otherwise 0."""
    if subtotal >= DISCOUNT_THRESHOLD:
        return DISCOUNT_RATE
    return 0.0


def calculate_shipping_fee(amount):
    """Returns 0 if amount is 50 or more (free shipping), otherwise 5.99."""
    if amount >= FREE_SHIPPING_THRESHOLD:
        return 0.0
    return SHIPPING_FEE


def calculate_final_total(items):