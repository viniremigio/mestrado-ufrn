class Node:
    def __init__(self, data: int, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        left = f"left:{self.left}"
        right = f"right:{self.right}"
        return f"[{self.data}, {left}, {right}]"


def insert(input, root, i, n):
    # Base case for recursion
    if i < n:
        temp = Node(arr[i])
        root = temp
        # insere o nó à esquerda da raíz
        root.left = insert(input, root.left, 2 * i + 1, n)
        # insere o nó à direita da raíz
        root.right = insert(input, root.right, 2 * i + 2, n)
    return root


# Function to print tree nodes in
# InOrder fashion
def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.data, end=" ")
        inOrder(root.right)


# Driver Code
if __name__ == '__main__':
    arr = [50, 35, 70, 25, 40, 65, 90, 30, 80]
    n = len(arr)
    root = None
    root = insert(arr, root, 0, n)
    inOrder(root)