def converter(value):
    if type(value) == list:
        return tuple(value)
    elif type(value) == tuple:
        return list(value)
    elif type(value) == str:
        return value[::-1]
    elif type(value) == bool:
        if value == True:
            return not value
        else:
            return not value
    elif type(value) == int:
        return value * value
    elif type(value) == float:
        return value * value

lst = ["aniket", False, True]
tup = (50.36, "Paris", True)
a = 2.5
b = 25
c = True
d = False
print(converter(tup))
