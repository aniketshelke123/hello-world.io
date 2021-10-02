M = 1000000007
f = 1
n = int(input())
for i in range(1, n + 1):
    f = (f * i) % M  # Now f never can
    # exceed 10^9+7
print(f)
import math
a = math.sqrt(2)
print(pow(2, 447))