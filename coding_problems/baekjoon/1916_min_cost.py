import sys
import heapq

num_nodes = int(sys.stdin.readline())
num_edges = int(sys.stdin.readline())

# Initialize each node edges
adj = {}
for i in range(1, num_nodes + 1):
    adj[i] = set()

for _ in range(num_edges):
    u, v, w = map(int, sys.stdin.readline().split())

    # Add Weight, Next Node to each Node
    adj[u].add((w, v))

start_node, end_node = map(int, sys.stdin.readline().split())

distances = [-1 for _ in range(num_nodes)]

heap = []
heapq.heappush(heap, (0, start_node))
while distances[end_node - 1] == -1:
    cur_weight, cur_node = heapq.heappop(heap)

    if distances[cur_node - 1] != -1:
        continue

    distances[cur_node - 1] = cur_weight

    for next_weight, next_node in adj[cur_node]:
        if distances[next_node - 1] == -1:
            heapq.heappush(heap, (next_weight + cur_weight, next_node))

    
print(distances[end_node - 1])
