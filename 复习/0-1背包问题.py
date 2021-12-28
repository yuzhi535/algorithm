weights = [1, 2, 3, 4]
money = [2, 3, 4, 5]
weight = 8


def bag(weights: list, money: list, weight: int) -> int:
    wsz = len(weights)
    dp = [0 for i in range(weight + 1)]
    for i in range(wsz):
        for j in range(weight, weights[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - weights[i]] + money[i])
    return dp[weight]


def bag_1(weights: list, money: list, weight: int) -> int:
    wsz = len(weights)
    dp = [[0 for j in range(weight + 1)] for i in range(weight + 1)]
    for i in range(wsz):
        for j in range(weight + 1):
            if j >= weights[i]:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i]] + money[i])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[wsz - 1][weight]


print(bag_1(weights=weights, money=money, weight=weight))
