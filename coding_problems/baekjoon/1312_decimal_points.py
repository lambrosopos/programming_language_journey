import sys

A, B, N = map(int, sys.stdin.readline().split())

digit, remainder = A // B, A % B
while N > 0:
    remainder *= 10
    digit, remainder = remainder // B, remainder % B

    N -= 1

print(digit)
