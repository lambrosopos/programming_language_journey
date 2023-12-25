import sys


def solve(sequence: str) -> str:
    next_char = sequence[-1]

    for i in range(len(sequence) - 2, -1, -1):
        chars = sequence[i] + next_char
        if chars in ("AG", "GA"):
            next_char = "C"
        elif chars in ("AC", "CA"):
            next_char = "A"
        elif chars in ("AT", "TA"):
            next_char = "G"
        elif chars in ("CG", "GC"):
            next_char = "T"
        elif chars in ("CT", "TC"):
            next_char = "G"
        elif chars in ("GT", "TG"):
            next_char = "A"

    return next_char

def main():
    N = int(sys.stdin.readline())
    DNA = sys.stdin.readline().rstrip()

    if N < 2:
        print(DNA)
    else:
        print(solve(DNA))


if __name__ == "__main__":
    main()
