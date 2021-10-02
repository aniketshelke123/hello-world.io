#program to print the gross salary of an employee
s=int(input("enter the salary of an employee"))
TA=s*8/100
DA=s*12/100
HRA=s*14/100
gross_s=s+TA+DA+HRA
print("gross salary is:",gross_s)