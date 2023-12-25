import sys

N = int(sys.stdin.readline())

def solve(num: int):
    for i in range(2, 1_000_000):
        if num % i == 0:
            return "NO"
    return "YES"

ans = []
for _ in range(N):
    num = int(sys.stdin.readline())
    ans.append(solve(num))

print(*ans, sep="\n")
