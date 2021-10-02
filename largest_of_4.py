#print smallest

# a = int(input("enter 4 numbers\n"))
# b = int(input())
# c = int(input())
# d = int(input())
#
# if a <= b and a <= c and a <= d:
#     print("a is Smallest ")
# elif b <= a and b <= c and b <= d:
#     print("b is  smallest")
# elif c <= a and c <= b and c <= d:
#     print("c is smallest")
# elif d <= a and d <= b and d <= c:
#     print("d is smallest")

list1 = [2, 2, 3, 4]
# for i in range(4):
#     num = int(input("enter number: "))
#     list1.append(num)
visited = set()
# printing the maximum element
for count in range(2):
    for i, num in enumerate(list1):
        if num == min(list1):
            if i == 0:
                if 'A' not in visited:
                    visited.add('A')
                    print("A is smallest")
                    print(visited)
                    break

            elif i == 1:
                if 'B' not in visited:
                    visited.add('A')
                    print(visited)
                    print("B is smallest")
                    break

            elif i == 2:
                if 'C' not in visited:
                    visited.add('C')
                    print(visited)
                    print("c is smallest")
                    break
            elif i == 3:
                if 'D' not in visited:
                    visited.add('S')
                    print(visited)
                    print("D is smallest")
                    break
            print("==========================")

# mylist = [5,2,3,1,1]
# minval = min(mylist)
# print(f"Smallest value is {minval}")
# smallest = [i for i, v in enumerate(mylist) if v == minval]
# print(f"The smallest value occurs at the following indexes: {smallest}")