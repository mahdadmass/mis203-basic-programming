# Lab 05 - Shipping Quote

## What the program does
Calculates the price of an order using four separate functions:
- `calculate_subtotal(price, quantity)` - price times quantity
- `calculate_discount_rate(subtotal)` - 10% discount if subtotal is 100 or more, otherwise 0
- `calculate_shipping_fee(amount)` - free shipping if amount is 50 or more, otherwise 5.99
- `calculate_final_total(price, quantity)` - uses the three functions above to get the final total

Two sample orders call the same functions with different numbers, so no calculation code is copied.

## How to run
```
python lab05_shipping_quote.py
```

Expected output:
```
Order 1 total: 90.0
Order 2 total: 25.99
All checks passed.
```

## Assert checks
- `calculate_discount_rate(100) == 0.10` (threshold boundary)
- `calculate_discount_rate(99) == 0` (just below the boundary)
- Order 1 total is 90.0
- Order 2 total is 25.99

## print vs return
- `print` only shows a value on the screen. The program cannot use it later.
- `return` gives the value back to the code that called the function, so it can be saved, used in calculations, or tested with `assert`.

Example: `calculate_subtotal` uses `return`, so `calculate_final_total` can use its result. The final `print(...)` lines only display the answers.
