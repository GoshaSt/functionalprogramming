def knapsack(weights, values, max_weight):
    n = len(weights)
    dp = [0] * (max_weight + 1)
    for i, w in enumerate(weights):
        for j in range(max_weight, w - 1, -1):
            dp[j] = max(dp[j], dp[j - w] + values[i])
    return dp[max_weight]


weights = [100, 300, 400, 500]
values = [1, 4, 5, 7]
max_weight = 800
print(knapsack(weights, values, max_weight))