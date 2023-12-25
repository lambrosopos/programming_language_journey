import sys
import heapq

num_nodes = int(sys.stdin.readline())
num_edges = int(sys.stdin.readline())

adj = [[] for _ in range(num_nodes + 1)]

for _ in range(num_edges):
    u, v, e = map(int, sys.stdin.readline().split())

    adj[u].append((e, v))
    adj[v].append((e, u))

def djikstra(start_node: int, end_node: int):
    q = []
    heapq.heappush(q, (0, start_node, start_node))

    # each path[i] => [cost, cities]
    paths = [[] for _ in range(num_nodes + 1)]
    while len(q) > 0:
        cur_weight, cur_node, previous_node = heapq.heappop(q)
        
        if len(paths[cur_node]) != 0 and paths[cur_node][0] < cur_weight:
            continue
        
        paths[cur_node] = [cur_weight, previous_node]

        for next_weight, next_node in adj[cur_node]:
            if len(paths[next_node]) == 0 or cur_weight + next_weight < paths[next_node][0]:
                heapq.heappush(q, (cur_weight + next_weight, next_node, cur_node))

    return paths


def main():
    start_node, end_node = map(int, sys.stdin.readline().split())

    paths = djikstra(start_node, end_node)

    min_path = [str(end_node)]
    cur_node = end_node
    while cur_node != paths[cur_node][1]:
        min_path.append(str(paths[cur_node][1]))
        cur_node = paths[cur_node][1]

    print(paths[end_node][0])
    print(len(min_path))
    print(" ".join(min_path[::-1]))

if __name__ == "__main__":
    main()
