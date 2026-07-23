# Take input from user

value = input("Enter String or Number: ")

# Reverse the input using slicing

reverse_value = value[::-1]

# Check weather original value and reverse value are same

if value == reverse_value:
    print("Palindrome")
else:
    print("Not a palindrome")