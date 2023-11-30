import heapq

class Node:
    def __init__(self, data: int, left_node = None, right_node = None):
        self.data = data
        self.left = left_node
        self.right = right_node

    def __lt__(self, node):
        return self.data < node.data

def min_path_sum(node: Node):
    heap = []
    heapq.heappush(heap, (node.data, node))

    min_sum = None
    while len(heap) > 0:
        cur_weight, cur_node = heapq.heappop(heap)

        # Reached leaf
        if cur_node.left is None and cur_node.right is None:
            if min_sum is None:
                min_sum = cur_weight
            else:
                min_sum = min(cur_weight, min_sum)

        if cur_node.left:
            heapq.heappush(heap, (cur_node.left.data + cur_weight, cur_node.left))

        if cur_node.right:
            heapq.heappush(heap, (cur_node.right.data + cur_weight, cur_node.right))

    return min_sum


def test_p135_1():
    node = Node(10)
    assert(min_path_sum(node) == 10)


def test_p135_2():
    node = Node(10, Node(5), Node(5))
    assert(min_path_sum(node) == 15)

def test_p135_3():
    node = Node(10, Node(5, None, Node(2)), Node(5))
    assert(min_path_sum(node) == 15)

def test_p135_4():
    node = Node(10, Node(5, None, Node(2)), Node(5, None, Node(1)))
    assert(min_path_sum(node) == 16)

def test_p135_5():
    node = Node(10, Node(5, None, Node(2)), Node(5, None, Node(1, Node(-1), None)))
    assert(min_path_sum(node) == 15)
