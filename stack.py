class Stack:
    def __init__(self) -> None:
        self.items = []

    def isEmpty(self) -> bool:
        return len(self.items) == 0
    
    def push(self, item) -> None:
        self.items.append(item)
    
    def pop(self) -> any:
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise Exception('Nothing found..')
    
    def peek(self) -> any:
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise Exception('Nothing found..')

    def size(self) -> int:
        return len(self.items)
