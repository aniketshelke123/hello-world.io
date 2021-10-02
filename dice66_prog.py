#prog to print the user who got a repetative 6,6 on a die roll
import random
# record{ "savataar": [3, 5, 6], "teacher": [2,6,6]
#dict to store the records
record1 = {}

player1 = input("enter player1 name: ")
record1[player1] = []
player2 = input("enter player2 name: ")
record1[player2] = []
player3 = input("enter player3 name: ")
record1[player3] = []
print("player1 name is: ", player1)
print("player2 name is: ", player2)
print("player3 name is: ", player3)
print("!!!roll a die!!!!")
print( player1 + " chance to roll a die")

i = 1
while True:
    a = random.randint(1, 6)
    print(player1 + " got: ",a)
    record1[player1].append(a)

    if a == 6:
        print(player1 + " play again")
        b = random.randint(1, 6)
        print(player1 + " got: ",b)
        record1[player1].append(b)

        if b == 6:
          print("hurrayyy!!!!!!!")
          print("congrats " + player1 + " won!!!")

          break

    print( player2 + " chance to roll a die")

    c = random.randint(1, 6)
    print(player2 + " got: ",c)
    record1[player2].append(c)
    if c == 6:
        print(player2 + " play again")
        d = random.randint(1, 6)
        print(player2 + " got: ", d)
        record1[player2].append(d)
        if d == 6:
            print("hurrayyy!!!!!!!")
            print("congrats " + player2 + " won!!!")

            break
    print(player3 + " chance to roll a die ")

    e = random.randint(1,6)
    print(player3 + " got: ", e)
    record1[player3].append(e)

    if e == 6:
        print(player3 + " play again")
        f = random.randint(1,6)
        print(player3 + " got: ",f)
        record1[player3].append(f)
        if f == 6:
            print("hurrayyy!!!!!!!")
            print("Congrats " + player3 + " won!!!")

            break
    print("start again\n")

    i = i + 1
print("********scores*********")
print(record1)






