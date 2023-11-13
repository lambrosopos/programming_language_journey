import sys
from collections import deque

num_nodes, num_edges = map(int, sys.stdin.readline().split())
num_nodes += 1

nodes = [ list() for _ in range(num_nodes) ]


for i in range(num_edges):
    A, B = map(int, sys.stdin.readline().split())
    nodes[A].append(B)
    nodes[B].append(A)

kb_score = [0] * num_nodes

def get_score(node: int):
    global nodes

    scores = [1e9] * num_nodes

    scores[0] = 0
    scores[node] = 0

    queue = deque([node])
    while len(queue) > 0:
        cur_node = queue.popleft()

        cur_score = scores[cur_node] + 1
        for n in nodes[cur_node]:
            if cur_score <= scores[n]:
                queue.append(n)
                scores[n] = min(cur_score, scores[n])

    return sum(scores)

for i in range(1, num_nodes):
    kb_score[i] = get_score(i)

lowest_score = kb_score[1]
lowest_idx = 1
for i in range(1, num_nodes):
    if kb_score[i] < lowest_score:
        lowest_score = kb_score[i]
        lowest_idx = i

print(lowest_idx)
