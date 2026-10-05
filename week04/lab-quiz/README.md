# Week 04 Lab Quiz - Sales Monitor

## Overview
This project contains the Python script `lab04_sales_monitor.py` which tracks and analyzes weekly sales performance based on a user-defined daily target and seven daily sales values.

## Features
- Prompts the user for a daily sales target.
- Uses a loop to collect 7 daily sales values.
- Re-prompts the user if a negative sales value is entered.
- Calculates and displays:
  - Weekly total sales.
  - Average daily sales.
  - Number of days meeting or exceeding the target.
- **Stretch Task Implemented:** Tracks the highest sale and its corresponding day number without using a list.

## Testing & Changes Log
- **Test Run:** Tested with a mix of values (e.g., `100, 150, -50 (re-prompted), 200, 90, 120, 130, 110` with a target of `100`).
- **Change Made After Testing:** Added input validation handling (`if sale < 0: continue`) to ensure negative numbers re-prompt the user for the same day without skipping the day counter index incorrectly.
