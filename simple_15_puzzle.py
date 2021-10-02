
Initial_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
answer = []
list_of_F = []
for i in range(16):
    Initial_state[i] = int(input())
temp = Initial_state[:]

print("\n>> Initial state...!!")
print("=" * 30)

# prints in matrix form
a = 0
for i in range(16):
    a = a + 1
    print(temp[i], end="\t")
    if a == 4:
        print()
        a = 0

print("=" * 30)


def swap_right():
    zero = 0
    for i, num in enumerate(Initial_state):
        if num == zero:
            if temp[-1] != zero:
                temp[i] = temp[i + 1]
                temp[i + 1] = num
                return temp
            else:
                return False


def swap_left():
    zero = 0
    for i, num in enumerate(Initial_state):
        if num == zero:
            if temp[0] != zero:
                temp[i] = temp[i - 1]
                temp[i - 1] = num
                return temp
            else:
                return False


def swap_up():
    zero = 0
    for i, num in enumerate(Initial_state):
        if num == zero:
            if i > 3:
                temp[i] = temp[i - 4]
                temp[i - 4] = num
                return temp
            else:
                return False


def swap_down():
    zero = 0
    for i, num in enumerate(Initial_state):
        if num == zero:
            try:
                temp[i] = temp[i + 4]
                temp[i + 4] = num
                return temp
            except:
                return False


def misplaced_tiles():
    # check value of H
    misplaced_tiles = 0
    for x, y in zip(temp, Goal_state):
        misplaced_tiles += x != y
    return misplaced_tiles


step = 0
G = 1
for count in range(45):
    f5 = 1000
    if Initial_state == Goal_state:
        break

    else:
        # right swap logic
        print("After right swap...!!")
        g = G
        temp = Initial_state[:]
        right_swap = swap_right()
        if right_swap:
            g += 1
            print("g is: ", g)
            h = misplaced_tiles()
            print("misplaced tiles are(h):", h)
            f1 = g + h
            list_of_F.append(f1)
            print("value of f is:", f1)

        else:
            list_of_F.append(f5)
        print('=' * 30)

        # left swap logic

        print("After left swap...!!")
        g = G
        temp = Initial_state[:]
        left_swap = swap_left()
        if left_swap:
            g += 1
            print("g is: ", g)
            h = misplaced_tiles()
            print("misplaced tiles are:", h)
            f2 = g + h
            list_of_F.append(f2)
            print("value of f is:", f2)

        else:
            list_of_F.append(f5)
        print('=' * 30)

        # UP swap logic

        print("After swapping upward...!!")
        g = G
        temp = Initial_state[:]
        up_swap = swap_up()
        if up_swap:
            g += 1
            print("g is: ", g)
            h = misplaced_tiles()
            print("misplaced tiles are:", h)
            f3 = g + h
            list_of_F.append(f3)
            print("value of f is:", f3)

        else:
            list_of_F.append(f5)

        print("=" * 30)

        # DOWN swap logic

        print("After swapping Down...!!")
        g = G
        temp = Initial_state[:]
        down_swap = swap_down()
        if down_swap:
            g += 1
            print("g is: ", g)
            h = misplaced_tiles()
            print("misplaced tiles are:", h)
            f4 = g + h
            list_of_F.append(f4)
            print("value of f is:", f4)

        else:
            list_of_F.append(f5)

        print("=" * 30)

        for i, num in enumerate(list_of_F):
            if num == min(list_of_F):
                if i == 0:
                    print("F1 is smallest...")
                    print("After swapping right...")
                    list_of_F.clear()
                    h = misplaced_tiles()
                    print('=' * 30)
                    temp = Initial_state[:]
                    temp = swap_right()
                    if temp:
                        answer.append('R')
                        Initial_state = temp[:]
                        break

                elif i == 1:
                    print("F2 is smallest...")
                    print("After swapping left...")
                    list_of_F.clear()
                    h = misplaced_tiles()
                    print('=' * 30)
                    temp = Initial_state[:]
                    temp = swap_left()
                    if temp:
                        answer.append('L')
                        Initial_state = temp[:]
                        break

                elif i == 2:
                    print("F3 is smallest...")
                    print("After swapping upward...")
                    list_of_F.clear()
                    h = misplaced_tiles()
                    print('=' * 30)
                    temp = Initial_state[:]
                    temp = swap_up()
                    if temp:
                        answer.append('U')
                        Initial_state = temp[:]
                        break

                elif i == 3:
                    print("F4 is smallest...")
                    print("After swapping down...")
                    list_of_F.clear()
                    h = misplaced_tiles()
                    print('=' * 30)
                    temp = Initial_state[:]
                    temp = swap_down()
                    if temp:
                        answer.append('D')
                        Initial_state = temp[:]
                        break

            G = g
            print("G id", G)
        print(">>>New Initial State ...!!")
        print('=' * 30)
        a = 0
        for i in range(16):
            a = a + 1
            print(Initial_state[i], end="\t")
            if a == 4:
                print()
                a = 0
        print('=' * 30)
    step = step + 1

    if h == 0:
        print(">> Solved...!!")
        #print(answer)
        break
    if step == 45:
        print(">>  Not solvable...!!!")
        break
print("=" * 30)
print(answer)
