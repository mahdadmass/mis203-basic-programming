

# 1. Get user inputs
price = float(input("Enter unit price (TRY): "))
stock = int(input("Enter available stock: "))
quantity = int(input("Enter requested quantity: "))
is_member = input("Is the customer a member? (yes/no): ").strip().lower() == "yes"

# 2. Validation checks
if quantity <= 0:
    print("Status: REJECTED - Quantity must be greater than zero.")
elif quantity > stock:
    print("Status: REJECTED - Insufficient stock available.")
else:
    # 3. Approved order processing
    print("Status: APPROVED - Stock is sufficient and quantity is valid.")
    
    subtotal = price * quantity
    
    # 4. Discount logic using 'and' logical operator
    if is_member and subtotal >= 500:
        final_price = subtotal * 0.90  # Apply 10% discount
        print("Promotion: 10% member discount applied.")
    else:
        final_price = subtotal
        print("Promotion: No discount applied.")
        
    print(f"Final Price: {final_price:.2f} TRY")
