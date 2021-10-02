from math import gcd

# sum gcd problem
Test_cases = int(input())

while Test_cases:
    n = int(input())

    while gcd(n, sum([int(i) for i in str(n)])) == 1:
        n = n + 1
    print(n)
    Test_cases -= 1
