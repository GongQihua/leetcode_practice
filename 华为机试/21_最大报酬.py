def maximize_reward(T, n, tasks):
    dp = [0] * (T + 1)

    for t, w in tasks:
        for i in range(T, t - 1, -1):
            dp[i] = max(dp[i], dp[i - t] + w)

    return dp[T]

if __name__ == "__main__":
    T, n = map(int, input().split())
    tasks = []

    for _ in range(n):
        t, w = map(int, input().split())
        tasks.append((t, w))
    
    result = maximize_reward(T, n, tasks)
    print(result)