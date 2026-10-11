
print("==============================")
print("  EXPENSE CATEGORY ANALYZER   ")
print("==============================")
print("Welcome! Let's track your expenses.")

expenses = []

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

total = 0
highest = expenses[0]
lowest = expenses[0]
category_totals = {}

for expense in expenses:
    total = total + expense["amount"]

    category = expense["category"]

    if category in category_totals:
       category_totals[category] += expense["amount"]
    else:
        category_totals[category] = expense["amount"]

    if (expense["amount"] > highest["amount"]):
        highest = expense

    if (expense["amount"] < lowest["amount"]):
        lowest = expense

print("==============================")
print("     FINAL EXPENSE REPORT     ")
print("==============================")

print("Total Expenses: ", round(total,2))

print("\nCategory-wise Expenses:")

for category, amount in category_totals.items():
    print(category, ": ₹", round(amount, 2))

print("\nHighest Expense:", highest["category"], "- ₹", highest["amount"])
print("Lowest Expense:", lowest["category"], "- ₹", lowest["amount"])