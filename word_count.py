import pprint

a = input("Enter 1st paragraph:\n")
b = input("Enter 2nd paragraph:\n")
c = input("Enter 3rd paragraph:\n")
d = input("Enter 4th paragraph:\n")
e = input("Enter the 5th paragraph:\n")
f = input("Enter the 6th paragraph:\n")
g = input("Enter the 7th paragraph:\n")

para = a + " " + b  + " " + c + " " + d + " " + e + " " + f + "  " + g

dict_count = {}

unique = set(para.split())

for word in unique:
    dict_count.update({word: 0})

for word in para.split():
    dict_count[word] += 1


pprint.pprint(dict_count)

#input
# If you did know to whom I gave the ring,
# If you did know for whom I gave the ring
# And would conceive for what I gave the ring
# And how unwillingly I left the ring,
# When naught would be accepted but the ring,
# You would abate the strength of your displeasure.
# — The Merchant of Venice by Shakespeare