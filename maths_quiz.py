import random
import time
winner = ""
play_dict = {}
time_info = {}

def quiz_ques():
      opr = ['+', '-', '*', '/', '>', '<']
      a = random.randint(1,10)
      b = random.randint(1,10)
      c = random.choice(opr)
      ques = str(a) + str(c) + str(b)
      ans = eval(ques)
      return ques,ans

no_of_players = int(input("Enter the number of players: "))
for num in range(no_of_players):
     name1 = input("Enter player name: ")
     play_dict.update({name1 : 0})
play_names = list(play_dict)

i = 0
while True:

   player_name = play_names[i]
   print(player_name + " Get Ready!!!")
   print("your quiz stars in next 3 seconds......")
   time.sleep(3)
   print("*******")
   start_time = time.perf_counter()
   for _ in range(3):
       question, ans = quiz_ques()
       print(question)
       missed = 0
       for _ in range(3):
           user_ans = float(input("enter your answer: "))
           if ans == user_ans:
               print("correct answer")
               break
           else:
               missed += 1
               print("wrong answer, try again")
       if missed == 3:
           print(missed)
           print("you missed all the 3 attempts")
           print("next question")

   end_time = time.perf_counter()
   time_took = end_time - start_time
   print("you took " + str(time_took))
   print("*******************************************************************")
   play_dict[player_name] = time_took

   i = i + 1
   if i == no_of_players:
        break
least = min(play_dict.values())
for name in play_dict:
    if play_dict[name] == least:
        winner = name
print(play_dict)
print("The winner is:", winner)
