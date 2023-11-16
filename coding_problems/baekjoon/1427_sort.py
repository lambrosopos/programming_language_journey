import sys

N = sys.stdin.readline().strip()

numbers = []
for c in N:
    numbers.append(int(c))

numbers.sort(reverse=True)

print(*numbers, sep="")
