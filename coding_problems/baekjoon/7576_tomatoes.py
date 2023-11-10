import sys
from collections import deque

W, H = map(int, sys.stdin.readline().split())

START, LAND, WALL = 1, 0, -1

board = [ list(map(int, sys.stdin.readline().split())) for _ in range(H) ]
tracked = [ [-1] * W for _ in range(H) ]

queue = deque()
# Queue start coordinates
for i in range(H):
    for j in range(W):
        if board[i][j] == START:
            tracked[i][j] = 0
            queue.append((i, j))

max_days = 0
while len(queue) > 0:
    i, j = queue.popleft()
    board[i][j] = 1

    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ni, nj = i + di, j + dj

        if ni < 0 or nj < 0 or ni >= H or nj >= W:
            continue

        # Skip if already visited
        if tracked[ni][nj] != -1 or board[ni][nj] == WALL:
            continue
        else:
            queue.append((ni, nj))
        
        tracked[ni][nj] = 1 + tracked[i][j]
        max_days = max(tracked[ni][nj], max_days)

is_unreached = False
for i in range(H):
    if is_unreached:
        break
    for j in range(W):
        if tracked[i][j] == -1 and board[i][j] == 0:
            is_unreached = True
            break

if is_unreached:
    print(-1)
else:
    print(max_days)


