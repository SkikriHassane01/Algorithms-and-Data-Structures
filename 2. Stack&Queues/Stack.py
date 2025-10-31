class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        if isinstance(item, list):
            self.items.extend(item)
        else:
            self.items.append(item)

    def is_empty(self):
        return len(self.items) == 0
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def size(self):
        return len(self.items)


# Example usage:
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push([2, 3, 4])
    print("Stack contents:", stack.items)
    print("Popped item:", stack.pop())
    print("Peek item:", stack.peek())
    print("Stack size:", stack.size())
    print("Is stack empty?", stack.is_empty())