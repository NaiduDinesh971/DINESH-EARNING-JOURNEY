import json

print("==============================")
print("     EXPENSE INSIGHTS")
print("==============================")


try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)

    print("\nExpenses loaded successfully!")

except FileNotFoundError:
    expenses = []
    print("\nNo expenses file found.")


total_spent = 0
highest = expenses[0]
lowest = expenses[0]

for expense in expenses:
    total_spent = total_spent + expense["amount"]

print("\n========== EXPENSE SUMMARY ==========")
print("Total expenses:", len(expenses))
print("Total amount spent: ₹", round(total_spent, 2))


category_totals = {}

for expense in expenses:
    category = expense["category"]
    amount = expense["amount"]

    if category in category_totals:
           category_totals[category] += expense["amount"]
    else:
        category_totals[category] = expense["amount"]
    
    if (expense["amount"] > highest["amount"]):
        highest = expense
    
    if (expense["amount"] < lowest["amount"]):
        lowest = expense


print("\n========== CATEGORY-WISE SPENDING ==========")

for category in category_totals:
    print(category, ": ₹", category_totals[category])

print("\nHighest Expense:", highest["category"], "- ₹", highest["amount"])
print("Lowest Expense:", lowest["category"], "- ₹", lowest["amount"])


print("\n========== SPENDING PERCENTAGES ==========")

for category in category_totals:
    percentage = (category_totals[category] / total_spent) * 100
    print(category, ":", round(percentage, 2), "%")
