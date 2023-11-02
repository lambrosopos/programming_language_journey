import sys

n = int(sys.stdin.readline())

queue = [i for i in range(1, n + 1)]

while len(queue) > 1:
    if len(queue) % 2 == 0:
        queue = [queue[i] for i in range(len(queue)) if i % 2 == 1]
    else:
        queue = [queue[-1]] + [queue[i] for i in range(len(queue) - 1) if i % 2 == 1]


print(queue.pop())
