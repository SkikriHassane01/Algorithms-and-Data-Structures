from single_linked_list import LinkedList

def merge_sort(linked_list: LinkedList):
    """
    Sorts a linked list in ascending order
    
        - Recursively divide the linked list into sub lists containing a single node
        - repeatedly merge the sub lists to produce sorted sub lists until one remains
    Return a sorted linked list
    """
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list: LinkedList):
    """
    Divide the unsorted list at mid into sub linked lists
    """
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None
        return left_half, right_half

    else:
        size = linked_list.size()
        mid = size // 2
        mid_node = linked_list.node_at_index(mid - 1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next
        mid_node.next = None # break the connection from the left_half
        return left_half, right_half


def merge(left: LinkedList, right: LinkedList):
    """
    Merges two linked lists, sorting by data in nodes
    Returns a new, merged list
    """
    merged = LinkedList()

    merged.add(0)

    current = merged.head

    left_head, right_head = left.head, right.head

    while left_head or right_head:

        if left_head is None:
            current.next = right_head
            right_head = right_head.next
        
        elif right_head is None:
            current.next = left_head
            left_head = left_head.next
        
        else:
            right_data = right_head.data
            left_data = left_head.data

            if left_data < right_data:
                current.next = left_head
                left_head = left_head.next

            else:
                current.next = right_head
                right_head = right_head.next
    
        current = current.next

    # discard the fake head
    head = merged.head.next
    merged.head = head

    return merged

if __name__ == "__main__":
    l = LinkedList()
    l.add(30)
    l.add(10)
    l.add(50)
    l.add(20)
    print("Unsorted linked list:")
    print(l)
    sorted_linked_list = merge_sort(l)
    print("Sorted linked list:")
    print(sorted_linked_list)
