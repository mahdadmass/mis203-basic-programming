# Lab 05 - Shipping Quote

def calculate_subtotal(price, quantity):
    # price times quantity
    return price * quantity


def calculate_discount_rate(subtotal):
    # 10% discount if subtotal is 100 or more
    if subtotal >= 100:
        return 0.10
    return 0


def calculate_shipping_fee(amount):
    # free shipping if amount is 50 or more
    if amount >= 50:
        return 0
    return 5.99


def calculate_final_total(price, quantity):
    # step 1: subtotal
    subtotal = calculate_subtotal(price, quantity)
    # step 2: discount
    rate = calculate_discount_rate(subtotal)
    discount = subtotal * rate
    after_discount = subtotal - discount
    # step 3: shipping
    shipping = calculate_shipping_fee(after_discount)
    # step 4: final total
    return round(after_discount + shipping, 2)


# Two sample orders (same function, different numbers)
total1 = calculate_final_total(25, 4)   # subtotal 100
total2 = calculate_final_total(10, 2)   # subtotal 20
print("Order 1 total:", total1)
print("Order 2 total:", total2)

# assert checks
assert calculate_discount_rate(100) == 0.10   # boundary: exactly 100
assert calculate_discount_rate(99) == 0       # just below the boundary
assert total1 == 90.0
assert total2 == 25.99

print("All checks passed.")
