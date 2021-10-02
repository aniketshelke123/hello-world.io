vowels = ['a', 'e' , 'i', 'o', 'u']
answer = []
vowels_dict = {'a': 0, 'e':0, 'i': 0, 'o': 0, 'u': 0}
st = input()
for i in st:
    if i in vowels:
        vowels_dict[i] += 1
    else:
        answer.append(i)

for j, k in vowels_dict.items():
    print(f'{j}: {k}')
print("".join(answer))


