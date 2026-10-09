print("==============================")
print("     DAILY BUDGET MANAGER     ")
print("==============================")

budget = float(input("Enter your daily budget: "))

print("Your daily budget is:", budget)

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
highest = expenses[0]
lowest = expenses[0]

for expense in expenses:
    total = total + expense["amount"]

    
    if expense["amount"] > highest["amount"]:
        highest = expense

    if expense["amount"] < lowest["amount"]:
        lowest = expense
    

remaining = budget - total

print("==============================")
print("       DAILY BUDGET REPORT    ")
print("==============================")

for expense in expenses:
    print(expense["category"], ":", expense["amount"])



print("------------------------------")
print("Daily Budget:", budget)
print("Total Expenses:", total)
print("Remaining Budget:", remaining)
print("Highest Expense Category:", highest["category"])
print("Highest Expense Amount:", highest["amount"])
print("lowest Expense Category:", lowest["category"])
print("lowest Expense Amount:", lowest["amount"])


if (remaining < 0):
    print("Warning: You exceeded your budget!")
else:
    print("You are within your budget!")