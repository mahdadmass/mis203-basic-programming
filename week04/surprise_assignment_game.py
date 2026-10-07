import random
import time

print("Welcome to the Two-Way Number Game!")
print("1. You guess the number")
print("2. Python guesses your number")

choice = input("Choose a mode (1 or 2): ")

if choice == "1":
    print("\n--- Mode 1: Guess the Number ---")
    secret = random.randint(1, 100)
    attempts = 0
    start_time = time.time()

    guess = 0
    while guess != secret:
        guess = int(input("Enter a number between 1 and 100: "))
        attempts = attempts + 1

        if guess < secret:
            print("Go HIGHER!")
        elif guess > secret:
            print("Go LOWER!")
        else:
            total_time = round(time.time() - start_time, 1)
            print("Correct!")
            print("You found it in", attempts, "attempts and", total_time, "seconds!")

elif choice == "2":
    print("\n--- Mode 2: Python Mind Reader ---")
    print("Think of a number between 1 and 100.")
    input("Press Enter when you are ready...")

    low = 1
    high = 100
    attempts = 0

    while low <= high:
        guess = (low + high) // 2
        attempts = attempts + 1

        print("Is your number", guess, "?")
        answer = input("Type 'higher', 'lower', or 'correct': ")

        if answer == "correct":
            print("Awesome! I found your number in", attempts, "attempts!")
            break
        elif answer == "higher":
            low = guess + 1
        elif answer == "lower":
            high = guess - 1

else:
    print("Invalid choice! Please run the code again.")
