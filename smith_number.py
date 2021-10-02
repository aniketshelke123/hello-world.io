# program to see if a given number n is smith or not
prime_fact = []
list_of_sum = []


def is_prime(i):  # checks if number i is prime or not
    count = 0
    j = 1
    while j <= i:
        if i % j == 0:
            count += 1
        j += 1
    return count == 2


def getSum(n):  # Gives the sum of digits in a number
     sum_of_digits = 0
     for digit in str(n):
        sum_of_digits += int(digit)
     return sum_of_digits

n = int(input("Enter any integer value: "))

k = n
sum_of_n = getSum(k)    # if n = 25 then sum_of_n is 2+5 = 7
i = 2
while i <= k:  #checks for prime factors for n and appends it into prime_fact
   if k % i == 0:
        k = k // i
        check = is_prime(i)
        if check:
            prime_fact.append(i)
            a = getSum(i)
            list_of_sum.append(a)
            if k % i == 0:
                continue
   i = i+1
print("***********")
print("prime factors :", prime_fact)

sum_of_primes = sum(list_of_sum)

if sum_of_n == sum_of_primes:
    if  is_prime(n) == True:
        print("It's a prime i.e not a smith number")
    else :
        print("It's a Smith number")
else:
    print("Not a smith number")