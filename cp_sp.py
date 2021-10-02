cp=int(input("enter the cost price\n"))
sp=int(input("enter the selling price\n"))

if(cp>sp):
    print("loss ")
    loss=cp-sp
    print("loss is",loss)
else:
    print("profit")
    profit=sp-cp
    print("profit is ",profit)

