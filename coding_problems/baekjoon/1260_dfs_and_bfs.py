import sys
sys.setrecursionlimit(10000)

def bfs(node_num: int, nodes: list[list[int]]):
    queue = [_ for _ in nodes[node_num]]
    numbers = [node_num]

    while len(queue) > 0:
        target_node = queue.pop(0)

        if target_node not in numbers:
            numbers.append(target_node)
            queue += nodes[target_node]

    return numbers

def dfs(node_num: int, nodes: list[list[int]]):
    # First array of nodes is explored nodes
    nodes[0].append(node_num)

    for target_node in nodes[node_num]:
        if target_node not in nodes[0]:
            dfs(target_node, nodes)


def main():
    total_nodes, total_edges, starting_node = map(int, sys.stdin.readline().split())

    nodes = [[] for _ in range(total_nodes + 1)]
    for _ in range(total_edges):
        from_node, to_node = map(int, sys.stdin.readline().split())

        # Add bidirectional edges to nodes
        nodes[from_node].append(to_node)
        nodes[to_node].append(from_node)


    # Sort in ascending order for base logic
    for idx in range(total_nodes + 1):
        nodes[idx].sort()

    dfs(starting_node, nodes)
    print(" ".join([str(_) for _ in nodes[0]]))
    print(" ".join([str(_) for _ in bfs(starting_node, nodes)]))


if __name__ == "__main__":
    main()
