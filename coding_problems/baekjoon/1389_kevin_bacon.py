import sys
import heapq

num_nodes, num_edges = map(int, sys.stdin.readline().split())


# Will use djikstra's algorithm to find the shortest path to all.

# Initialize adjacent edges
adj = {}
for i in range(1, num_nodes + 1):
    adj[i] = []

for _ in range(num_edges):
    from_node, to_node = map(int, sys.stdin.readline().split())

    # Attach a double edge for going from and to
    adj[from_node].append((1, to_node))
    adj[to_node].append((1, from_node))

def djikstra(node: int) -> int:
    """
    Return a number which is the sum of the cost to travel to edges.
    """
    distances = [-1] * (num_nodes + 1)
    # revert first index to zero, since will not be using it.
    distances[0] = 0

    heap = []
    heapq.heappush(heap, (0, node))

    while len(heap) > 0:
        cur_weight, cur_node = heapq.heappop(heap)

        if distances[cur_node] != -1:
            continue

        # Establish current weight for the current node
        distances[cur_node] = cur_weight

        for next_weight, next_node in adj[cur_node]:
            if distances[next_node] == -1:
                heapq.heappush(heap, (cur_weight + next_weight, next_node))

    return sum(distances)


scores = []
for node in range(1, num_nodes + 1):
    # add the individual scores
    score = djikstra(node)
    scores.append(score)


# Get the idx for the minimum score.
min_idx = 0
for i in range(num_nodes):
    if scores[i] < scores[min_idx]:
        min_idx = i

print(min_idx + 1)
