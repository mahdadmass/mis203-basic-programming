# Program statistics tracking
tickets_sold = 0
total_revenue = 0.0
free_tickets = 0

while True:
    # 1. Customer name input
    name = input("Customer name (or q to quit): ")
    if name.lower() == 'q':
        break

    # 2. Age input and validation
    age = int(input("Age: "))
    if age < 0 or age > 120:
        print("Invalid age.")
        continue

    # 3. Day input and validation
    day = input("Day (weekday/weekend): ").strip().lower()
    if day not in ['weekday', 'weekend']:
        print("Invalid day.")
        continue

    # 4. Student status input and validation
    is_student = input("Student (yes/no): ").strip().lower()
    if is_student not in ['yes', 'no']:
        print("Please answer yes or no.")
        continue

    # Base price calculation
    if day == 'weekday':
        base_price = 200.0
    else:
        base_price = 250.0

    # 5. Discount rules evaluated in strict order
    if age < 6:
        discount = 1.00
        category = "Free"
    elif age >= 65:
        discount = 0.50
        category = "Senior"
    elif 6 <= age <= 12:
        discount = 0.40
        category = "Child"
    elif is_student == 'yes' and age <= 25:
        discount = 0.30
        category = "Student"
    else:
        discount = 0.00
        category = "Standard"

    # Final price calculation
    final_price = base_price * (1 - discount)

    # 6. Print result for the current customer
    print(f"{name}: {final_price:.2f} TRY ({category})")

    # Update summary tracking variables
    tickets_sold += 1
    total_revenue += final_price
    if final_price == 0:
        free_tickets += 1

# 7. Final summary output after loop ends
if tickets_sold == 0:
    print("No tickets sold.")
else:
    avg_price = total_revenue / tickets_sold
    print(f"Tickets sold: {tickets_sold}")
    print(f"Total revenue: {total_revenue:.2f} TRY")
    print(f"Average price: {avg_price:.2f} TRY")
    print(f"Free tickets: {free_tickets}")
