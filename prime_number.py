n = int(input("Enter any interger value: "))
i = 1
count = 0
while i <= n:
     if  n % i == 0:
        count += 1
     i += 1

if count == 2:
    print("prime number")
else:
    print("not prime")