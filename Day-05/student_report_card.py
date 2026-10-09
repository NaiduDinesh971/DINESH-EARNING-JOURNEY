name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

num_subjects = int(input("Enter number of subjects: "))

if (num_subjects > 0):
    print("Number of subjects: ", num_subjects)
else:
    print("Number of subjects must be greater than 0.")

subjects = []
marks = []

for i in range(num_subjects):
    subject = input(f"Enter subject {i + 1}: ")
    subjects.append(subject)

    while True:
        mark = float(input(f"Enter marks for {subject}: "))

        if (0 <= mark <= 100):
            marks.append(mark)
            break
        else:
            print("Invalid marks! Enter a value between 0 and 100.")

student = {
    "name": name,
    "roll_no": roll_no,
    "subjects": subjects,
    "marks": marks
}

total = sum(student["marks"])
average = total / len(student["marks"])

if (average >= 90):
    grade = "A"
elif (average >= 80):
    grade = "B"
elif (average >= 70):
    grade = "C"
elif (average >= 60):
    grade = "D"
else:
    grade = "F"

if (average >= 40):
    result = "Pass"
else:
    result = "Fail"

print()
print("================================")
print("       STUDENT REPORT CARD")
print("================================")
print("Name:", student["name"])
print("Roll No:", student["roll_no"])
print("--------------------------------")

for i in range(len(student["subjects"])):
    print(student["subjects"][i], ":", student["marks"][i])

print("--------------------------------")
print("Total:", total)
print("Average:", round(average, 2))
print("Grade:", grade)
print("Result:", result)
print("================================")