import sys
from collections import deque

N = int(sys.stdin.readline())

"""
3
1234 3412
1000 1
1 16
"""

def doubler(num: int) -> int:
    if num * 2 >= 10_000:
        return (num * 2) % 10_000
    return num * 2

def subtract(num: int) -> int:
    if num - 1 < 0:
        return 9999
    return num - 1

def pad_zeroes(num: int) -> str:
    num = str(num)
    if len(num) < 4:
        num = "0" * (4 - len(num)) + num
    return num

def shift_left(num: int) -> int:
    str_num = pad_zeroes(num)
    num = str_num[1:] + str_num[0]

    return int(num)

def shift_right(num: int) -> int:
    str_num = pad_zeroes(num)
    num = str_num[-1] + str_num[:3]

    return int(num)


def solve(start_num: int, end_num: int) -> str:
    visited = [-1] * 10_000
    visited[start_num] = 1
    path = [""] * 10_000

    queue = deque([start_num])
    while len(queue) > 0:
        num = queue.popleft()
        
        # print(f"{num=}, {visited[num]=}, {path[num]=}, {queue=}")

        if num == end_num:
            break

        double_num = doubler(num)
        if visited[double_num] == -1:
            queue.append(double_num)
            visited[double_num] = 1
            path[double_num] = path[num] + "D"
            
        subtract_num = subtract(num)
        if visited[subtract_num] == -1:
            queue.append(subtract_num)
            visited[subtract_num] = 1
            path[subtract_num] = path[num] + "S"

        left_num = shift_left(num)
        if visited[left_num] == -1:
            queue.append(left_num)
            visited[left_num] = 1
            path[left_num] = path[num] + "L"

        right_num = shift_right(num)
        if visited[right_num] == -1:
            queue.append(right_num)
            visited[right_num] = 1
            path[right_num] = path[num] + "R"

    return path[end_num]

answers = []
for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())
    answers.append(solve(A, B))

for a in answers:
    print(a)
