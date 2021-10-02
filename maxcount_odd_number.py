answer = []
di = {}


def max_count_odd_number(str_list):
    for i in str_list:
        if int(i) % 2 != 0:
            di[i] = str_list.count(i)

    # print(di)
    all_values = di.values()
    max_value = max(all_values)
    for i, value in di.items():
        if value == max_value:
            return i


st = input()
str_list = st.split(" ")
print(max_count_odd_number(str_list))
