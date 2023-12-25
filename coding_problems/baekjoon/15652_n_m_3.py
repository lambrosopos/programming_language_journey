import sys

N, M = map(int, sys.stdin.readline().split())

def print_sequence(start_idx: int, sequence: str):
    if len(sequence) == (M * 2) - 1:
        print(sequence)
        return

    for i in range(start_idx, N + 1):
        print_sequence(i, f"{sequence} {i}")

def main():
    for i in range(1, N + 1):
        print_sequence(i, f"{i}")

if __name__ == "__main__":
    main()
