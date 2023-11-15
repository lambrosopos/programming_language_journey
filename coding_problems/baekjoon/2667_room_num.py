import sys
from collections import deque

N = int(sys.stdin.readline())

board = []
for _ in range(N):
    line = sys.stdin.readline().strip()

    row = []
    for c in line:
        row.append(int(c))

    board.append(row)


def bfs(coord: tuple[int, int], board: list[list[int]]):
    total_size = 0

    queue = deque([coord])
    while len(queue) > 0:
        i, j = queue.popleft()

        if board[i][j] != 1:
            continue

        board[i][j] = -1
        total_size += 1


        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + di, j + dj

            if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == 1:
                queue.append((ni, nj))

    return total_size


room_size = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            room_size.append(bfs((i, j), board))


print(len(room_size))
room_size.sort()
for r in room_size:
    print(r)
