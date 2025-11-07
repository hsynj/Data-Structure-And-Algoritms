class Node:
    def __init__(self, data: any) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self.size = 0

    def isEmpty(self) -> bool:
        if self.size == 0 or self._head is None:
            return True
        return False

    def index(self, value: any) -> int:
        current = self._head
        index = 0
        while current != value:
            current = current.next
            index += 1
        return index

    def get_by_index(self, index: int) -> Node | None:
        current = self._head
        while index != 0:
            current = current.next
            index -= 1
        return current

    # insert to end of list
    def append(self, data: any) -> None:
        new_node = Node(data)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self.size += 1

    # insert to beginning of list
    def prepend(self, data: any) -> None:
        new_node = Node(data)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head = new_node
        self.size += 1

    # insert to middle of list
    def add(self, data: any, position: int) -> None:
        if position is None:
            self.append(data)
            return
        if 0 <= position < self.size:
            current = self.get_by_index(position)
            
    

    def remove(self, data: any) -> None:
        if self.isEmpty():
            print('list is empty')
            return
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
        if self.isEmpty():
            print('list is empty')
            return
        self._head = None
        self.size = 0

    def display(self) -> None:
        current = self._head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
