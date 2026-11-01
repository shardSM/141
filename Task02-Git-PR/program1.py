# Check whether a number is even or odd
n = int(input("Enter a number: "))
if n % 2 == 0:              # % gives the remainder; remainder 0 means divisible by 2
    print(n, "is Even")
else:
    print(n, "is Odd")
