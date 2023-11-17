import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort()
B.sort(reverse=True)

n_sum = 0
for i in range(N):
    n_sum += A[i] * B[i]

print(n_sum)
