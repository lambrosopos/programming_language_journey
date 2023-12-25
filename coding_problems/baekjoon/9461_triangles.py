import sys

N = int(sys.stdin.readline())

dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1


def solve(num: int):
    if dp[num] != 0:
        return dp[num]

    dp[num] = solve(num - 2) + solve(num - 3)

    return dp[num]

ans = []
for _ in range(N):
    ans.append(solve(int(sys.stdin.readline())))

print(*ans, sep="\n")
