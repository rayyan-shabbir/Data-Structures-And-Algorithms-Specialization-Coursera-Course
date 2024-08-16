import sys

sys.setrecursionlimit(10**6)  # Max depth of recursion

class TreeNode:
    def __init__(self, key=0, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def buildTree(self, t, index):
        if index == -1:
            return None
        
        node = TreeNode(t[index][0])
        node.left = self.buildTree(t, t[index][1])
        node.right = self.buildTree(t, t[index][2])
        
        return node

    def inOrder(self, root, result):
        if root:
            self.inOrder(root.left, result)
            result.append(root.key)
            self.inOrder(root.right, result)

    def preOrder(self, root, result):
        if root:
            result.append(root.key)
            self.preOrder(root.left, result)
            self.preOrder(root.right, result)

    def postOrder(self, root, result):
        if root:
            self.postOrder(root.left, result)
            self.postOrder(root.right, result)
            result.append(root.key)

def read():
    n = int(sys.stdin.readline())
    tuple_array = []

    for _ in range(n):
        a, b, c = map(int, sys.stdin.readline().split())
        tuple_array.append((a, b, c))

    return tuple_array

def main():
    tree = TreeNode()
    t = read()
    root = tree.buildTree(t, 0)

    in_order_result = []
    pre_order_result = []
    post_order_result = []

    tree.inOrder(root, in_order_result)
    tree.preOrder(root, pre_order_result)
    tree.postOrder(root, post_order_result)

    print(" ".join(map(str, in_order_result)))
    print(" ".join(map(str, pre_order_result)))
    print(" ".join(map(str, post_order_result)))

if __name__ == "__main__":
    main()
