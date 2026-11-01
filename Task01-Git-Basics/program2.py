# Greatest of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Greatest number is", a)
elif b > a:
    print("Greatest number is", b)
else:
    print("Both numbers are equal")
