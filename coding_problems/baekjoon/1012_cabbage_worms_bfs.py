import sys

def bfs(x: int, y: int, board: list[list[int]]) -> None:
    W, H = len(board[0]), len(board)
    queue = [(y, x)]
    while len(queue) > 0:
        i, j = queue.pop()
        board[i][j] = -1

        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < H and 0 <= nj < W and board[ni][nj] == 1:
                queue.append((ni, nj))


def solve():
    W, H, num_cabbages = map(int, sys.stdin.readline().split())

    board = [ [0] * W for _ in range(H) ]

    for _ in range(num_cabbages):
        x, y = map(int, sys.stdin.readline().split())
        board[y][x] = 1

    count = 0
    for i in range(H):
        for j in range(W):
            if board[i][j] == 1:
                bfs(x=j, y=i, board=board)
                count += 1

    return count


def main():
    total_n = int(sys.stdin.readline())

    answers = []
    for _ in range(total_n):
        answers.append(solve())

    for a in answers:
        print(a)

if __name__ == "__main__":
    main()
