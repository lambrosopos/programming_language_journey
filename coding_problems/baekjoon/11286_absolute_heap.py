import sys

N = int(sys.stdin.readline())

def push(heap: list[int], node: int):
    heap.append(node)

    idx = len(heap) - 1
    while idx > 0:
        root_idx = (idx - 1) // 2
        root_node = heap[root_idx]
        cur_node = heap[idx]

        if abs(root_node) < abs(cur_node):
            # Stop if root node is smaller
            break

        if abs(root_node) == abs(cur_node) and root_node < cur_node:
            # Stop if abs values are same but root node is smaller
            break

        # Swap root and current node
        temp_val = root_node
        heap[root_idx] = cur_node
        heap[idx] = temp_val

        idx = root_idx

def pop(heap: list[int]):
    if len(heap) == 0:
        return 0

    root_node = heap[0]
    last_node = heap[-1]
    heap[0] = last_node
    heap.pop()

    heap_size = len(heap)

    cur_idx = 0
    while cur_idx < heap_size:
        next_idx = cur_idx
        left_idx = cur_idx * 2 + 1
        right_idx = cur_idx * 2 + 2

        # Stop if left idx is bigger than actual heap size
        if left_idx >= heap_size:
            break

        # Start with left idx
        if abs(heap[left_idx]) < abs(heap[next_idx]):
            next_idx = left_idx
        elif abs(heap[left_idx]) == abs(heap[next_idx]) and heap[left_idx] < heap[next_idx]:
            next_idx = left_idx

        # Continue with right idx
        if right_idx < heap_size:
            if abs(heap[right_idx]) < abs(heap[next_idx]):
                next_idx = right_idx
            elif abs(heap[right_idx]) == abs(heap[next_idx]) and heap[right_idx] < heap[next_idx]:
                next_idx = right_idx

        # Check if cur_idx is the same
        if cur_idx == next_idx:
            break

        temp_val = heap[next_idx]
        heap[next_idx] = heap[cur_idx]
        heap[cur_idx] = temp_val

        cur_idx = next_idx

    return root_node

pq = []

ans = []
for _ in range(N):
    num = int(sys.stdin.readline())

    if num == 0:
        ans.append(pop(pq))
    else:
        push(pq, num)


for a in ans:
    print(a)
