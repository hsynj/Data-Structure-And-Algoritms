from node import DoubleNode
from single_linked_list import SingleLinkedList

class DoubleLinkedList(SingleLinkedList):
    """
    A doubly linked list implementation.
    
    This class provides methods for common linked list operations such as
    insertion, deletion, and traversal.
    
    Attributes:
        _head (Node): Reference to the first node in the list.
        _tail (Node): Reference to the last node in the list.
        size (int): The number of nodes in the list.
    """
    
    def __init__(self) -> None:
        """Initialize an empty double linked list."""
        super().__init__()

    def isEmpty(self):
        """
        Check if the doubly linked list is empty.
        
        Returns:
            bool: True if the list is empty, False otherwise.
            
        Time Complexity: O(1)
        """
        return super().isEmpty()

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
        return super().index(value)

    def get_by_index(self, index) -> DoubleNode | None:
        """
        Retrieve the node at the specified index.
        
        Args:
            index (int): The zero-based index of the node to retrieve.
            
        Returns:
            DoubleNode | None: The node at the specified index, or None if index is out of bounds.
            
        Time Complexity: O(n) where n is the index value.
        """
        if 0 <= index < self.size:
            current = self._head
            while index != 0:
                current = current.next
                index -= 1
            return current
        else:
            raise Exception("Index out of bounds")
    
    def append(self, data):
        """
        Insert a new node at the end of the list.
        
        Args:
            data (any): The data to store in the new node.
            
        Time Complexity: O(1)
        """
        new_node = DoubleNode(data)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            new_node.prev = self._tail
            self._tail = new_node

        self.size += 1
    
    def prepend(self, data: any) -> None:
        """
        Insert a new node at the beginning of the list.
        
        Args:
            data (any): The data to store in the new node.
            
        Time Complexity: O(1)
        """
        new_node = DoubleNode(data)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
        self.size += 1

    def add(self, data: any, position: int) -> None:
        """
        Insert a new node at the specified position in the list.
        
        Args:
            data (any): The data to store in the new node.
            position (int): The index at which to insert the new node.
                           If None or equal to size, appends to the end.
                           If 0, prepends to the beginning.
                           
        Time Complexity: O(n) where n is the position.
        
        Note:
            If position is out of bounds (< 0 or > size), no insertion occurs.
            Updates both next and prev pointers to maintain doubly linked structure.
        """
        if position is None or position == self.size:
            self.append(data)
            return
        elif position == 0:
            self.prepend(data)
            return
        elif 0 < position < self.size:
            current = self.get_by_index(position)
            # previous = self.get_by_index(position - 1) O(n)
            previous = current.prev # O(1)
            new_node = DoubleNode(data)
            new_node.next = current
            new_node.prev = previous
            previous.next = new_node
            current.prev = new_node
            self.size += 1

    def remove(self, data: any) -> None:
        """
        Remove the first node containing the specified data.
        
        Args:
            data (any): The data value to search for and remove.
            
        Time Complexity: O(n) where n is the number of nodes.
        
        Note:
            If the list is empty, raises ValueError.
            If data is not found, no action is taken.
        """
        if self.isEmpty():
            raise ValueError('list is empty')
        
        current = self._head
        
        while current is not None:
            if current.data == data:
                # Case 1: Node is the head
                if current == self._head:
                    self._head = current.next
                    if self._head is not None:
                        self._head.prev = None
                    else:
                        self._tail = None
                
                # Case 2: Node is the tail
                elif current == self._tail:
                    self._tail = current.prev
                    self._tail.next = None
                
                # Case 3: Node is in the middle
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                
                self.size -= 1
                return
            
            current = current.next

    def remove_all(self) -> None:
        """
        Remove all nodes from the list, clearing it completely.
        
        Time Complexity: O(1)
        
        Note:
            Resets the list to an empty state by clearing head, tail, and size.
            If the list is already empty, raises ValueError.
        """
        super().remove_all()

    def display(self) -> None:
        """
        Print all elements in the list from head to tail.
        
        The output format is: data1 <-> data2 <-> data3 <-> None
        
        Time Complexity: O(n) where n is the number of nodes.
        """
        current = self._head
        while current is not None:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")