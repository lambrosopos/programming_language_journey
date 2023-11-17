import sys

N = int(sys.stdin.readline())

count = 0
for length in [64, 32, 16, 8, 4, 2, 1]:
    while N // length >= 1:
        count += N // length
        N = N % length

print(count)

