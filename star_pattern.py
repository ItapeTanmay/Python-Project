n = 7

for i in range(4):
    print("  " * i + "* " * (n - 2 * i))

print("  " * 3 + "*")

for i in range(2, -1, -1):
    print("  " * i + "* " * (n - 2 * i))