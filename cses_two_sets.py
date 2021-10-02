even = []
odd = []
one_to_n = []
set_a = []
set_b = []

n = int(input())
sum_of_n = int(n * (n + 1) / 2)
if sum_of_n % 2 == 0:
    if n % 2 == 0:
        for _ in range(1, n + 1):
            one_to_n.append(_)
        for num in range(int(len(one_to_n) / 2)):
            if num % 2 == 0:
                set_a.append(one_to_n[0])
                set_a.append(one_to_n[-1])
                one_to_n.pop(0)
                one_to_n.pop()
            else:
                set_b.append(one_to_n[0])
                set_b.append(one_to_n[-1])
                one_to_n.pop(0)
                one_to_n.pop()

    else:
        for i in range(1, n + 1):
            one_to_n.append(i)
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        sum_of_half = 0
        sum_of_one_to_n = sum(one_to_n)
        while True:
            if sum_of_half != (sum_of_one_to_n / 2):
                set_a.append(odd[-1])
                sum_of_half += odd[-1]
                odd.pop()

            if sum_of_half != (sum_of_one_to_n / 2):
                set_a.append(even[0])
                sum_of_half += even[0]
                even.pop(0)
            if sum_of_half == (sum_of_one_to_n / 2):
                set_b = even
                set_b.extend(odd)
                break

    print("YES")
    print(len(set_a))
    print(*set_a)
    print(len(set_b))
    print(*set_b)
else:
    print("NO")
