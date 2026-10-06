def calculate_total(marks):
    return sum(marks)

def calculate_average(marks):
    return sum(marks) / len(marks) 

def calculate_grade(average):
    if(average >= 90):
        return "A"
    elif(average >= 80):
            return "B"
    elif(average >= 70):
            return "C"
    elif(average >= 60):
            return "D"
    else:
            return "F"

def calculate_result(average):
      if(average >= 40):
            return "Pass"
      else:
            return "Fail"
    
    

marks = []

no_of_subjects = int(input("enter no of subjects: "))
for i in range(no_of_subjects):
    mark = int(input(f"enter marks for subject {i+1}: "))
    while (mark < 0 or mark > 100):
        print("Invalid marks entered. please enter marks between 0 and 100")
        mark = int(input(f"enter marks for subject {i+1}: "))
    
    marks.append(mark)

total = calculate_total(marks)
average = calculate_average(marks)
grade = calculate_grade(average)
result = calculate_result(average)

print("Marks: ", marks)
print("Total: ", total)
print("Average: ", average)
print("Grade: ", grade)
print("Result: ",result)