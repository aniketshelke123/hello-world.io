

# program to insert or remove form a nested list

num = [[1, 2, 3, 4]]
# del num[0][0]
# num[0].insert(0, 4)
# print(num)

# OR

num[0].insert(0, num[0].pop(3))
print(num)
