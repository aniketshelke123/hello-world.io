#Write a program to print the laargest truss taking two input
#a truss is a triangle here used by architect
b1=int(input("enter the base of the truss")) 
h1=int(input("enter the height of truss"))
a1=(b1*h1/2)
print("the area of truss A is: 0",a1)
b2=int(input("enter the base of the truss"))
h2=int(input("enter the height of truss"))
p1=(b2*h2/2)
print("the area of truss B is: ",b1)
if(a1>p1):
    print("a1 is greater")
else:
    print("p1 is greater")