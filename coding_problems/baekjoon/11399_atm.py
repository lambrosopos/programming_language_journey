import sys

N = int(sys.stdin.readline())
times = list(map(int, sys.stdin.readline().split()))

times.sort()

total = 0
acc = 0
for i in times:
    acc += i
    total += acc

print(total)
