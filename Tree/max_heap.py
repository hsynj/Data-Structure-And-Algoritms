class MaxHeap:
    """
    Implementation of a Max Heap data structure.
    In a Max Heap, for any given node I, the value of I is greater than or equal to
    the values of its children.
    """
    def __init__(self, data: list[int] | None = None):
        """
        Initializes the heap.
        
        Args:
            data (list[int] | None): An optional initial list to convert into a heap.
        """
        self.heap = []
        if data:
            self.heap = data[:]
            self._build_heap()

    def _build_heap(self):
        """
        Converts the internal list into a max heap in O(n) time complexity.
        Starts from the last non-leaf node and sifts down.
        """
        n = len(self.heap)
        # Start from the last non-leaf node and move up to the root
        for i in range(n // 2 - 1, -1, -1):
            self._sift_down(i)

    def add(self, key: int):
        """
        Inserts a new key into the heap and maintains the heap property.
        
        Args:
            key (int): The value to add.
        """
        self.heap.append(key)
        self._sift_up(len(self.heap) - 1)

    def delete(self) -> int | None:
        """
        Removes and returns the maximum element (the root) from the heap.
        
        Returns:
            int | None: The maximum value or None if heap is empty.
        """
        if not self.heap:
            return None
        
        max_val = self.heap[0]
        
        # Move the last element to the root and remove the last element
        last_val = self.heap.pop()
        
        if self.heap:
            self.heap[0] = last_val
            self._sift_down(0)
            
        return max_val

    def get_heap(self) -> list[int]:
        """Returns the current state of the heap as a list."""
        return self.heap

    def _sift_up(self, index: int):
        """Moves the element at 'index' up to its correct position."""
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._sift_up(parent)

    def _sift_down(self, index: int):
        """Moves the element at 'index' down to its correct position."""
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2
        n = len(self.heap)

        if left < n and self.heap[left] > self.heap[largest]:
            largest = left
        
        if right < n and self.heap[right] > self.heap[largest]:
            largest = right
            
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._sift_down(largest)
