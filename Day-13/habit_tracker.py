import json
from datetime import date
today = str(date.today())
print("Tracking date:", today)

print("==============================")
print("      PERSONAL HABIT TRACKER")
print("==============================")

habits = ["Coding Python", "Reading", "Exercise", "Drinking Water"]
completed_habits = []

for habit in habits:
    print("\nDid you complete:", habit, "?")
    answer = input("Enter yes or no: ")

    if (answer.lower() == "yes"):
        completed_habits.append(habit)

pending = len(habits) - len(completed_habits)

print("\n========== DAILY SUMMARY ==========")

print("Total habits:", len(habits))
print("Completed habits:", len(completed_habits))
print("Pending habits:", pending)

print("\nCompleted today:")
for habit in completed_habits:
    print("-", habit)

progress = (len(completed_habits) / len(habits)) * 100
print("\nDaily progress:", round(progress, 2), "%")

with open("Day-13/habits.json", "r") as file:
    all_records = json.load(file)

all_records[today] = completed_habits

with open("Day-13/habits.json", "w") as file:
    json.dump(all_records, file, indent=4)

print("\nDaily habit record saved!")
print("Date:", today)
print("Habits saved:", all_records[today])
