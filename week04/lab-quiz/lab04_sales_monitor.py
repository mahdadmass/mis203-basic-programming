# Ask for a daily target
target = float(input("Enter daily target: "))
total = 0
target_count = 0
highest_sale = 0
highest_sale_day = 0
day = 1
# Loop to get sales for 7 days
while day<= 7:
  sale = float(input(f"Enter sales for day {day}: "))
# Re-prompt when a sale is negative
if sale <0:
  print("Sales cannot be negative. Please try again.")
        continue
# Calculate weekly total
total+= sale
# Check if the target is met or exceeded (includes equality)
if sale >= target:
  target_count += 1
# Stretch Task: Track the highest sale and its day number without using a list
if sale > highest_sale:
  highest_sale = sale
highest_sale_day = day
day+=1
# Calculate average
average =total/7
# Display results
print("\n--- Weekly Sales Report ---")
print(f"Weekly total: {total:.2f}")
print(f"Average sales: {average:.2f}")
print(f"Days meeting target: {target_count}")
print(f"Highest sale: {highest_sale:.2f}")
print(f"Highest sale day: Day {highest_day}")
