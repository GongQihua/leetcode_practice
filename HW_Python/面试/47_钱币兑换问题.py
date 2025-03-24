def count_ways(N):
    dp = [0] * (N + 1)
    dp[0] = 1

    for coin in [1,2,3]:
        for i in range(coin, N + 1):
            dp[i] += dp[i - coin]
    return dp[N]


N = 5
print(count_ways(N))  # 5