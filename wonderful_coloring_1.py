
red = []
green = []
st_list = []
test_cases = int(input())
for j in range(test_cases):
    st = str(input())
    for i in st:
        st_list.append(i)

    "count letters"
    counts = {}
    for letter in st_list:
        if letter not in counts:
            counts[letter] = 1
        else:
            counts[letter] += 1
    print(counts)
    "make lists"
    for letter, count in counts.items():
        if count > 1:
            red.append(letter)
            green.append(letter)
            # print(red, green)
        else:
            red.append(letter)
            green, red = red, green
            # print(red, green)
            # print("enddd")
    # print(red, green)
    if len(red) == 0 or len(green) == 0:
        print(0)
    else:
        print(min(len(red), len(green)))
    red.clear()
    green.clear()
    st_list.clear()
