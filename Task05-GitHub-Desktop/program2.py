# Check whether a string is a palindrome
s = input("Enter a string: ")
if s == s[::-1]:            # compare the string with its reverse
    print(s, "is a Palindrome")
else:
    print(s, "is not a Palindrome")
