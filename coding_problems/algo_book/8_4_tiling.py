def solution(tile_length: int) -> int:
    dp = [0] * tile_length
    dp[0] = 1
    dp[1] = 3

    for i in range(2, tile_length):
        dp[i] = dp[i-1] + 1 + (dp[i - 2] * 2)

    return dp[-1] % 796796

print(solution(3))
