import sys

H, W = map(int, sys.stdin.readline().split())
WALL, LAND = 0, 1

board = [ [0] * W for _ in range(H) ]
for i in range(H):
    row = sys.stdin.readline()
    for j in range(W):
        board[i][j] = int(row[j])

tracked = [ [-1] * W for _ in range(H) ]
tracked[0][0] = 1

def bfs(x: int, y: int, board: list[list[int]], tracked: list[list[int]]):
    queue = [(y, x)]
    reached_end = False
    while len(queue) > 0 and not reached_end:
        i, j = queue.pop(0)

        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni, nj = i + di, j + dj

            # Skip out of bounds
            if ni < 0 or ni >= H or nj < 0 or nj >= W:
                continue

            if ni == (H - 1) and nj == (W - 1):
                if tracked[ni][nj] == tracked[i][j] + 1:
                    reached_end = True


            # Skip when wall
            if board[ni][nj] == WALL:
                continue
            elif tracked[ni][nj] != -1:
                if tracked[ni][nj] == (tracked[i][j] + 1):
                    continue
            else:
                queue.append((ni, nj))

            # not visited yet -> init value
            if tracked[ni][nj] == -1:
                tracked[ni][nj] = 1 + tracked[i][j]
            else:
                tracked[ni][nj] = min(tracked[ni][nj], 1 + tracked[i][j])

bfs(x=0, y=0, board=board, tracked=tracked)

print(tracked[H - 1][W - 1])
