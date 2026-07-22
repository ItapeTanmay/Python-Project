numbers = [10, 25, 7, 98, 43, 67]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest number is",largest)
