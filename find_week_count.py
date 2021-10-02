
week = {"mon":0, "tue": 1, "wed": 2, "thu": 3, "fri": 4, "sat": 5, "sun":6}

day = input()
total_days = int(input())
count = 0

for index in range(0, total_days):
    x = week[day] + 1
    if (index + x) % 7 == 6:
        count += 1

print(count)


