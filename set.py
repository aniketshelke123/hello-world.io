
lst = []
visited = set()
for i in range(2):
    a = int(input("Enter any integer: "))
    lst.append(a)


for i in range(1):
    for num in lst:
        if num == min(lst):
            print("Yes")
            visited.add(num)



print(visited, "visited set")
