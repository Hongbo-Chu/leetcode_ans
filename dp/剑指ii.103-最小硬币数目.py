#
# def coinChange(coins: list, amount: int) -> int:
#     # 用动态规划
#     f = [float("inf")] * (amount+1)  # i面值需要f[i]美硬币
#     coins.sort()
#     for i in range(len(coins)):
#         if coins[i]<=amount:
#             f[coins[i]] = 1
#     f[0] = 0
#     print(f)
#
#     for j in range(1, amount+1):
#         for k in range(len(coins)):
#             if j - coins[k] > 0:
#                 f[j] = min(f[j], f[j - coins[k]]+1)
#     print(f)
#
#     return f[amount]
#
# print(coinChange([1], 0))


def coinChange(coins: list, amount: int) -> int:
    dp = [float("inf")]*(amount+1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] = min(dp[i], dp[i-coin]+1)
    return dp[amount] if dp[amount] != float("inf") else -1

print(coinChange([2,5,7],27))