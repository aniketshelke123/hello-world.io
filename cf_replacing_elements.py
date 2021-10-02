def check():
    for a in range(len(array)):
        for b in array[a+1:]:
            if int(array[a]) + int(b) <= int(d):
                replace = int(array[a] + b)
                return replace

    return False


test_cases = int(input())
for l in range(test_cases):
    n_d = input()
    n, d = n_d.split(" ")
    array = list(map(int, input().split()))
    replace = check()
    # array = map(lambda x: replace if int(x) > int(d) else x, array)
    win = 0
    lose = 0
    for index, x in enumerate(array):
        if int(x) > int(d):
            if replace:
                array[index] = replace
                win += 1
            if not replace:
                lose += 1
            # elif int(x) <= int(d):
            #     win += 1
    print("win", win)
    print("lose", lose)
    if win:
        print("yes")
        # break
    elif lose:
        print("No")
    elif win == 0 and lose == 0:
        print("yes")
    print(array)


