# program for euclid problem
a = int(input("enter a: "))
b = int(input("enter b: "))
d = 0
k = 1
while k <= a and k <= b:
    if a % k == 0 and b % k == 0:
        d = k
    k = k + 1
print("GCD is:", d)

i = -1
j = -1
x = 0
y = 0
while i <= 10000:
    while j <= 10000:
        if (a * i + b * j == d) and i <= j:
            x = i
            y = j
        j += 1
    i += 1
print(" p: q : d")
print(x, y, d)
