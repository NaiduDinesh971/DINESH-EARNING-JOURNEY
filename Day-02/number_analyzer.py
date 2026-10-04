number = int(input("enter a number: "))
print("Number: ", number)

if(number > 0):
    print("positive")
elif(number < 0):
    print("negative")
else:
    print("zero")

if(number%2 == 0):
    print("even")
else:
    print("odd")

print("square of the number: ", number * number)
print("cube of the number: ", number * number * number)