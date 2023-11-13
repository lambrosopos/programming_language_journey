import sys
from collections import deque

start, end = map(int, sys.stdin.readline().split())

tracked = [1e9] * 100_001
tracked[start] = 0

queue = deque([start])
while len(queue) > 0:
    node = queue.popleft()
    cur_time = tracked[node] + 1

    if node - 1 > -1 and cur_time <= tracked[node - 1]:
        queue.append(node - 1)
        tracked[node - 1] = min(tracked[node - 1], cur_time)

    if node + 1 < 100_001 and cur_time <= tracked[node + 1]:
        queue.append(node + 1)
        tracked[node + 1] = min(tracked[node + 1], cur_time)

    if node * 2 < 100_001 and cur_time <= tracked[node * 2]:
        queue.append(node * 2)
        tracked[node * 2] = min(tracked[node * 2], cur_time)

print(tracked[end])
