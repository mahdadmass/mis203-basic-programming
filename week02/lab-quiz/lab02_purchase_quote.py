# Prompt for inputs using int() for quantities and float() for money

qty1 = int(input("Enter quantity for item 1 : "))
price1 = float(input("Enter price for item 1 : ")) 

qty2 = int(input("Enter quantity for item 2: "))
price2 = float(input("Enter float for item 2: "))
             
delivery_fee = float(input("Enter Delivery Fee :")) 
tax_rate = float(input("Enter Tax percentage (e.g.,10 for 10% :"))/100

# Calculations
subtotal =(qty1 * price1) + (qty2 * price2)
tax_amount = subtotal * tax_rate
final_total = subtotal + tax_rate + delivery_fee

# Output formatted to 2 decimal places
print("\n--- Purchase Quote ---")
print(f"Subtotal: {subtotal:.2f} TRY")
print(f"Tax ({tax_rate * 100:.0f}%): {tax_amount:.2f} TRY")
print(f"Delivery Fee: {delivery_fee:.2f} TRY")
print(f"Final Total: {final_total:.2f} TRY")
