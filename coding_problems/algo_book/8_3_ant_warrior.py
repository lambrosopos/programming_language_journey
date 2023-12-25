example_1 = [
        4, [1, 3, 1, 5]
        ]


def solution(N, storages):
    dp = [0] * N

    dp[0] = storages[0]
    dp[1] = storages[1]

    for i in range(2, N):
        dp[i] = max(storages[i] + dp[i - 2], dp[i - 1])
        print(dp)

    return dp[-1]


print(solution(*example_1))
