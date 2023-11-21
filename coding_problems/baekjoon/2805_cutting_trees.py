import sys

N, length = map(int, sys.stdin.readline().split())

trees = list(map(int, sys.stdin.readline().split()))

right = max(trees)
left = 1

while left <= right:
    mid = (left + right) // 2

    tree_cut = 0
    for t in trees:
        if t > mid:
            tree_cut += t - mid

    if tree_cut >= length:
        left = mid + 1
    else:
        right = mid - 1

print(right)
