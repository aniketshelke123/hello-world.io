import collections as co

student = co.namedtuple("student", ["name", "enroll", "email"])
a = input("enter name: ")
b = input("enter enroll: ")
c = input("enter email: ")
S = student(a, b, c )
print(S[0], S[1], S[2])