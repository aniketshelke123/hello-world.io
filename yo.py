#Num = list(map(int, input().split()))
ls = []
dt = {}
unique = set()

requiredstring = input()
for i in requiredstring:
    unique.add(i)
print(unique)

for i in unique:
    count = requiredstring.count(i)
    dt[i] = count
print(dt)

for index, value in dt.items():
    if value <= 3:
        ls.append(value)
print(max(ls))