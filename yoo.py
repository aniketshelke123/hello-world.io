a, b = 0, 0
x = 0 
y = 0 
z = int(input())
while x < 100:
    while y < 100:
        if 2* x + 3* y == z:
            a = x
            b = y
        y += 1
    x += 1

print(a, " ", b)
