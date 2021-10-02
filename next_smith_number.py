# program for giving the next smith number after n
prime_fact = []
list_of_sum = []
smith = 0
smith_list = []


def is_prime(i):   # checks if i is prime or not
    count = 0
    j = 1
    while j <= i:
        if i % j == 0:
            count += 1
        j += 1
    return count == 2


def getSum(k):
    sum_of_digits = 0
    for digit in str(k):
        sum_of_digits += int(digit)
    return sum_of_digits


n = int(input("Enter any integer value: "))
while True:
        k = n
        sum_of_nn = getSum(k)
        i = 2
        while i <= k:
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

        sum_of_primes = sum(list_of_sum)
        if sum_of_nn == sum_of_primes:
            if is_prime(n) == True:
                prime_fact = []
                list_of_sum = []
                n = n + 1
            else:
                #print("The Smith number is: ", n)
                smith_list.append(n)
                smith = smith + 1
                continue
        else:
            #print("not a smith number")
            prime_fact = []
            list_of_sum = []
            n = n + 1

        if smith == 5:  # comment this out if u want to print only the next smith number
            break
print("**********************************")
print("The smith numbers  are: ", smith_list)
