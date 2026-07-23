num = int(input("Enter a number: "))

temp = num
digits = len(str(num))
total = 0

while temp > 0:
    digit = temp % 10
    total = total + (digit ** digits)
    temp = temp // 10

if total == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")