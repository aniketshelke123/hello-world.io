num = int(input())
a = num
reversed_num = 0
while abs(num) != 0:
    digit = abs(num) % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print(a - reversed_num)