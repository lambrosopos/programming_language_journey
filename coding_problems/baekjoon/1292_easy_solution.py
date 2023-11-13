import sys

start, end = map(int, sys.stdin.readline().split())

numbers = []
for i in range(1, 1001):
    for j in range(i):
        numbers.append(i)

print(sum(numbers[start - 1:end]))

