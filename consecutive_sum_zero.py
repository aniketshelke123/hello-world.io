

n = int(input())
n_list = list(map(int, input().split()))
# n_list = [2, 3, -3, 4, -4, 5, 6, -6, -5, 10]
found = False
for i in range(len(n_list)):
    z = i + 1
    while z < len(n_list):
        if found is True:
            break
        if sum(n_list[i:z+1]) == 0:
            print(1)
            found = True
            break

        if not found:
            z += 1

if not found:
    print(0)
