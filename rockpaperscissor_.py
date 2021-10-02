# program to print the game of stone ,paper, scissor.
# ask how many times to play
# user vs computer
import random

win = 0
lose = 0
tie = 0

print("Play Stone,Paper,Scissor Game")
print("enter your name: ")
nm=input()
print("how many times would you like to play")
p=int(input())
i=1
while  i<=p:
    print("choose any one value: ")
    print("1-stone\n2-paper\n3-scissor ")
    a=int(input())

    if (a==1):
       print(nm+" choose 1-Stone")
    elif(a==2):
       print(nm+" choose 2-Paper")
    else:
       print(nm+" choose 3-Scissor")
    b=random.randint(1,3)

    if(b==1):
       print("Computer choose 1-Stone")
    elif(b==2):
       print("Computer choose 2-Paper")
    else:
       print("Computer choose 3-Scissor")

    1=="stone"
    2=="paper"
    3=="scissor"

    if(a==1 and b==2) or (a==2 and b==3) or(a==3 and b==1):
       print("computer wins\n")
       result='lose'
    elif (a==1) and (b==3) or (a==2 and b==1) or (a==3 and b==2):
       print(nm + " wins\n")
       result='win'
    elif (a==1) and (b==1) or (a==2 and b==2) or (a==3 and b==3):
       print("match draw!\n")
       result='tie'
    i=i+1

    if (result=='win'):
        win +=1

    if(result=='lose'):
        lose =+1

    if(result=='tie'):
        tie +=1


print(nm + " won: ",win)
print("computer won: ", lose)
print("game tie: ", tie)

