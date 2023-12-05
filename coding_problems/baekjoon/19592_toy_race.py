import sys

N = int(sys.stdin.readline())

def solve():
    N, X, Y = map(int, sys.stdin.readline().split())
    
    winner = 1e9
    V = 0
    for i, c in enumerate(list(map(int, sys.stdin.readline().split()))):
        if i == (N - 1):
            # If no need for booster
            if X / c < winner:
                return V
            V = c

        winner = min(winner, X / c)

    left = 0
    right = Y * 2

    while left <= right:
        mid = (left + right) // 2

        course_record = 1 + ((X - mid) // V)

        if course_record > winner:
            left = mid + 1
        else:
            right = mid - 1

    if 1 + ((X - right) // V) >= winner:
        return -1

    return right
    

answers = [0] * N
for i in range(N):
    answers[i] = solve()

print(*answers, sep="\n")
