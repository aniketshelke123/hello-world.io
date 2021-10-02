
n = int(input())
elements = list(map(int, input().split()))
find_k = int(input())
step = int(input())
flag = True

for i in range(0, n, step):
    count, temp = 0, i
    while i < temp + step:
        if elements[i] != find_k:
            count += 1
        if elements[i] == find_k:
            count -= 1
        i = i + 1
    if count == step:
        flag = False
        break

if flag:
    print(1)
else:
    print(0)
