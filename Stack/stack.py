class Stack:
    """
    A stack data structure implementation using a Python list.
    
    The stack follows the Last-In-First-Out (LIFO) principle.
    
    Attributes:
        items (list): The internal list storing stack elements.
    """
    
    def __init__(self) -> None:
        """Initialize an empty stack."""
        self.items = []

    def isEmpty(self) -> bool:
        """
        Check if the stack is empty.
        
        Returns:
            bool: True if the stack is empty, False otherwise.
            
        Time Complexity: O(1)
        """
        return len(self.items) == 0
    
    def push(self, item) -> None:
        """
        Add an item to the top of the stack.
        
        Args:
            item (any): The item to add to the stack.
            
        Time Complexity: O(1)
        """
        self.items.append(item)
    
    def pop(self) -> any:
        """
        Remove and return the item at the top of the stack.
        
        Returns:
            any: The item removed from the top of the stack.
            
        Raises:
            Exception: If the stack is empty.
            
        Time Complexity: O(1)
        """
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise Exception('Nothing found..')
    
    def peek(self) -> any:
        """
        Return the item at the top of the stack without removing it.
        
        Returns:
            any: The item at the top of the stack.
            
        Raises:
            Exception: If the stack is empty.
            
        Time Complexity: O(1)
        """
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise Exception('Nothing found..')

    def size(self) -> int:
        """
        Return the number of items in the stack.
        
        Returns:
            int: The number of items currently in the stack.
            
        Time Complexity: O(1)
        """
        return len(self.items)
