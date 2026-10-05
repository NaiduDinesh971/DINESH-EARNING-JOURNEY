marks = []

no_of_subjects = int(input("enter no of subjects: "))
for i in range(no_of_subjects):
    mark = int(input(f"enter marks for subject {i+1}: "))
    while (mark < 0 or mark > 100):
        print("Invalid marks entered. please enter marks between 0 and 100")
        mark = int(input(f"enter marks for subject {i+1}: "))
    
    marks.append(mark)

print("Marks: ", marks)
print("Total: ", sum(marks))
print("Number of subjects: ", len(marks))
print("Highest: ", max(marks))
print("Lowest: ", min(marks))
avg = sum(marks) / len(marks)
print("Average: ", avg)

if (avg >= 90):
    print("Grade: A")
elif (avg >= 80):
    print("Grade: B")
elif (avg >= 70):
    print("Grade: C")
elif (avg >= 60):
    print("Grade: D")
else:
    print("Grade: F")

if (avg >= 40):
    print("Result: Pass")
else:
    print("Result: Fail")


