#prog fro print() function
# lst = ["rahul", 52, True, 41.255]
# print(lst)
# print("my name is aniket")
# print("i love to play football")

#prog for input()
# print("Where are you from: ")
# place = input()
# college = input("enter your college name: ")

# prog for bin()
# it returns the binary number for the given value
# a = 20
# b = bin(a)
# print(a)
# print(b)
# print(type(b))

#prog for oct(), it converts int into octal value
#not applicable for float
# a = 20
# b = oct(a)
# print(a)
# print(b)

# prog for hex(), it converts into hexadcimal
# not works for float
# a = 20
# b = hex(a)
# print(a)
# print(b)

#prog for ord(), returns the ASCII value
#can pass only single character
# char = ord("a")
# char2 = ord("A")
# print(char)
# print(char2)

#prog for chr(), returns the ASCII character for ASCII value
# num = chr(20)
# num2 = chr(100)
# print(num)
# print(num2)

# prog for eval(), return the answer for any arithmatic operations
# solve = eval("2 * 45 / 5 + 22")
# print(solve)

#prog for zip():
# lst = ["aniket", 41.25, False, 200]
# tup = ("Raj", 85, True)
# a = dict(zip(lst, tup))
# b = tuple(zip(lst, tup))
# print(a)
# print(b)

#prog for type(), returns datatype
lst = [True, 5.214, "vishal", [2000, 10.25], 100]
for elements in lst:
    print(type(elements))


