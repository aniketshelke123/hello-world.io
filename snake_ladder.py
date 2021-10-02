#program for snake and ladder with two players

import random
# ladder
#{1:38, 4:14, 8:30, 21:42, 28:76, 50:67, 71:92, 80:99, }
# snakes
#{32:10, 36:6, 48:26, 62:18, 88:24, 95:56, 97:78}
record = {}
place = {}

player1 = input("enter the name of player 1: ")
record[player1] = []
place[player1] = []
player2 = input("enter the name of player 2: ")
place[player2] = []
record[player2] = []
print("player1 name is: ", player1)
print("player2 name is: ", player2)

def  ladder(v):
    if v == 1:
        v = 38
        print("\nWOW! you got a ladder \n your score is", v)
        return v
    if v == 4:
        v = 14
        print("\nWOW!! you got a ladder \n your score is", v)
        return v
    if v == 21:
        v = 42
        print("\nWOW!! you got a ladder \n your score is", v)
        return v
    if v == 28:
        v = 76
        print("\nWOW!! you got a ladder \n your score is", v)
        return v
    if v == 50:
        v = 67
        print("\nWOW!! you got a ladder \n your score is", v)
        return v
    if v == 71:
        v = 92
        print("\nWOW!! you got a ladder \n your score is", v)
        return v
    if v == 80:
        v = 99
        print("\nWOW!! you got a ladder \n your score is", v)
        return v
    return v
def snake(s):
    if s == 32:
        s = 10
        print("\nOOPS.... you got a snake\n you are at", s)
        return s
    if s == 36:
        s = 6
        print("\nOOPS.... you got a snake\n you are at", s)
        return s
    if s == 48:
        s = 26
        print("\nOOPS... you got a snake\n you are at", s)
        return s
    if s == 62:
        s = 18
        print("\nOOPS.... you got a snake\n you are at", s)
        return s
    if s == 88:
        s = 24
        print("\nOOPS.... you got a snake\n you are at", s)
        return s
    if s == 95:
        s = 56
        print("\nOOPS.... you got a snake\n you are at", s)
        return s
    if s == 97:
        s = 78
        print("\nOOPS.... you got a snake\n you are at", s)
        return s
    return s
pos1 = 0
pos2 = 0
i = 1
while True:

    roll = random.randint(1, 6)
    print(player1 + " got: ",roll)
    if roll + pos1 > 100:
        print("exceeds the limit 100")

    else:
        pos1 += roll
        if pos1 == 1 or pos1 == 4 or pos1 == 8 or pos1 == 21 or pos1 == 28 or pos1 == 50:
            square = ladder(pos1)
            print(player1 + " position is: ", square)
            pos1 = square
        elif pos1 == 32 or pos1 == 36 or pos1 == 48 or pos1 == 62 or pos1 == 88 or pos1 == 95 or pos1 == 97:
            square = snake(pos1)
            print(player1 + " position is: ", square)
            pos1 = square
        else:
            print(player1 + " position is: ", pos1)
        record[player1].append(roll)
        place[player1].append(pos1)

    print(player2 + " chance to roll a dice ")

    roll = random.randint(1, 6)
    print(player2 + " got: ", roll)
    if roll + pos2 > 100:
        print("exceeds the limit 100")
    else:
        pos2 += roll
        if pos2 == 1 or pos2 == 4 or pos2 == 8 or pos2 == 21 or pos2 == 28 or pos2 == 50:
            square = ladder(pos2)
            print(player1 + " position is: ", square)
            pos2 = square
        elif pos2 == 32 or pos2 == 36 or pos2 == 48 or pos2 == 62 or pos2 == 88 or pos2 == 95 or pos2 == 97:
            square = snake(pos2)
            print(player2 + " position is: ", square)
            pos2 = square
        else:
            print(player2 + " position is: ", pos2)
            record[player2].append(roll)
            place[player2].append(pos2)

    if pos1 == 100:
        print("********************************************")
        print(player1 + " won the match\n")
        break
    if pos2 == 100:
        print("********************************************")
        print(player2 + " won the match\n")
        break
    if pos1 == 100 or pos2 == 100:
        break
    print(player1 + " chance to roll a dice ")
print("***********************************************")
print(player1 + " reached ", pos1)
print(player2 + " reached ", pos2)
print("*** dice rolled *********")
print(record,"\n")
print("*****Ladder position*******")
print(place)






