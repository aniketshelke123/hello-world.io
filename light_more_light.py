# prog for light bulb
bulb = {}
bulb.get(round, False)

n = int(input("Enter the number of bulbs: "))
i = 1
while i <= n:
    for round in range(1, n+1):
        if round % i == 0:
            bulb[round] = not bulb.get(round, False)
    i += 1
print("************")
# print(bulb)
if not bulb.get(n):
    print("Last bulb is off")
else:
    print("Last bulb is on")
