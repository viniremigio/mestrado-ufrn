class Node:
    def __init__(self, data: int, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        left = f"left:{self.left}"
        right = f"right:{self.right}"
        return f"[{self.data}, {left}, {right}]"


class BinarySearchOps:
    def delete_node(self, root: Node, key: int):

        ## Caso base
        if root is None:
            return root

        ## Busca à esquerda da árvore se o valor for menor que o root
        if key < root.data:
            root.left = self.delete_node(root.left, key)

        ## Busca à direita da árvore se o valor for menor que o root
        elif (key > root.data):
            root.right = self.delete_node(root.right, key)

        else:
            # Caso base de remoção quando chega mais à esquerda
            if root.left is None:
                temp = root.right
                root = None
                return temp

            # Caso base de remoção quando chega mais à direita
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Encontra o nó mais à esquerda da subárvore direita
            # Este nó será a nova raíz
            temp = self.tree_minimum(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right, temp.key)

        return root

    def tree_minimum(self, x: Node):
        """
        Encontra o nó mais a esquerda da árvore
        :param x:
        :return:
        """
        while x.left is not None:
            x  = x.left
        return x


if __name__ == '__main__':
    tree = Node(50, Node(35, Node(25, None,  Node(30)), Node(40)), Node(70, Node(65), Node(90, Node(80), None)))
    ops = BinarySearchOps()
    new_tree = ops.delete_node(tree, 40)
    print(new_tree)




