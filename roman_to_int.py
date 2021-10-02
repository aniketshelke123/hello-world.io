
def convert_to_int(roman):
    roman_dict = {'I': 1, 'V': 5, 'X': 10 ,'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    for i in range(0, len(roman)):
        if i + 1 < len(roman) and roman_dict[roman[i]] < roman_dict[roman[i + 1]]:
            res -= roman_dict[roman[i]]
        else:
            res += roman_dict[roman[i]]
    return res                  

roman = input()
print(convert_to_int(roman))

