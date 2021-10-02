requeststring = input()
charcode = input()
count = 0
asci_value = ord(charcode)
for i in requeststring:
    if asci_value == ord(i):
        count += 1
print(count)