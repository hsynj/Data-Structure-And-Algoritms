class SingleNode:
    """
    Initialize a new single node with the given data.
    
    Attributes:
        data (any): The data stored in the node.
        next (Node): Reference to the next node in the list.
    """
    
    def __init__(self, data: any) -> None:
        """
        Initialize a new node with the given data.
        
        Args:
            data (any): The data to store in the node.
        """
        self.data = data
        self.next = None

class DoubleNode:
    def __init__(self, data: any) -> None:
        """
        Initialize a new double node with the given data.
        
        Args:
            data (any): The data to store in the node.
            next (Node): Reference to the next node in the list.
            prev (Node): Reference to the previous node in the list.
        """
        self.data = data
        self.next = None
        self.prev = None
