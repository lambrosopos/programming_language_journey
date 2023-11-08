import sys

num_people, num_parties = map(int, sys.stdin.readline().split())

truth_line = [int(_) for _ in sys.stdin.readline().split()]
num_truth, truth_ids = truth_line[0], truth_line[1:]

ranks = [1 for _ in range(num_people + 1)]
nodes = [_ for _ in range(num_people + 1)]


def find(node: int):
    if node == nodes[node]:
        return node

    # apply optimization to compress tree traversals
    nodes[node] = find(nodes[node])
    return nodes[node]

def union(node_1: int, node_2: int):
    root_1 = find(node_1)
    root_2 = find(node_2)

    # Nothing if they are already same group
    if root_1 == root_2:
        return

    # Merge two node groups together
    if root_1 in truth_ids and root_2 not in truth_ids:
        nodes[root_2] = root_1
    elif root_2 in truth_ids and root_1 not in truth_ids:
        nodes[root_1] = root_2
    else:
        # Both are truth people, use rank
        if ranks[root_1] > ranks[root_2]:
            nodes[root_2] = root_1
        elif ranks[root_2] > ranks[root_1]:
            nodes[root_1] = root_2
        else:
            nodes[root_2] = root_1
            ranks[root_1] += 1


party_lines = []
for _ in range(num_parties):
    party_line = [int(_) for _ in sys.stdin.readline().split()]
    party_lines.append(party_line)

    for person in party_line[1:]:
        for person_2 in party_line[1:]:
            if person == person_2:
                continue

            union(person, person_2)

count = 0
for party in party_lines:
    can_spread = True
    for person in party[1:]:
        if find(person) in truth_ids:
            can_spread = False
            break

    if can_spread:
        count += 1

# print(nodes)
print(count)
