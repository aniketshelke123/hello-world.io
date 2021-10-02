
lst1 = []
lst2 = []
n = int(input())
array = list(map(int, input().split()))

for i in array:
    lst1.append(i + 1)

print(lst1)
M = max(lst1)
largest = lst1.index(M)

for i in range(len(lst1)):
    if i == largest:
        lst2.append(lst1[i])
    else:
        lst2.append(lst1[i] + 1)
print(lst2)