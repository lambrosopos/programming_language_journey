import sys
from collections import defaultdict
from operator import itemgetter

N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(N)]
numbers.sort()

def mcn():
    count_dict = defaultdict(int)
    for n in numbers:
        count_dict[n] += 1

    max_sort = sorted(count_dict.items(), key=itemgetter(1), reverse=True)

    if len(max_sort) > 1 and max_sort[0][1] == max_sort[1][1]:
        return max_sort[1][0]

    return max_sort[0][0]


def round(num: float) -> int:
    is_neg = -1 if num < 0 else 1
    num = abs(num)

    if num - int(num) >= 0.5:
        return is_neg * (int(num) + 1)
    return is_neg * int(num)

print(round(sum(numbers) / N))
print(numbers[N//2])
most_common = mcn()
print(most_common)
print(numbers[-1] - numbers[0])



