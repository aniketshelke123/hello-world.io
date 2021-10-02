import random
run = [0,1,2,3,4,5,6,"OUT"]
out = ["catch out","LBW","stumping","run out","hit wicket","bowled"]
tsc = [0,0]
w = [0,0]
b = False


def show(bat1,bat2,sc1,sc2,w1,w2):
    if sc2 > sc1:
        a = 10 - w2
        print("CONGRATULATIONS!!", bat2, "WON!! the match", a, "wickets")
    else:
        g = sc1 - sc2
        print("CONGRATULATIONS!!", bat1, "WON!! the match", g, "runs")
    if tsc[0] == tsc[1]:
        print("Match got TIED")
    print("from show")


q = False
r1 = r2 = r3 = r4 = 0


def call_toss(q):
    print("Captain of first team TOSS the coin\nCaptain of second team call")
    print("1:Head\n2:Tail")
    print("Enter your call")
    call = int(input())
    print("Captain of first team press enter to toss the coin")
    input()
    toss = ["HEAD", "TAIL"]
    cl = random.choice(toss)
    if (call == 1 and cl == "HEAD") or (call == 2 and cl == "TAIL"):
        print("It's", cl, "Congo!! You won the Toss")
        print("what will you choose\n1:Batting\n2:Bowling")
        ch = int(input())
        if ch == 1:
            print(team2, "choose to Bat first\n", team1,"will Bowl")
            BATTING(nms2,tsc,w,1,plsc2)   #calling for first inning
            print("'One inning completed'\n", team2, "scored", tsc[1], "runs with loss of", w[1], "wickets")
            q = True
            print(team1,"need",tsc[1]+1,"to win the match")
            print("Second inning starts")
            print(team1, "will bat now")
            BATTING(nms1,tsc,w,0,plsc1)   #calling for seconf inning
            show(team2,team1,tsc[1],tsc[0],w[1],w[0])
        elif ch == 2:
            print(team2, "chose to bowl first\n", team1, "will Bat")
            BATTING(nms1,tsc,w,0,plsc1)  #calling for first inning
            print("One inning completed\n", team1, "scored", tsc[0], "runs with loss of", w[0], "wickets")
            q = True
            print(team2, "need", tsc[0] + 1, "to win the match")
            print("Second inning starts")
            print(team2, "will bat now")
            BATTING(nms2,tsc,w,1,plsc2)  #calling for seconf inning
            show(team1,team2,tsc[0],tsc[1],w[0],w[1])
    else:
        print("It's", cl, team1, "won the Toss")
        print("what will you choose\n1:Batting\n2:Bowling")
        ch = int(input())
        if ch == 1:
            print(team1, "chose to Bat first\n", team2, "will Bowl")
            BATTING(nms1,tsc,w,0,plsc1)  #calling for first inning
            print("One inning completed\n", team1, "scored", tsc[0], "runs with loss of", w[0], "wickets")
            q = True
            print(team2, "need", tsc[0] + 1, "to win the match")
            print("Second inning starts")
            print(team2, "will bat now")
            BATTING(nms2,tsc,w,1,plsc2)  #calling for seconf inning
            show(team1,team2,tsc[0],tsc[1],w[0],w[1])
        elif ch == 2:
            print(team1, "chose to bowl first\n", team2, "will Bat")
            BATTING(nms2,tsc,w,1,plsc2)#calling for first inning
            print("One inning completed\n",team2,"scored",tsc[1],"runs with loss of",w[1],"wickets")
            q = True
            print(team1, "need", tsc[1] + 1, "to win the match")
            print("Second inning starts")
            print(team1,"will bat now")
            BATTING(nms1,tsc,w,0,plsc1)  #calling for second inning
            show(team2,team1,tsc[1],tsc[0],w[1],w[0])


f = False
# q = False


def BATTING(team,tsc,w,t,p):
    h = 0      #for changing players
    b = 0     #for counting balls
    ov = 0   #for counting over
    while True:

        print(team[h],"is batting")
        r = random.choice(run)
        input()
        if r == "OUT":
            o = random.choice(out)
            print(team[h],"got out by:",o)
            h = h + 1
            w[t] = w[t] + 1
        elif r == 4:
            print(team[h]," hit the BOUNDARY")
            tsc[t] = tsc[t] + r
            if q == True:
                plsc2[h] = plsc2[h] + r
            else:
                plsc1[h] = plsc1[h] + r
        elif r == 6:
            print(team[h], " hit the SIXXERR!!!!")
            tsc[t] = tsc[t] + r
            if q == True:
                plsc2[h] = plsc2[h] + r
            else:
                plsc1[h] = plsc1[h] + r
        else:
            print(team[h],"scored",r,"run")
            tsc[t] = tsc[t] + r    #total score of team
            if q == True:
                plsc2[h] = plsc2[h] + r
            else:
                plsc1[h] = plsc1[h] + r  #total score of player batting
        if q == True and (tsc[1] > tsc[0] or tsc[0] > tsc[1]):
            #f = True
            #z = f
            break

        b = b + 1
        print("Total Score:",tsc[t])
        #print(plsc1)
        #print(plsc2)
        if b == 6:
            ov = ov + 1
            print(ov,"over completed")
            print("Score:",tsc[t],"Wicket:",w[t])
            b = 0
        if h == 11:
            print("All Out")
            break
        if (ov == 5 and over == 1) or (ov == 10 and over == 2):
            break

print("WELCOME TO 'AURANGABAD PREMIER LEAGUE'")
d1 = {}
print("Enter name of first team")
team1 = input()
d1[team1] = []
print("Enter name of second team")
team2 = input()
d1[team2] = []
print("Enter number of overs of the match:\n1-5 overs\n2-10 overs")
over = int(input())
print(d1)
print(over)
names =["Rahul","Akash","Sameer","Ramesh","Suresh","Karan","Adnan","Nadeem","Sundar","Natrajan","Moin","Pande",
        "Jadhav","Pranav","Parth","Sagar","Shubham","Rushi","Tiwari","Gopal","Piyush","Kartik","Amey","Mustafa",
        "Yash","Arjun","Kunal","Vivek","Pratik","Vedant","Tejas","Ashwin","Nikhil","Siraj","Suraj","Hasan","Ajas"]
i = 0
plsc1 = []; nms1 = [] #nms1 for names of the players of team 1
nms2 = []  #nms2 for names of the players of team 2
while i < 11:
    nm = random.choice(names)
    d1[team1].append(nm)
    plsc1.append(0)
    i = i + 1
nms1 = d1[team1]
print(team1,"players are",d1[team1])
i = 0
plsc2 = []
while i < 11:
    nm = random.choice(names)
    d1[team2].append(nm)
    plsc2.append(0)
    i = i + 1
nms2 = d1[team2]
print(team2,"players are",d1[team2])
call_toss(q)