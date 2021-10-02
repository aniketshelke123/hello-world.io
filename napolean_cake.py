answer = []
cake_dict = {}
test_cases = int(input())
for num in range(test_cases):
    no_of_cakes = int(input())
    no_of_cake_layers = list(map(int, input().split(" ")))
    # print(no_of_cake_layers)

    counter = 1
    for i in no_of_cake_layers:
        cake_dict[counter] = i
        counter += 1

    for index, values in cake_dict.items():
        if values == 0:
            cake_dict[index] = False
        else:
            # print(values, index)
            for k in range(values):
                # print("k , Value, index is:", k, values, index)
                if index - k == 0:
                    break
                else:
                    cake_dict[index - k] = True
                # print(temp)
    # print(cake_dict)
    for values in cake_dict.values():
        if not values:
            answer.append(0)
        else:
            answer.append(1)
    print(*answer)
    cake_dict.clear()
    answer.clear()
