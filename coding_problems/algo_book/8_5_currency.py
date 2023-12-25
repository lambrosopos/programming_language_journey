import sys

N, M = map(int, sys.stdin.readline().split())
change = [int(sys.stdin.readline()) for _ in range(N)]

def solution():
    dp = [10_001] * (M + 1)
    dp[0] = 0

    for i in range(1, M + 1):
        for c in change:
            # 현재 금액 빼기 단위가 음수인 경우, 즉 도달할 수 없는 경우
            if i - c < 0:
                continue

            dp[i] = min(dp[i], dp[i - c] + 1)

    return dp[M] if dp[M] != 10_001 else -1

print(solution())
