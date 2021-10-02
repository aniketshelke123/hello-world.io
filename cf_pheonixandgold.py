import random
answer = []


def fun_c(list_of_weight, limit):
    print("fun_cs")
    for i in range(10):
        q = list_of_weight.copy()
        random.shuffle(q)
        print("q is:", q)
        check = fun_b(q, limit)
        if check:
            # weight_list.clear()
            # answer.append(q)
            # print("answer is:", answer)
            print(check)
            print(answer.append(check))
            return check
        if not check:
            print(q, "asd")
            random.shuffle(q)
            fun_b(q, limit)
    return False


def fun_b(list_of_weight, limit):
    print("sss")
    sum_of_weight = 0
    p = list_of_weight.copy()
    print("p is", p)
    for w in p:
        sum_of_weight += w
        if sum_of_weight > limit:
            return p
        elif sum_of_weight == limit:
            return False


test_cases = int(input())
i = 0
while i < test_cases:
    no_of_weight, x = map(int, input().split(" "))
    weight_list = list(map(int, input().split(" ")))
    # print(weight_list)
    # print("=" * 30)
    maxi = max(weight_list)
    for weight in weight_list:
        if maxi > x:
            # print("maxi", maxi)
            weight_list.remove(maxi)
            # print(weight_list)
            new = [maxi]
            # print(new + weight_list)
            print("YES")
            print(*new + weight_list)
            break

        else:
            if weight < x:
                b = fun_b(weight_list, x)
                if b:
                    print("Yes")
                    print(*weight_list)
                    break
                if not b:
                    print("weight", weight_list)
                    z = fun_c(weight_list, x)
                    if z:
                        print("YES")
                        print(z)
                        break
                    if not z:
                        print("NO")
                        break
            elif weight == x:
                # print("weight == x")
                c = fun_c(weight_list, x)
                if c:
                    print("YES")
                    print(*weight_list)
                    break
                else:
                    print("NO")
                    break
        weight_list.clear()
    i += 1

# while True:
#     for index, weight in enumerate(weight_list):
#         if weight > x:
#             weight_list[0], weight_list[index] = weight_list[index], weight_list[0]
#             print("YES")
#             print(*weight_list)
#             break
#         else:
#             print("dsf")
#             break
#     break
