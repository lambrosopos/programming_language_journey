import sys
import heapq

num_nodes, num_edges = map(int, sys.stdin.readline().split())

adj = {}
for i in range(1, num_nodes + 1):
    adj[i] = []

for _ in range(num_edges):
    u, v, e = map(int, sys.stdin.readline().split())

    adj[u].append([e, v])
    adj[v].append([e, u])

def djikstra(start):
    # Init visited array
    visited = [1e9] * (num_nodes + 1)

    heap = []
    # Weight, Node
    heapq.heappush(heap, [0, start])
    while len(heap) > 0:
        cur_weight, cur_node = heapq.heappop(heap)

        if visited[cur_node] < 1e9:
            continue

        visited[cur_node] = cur_weight

        for next_weight, next_node in adj[cur_node]:
            if visited[next_node] == 1e9:
                heapq.heappush(heap, [cur_weight + next_weight, next_node])

    return visited

def main():
    n, m = map(int, sys.stdin.readline().split())

    first_path = djikstra(1)
    from_n = djikstra(n)
    from_m = djikstra(m)

    first_distance = first_path[n] + from_n[m] + from_m[num_nodes]
    second_distance = first_path[m] + from_m[n] + from_n[num_nodes]

    distance = min(first_distance, second_distance)

    if distance < 1e9:
        print(distance)
    else:
        print(-1)

main()
