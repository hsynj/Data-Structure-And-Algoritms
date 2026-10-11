class Node:
    """
    Represents a node in the Binary Search Tree.
    """
    def __init__(self, key: int):
        self.key = key
        self.left: 'Node | None' = None
        self.right: 'Node | None' = None


class BinarySearchTree:
    """
    Implementation of a Binary Search Tree (BST) with additional methods
    for counting nodes and conditional pruning.
    """
    def __init__(self):
        self.root: Node | None = None

    def insert(self, key: int):
        """Inserts a new key into the BST."""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current: Node, key: int):
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert_recursive(current.left, key)
        elif key > current.key:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert_recursive(current.right, key)

    def inorder_traversal(self) -> list[int]:
        """Returns the in-order traversal of the tree as a list."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node: Node | None, result: list[int]):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)

    # --- Question 1: Count Non-Leaf Nodes ---
    def count_non_leaf_nodes(self) -> int:
        """Calculates the number of non-leaf (internal) nodes."""
        return self._count_non_leaf_recursive(self.root)

    def _count_non_leaf_recursive(self, node: Node | None) -> int:
        if node is None or (node.left is None and node.right is None):
            return 0
        
        return 1 + self._count_non_leaf_recursive(node.left) + \
               self._count_non_leaf_recursive(node.right)

    # --- Question 2: Count Leaf Nodes ---
    def count_leaf_nodes(self) -> int:
        """Calculates the number of leaf nodes."""
        return self._count_leaf_recursive(self.root)

    def _count_leaf_recursive(self, node: Node | None) -> int:
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self._count_leaf_recursive(node.left) + \
               self._count_leaf_recursive(node.right)

    # --- Question 3: Delete nodes greater than 'a' ---
    def remove_nodes_greater_than(self, a: int):
        """Removes all nodes with a value greater than 'a'."""
        self.root = self._remove_greater_recursive(self.root, a)

    def _remove_greater_recursive(self, node: Node | None, a: int) -> Node | None:
        if node is None:
            return None
        
        if node.key > a:
            return self._remove_greater_recursive(node.left, a)
        
        node.right = self._remove_greater_recursive(node.right, a)
        return node

    # --- Helper for Standard Deletion ---
    def delete(self, key: int):
        """Standard BST deletion method."""
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node: Node | None, key: int) -> Node | None:
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete_recursive(node.right, temp.key)
        
        return node

    def _min_value_node(self, node: Node) -> Node:
        current = node
        while current.left is not None:
            current = current.left
        return current
