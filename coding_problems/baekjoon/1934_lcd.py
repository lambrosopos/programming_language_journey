import sys

N = int(sys.stdin.readline())

def lcm(A: int, B: int):
    return (A * B) // gcd(A, B)

def gcd(A: int, B: int):
    if B == 0:
        return A
    return gcd(B, A % B)


answers = []
for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())
    answers.append(lcm(A, B))

for a in answers:
    print(a)
