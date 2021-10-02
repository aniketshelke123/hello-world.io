
# ls = [1, 2, 3, 5]

# program to check and print ordinary numbers
list_of_ordinary = []
test_cases = int(input())
for j in range(test_cases):
    num = int(input())
    for i in range(1, num + 1):
        if len(set(str(i))) == 1:
            list_of_ordinary.append(i)

    print(len(list_of_ordinary))
    list_of_ordinary.clear()


