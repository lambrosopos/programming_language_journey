import sys
import math

def solve():
    # Combination Theory
    N, M = map(int, sys.stdin.readline().split())
    return math.factorial(M) // (math.factorial(N) * math.factorial(M - N))


N = int(sys.stdin.readline())

ans = []
for _ in range(N):
    ans.append(solve())

for a in ans:
    print(a)
