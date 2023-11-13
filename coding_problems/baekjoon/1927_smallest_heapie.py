import sys

class Heap:
    def __init__(self):
        self.heap = []

    def size(self):
        return len(self.heap)

    def push(self, node: int):
        # Add to heap
        self.heap.append(node)

        idx = self.size() - 1
        while idx > 0 and self.heap[(idx - 1) // 2] > self.heap[idx]:
            temp_val = self.heap[(idx-1)//2]
            self.heap[(idx-1)//2] = self.heap[idx]
            self.heap[idx] = temp_val

            idx = (idx - 1) // 2

    def pop(self) -> int:
        if self.size() == 0:
            return 0

        # Swap last leaf node and root node
        root_val = self.heap[0]
        last_val = self.heap[-1]
        self.heap[0] = last_val

        self.heap.pop()

        here = 0
        while True:
            left, right = (here * 2) + 1, (here * 2) + 2

            if left >= self.size():
                break

            next_idx = here
            if self.heap[next_idx] > self.heap[left]:
                next_idx = left

            if right < self.size() and self.heap[next_idx] > self.heap[right]:
                next_idx = right

            if next_idx == here:
                break

            self.heap[here], self.heap[next_idx] = self.heap[next_idx], self.heap[here]

            here = next_idx


        return root_val

N = int(sys.stdin.readline())

h1 = Heap()

popped = []
for i in range(N):
    num = int(sys.stdin.readline())

    if num == 0:
        popped.append(h1.pop())
    else:
        h1.push(num)


for p in popped:
    print(p)
