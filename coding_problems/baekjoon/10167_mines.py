import sys
from collections import defaultdict


def grid_compression(grid):
    x_compression = {}
    x_coords = [_[0] for _ in grid]
    x_coords.sort()

    cols = 0
    for n in set(x_coords):
        if x_compression.get(n) is None:
            x_compression[n] = cols
            cols += 1

    y_compression = {}
    y_coords = [_[1] for _ in grid]
    y_coords.sort()

    rows = 0
    for n in set(y_coords):
        if y_compression.get(n) is None:
            y_compression[n] = rows
            rows += 1

    gc = [[0] * cols for _ in range(rows)]

    for x, y, v in grid:
        gc[y_compression[y]][x_compression[x]] = v

    return gc


def prefix_sum(grid):
    N, M = len(grid) + 1, len(grid[0]) + 1

    ps = [[0] * M for _ in range(N)]
    ps[1][1] = grid[0][0]

    # First column
    for i in range(1, N):
        ps[i][1] = ps[i - 1][1] + grid[i - 1][0]

    # First row
    for i in range(1, M):
        ps[1][i] = ps[1][i - 1] + grid[0][i - 1]

    for i in range(2, N):
        for j in range(2, M):
            ps[i][j] = grid[i - 1][j - 1] + ps[i - 1][j] + ps[i][j - 1] - ps[i - 1][j - 1]

    return ps

def find_max(ps):
    N, M = len(ps), len(ps[0])

    max_sum = 0
    for i in range(N):
        for j in range(M):
            for k in range(i + 1, N):
                for l in range(j + 1, M):
                    max_sum = max(max_sum, ps[k][l] + ps[i][j] - ps[k][j] - ps[i][l])

    return max_sum

    # max_grid = [[0] * M for _ in range(N)]
    #
    # for i in range(N):
    #     for j in range(M):
    #         cur_sum = ps[i][j]
    #
    #         if i - 1 >= 0:
    #             cur_sum -= ps[i - 1][j]
    #
    #         if j - 1 >= 0:
    #             cur_sum -= ps[i][j - 1]
    #
    #         if i - 1 >= 0 and j - 1 >= 0:
    #             cur_sum += ps[i - 1][j - 1]
    #
    #         max_grid[i][j] = cur_sum
    #
    # return max_grid

def main():
    N = int(sys.stdin.readline())

    coords = []
    for i in range(N):
        X, Y, V = map(int, sys.stdin.readline().split())

        coords.append((X, Y, V))

    gc = grid_compression(coords)

    # print(*gc, sep="\n")
    # print()
    
    ps = prefix_sum(gc)

    # print(*ps, sep="\n")
    # print()

    max_sum = find_max(ps)

    print(max_sum)

if __name__ == "__main__":
    main()
