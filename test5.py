vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
requiredstring = input()
count = 0
for i in range(len(requiredstring) - 1):
    if requiredstring[i] in vowels:
        if requiredstring[i + 1] not in vowels:
            count += 1
print(count)