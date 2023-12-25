import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

def bs(left, right, target, source):
    while left < right:
        mid = (left + right) // 2

        # 2 3 4 5 
        if source[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


def solution():
    lis = [0] * N
    lis[0] = numbers[0]

    idx = 0
    for n in numbers[1:]:
        if n > lis[idx]:
            lis[idx + 1] = n
            idx += 1
        else:
            replace_idx = bs(0, idx, n, lis)
            lis[replace_idx] = n

    return idx + 1

print(solution())
