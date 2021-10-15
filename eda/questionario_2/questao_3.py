class Node:
    def __init__(self, data, children):
        self.data = data
        self.children = children


class Tree:
    def preorder_recursive(self, root):
        if root is not None:
            print(root.data)
            for child in root.children:
                self.preorder_recursive(child)

    def preorder_interative(self, root):
        if root is None:
            return

        queue = list()
        queue.append(root)

        while len(queue) > 0:
            node = queue.pop()
            print(node.data)
            for i in reversed(range(len(node.children))):
                queue.append(node.children[i])



if __name__ == '__main__':
    node = Node("A", [Node("B", [Node("D", [Node("J", [])]), Node("H", [])]), Node("C", [Node("E", []), Node("F", [Node("I", [])])])])
    tree = Tree()
    print("Recursivo")
    tree.preorder_recursive(node)
    print("Interativo")
    tree.preorder_interative(node)




