# Given an expression "x = y". You need to add plus(es) sign inside value of 'x' in such a way that it becomes equal to
# value of 'y' You try to add minimum numbers of plus(es) in value of 'x'. If there is no matching result then print
# (-1).


def num_into_digits(x):
    digits = [int(ele) for ele in str(x)]
    return digits


x = int(input("Enter any integer: "))
y = int(input("Enter any integer: "))
print(num_into_digits(x))
a = num_into_digits(x)
length = a.__len__()
print(length)
val = 1
i = 1
while i <= length:
    val = val * 10
    i += 1
print(val)


