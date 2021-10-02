# Define a function "fun(x)" in such way: Add 1 to this value of 'x', if the result of addition
# contains any trailing zeroes (0) then remove all trailing zeroes and return the final value.
# If the result of addition does not contain any trailing zeroes then return the addition result.


def fun(num):
    # using list comprehensions
    digits = [int(num) for num in str(num)]
    no_zero_digits = [str(digits) for digits in digits if digits != 0]
    return no_zero_digits


num = int(input("enter any integer: "))
num += 1
list_of_digits = fun(num)
b = "".join(list_of_digits)
print(b)


