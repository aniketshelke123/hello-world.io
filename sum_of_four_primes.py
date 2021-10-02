#sum of four prime numbers
def is_prime(i): # checks if i is prime or not

    count = 0
    j = 1
    while j <= i:
        if i % j == 0: #5 % 1==0
            count += 1
        j += 1
    return count == 2

n = int(input("Enter any integer: "))

if n <= 7:
    print("not possible")
else:
    if n % 2 == 0:
        #print("the first 2 prime numbers are 2 ,2 ")
        n = n - 4
        #print("n is :", n)

    else:
        #print("first two prime numbers are 2 , 3")
        n = n - 5
        #print("n is: ", n)

z = 0
j = 2
while j < n:
    if is_prime(j) and is_prime(n-j):
        if n % 2 == 0:
            print(2,  2,  j,  n-j)
        else:
            print(2,  3,  j,  n-j)
        z = 1
        break
    j += 1

if z == 0:
    print("impossible")
