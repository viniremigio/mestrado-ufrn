class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


class Tree:
    def preorder(self, root):
        if root is not None:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)

    def inlevelorder(self, root):
        if root is None:
            return

        queue = list()
        queue.append(root)

        while len(queue) > 0:

            print(queue[0].data)
            node = queue.pop(0)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)


if __name__ == '__main__':
    node = Node("A", Node("B", Node("D", None,  Node("J", None, None)), Node("H", None, None)), Node("C", Node("E", None, None), Node("F", Node("I", None, None), None)))
    tree = Tree()
    tree.inlevelorder(node)




