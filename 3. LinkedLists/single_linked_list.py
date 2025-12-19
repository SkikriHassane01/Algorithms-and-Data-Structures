class Node:
    """
    Object for storing a single node of a linked list.
    has two attributes:
        - data
        - link to the next node in the list
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return f"<Node Data: {self.data}>"

class LinkedList:
    """
    Singly Linked List
    """
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None
    
    def size(self):
        """
        Return the number of nodes in the list 
        it tack O(n)
        """
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
        
    def add(self, data):
        """
        Adds new node at the head of the list 
        tack O(1)
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert(self, data, index):
        """
        Insert data at a specific index
        if index at 0 (head of linked list) we will use add method ==> O(1)
        else O(n)
        """
        if index == 0:
            self.add(data)
        elif index > 0:
            position = index
            current = self.head
            new_node = Node(data)
            while position > 1:
                current = current.next
                position -= 1
            
            previous_node = current
            next_node = current.next
            
            previous_node.next = new_node
            new_node.next = next_node
    
    def remove_key(self, key):
        current = self.head
        previous = None
        found = False
        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next
            elif current.data == key:
                found = True
                previous.next = current.next
            else:
                previous = current
                current = current.next
        if found:
            return current.data
        else:
            return f"the key {key} isn't exist"
                
    def remove_index(self, index):
        current = self.head
        
        if index == 0:
            self.head = current.next
        
        elif index > 0:
            position = index
            while position > 2:
                current = current.next
                position -= 1
            current.next = current.next.next
        
        return current.data
    
    def search(self, key):
        """
        Search for the first node that match the key or Node if not found, it tack O(n)
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next
        return None

    def node_at_index(self, index):
        if index == 0:
            return self.head

        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next
                position += 1
            return current

    def __repr__(self):
        nodes = []
        current = self.head
        
        while current:
            if current is self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next is None:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"{current.data}")
            current = current.next
        return '->'.join(nodes)
        
    
# Example usage:
if __name__ == "__main__":
        
            
    N1 = Node(10)
    N2 = Node(20)
    print(N1)
    print(N2)

    linked_list = LinkedList()
    linked_list.add(10)
    linked_list.add(20)
    linked_list.add(30)
    linked_list.add(40)

    print(linked_list.size())

    print(linked_list)

    i = linked_list.search(10)
    print(i)

    linked_list.insert(50, 4)
    print(linked_list)

    removed_key = linked_list.remove_key(100)
    print(removed_key)
    print(linked_list)

    removed_index = linked_list.remove_index(2)
    print(removed_index)
    print(linked_list)