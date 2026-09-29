## Week 03

* **AI Tool Used:** ChatGPT / Gemini
* **Prompt Used:** "Write a Python program that sells cinema tickets according to the week 03 assignment instructions, validating input for age, day, and student status, applying discount rules in order, and printing summary statistics at the end."
* **What did you change?** I reviewed the prompt structure, formatted user inputs with `.strip().lower()` to handle case sensitivity automatically, and formatted price outputs with 2 decimal places using f-strings to strictly align with the sample output.
* **Tests:**
  1. Input: Name="Can", Age=5 (Boundary: age < 6), Day="weekend", Student="no" -> Result: `Can: 0.00 TRY (Free)`
  2. Input: Name="Deniz", Age=10 (Boundary: age 6 to 12), Day="weekday", Student="no" -> Result: `Deniz: 120.00 TRY (Child)`
  3. Input: Name="Mert", Age=26 (Boundary: student age limit > 25), Day="weekday", Student="yes" -> Result: `Mert: 200.00 TRY (Standard)`
* **Why does the order of the rules matter?** Order matters because Python evaluates `if-elif` conditional blocks sequentially top-to-bottom and exits the block on the first matching condition. If the Student rule was placed before the Child rule, a 10-year-old student would incorrectly receive a 30% Student discount instead of the higher 40% Child discount meant for their age group.
