import sys
import heapq

num_nodes, num_edges = map(int, sys.stdin.readline().split())
start_node = int(sys.stdin.readline())

adj = {}
for i in range(1, num_nodes + 1):
    adj[i] = []

for _ in range(num_edges):
    u, v, w = map(int, sys.stdin.readline().split())
    adj[u].append((v, w))

queue = []
heapq.heappush(queue, (0, start_node))

shortest = {}
while len(queue) > 0:
    cur_weight, cur_node = heapq.heappop(queue)

    if shortest.get(cur_node):
        continue

    shortest[cur_node] = cur_weight

    for next_node, next_weight in adj.get(cur_node):
        if shortest.get(next_node) is None:
            heapq.heappush(queue, (next_weight + cur_weight, next_node))

for i in range(num_nodes):
    print(shortest.get(i + 1, "INF"))
