from node import SingleNode
class SingleLinkedList:
    """
    A singly linked list implementation.
    
    This class provides methods for common linked list operations such as
    insertion, deletion, and traversal.
    
    Attributes:
        _head (Node): Reference to the first node in the list.
        _tail (Node): Reference to the last node in the list.
        size (int): The number of nodes in the list.
    """
    
    def __init__(self) -> None:
        """Initialize an empty single linked list."""
        self._head = None
        self._tail = None
        self.size = 0

    def isEmpty(self) -> bool:
        """
        Check if the linked list is empty.
        
        Returns:
            bool: True if the list is empty, False otherwise.
        """
        if self.size == 0 or self._head is None:
            return True
        return False

    def index(self, value: any) -> int:
        """
        Find the index of the first node with the given value.
        
        Args:
            value (any): The node object to find.
            
        Returns:
            int: The index of the node in the list.
            
        Note:
            This method searches for a node object, not data value.
        """
        current = self._head
        index = 0
        while current.data != value:
            current = current.next
            index += 1
        return index

    def get_by_index(self, index: int) -> SingleNode | None:
        """
        Retrieve the node at the specified index.
        
        Args:
            index (int): The zero-based index of the node to retrieve.
            
        Returns:
            Node | None: The node at the specified index, or None if index is out of bounds.
        """
        if 0 <= index < self.size:
            current = self._head
            while index != 0:
                current = current.next
                index -= 1
            return current
        else:
            raise Exception("Index out of bounds")

    # insert to end of list
    def append(self, data: any) -> None:
        """
        Insert a new node at the end of the list.
        
        Args:
            data (any): The data to store in the new node.
            
        Time Complexity: O(1)
        """
        new_node = SingleNode(data)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self.size += 1

    # insert to beginning of list
    def prepend(self, data: any) -> None:
        """
        Insert a new node at the beginning of the list.
        
        Args:
            data (any): The data to store in the new node.
            
        Time Complexity: O(1)
        """
        new_node = SingleNode(data)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head = new_node
        self.size += 1

    # insert to middle of list
    def add(self, data: any, position: int) -> None:
        """
        Insert a new node at the specified position in the list.
        
        Args:
            data (any): The data to store in the new node.
            position (int): The index at which to insert the new node.
                           If None, appends to the end.
                           If 0, prepends to the beginning.
                           
        Time Complexity: O(n) where n is the position.
        
        Note:
            If position is out of bounds (< 0 or >= size), no insertion occurs.
        """
        if position is None:
            self.append(data)
            return
        elif position == 0:
            self.prepend(data)
            return
        elif 0 < position < self.size:
            current = self.get_by_index(position)
            previous = self.get_by_index(position - 1)
            new_node = SingleNode(data)
            new_node.next = current
            previous.next = new_node
            self.size += 1

    def remove(self, data: any) -> None:
        """
        Remove the first node containing the specified data.
        
        Args:
            data (any): The data value to search for and remove.
            
        Time Complexity: O(n) where n is the number of nodes.
        
        Note:
            If the list is empty, prints 'list is empty'.
            If data is not found, no action is taken.
        """
        if self.isEmpty():
            raise ValueError('list is empty')

        if self._head.data == data:
            self._head = self._head.next
            self.size -= 1
            if self._head is None:
                self._tail = None
            return
        current = self._head.next
        previous = self._head
        while current is not None:
            if current.data == data:
                previous.next = current.next
                if current == self._tail:
                    self._tail = previous
                self.size -= 1
                return
            previous = current
            current = current.next

    def remove_all(self) -> None:
        """
        Remove all nodes from the list, clearing it completely.
        
        Time Complexity: O(1)
        
        Note:
            If the list is already empty, prints 'list is empty'.
        """
        if self.isEmpty():
            raise ValueError('list is empty')

        self._head = None
        self._tail = None
        self.size = 0

    def display(self) -> None:
        """
        Print all elements in the list in order.
        
        The output format is: data1 -> data2 -> data3 -> None
        
        Time Complexity: O(n) where n is the number of nodes.
        """
        current = self._head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")