# program to print the game of stone ,paper, scissor.
import random

win = 0
lose = 0
tie = 0

print ("Play Stone,Paper,Scissor Game")

i = 1
while  True:
    i = i + 1

    a = random.randint(1,3)

    if (a==1):
       print("computer1 choose 1-Stone")
    elif(a==2):
       print("computer1 choose 2-Paper")
    else:
       print("computer1 choose 3-Scissor")

    b = random.randint(1,3)

    if(b==1):
       print("Computer2 choose 1-Stone")
    elif(b==2):
       print("Computer2 choose 2-Paper")
    else:
       print("Computer2 choose 3-Scissor")

    1=="stone"
    2=="paper"
    3=="scissor"

    if(a==1 and b==2) or (a==2 and b==3) or(a==3 and b==1):
       print("computer2 wins\n")
       result='lose'
    elif (a==1) and (b==3) or (a==2 and b==1) or (a==3 and b==2):
       print("computer1 wins\n")
       result='win'
    elif (a==1) and (b==1) or (a==2 and b==2) or (a==3 and b==3):
       print("match draw!\n")
       result='tie'

    if(i>6  ):
      break




    if (result=='win'):
        win +=1

    if(result=='lose'):
        lose =+1

    if(result=='tie'):
        tie +=1


print( "computer1 won: ",win)
print("computer2 won: ", lose)
print("game tie: ", tie)

