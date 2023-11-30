import sys
from collections import deque

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

# Fine if the smallest number comes in first
least_count = (N-2)*(N-2) + (2*(N*N)) + 2*(N-2)*N
second_count = N*4 + (N-2)*4
last_count = 4

def opposite_num(num: int) -> int:
    return abs(5 - num)

# Numbers come in different order
def solve(idx: int) -> list[int]:
    combination = []
    min_sum = sum(numbers)

    banned_nums = [idx, opposite_num(idx)]
    for i in range(6):
        if i in banned_nums:
            continue
        for j in range(6):
            if j in banned_nums or i == j or i == opposite_num(j):
                continue

            new_sum = numbers[idx] + numbers[i] + numbers[j]
            if new_sum < min_sum:
                min_sum = new_sum
                combination = [idx, i, j]
    
    return combination

smallest_combination = [0, 1, 2]
for i in range(6):
    combination = solve(i)
    if sum([numbers[_] for _ in combination]) < sum([numbers[_] for _ in smallest_combination]):
        smallest_combination = combination

new_numbers = [numbers[_] for _ in smallest_combination]
new_numbers.sort()

min_sum = 0
min_sum += new_numbers[0] * least_count
min_sum += new_numbers[1] * second_count
min_sum += new_numbers[2] * last_count

if N == 1:
    numbers.sort()
    print(sum(numbers[:5]))
else:
    print(min_sum)
