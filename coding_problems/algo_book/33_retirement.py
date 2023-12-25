import sys

N = int(sys.stdin.readline())

times = [0] * N
profit = [0] * N
for i in range(N):
    t, p = map(int, sys.stdin.readline().split())
    
    times[i] = t
    profit[i] = p


def solution():
    dp = [0] * (N + 1)

    sum_max = 0
    for i in range(N - 1, -1, -1):
        t, p = times[i], profit[i]

        if i + t <= N:
            dp[i] = max(p + dp[i + t], sum_max)
            sum_max = dp[i]
        else:
            dp[i] = sum_max

    return sum_max


print(solution())
