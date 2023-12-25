import sys

N, M = map(int, sys.stdin.readline().split())
numbers = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def solution():
    dp = [[0] * M for _ in range(N)]
    
    for i in range(N):
        dp[i][0] = numbers[i][0]

    for i in range(1, M):
        for j in range(N):
            left_top, left, left_bottom = 0, 0, 0

            if j - 1 >= 0:
                left_top = dp[j - 1][i - 1]

            left = dp[j][i - 1]

            if j + 1 < N:
                left_bottom = dp[j + 1][i - 1]

            dp[j][i] = numbers[j][i] + max(left_top, left, left_bottom)

    # print(*dp, sep="\n")

    return max([dp[i][-1] for i in range(N)])


print(solution())
