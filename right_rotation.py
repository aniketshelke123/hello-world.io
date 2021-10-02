
answer = []
num = [1 ,2, 3 , 4 ,5]
k = 1
for i in range(0, len(num)):
    temp = num[(i - k) % len(num)]
    answer.append(temp)

print(answer)

    
