print("==============================")
print("   PERSONAL SAVINGS TRACKER   ")
print("==============================")


while True:
    try:
        goal = float(input("Enter your savings goal (₹): "))

        if (goal > 0):
            break
        else:
            print("Savings goal must be greater than 0.")

    except ValueError:
        print("Invalid input! Please enter a number.")



while True:
    try:
        current_savings = float(input("Enter your current savings (₹): "))

        if (current_savings >= 0):
            break
        else:
            print("Savings cannot be negative. Try again.")

    except ValueError:
        print("Invalid input! Please enter a number.")


remaining = goal - current_savings
print("------------------------------")
print("Remaining amount: ₹", remaining)

progress = (current_savings / goal) * 100
print("Savings progress:", round(progress, 2), "%")

if (current_savings >= goal):
    print("Congratulations! 🎉 You reached your savings goal!")
else:
    print("Keep saving! You can reach your goal!")