import sys

A, B = map(int, sys.stdin.readline().split())

def reverse(num: int) -> int:
    num = str(num)
    return int(num[::-1])

print(reverse(reverse(A) + reverse(B)))
