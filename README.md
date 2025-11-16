Expense Tracker v4

A modular, beginner‑friendly Python project that helps you track your expenses, calculate totals, analyze spending per category, find the most/least expensive items, and check whether you're within your monthly budget.

This version follows clean architecture using multiple modules, making it easier to maintain, scale, and reuse.

*Features

Input Module (input_data.py)

Collects product name, category, and price

Validates empty names, invalid category, and negative prices

Prevents program crashes with error handling

*Calculations Module (expenses_calculations.py)

Total expenses

Total per category (e.g., food, transport, shopping)

Most expensive and cheapest product

Budget limit check (default monthly ¥50,000)

✔️ Main Program (main.py)

Calls all functions

Generates two report files:

JSON report (expense_report_v4.json)

Readable TXT report (expense_report_v4.txt)

Prints final report in the terminal

# project structure
expense_racker_v4/
│
├── input_data.py
├── expenses_calculations.py
├── main.py
├── expense_report_v4.json
└── expense_report_v4.txt

