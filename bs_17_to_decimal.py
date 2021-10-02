

numbers = range(17)
digits = '0123456789ABCDEFG'
mapping = dict(zip(digits, numbers))

num = input()
base = input())   # use 17 or any base you want to convert to decimal_value

power = 1
decimal_value = 0
for i in reversed(num):
    rem = mapping[i]
    # print("rem: ", rem)

    decimal_value += int(rem) * power
    power *= base

print(decimal_value)



