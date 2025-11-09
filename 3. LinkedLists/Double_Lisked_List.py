class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
class MyLinkedList:

    def __init__(self):
        # create a two dummy node to not deal with the edg cases
        self.left = Node(0)
        self.right = Node(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        current = self.left.next
        i = 0
        while current != self.right:
            if i == index:
                return current.val
            current = current.next
            i += 1
        return -1
    
    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.left.next
        new_node.prev = self.left
        self.left.next.prev = new_node
        self.left.next = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.right
        new_node.prev = self.right.prev
        self.right.prev.next = new_node
        self.right.prev = new_node 

    def addAtIndex(self, index: int, val: int) -> None:
        current = self.left.next
        i = 0
        while current != self.right:
            if i == index:
                new_node = Node(val)
                new_node.next = current
                new_node.prev = current.prev
                current.prev.next = new_node
                current.prev = new_node
                return
            current = current.next
            i += 1
        if i == index:
            self.addAtTail(val)

    def deleteAtIndex(self, index: int) -> None:
        current = self.left.next
        i = 0
        while current != self.right:
            if i == index:
                current.prev.next = current.next
                current.next.prev = current.prev
                return
            current = current.next
            i += 1
        return

if __name__ == "__main__":
    L = MyLinkedList()
    L.addAtHead(1)
    L.addAtHead(2)
    L.addAtTail(3)
    L.addAtIndex(1, 4)  # linked list becomes 2->4->1->3
    L.deleteAtIndex(2)  # linked list becomes 2->4->3
    print(L.get(0))  # Output: 2
    print(L.get(1))  # Output: 4
    print(L.get(2))  # Output: 3