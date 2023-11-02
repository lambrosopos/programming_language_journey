import sys

total_len = int(sys.stdin.readline())

ordered_numbers = [False] * 1_000_001

for i in range(total_len):
    num = int(sys.stdin.readline())
    ordered_numbers[num] = True

for idx, n in enumerate(ordered_numbers):
    if n is True:
        print(idx)
