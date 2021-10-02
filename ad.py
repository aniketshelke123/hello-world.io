import random
check=[]

n1=int(input("ENTER VALUE OF X :"))
n2=int(input("ENTER VALUE OF Y :"))
ord=[int (e) for e in str(n1)]
q=ord.__len__()

temp=n1
val=1
i=1
while(i<q):
    val=val*10
    i=i+1
i=1

while(True):
    n1=n1//val
    val=val//10
    ord.append(n1)
    n1=temp
    if (val == 0):
        break
    i = i + 1
add=0
i=0
while(True):
    op=random.choice(ord)
    if (check == op):
        continue
    check.append(op)
    w=sum(check)
    if (w > n2):
        add = 0
        check.clear()
        continue
    if(w==n2):
        break
    i=i+1
print("Result =  X",check, "Which is equal to Y that is  Y = ",n2)