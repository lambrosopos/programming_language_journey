from collections import deque

def bfs(i, j, land, visited):
    j_list, count = set(), 0
    H, W = len(land), len(land[0])
    queue = deque([(i, j)])
    while len(queue) > 0:
        i, j = queue.popleft()
        
        if visited[i][j] == 1:
            continue
            
        visited[i][j] = 1
        count += 1
        j_list.add(j)
        
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni, nj = i + di, j + dj
            
            if ni < 0 or nj < 0 or ni >= H or nj >= W:
                continue
                
            if visited[ni][nj] == 1 or land[ni][nj] == 0:
                continue
                
            queue.append((ni, nj))

    return j_list, count


def solution(land):
    H, W = len(land), len(land[0])
    visited = [[0] * W for _ in range(H)]
    
    vertical_strips = [0] * W
    for i in range(H):
        for j in range(W):
            if land[i][j] == 1 and visited[i][j] == 0:
                j_list, count = bfs(i, j, land, visited)

                for v in j_list:
                    vertical_strips[v] += count

    return max(vertical_strips)

l = [[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]

print(solution(l))
