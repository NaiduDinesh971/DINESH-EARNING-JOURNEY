

print("==============================")
print("   PERSONAL SAVINGS TRACKER")
print("==============================")

goal = float(input("Enter your savings goal (₹): "))
saved = float(input("Enter the amount you have saved (₹): "))

if (goal <= 0 or saved < 0):
    print("Please enter a goal greater than zero and savings that are not negative.")

else:
    remaining = max(goal - saved, 0)
    progress = (saved / goal) * 100

    print("\n========== SAVINGS SUMMARY ==========")
    print("Savings goal: ₹", goal)
    print("Already saved: ₹", saved)
    print("Amount remaining: ₹", remaining)
    print("Savings progress:", round(min(progress, 100), 2), "%")

    print("\n========== SAVINGS STATUS ==========")

    if saved >= goal:
        print("Congratulations! You reached your savings goal!")
    else:
        print("Keep saving! You can reach your goal!")
