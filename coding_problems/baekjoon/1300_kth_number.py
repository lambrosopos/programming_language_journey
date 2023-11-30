import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

left = 0
right = K # num has to be at least K

ans = K
while left <= right:
    mid = (left + right) // 2

    # count all the numbers for each row in N if smaller than mid
    count = 0
    for i in range(1, N + 1):
        count += min(mid // i, N) # Add N in case all [i][j] is smaller

    if count < K:
        # raise the left index since K has at K items before
        left = mid + 1
    elif count >= K:
        ans = mid
        right = mid - 1

print(ans)
