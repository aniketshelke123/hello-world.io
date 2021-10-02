
answer = []
num = [1 ,2, 3 , 4 ,5]
k = 1
for i in range(0, len(num)):
    temp = num[(i - k) % len(num)]  # right rotation
    # temp = num[(i + k) % len(num)]  for left roation
    answer.append(temp)

print(answer)

    
