import json
print("==============================")
print("   PERSONAL FINANCE TRACKER   ")
print("==============================")

while True:
    try:
        budget = int(input("Enter your monthly budget: "))

        if (budget > 0):
            break
        else:
            print("Budget must be a positive integer.")

    except ValueError:
        print("Invalid input! Please enter a number.")

try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
except FileNotFoundError:
    expenses = []

previous_expenses = expenses.copy()

while True:
    try:
        num_expenses = int(input("Enter no of expenses: "))

        if (num_expenses > 0):
            break
        else:
            print("Number of expenses must be a positive integer.")

    except ValueError:
        print("Invalid input! Please enter a number.")

for i in range(num_expenses):
    while True:
        category = input(f"Enter category of expense {i + 1}: ").strip().title()

        if category == "":
            print("Category cannot be empty.")
        else:
            break

    while True:
            try:
                amount = float(input(f"enter amount for {category}: "))
    
                if (amount > 0):
                    break
                else:
                    print("Amount should not be negative.")
    
            except ValueError:
                print("Invalid input! Please enter a number.")
    
    expense = {"category": category, "amount": amount}
    expenses.append(expense)

print("\n======== PREVIOUS EXPENSES =========")

if len(previous_expenses) == 0:
    print("No previous expenses found.")
else:
    for expense in previous_expenses:
        print(expense["category"], ": ₹", expense["amount"])

print("\n========== NEW EXPENSES ==========")

for i in range(len(previous_expenses), len(expenses)):
    expense = expenses[i]
    print(expense["category"], ": ₹", expense["amount"])


total = 0
category_totals = {}

total = 0
category_totals = {}

for expense in expenses:
    total = total + expense["amount"]

    category = expense["category"]

    if category in category_totals:
        category_totals[category] += expense["amount"]
    else:
        category_totals[category] = expense["amount"]

remaining = budget - total

print("\n========== SUMMARY ==========")
print("Monthly budget: ₹", round(budget, 2))
print("Total spent: ₹", round(total, 2))

print("\nCategory-wise Expenses:")

for category, amount in category_totals.items():
    print(category, ": ₹", round(amount, 2))

print("Remaining budget: ₹", round(remaining, 2))

if (remaining < 0):
    print("Warning: You exceeded your budget!")
else:
    print("You are within your budget!")

with open("expenses.json", "w") as file:
    json.dump(expenses, file, indent=4)

print("Expenses saved successfully!")

