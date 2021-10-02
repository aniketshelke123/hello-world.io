while True:
    s = int(input("Y: "))

    if (s >= 0 and s <= 12):
        break

for i in range(s):

    print("_" * (s - 1 - i), end="")
    print("*" * (1 + i), end="")
    print(" " * (i + 1), end="")
    print("_" * (s - 1 - i), end="")
    print("" * (i))