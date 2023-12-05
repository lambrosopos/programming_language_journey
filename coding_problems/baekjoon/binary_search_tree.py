import sys 
sys.setrecursionlimit(10**9)


class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.data}"

    def __repr__(self):
        return f"{self.data}"


class BstTree:
    def __init__(self, root: Node = None):
        self.root = root

    def insert(self, node: Node):
        cur_node = self.root

        if cur_node is None:
            self.root = node
        else:
            while cur_node:
                if node.data < cur_node.data:
                    if cur_node.left:
                        cur_node = cur_node.left
                    else:
                        cur_node.left = node
                        cur_node = None
                else:
                    if cur_node.right:
                        cur_node = cur_node.right
                    else:
                        cur_node.right = node
                        cur_node = None

    def traverse(self):
        def recur(node: Node):
            if node is None:
                return

            recur(node.left)
            recur(node.right)

            print(node.data)

        recur(self.root)


tree = BstTree()
while True:
    line = sys.stdin.readline().strip()

    if line == "":
        break

    node = Node(int(line))
    tree.insert(node)


tree.traverse()
