"""
Using divide and conquer strategy to minimize calculations
"""
import sys

A, B, C = map(int, sys.stdin.readline().split())

def divide_and_conquer(a: int, b: int):
    if b == 1:
        return a

    half = divide_and_conquer(a, b // 2)
    total = half * half % C
    print(f"{b=}, {half=}, {total=}")

    if b % 2 == 1:
        return total * a
    return total

def main():
    ans = divide_and_conquer(A, B) % C
    print(ans)

if __name__ == "__main__":
    main()
