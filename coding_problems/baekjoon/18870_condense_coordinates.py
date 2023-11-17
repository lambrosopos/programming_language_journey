import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

counts = {}
new_n = list(set(numbers))
new_n.sort()

for i, n in enumerate(new_n):
    counts[n] = i

for n in numbers:
    print(counts[n], end= " ")
