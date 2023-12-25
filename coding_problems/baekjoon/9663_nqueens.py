import sys
import time
import copy

start = time.time()
sys.setrecursionlimit(10_000_000)

N = int(sys.stdin.readline())

def place_q(queen_i: int, queen_j: int, board: list[list[int]]):
    # Place a queen.
    board[queen_i][queen_j] = "Q"

    directions = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1)
        ]

    for di, dj in directions:
        ni, nj = queen_i, queen_j
        while True:
            ni += di
            nj += dj

            if 0 > ni or 0 > nj or N <= ni or N <= nj:
                break

            board[ni][nj] = 1

    # For each available squares, place another queen.
    count = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0 or N * (i + j) <= N * (queen_i + queen_j):
                continue

            count += place_q(i, j, copy.deepcopy(board))

    # Recursive the above steps.
    queens = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == "Q":
                queens += 1

    if queens == N:
        count += 1

    return count

count = 0
for i in range(N):
    for j in range(N):
        board = [[0] * N for _ in range(N)]
        count += place_q(i, j, board)

print(count)

print(f"total time: {time.time() - start}")
