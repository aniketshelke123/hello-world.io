binary_list = []
def convert_to_binary():
    return bin(num)


def append_to_list():
    for digit in binary_num:
        binary_list.append(digit)

def max_zero():
    count, max_count = 0, 0
    for digit in binary_list:
        if digit == '1':
            count = 0
        else:
            count += 1
            if count > max_count:
                max_count = count
    return max_count

num = int(input("Enter any number: "))
binary_num = convert_to_binary()
print(binary_num)
append_to_list()
binary_list = binary_list[2:]
print(binary_list)
print("continuous maximum zeroes are: ", max_zero())

