# Lab 01 - Student Introduction Card

## Overview
This Python script prompts the user for 5 pieces of information (Name, Student ID, Department, GitHub Username, and Programming Goal) and outputs a formatted Student Introduction Card.

## Concept Explanations (Acceptance Check #4)
* **`input()`**: Captures text typed by the user from the console and stores it as a string variable in memory.
* **`print()`**: Displays formatted text or variable values on the terminal output screen.

## Stretch Task Reflection
* **Observation (Empty Name Test)**: When entering an empty string for the name, the program still executes and prints an empty field next to `Name :`.
* **Future Improvement**: Add input validation (e.g., a `while` loop) to re-prompt the user if any essential field (like name or ID) is left blank.

## Testing & Iteration Notes
* **Test Ran**: Ran the script with test input (`Mahdad Maasoum`, `2404109914`, `Management Information Systems`, `github_user`, `Master Python`). Then changed the Department value to verify that the output updates dynamically.
* **Changes Made After Testing**: Improved output formatting by adding divider lines (`=`) and alignment to make the final student card more readable and neat.
