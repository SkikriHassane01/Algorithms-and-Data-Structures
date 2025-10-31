class Queues:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        if isinstance(item, list):
            self.items.extend(item)
        else:
            self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def size(self):
        return len(self.items)
    
# Example usage:
if __name__ == "__main__":
    queue = Queues()
    queue.enqueue(1)
    queue.enqueue([2, 3, 4])
    print("Queue contents:", queue.items)
    print("Dequeued item:", queue.dequeue())
    print("Front item:", queue.front())
    print("Queue size:", queue.size())
    print("Is queue empty?", queue.is_empty())

    # using collections.deque for better performance
    from collections import deque
    deque_queue = deque()
    deque_queue.append(1)
    deque_queue.extend([2, 3, 4])
    print("Deque contents:", list(deque_queue))
    print("Dequeued item from deque:", deque_queue.popleft())
    print("Front item from deque:", deque_queue[0])
    print("Deque size:", len(deque_queue))
    print("Is deque empty?", len(deque_queue) == 0)

    