import sys
import heapq

N = int(sys.stdin.readline())

class Node:
    def __init__(self, data: int):
        self.data = data
        self.edges = []

    def __lt__(self, node):
        return self.data < node.data

nodes = [Node(_) for _ in range(N + 1)]
for _ in range(N - 1):
    A, B = map(int, sys.stdin.readline().split())

    nodes[A].edges.append(nodes[B])
    nodes[B].edges.append(nodes[A])

parents = [0] * (N + 1)
q = []
heapq.heappush(q, (nodes[1], 1))
while len(q) > 0:
    cur_node, parent_node = heapq.heappop(q)

    if parents[cur_node.data] != 0:
        continue

    parents[cur_node.data] = parent_node

    for next_node in cur_node.edges:
        heapq.heappush(q, [next_node, cur_node.data])

for i in range(2, N + 1):
    print(parents[i])


