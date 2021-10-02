
odd = []
even = []
res = []
test_cases = int(input())
for j in range(test_cases):
    n = int(input())
    array = list(map(int, input().split()))

    for i in array:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    print(*odd+even)
    odd.clear()
    even.clear()

