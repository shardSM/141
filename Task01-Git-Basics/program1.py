# Multiplication table of any number
n = int(input("Enter a number: "))      # read the number from the user
for i in range(1, 11):                  # i takes values 1 to 10
    print(f"{n} x {i} = {n * i}")       # e.g. 5 x 3 = 15
