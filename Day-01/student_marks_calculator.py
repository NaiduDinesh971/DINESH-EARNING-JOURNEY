def calculate_total(a,b,c):
    return a+b+c
name = input("enter your name: ")
a = int(input("enter C marks: "))
b = int(input("enter python marks: "))
c = int(input("enter java marks: "))

print("... STUDENT REPORT ...")
print("student name: ", name)
print("C: ",a)
print("Python: ",b)
print("Java: ",c)
result = calculate_total(a,b,c)
print("Total: ", result)
avg = result/3
print("Average: ",avg)
per = (result/300)*100
print("Percentage: ", per)

if (per >= 90):
    print("A+")
    print("pass")
elif (per >= 80):
    print("A")
    print("pass")
elif (per >= 70):
    print("B")
    print("pass")
elif (per >= 60):
    print("C")
    print("pass")
elif (per >= 50):
    print("D")
    print("pass")
else:
    print("Fail")
