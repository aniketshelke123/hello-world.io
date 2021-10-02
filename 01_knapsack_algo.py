
def knapsack(maxWeight, weights, costs,  n):
    a = [[0 for x in range(maxWeight + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for j in range(maxWeight + 1):
            if i == 0 or j == 0:
                a[i][j] = 0
            elif weights[i - 1] <= j:
                a[i][j] = max(a[i - 1][j], costs[i-1] + a[i - 1][j - weights[i-1]])

            else:
                a[i][j] = a[i - 1][j]
    return a[n][maxWeight]


weights = [100, 100, 300]
costs = [1, 1, 1]
maxWeight = 300
n = len(costs)
print('=' * 30)
print(knapsack(maxWeight, weights, costs, n))











# def knapSack(maxWeight, weights, cost, n):
#     a = [[0 for x in range(maxWeight + 1)] for x in range(n + 1)]
#
#     # Build table K[][] in bottom up manner
#     for i in range(n + 1):
#         for j in range(maxWeight + 1):
#             if i == 0 or j == 0:
#                 a[i][j] = 0
#             elif weights[i - 1] <= j:
#                 a[i][j] = max(cost[i - 1]
#                               + a[i - 1][j - weights[i - 1]],
#                               a[i - 1][j])
#             else:
#                 a[i][j] = a[i - 1][j]
#
#     return a[n][maxWeight]
#
#
# cost = [600, 1000, 1500]
# weights = [2, 3, 4]
# maxWeight = 6
# n = len(cost)
# #print(len(maxWeight))
# print(knapSack(maxWeight, weights, cost, n))
