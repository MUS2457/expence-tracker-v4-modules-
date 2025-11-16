from input_data import input_data
from expences_calculations import tl_expences, tl_per_category, top_low_product, budget_limit
import json
from datetime import datetime

# Get expenses from user
expenses = input_data()

#  Calculate statistics
total = tl_expences(expenses)
per_category = tl_per_category(expenses)
top_low = top_low_product(expenses)
budget = budget_limit(expenses, budget=50000)

now = datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

report = {
    "timestamp": timestamp,
    "total_expenses": total,
    "total_per_category": per_category,
    "top_low_product": top_low,
    "budget_status": budget,
    "expenses": expenses
}

with open("expense_report_v4.json", "w") as f:
    json.dump(report, f, indent=4)

with open("expense_report_v4.txt", "a") as f:
    f.write(f"Expense Report - {timestamp}\n\n")
    f.write(f"Total Expenses: {total['total price']}\n")
    f.write(f"By Category:\n")
    for cat, amt in per_category.items():
        f.write(f"  {cat}: {amt}\n")
    f.write(f"Most & Least Expensive Products:\n")
    f.write(f"  Most expensive: {top_low['most_expensive_product']} - {top_low['price_of_most_expensive']}\n")
    f.write(f"  Cheapest: {top_low['cheapest_product']} - {top_low['price_of_cheapest']}\n")
    f.write(f"Budget Status: {budget}\n")
    f.write("\nDetailed Expenses:\n")
    for item, info in expenses.items():
        f.write(f"  {item} ({info['category']}): {info['price']}\n")
    f.write("\n" + "="*40 + "\n\n")

# Print report in terminal
print(report)
