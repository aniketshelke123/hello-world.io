#program for alternate six(6,6)by using dictionary and list

import random
scores = {}
pnames = []

print("enter number of players: ")
pl = int(input())
print("enter names of", pl , "players")

i = 1
while i <= pl:
    n = input()
    pnames.append(n)
    scores[n] = list([])
    i = i + 1
first_six = False
pl_index = 0

while True:
    print("play your turn ", pnames[pl_index])
    print("press enter to rol the dice")
    input()
    sc = random.randint(1, 6)
    print("you rolled ", sc)
    scores[pnames[pl_index]].append(sc)

    if sc == 6 and first_six == False :
            first_six = True
            print("repeat your turn")
    elif sc == 6 and first_six == True:
            print(pnames[pl_index], "you win....!")
            break

    else:
            first_six = False
            pl_index = pl_index + 1

            if pl_index == pl:
                  pl_index = 0
print(scores)