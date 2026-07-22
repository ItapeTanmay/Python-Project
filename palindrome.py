name=input("Enter String: ")
if name.upper() == name[::-1].upper():
    print("Palindrome")
else:
    print("Not Palindrome")