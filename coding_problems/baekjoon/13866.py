import sys

levels = list(map(int, sys.stdin.readline().split()))

levels.sort(reverse=True)

print(levels)

print(levels[0] + levels[3] - levels[1] - levels[2])
