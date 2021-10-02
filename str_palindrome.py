import math
odd = []


def solve(s, k):
    flag = 1
    for i in range(0, len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            flag = 0
            break
    if flag == 1:
        if K > 1:
            return 1     # its a palindrome
    return 0


S = input()
K = int(input())
print(solve(S, K))

