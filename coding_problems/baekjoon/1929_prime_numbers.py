import sys
import itertools

start_num, end_num = map(int, sys.stdin.readline().strip().split())

is_primes = [True] * (end_num + 1)

is_primes[0] = not is_primes[0]
is_primes[1] = not is_primes[1]

idx = 2
while idx ** 2 <= end_num:
    if is_primes[idx]:
        for i in range(idx * 2, end_num + 1, idx):
            is_primes[i] = False

    idx += 1

print("\n".join(map(str, itertools.compress(range(start_num, end_num + 1), is_primes[start_num:end_num + 1]))))

