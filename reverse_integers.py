
x = int(input())

negative = False
if x < 0:
    negative = True
    x = abs(x)

rev = 0
while x != 0:
    pop = x % 10
    x //= 10
    rev = rev * 10 + pop

if negative:
    rev = rev * -1

print(rev)