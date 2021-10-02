lst = [3, 1, 5]
k=1
k2=2
for i in range(len(lst)):
    if lst[i] != 0 and k == 1:
        lst[i] -= 1
        k -= 1
        continue
    if lst[i] >= 0:  # and k2 !=0:
        lst[i] += 1
        # k2-=1
        break

print(lst)
