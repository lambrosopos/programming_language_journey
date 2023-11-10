import sys

N = int(sys.stdin.readline())

dp_list = [0] * 12
def dp(num: int) -> int:
    count = 0

    if num < 0:
        return count
    elif num == 0:
        return 1
    elif dp_list[num]:
        return dp_list[num]
    
    dp_list[num - 1] = dp(num - 1)
    dp_list[num - 2] = dp(num - 2)
    dp_list[num - 3] = dp(num - 3)

    count += dp_list[num - 1]
    count += dp_list[num - 2]
    count += dp_list[num - 3]

    return count

answers = [0] * N
for i in range(N):
    answers[i] = dp(int(sys.stdin.readline()))

print(*answers, sep="\n")
