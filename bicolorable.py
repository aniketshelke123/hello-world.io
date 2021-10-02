#
# dict_of_pairs = {}
# answer = {}
# visited = []
# vertices = int(input("Enter the number of vertices: "))
# pairs = int(input("Enter the number of pairs: "))
#
# colors = ["red", "blue"]
# col_len = len(colors)
# col_cur = 0
#
# for i in range(pairs):
#     a, b = input("Enter the graph pairs seperated by ',' : ").split(',')
#     dict_of_pairs[i] = a, b
#     if a not in visited:
#         answer[a] = colors[col_cur]
#         visited.append(a)
#         col_cur = (col_cur+1) % col_len
#     else:
#         col_cur = (colors.index(answer[a])+1) % col_len
#     if b not in visited:
#         answer[b] = colors[col_cur]
#         visited.append(b)
#         col_cur = (col_cur+1) % col_len
#
# print(answer)
#
# for value in dict_of_pairs.values():
#     a, b = value
#     if answer.get(a) == answer.get(b):
#     #if answer.get(x for x in 'ab') == 'red' or answer.get(x for x in 'ab') == 'blue':
#         print('=' * 30)
#         print("not-bicolorable..!!")
#         break
#
# else:
#     print('=' * 30)
#     print("Bicolorable..!!")
#



#
# dict_of_pairs = {}
# answer = {}
# visited = []
# vertices = int(input("Enter the number of vertices: "))
# pairs = int(input("Enter the number of pairs: "))
#
# for i in range(pairs):
#     a, b = input("Enter the graph pairs seperated by ',' : ").split(',')
#     dict_of_pairs[i] = a, b
#     if a not in visited:
#         answer[a] = 'red'
#         visited.append(a)
#     if b not in visited:
#         answer[b] = 'blue'
#         visited.append(b)
#     # print(visited)
# # print(dict_of_pairs)
# print(answer)
#
#
# for value in dict_of_pairs.values():
#     a, b = value
#     if answer.get(a) == answer.get(b):
#     # if answer.get(x for x in 'ab') == 'red' or answer.get(x for x in 'ab') == 'blue':
#         print('=' * 30)
#         print("not-bicolorable..!!")
#         break
#
# else:
#     print('=' * 30)
#     print("Bicolorable..!!")
#     # break
vertex = {}
color = {}
edge = int(input("ENTER NUMBER OF EDGES : "))
vertices = int(input("ENTER NUMBER OF VERTICES : "))
i = 0
while i < vertices:
    a, b = input().split()
    color[a] = "red",
    color[b] = "blue"
    vertex.setdefault(i, [a]).append(b)
    i = i + 1
count = 0
i = 0
while i < vertex.__len__():
    a = vertex[i][0]
    b = vertex[i][1]
    if color[a] == color[b]:
        count = 1
        print("=" * 30)
        print('NOT BICOLORABLE')
        break
    i = i + 1
if count == 0:
    print("=" * 30)
    print('BICOLORABLE')


