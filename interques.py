#program to find group for a given book sale count
a=int(input("enter a number"))
if(a>30 and a<50):
    print("D")
elif(a>51 and a<60):
    print("C")
elif(a>61 and a<80):
    print("B")
elif(a>81 and a<100):
    print("A")
else:
    print("NOT Available")
