# prog for character count
dict = {}


def split(a):
    return list(a)


x = input("Enter 1st paragraph:\n")
y = input("enter 2nd paragraph:\n")
z = input("Enter 3rd paragraph:\n")

a = x + " " + y + " " + z
c = split(a)
for word in c:
    if word == " ":
        continue
    dict.update({word: 0})
for word in c:
    if word == " ":
        continue
    dict[word] += 1
print("***************")
print(dict)




