

n = int(input())
elements = list(map(int, input().split()))
find = int(input())
elements.sort()
flag = 0
index = n  
for i in range(0, n):
    if find < elements[i]:
        index = i
        flag = 1 
        break
if flag == 0: 
   print(index)
else:
    print(index)




