num = int(input("Enter a number: "))

square = num * num
temp = square
sum_digits = 0

while temp > 0:
    digit = temp % 10
    sum_digits += digit
    temp = temp // 10

if sum_digits == num:
    print(num, "is a Neon Number")
else:
    print(num, "is not a Neon Number")