# if player1 == 100:
#     print("hurray...!!!!\n " + player1 + " won the game....")
# else:
#    print("hurray...!!!!\n " + player2 + " won the game....")



    # if sc == 1:

    #     if 100 % pos1 in [1, 2, 3, 4, 5, 6] and pos1 > 93:
    #          if sc == 100 % pos1:
    #              break
    #     pos1 = pos1 + sc
    #     print(player1 + " position is  ", pos1)
    #
    # elif sc == 2:

    #     if 100 % pos1 in [1, 2, 3, 4, 5, 6] and pos1 > 93:
    #        if sc == 100 % pos1:
    #            break
    #     pos1 = pos1 + sc
    #     print(player1 + " position is  ", pos1)
    #
    # elif sc == 3:

    #     if 100 % pos1 in [1, 2, 3, 4, 5, 6] and pos1 > 93:
    #          if sc == 100 % pos1:
    #              break
    #     pos1 = pos1 + sc
    #     print(player1 + " position is  ", pos1)
    #
    # elif sc == 4:

    #     if 100 % pos1 in [1, 2, 3, 4, 5, 6] and pos1 > 93:
    #        if sc == 100 % pos1:
    #            break
    #     pos1 = pos1 + sc
    #     print(player1 + " position is  ", pos1)
    #
    # elif sc == 5:

    #     if 100 % pos1 in [1, 2, 3, 4, 5, 6] and pos1 > 93:
    #        if sc == 100 % pos1:
    #            break
    #     pos1 = pos1 + sc
    #     print(player1 + " position is  ", pos1)
    #
    # elif sc == 6:

    #     if 100 % pos1 in [1, 2, 3, 4, 5, 6] and pos1 > 93:
    #        if sc == 100 % pos1:
    #            break
    #     pos1 = pos1 + sc
    #     print(player1 + " position is  ", pos1)
    #     print(player1 + " roll  again")
    #
    #     sc1 = random.randint(1, 6)
    #     print(player1 + " got: ", sc1)
    #
    #     if sc1 == 6:

    #         if 100 % pos1 in [1, 2, 3, 4, 5, 6] and pos1 > 93:
    #            if sc == 100 % pos1:
    #                break
    #         pos1 = pos1 + sc1
    #         print(player1 + " position is  ", pos1)
    #
    # sc3 = random.randint(1, 6)
    # print(player2 + " got: ", sc3)
    #
    #
    # if sc3 == 1:

    #     if 100 % pos2 in [1, 2, 3, 4, 5, 6] and pos2 > 93:
    #        if sc == 100 % pos2:
    #            break
    #     pos2 = pos2 + sc3
    #     print(player2 + " position is  ", pos2)
    #
    # elif sc3 == 2:

    #     if 100 % pos2 in [1, 2, 3, 4, 5, 6] and pos2 > 93:
    #        if sc == 100 % pos2:
    #            break
    #     pos2 = pos2 + sc3
    #     print(player2 + " position is  ", pos2)
    #
    # elif sc3 == 3:

    #     if 100 % pos2 in [1, 2, 3, 4, 5, 6] and pos2 > 93:
    #        if sc == 100 % pos2:
    #            break
    #     pos2 = pos2 + sc3
    #     print(player2 + " position is  ", pos2)
    #
    # elif sc3 == 4:

    #     if 100 % pos2 in [1, 2, 3, 4, 5, 6] and pos2 > 93:
    #        if sc == 100 % pos2:
    #            break
    #     pos2 = pos2 + sc3
    #     print(player2 + " position is  ", pos2)
    #
    # elif sc3 == 5:

    #     if 100 % pos2 in [1, 2, 3, 4, 5, 6] and pos2 > 93:
    #       if sc == 100 % pos2:
    #           break
    #     pos2 = pos2 + sc3
    #     print(player2 + " position is  ", pos2)
    #
    # else:

    #     if 100 % pos2 in [1, 2, 3, 4, 5, 6] and pos2 > 93:
    #        if sc == 100 % pos2:
    #            break
    #     pos2 = pos2 + sc3
    #     print(player2 + " position is  ", pos2)
    #     print(player2 + " roll  again")
    #
    #     sc4 = random.randint(1, 6)
    #     print(player2 + " got: ", sc4)
    #
    #     if sc4 == 6:
    #        # if pos2 >= 100:
    #             #continue
    #         if 100 % pos2 in [1, 2, 3, 4, 5, 6] and pos2 > 93:
    #            if sc == 100 % pos2:
    #                break
    #         pos2 = pos2 + sc4
    #         print(player2 + " position is  ", pos2)
    #
    #     else:

    #         if 100 % pos2 in [1, 2, 3, 4, 5, 6] and pos2 > 93:
    #            if sc == 100 % pos2:
    #                break
    #         pos2 = pos2 + sc4
    #         print(player2 + " position is  ", pos2)
    #
    #
    # if pos1 >= 100 or  pos2 >= 100:
    #     break





