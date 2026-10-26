# Lab 05 - Shipping Quote

## What the program does
Calculates the price of an order using four separate functions:
- `calculate_subtotal` - adds price x quantity for all items
- `calculate_discount_rate` - 10% discount if subtotal is 100 or more
- `calculate_shipping_fee` - free shipping if amount is 50 or more, otherwise 5.99
- `calculate_final_total` - combines everything into the final total

Two sample orders use the same functions (no copied code).

## How to run
python lab05_shipping_quote.py

## print vs return
- `print` only shows a value on the screen. The program cannot use it later.
- `return` gives the value back to the code that called the function, so it can be saved, used in calculations, or tested with `assert`.

## Submission
Saved in my course repository at `week05/lab-quiz/lab05_shipping_quote.py`.