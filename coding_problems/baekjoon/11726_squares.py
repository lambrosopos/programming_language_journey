import sys

N = int(sys.stdin.readline())

a, b = 1, 1
for i in range(N):
    a, b = b, a + b

print(a)
