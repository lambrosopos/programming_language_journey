import sys
sys.setrecursionlimit(10_000_000)

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()

def print_sequence(start_idx: int, sequence: str):
    if len(sequence) == (M * 2) - 1:
        print(sequence)
        return

    for i, n in enumerate(numbers):
        if i == start_idx:
            continue

        print_sequence(i + 1, f"{sequence} {n}")

def main():
    for i, n in enumerate(numbers):
        print_sequence(i, f"{n}")

if __name__ == "__main__":
    main()
