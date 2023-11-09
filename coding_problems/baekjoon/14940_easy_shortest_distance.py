import sys

LAND, WALL, START = 1, 0, 2

height, width = map(int, sys.stdin.readline().split())
land_map = [ list(map(int, sys.stdin.readline().split())) for _ in range(height)]

s_x, s_y = 0, 0
for i in range(height):
    for j in range(width):
        if land_map[i][j] == 2:
            s_x, s_y = j, i

visited = [ [-1] * width for _ in range(height)]
visited[s_y][s_x] = 0
directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]


queue = [(s_x, s_y)]
while len(queue) > 0:
    x, y = queue.pop(0)
    for delta_x, delta_y in directions:
        c_x = delta_x + x
        c_y = delta_y + y

        if 0 <= c_x < width and 0 <= c_y < height and visited[c_y][c_x] == -1:
            if land_map[c_y][c_x] == LAND:
                visited[c_y][c_x] = visited[y][x] + 1
                queue.append((c_x, c_y))

for i in range(height):
    for j in range(width):
        if visited[i][j] == -1 and land_map[i][j] == WALL:
            visited[i][j] = 0

for v in visited:
    print(*v)
