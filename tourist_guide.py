from collections import defaultdict
visited = []
# list_of_bus_capacity = []
subs = []
total = []
max_capacity_for_a_given_route = []

class operation:
    def __init__(self):
        self.graph_info = defaultdict(list)
        self.list_of_bus_capacity = defaultdict(list)

    def inserting_values(self):
        pairs = int(input("pairs : "))
        i = 0
        while i < pairs:
            vertex1, vertex2, capacity = map(int, input().split(" "))
            self.graph_info[vertex1].append(vertex2)
            self.list_of_bus_capacity[vertex1, vertex2].append(capacity)
            i = i + 1
        # start, des = map(int, input().split(" "))

        # print(self.graph_info)
        # print(self.list_of_bus_capacity)

    def find_path(self, visited, start, destination):

        visited.append(start)
        if start == destination:
            for i in range(len(visited) - 1):
                subs.append((visited[i], visited[i + 1]))
            for sub in subs:
                # print(self.list_of_bus_capacity[sub])
                total.append(self.list_of_bus_capacity[sub])
            # print(visited)
            max_capacity_for_a_given_route.append(min(total))
            total.clear()
            subs.clear()

        else:
            for neighbour in self.graph_info[start]:
                if neighbour not in visited:
                    self.find_path(visited, neighbour, destination)

        visited.pop()

    def print_path(self):
        start = 1
        destination = 7

        self.find_path(visited, start, destination)


vertices = 7
g = operation()
g.inserting_values()
g.print_path()

capacity_for_best_route = max(max_capacity_for_a_given_route)
print("=" * 30)
for num in capacity_for_best_route:
    if 99 % num > 0:
        print((99 // (num - 1) + 1))
    else:
        print(99 // num)
