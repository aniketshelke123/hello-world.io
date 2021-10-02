# program for Factovisors
n = int(input("enter n: "))
m = int(input("enter m: "))
fact = 1
i = 1
while i <= n:
    fact = fact * i
    i += 1
#print("Factorial of n is: ", fact)

if fact % m == 0:
    print(str(n) + "! is divisible by " + str(m))
else:
    print(str(n) + "! is not divisible by " + str(m))
