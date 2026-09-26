total_students = 0
total_score = 0

while True:
    name = input("Enter student name (or q to quit): ")

    if name.lower() == "q":
        break

    score = float(input("Enter score: "))

    if score < 0 or score > 100:
        print("Invalid score. Please enter a number between 0 and 100.")
        continue

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"{name}: {score:g} -> {grade}")

    total_students += 1
    total_score += score

if total_students == 0:
    print("No students entered.")
else:
    average_score = total_score / total_students
    print(f"Total students: {total_students}")
    print(f"Average score: {average_score:.2f}")