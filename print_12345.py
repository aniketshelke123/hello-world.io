#if __name__ == '__main__':
   # n = int(input().strip(__doc__))
#if n % 2 != 0:
#     print("Weird")
# if n % 2 == 0:
#     if n>6 and n<20:
#         print("Weird")
#     else:
#         print("Not Weird")
# ls = []
# ls2 = []
# n = int(input("Enter any interger n: "))
#
# for num in range(1, n+1):
#      a = ls.append(num)
# for num in ls:
#     ls2.append(str(num))
# print(ls2)
#
# controller = ""
# for num in ls2:
#     controller += num
# print(controller)


#or

ls = []
ls2 = []
n = int(input("Enter any interger n: "))

for num in range(1, n+1):
     a = ls.append(num)
print(ls)
for num in ls:
    ls2.append(str(num))
print(ls2)
d = "".join(ls2)
print(d)


