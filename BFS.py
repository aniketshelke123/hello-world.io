
from collections import deque

state = {}
visited = []
graph_dict = {0: [0, 1, 2, 3], 1: [4, 5], 2: [6, 7], 3: [8, 9], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
search_queue = deque()
search_queue += graph_dict[0]

while search_queue:
    person = search_queue.popleft()
    print(person)
    if person not in visited:
        visited.append(person)
        if person == 8:
            print("person found..!")
            break
        else:
            search_queue += graph_dict[person]

print("visited", visited)


