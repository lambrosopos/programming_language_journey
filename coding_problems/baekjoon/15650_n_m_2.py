import sys

N, M = map(int, sys.stdin.readline().split())

def print_sequence(start_i, sequence: str):
    if len(sequence) == (2 * M - 1):
        print(sequence)
        return

    for j in range(start_i, N + 1):
        print_sequence(j + 1, f"{sequence} {j}")

for i in range(1, N - M + 2):
    print_sequence(i + 1, f"{i}")
