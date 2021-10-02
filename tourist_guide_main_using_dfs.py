from collections import defaultdict
visited = []
list_of_bus_capacity = defaultdict(list)
subs = []
total = []
max_capacity_for_a_given_route = []


def dfs(visited, graph, node, destination):
    visited.append(node)
    # print('visited', visited)
    if node == destination:
        for i in range(len(visited) - 1):
            subs.append((visited[i], visited[i + 1]))
        for sub in subs:
            # print(self.list_of_bus_capacity[sub])
            total.append(list_of_bus_capacity[sub])
        # print(visited)
        max_capacity_for_a_given_route.append(min(total))
        total.clear()
        subs.clear()
        # print(visited)
    else:
        for neighbour in graph[node]:
            if neighbour not in visited:
                dfs(visited, graph, neighbour, destination)
    visited.pop()


# Driver Code
graph = defaultdict(list)
vertices = input("Enter vertices: ")
pairs = int(input("enter pairs : "))

for num in range(pairs):
    v1, v2, capacity = map(int, input().split())
    graph[v1].append(v2)
    list_of_bus_capacity[v1, v2].append(capacity)

node = int(input("enter starting point: "))
destination = int(input("Enter destination: "))
no_of_passengers = int(input("Enter the number of passengers: "))
dfs(visited, graph, node, destination)

capacity_for_best_route = max(max_capacity_for_a_given_route)
print("=" * 30)
for num in capacity_for_best_route:
    if no_of_passengers % num > 0:
        trips = (no_of_passengers // (num - 1) + 1)
        print("No of trips: ", trips)
    else:
        trips = no_of_passengers // num
        print("No of trips: ", trips)








# Important code to get the weights from graph using path

# path weight finding
# weights = {
#   (1, 2): 30,
#   (2, 4): 25,
#   (4, 7): 35
# }
# path = [1, 2, 4, 7]
# subs = []
# total = []
# for i in range(len(path)-1):
#     print(path[i], path[i + 1])
#     subs.append((path[i], path[i+1]))
# for sub in subs:
#     print(weights[sub])
#     total.append(weights[sub])
# print(subs)
# print(total)

