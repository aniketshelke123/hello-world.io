
A = []
B = []

weight = [int(input("enter player " + str(i) + " weight: ")) for i in range(1, int(input("enter no of players: "))+1)]
no_of_players = len(weight)
max_len = (len(weight) + 1) // 2

for i in range(no_of_players):
    if len(A) < max_len:
        if not weight:
            break
        else:
            max_weight = max(weight)
            if sum(A) <= sum(B):
                A.append(max_weight)
                weight.remove(max_weight)

    if len(B) < max_len:
        if not weight:
            break
        else:
            max_weight = max(weight)
            if sum(B) <= sum(A):
                B.append(max_weight)
                weight.remove(max_weight)

if len(B) == max_len:
    for i in weight:
        A.append(i)
else:
    for i in weight:
        B.append(i)


print('=' * 10)
print("Team 1 players:", A, "=", sum(A))
print("Team 2 players:", B, "=", sum(B))










# def split_weights(ws):
#     l1, l2 = [], []
#     s1, s2 = 0, 0
#     maxlen = (len(ws) + 1) // 2
#     for i, w in enumerate(reversed(ws)):
#         if s1 <= s2:
#             l1.append(w)
#             s1 += w
#             if len(l1) == maxlen:
#                 return l1, [*l2, *ws[:-i - 1]]
#         else:
#             l2.append(w)
#             s2 += w
#             if len(l2) == maxlen:
#                 return [*l1, *ws[:-i - 1]], l2
#
#
# print(split_weights([1, 2, 12, 13, 14, 15]))
# print(split_weights([1, 2, 3, 4, 5, 15]))
# print(split_weights([1, 2, 3, 4, 5, 6, 7]))
# print(split_weights([1, 2, 3, 14, 14, 15]))
