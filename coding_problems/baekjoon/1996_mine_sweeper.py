import sys

N = int(sys.stdin.readline().strip())

mines = [sys.stdin.readline().strip() for _ in range(N)]
land = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        # If mine, mark with *
        if mines[i][j] != ".":
            land[i][j] = "*"
        else:
            # Check NESW
            mine_count = 0
            for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                ni, nj = i + di, j + dj

                if ni < 0 or nj < 0 or ni >= N or nj >= N or mines[ni][nj] == ".":
                    continue

                mine_count += int(mines[ni][nj])

            # Check diagonals
            for di, dj in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                ni, nj = i + di, j + dj

                if ni < 0 or nj < 0 or ni >= N or nj >= N or mines[ni][nj] == ".":
                    continue

                mine_count += int(mines[ni][nj])

            land[i][j] = "M" if mine_count > 9 else str(mine_count)

for l in land:
    print("".join(l))
