rows = 8

for i in range(rows):

    # Left pattern
    for j in range(4):
        if i >= j and i < rows - j:
            print("* ", end="")
        else:
            print("  ", end="")

    # Middle gap
    print("    ", end="")   # 8 spaces

    # Right mirrored pattern
    for j in range(3, -1, -1):
        if i >= j and i < rows - j:
            print("* ", end="")
        else:
            print("  ", end="")

    print()