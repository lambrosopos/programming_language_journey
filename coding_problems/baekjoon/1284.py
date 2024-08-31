import sys


def solve(num: str) -> int:
    total = 2 + (len(num) - 1)

    for n in num:
        if n == '1':
            total += 2
        elif n == '0':
            total += 4
        else:
            total += 3

    return total


def main():
    while True:
        num = sys.stdin.readline().rstrip()

        if num == '0':
            break
        else:
            print(solve(num))

if __name__ == "__main__":
    main()
