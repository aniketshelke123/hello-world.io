
answer = []

test_cases = int(input())
for test in range(test_cases):
    N = int(input())
    string = list(str(input()))
    Q = int(input())

    X = list(map(int, input().split()))
    Y = list(map(str, input().split()))

    # modifying the strings...............
    for st in range(len(X)):
        num_in_x = X[st]
        string[num_in_x - 1] = Y[st]
        # print(string)
        count = 1
        maximum = 1

        # counting the consecutive distinct substring
        if len(string) > 1:
            for i in range(1, len(string)):
                if string[i - 1] == string[i]:
                    count += 1
                    if count > maximum:
                        maximum = count
                else:
                    count = 1
            answer.append(maximum)

    print(*answer)
