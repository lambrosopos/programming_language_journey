import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()

def solve(idx: int) -> int:
    temp_list = numbers[0:idx] + numbers[idx + 1:]

    left = 0
    right = len(temp_list) - 1

    while left < right:
        temp_num = temp_list[left] + temp_list[right]

        if temp_num == numbers[idx]:
            return 1
        elif temp_num > numbers[idx]:
            right -= 1
        elif temp_num < numbers[idx]:
            left += 1

    return 0



count = 0
for i in range(N):
    count += solve(i)

print(count)
