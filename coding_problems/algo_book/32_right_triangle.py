import sys

N = int(sys.stdin.readline())
triangle = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def solution():
    dp = [[0] * i for i in range(1, N + 1)]
    dp[0][0] = triangle[0][0]

    for i in range(1, N):
        for j in range(i + 1):
            left, right = 0, 0

            if j - 1 >= 0:
                left = dp[i - 1][j - 1]

            if j < i:
                right = dp[i - 1][j]

            dp[i][j] = triangle[i][j] + max(left, right)

    return max(dp[-1])

print(solution())
