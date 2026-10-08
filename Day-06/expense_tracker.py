expenses = []

num_expenses = int(input("enter no.of expenses: "))
if (num_expenses > 0):
    print("Number of expenses: ", num_expenses)
else: 
    print("Number of expenses must be greater than 0.")

for i in range(num_expenses):
    category = input(f"enter category of expense {i + 1}: ")
    amount = float(input(f"enter amount for {category}: "))

    expense = {"category": category, "amount": amount}
    expenses.append(expense)

total = 0
highest = expenses[0]["amount"]
lowest = expenses[0]["amount"]

for expense in expenses:
    total = total + expense["amount"]

    if (expense["amount"] > highest):
        highest = expense["amount"]

    if (expense["amount"] < lowest):
        lowest = expense["amount"]

average = total / len(expenses)

print("==============================")
print("  PERSONAL EXPENSE TRACKER  ")
print("==============================")

for expense in expenses:
    print(expense["category"], ":", expense["amount"])

print("------------------------------")
print("Total Expenses: ", total)
print("Average Expense: ", round(average, 2))
print("Highest Expense: ", highest)
print("Lowest Expense: ", lowest)
print("==============================")
    