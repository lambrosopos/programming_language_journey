import sys

N = int(sys.stdin.readline())

heap = []

def heap_push(heap: list[int], node: int):
    heap_size = len(heap)
    heap.append(node)

    idx = heap_size
    while idx > 0 and heap[idx] > heap[(idx - 1) // 2]:
        root_idx = (idx - 1) // 2
        heap[root_idx], heap[idx] = heap[idx], heap[root_idx]
        idx = root_idx


def heap_pop(heap: list[int]) -> int:
    if len(heap) == 0:
        return 0

    root_val = heap[0]
    heap[0] = heap[-1]
    heap.pop()

    heap_size = len(heap)

    cur_idx = 0
    while True:
        # Check left and right, swap with larger value
        left, right = (cur_idx * 2) + 1, (cur_idx * 2) + 2

        # Retrieve next idx for value
        next_idx = cur_idx

        # Check and swap with left
        if left < heap_size and heap[left] > heap[next_idx]:
            next_idx = left

        # CHeck for right value
        if right < heap_size and heap[right] > heap[next_idx]:
            next_idx = right


        # If no change, exit loop
        if next_idx == cur_idx:
            break

        # Swap values
        heap[cur_idx], heap[next_idx] = heap[next_idx], heap[cur_idx]
        cur_idx = next_idx


    return root_val


ans = []
for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        ans.append(heap_pop(heap))
    else:
        heap_push(heap, num)


for a in ans:
    print(a)
