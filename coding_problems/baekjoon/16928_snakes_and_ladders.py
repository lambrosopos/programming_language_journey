import sys
from collections import deque

SQUARES = 100
ladders, snakes = map(int, sys.stdin.readline().split())

board = [0] * (SQUARES + 1)

# Set up ladders and snakes
for i in range(ladders + snakes):
    start, end = map(int, sys.stdin.readline().split())
    board[start] = end

tracked = [0] * (SQUARES + 1)


# Start from square 1
queue = deque([1])
while len(queue) > 0:
    x = queue.popleft()

    # dice rolls
    for i in range(1, 7):
        nx = i + x

        # Skip if over 100
        if nx > SQUARES:
            continue

        # Apply snakes/ladders
        while board[nx] > 0:
            nx = board[nx]

        y = nx

        # If not visited
        if tracked[y] == 0:
            tracked[y] = tracked[x] + 1
        # Skip if current movement is longer
        elif tracked[x] + 1 > tracked[y]:
            continue
        else:
            tracked[y] = min(tracked[y], tracked[x] + 1)

        queue.append(y)

print(tracked[SQUARES])

