
lst = []
ans = []
N = int(input())

for i in range(N):
    ele = int(input())
    lst.append(ele)

first = lst[0]
last = lst[N - 1]

for i in range(first, last + 1):
    if i not in lst:
        print(i)
