import sys

num_nodes, num_edges = map(int, sys.stdin.readline().split())

nodes = [_ for _ in range(num_nodes + 1)]

def union(node_1: int, node_2: int):
    root_1 = find(node_1)
    root_2 = find(node_2)

    if root_1 == root_2:
        return

    nodes[root_2] = root_1


def find(node: int):
    if node == nodes[node]:
        return node

    root_node = find(nodes[node])
    nodes[node] = root_node

    return root_node

for _ in range(num_edges):
    from_node, to_node = map(int, sys.stdin.readline().split())

    union(from_node, to_node)

roots = set()
for i in range(1, num_nodes + 1):
    roots.add(find(i))

print(len(roots))
