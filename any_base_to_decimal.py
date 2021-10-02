num = int(input())
base = int(input())

power = 1
decimal_value = 0
while (num > 0):
    rem = num % 10
    num //= 10

    decimal_value += rem * power
    power *= base

print(decimal_value)

