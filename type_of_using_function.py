from ast import literal_eval

def type_of(itr):
    for ele in itr:
        print(type(ele))

lst = ["aniket", 25.55, "vikas", False, 200]
tp = (100, True, "sagar", "abhi", 61.26)
print("list: ", lst)
print("tuple: ", tp)

for _ in range(2):
    lst.append(literal_eval(input("enter elements to enter in a list: ")))
print("updated list is:", lst)

type_of(lst)
print("**************")
type_of(tp)
