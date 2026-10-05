#Week 04 Lab Quiz - Sales Monitor

#Description

lab04_sales_monitor.py is a Python script that takes a daily target and seven daily sales values from the user. It calculates the weekly total, average, counts how many days met or exceeded the target, and handles negative input validation by re-prompting. It also includes the stretch task: finding the highest sale and its corresponding day without using a list.

#Testing

Test Run: Tested with a daily target of 100 and seven sales values: 90, 105, 120, 85, 110, 130, 95.

Result: Total sales = 735.00, Average = 105.00, Target count = 4, Highest Sale = 130.00 (on Day 6).

Change Made After Testing: Added an input validation check using continue to handle negative sales values seamlessly without skipping the day counter improperly.
