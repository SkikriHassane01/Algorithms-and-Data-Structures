def merge_sort(lst):
    """
    Sort a list in ascending order
    returns a new sorted list
    
    steps:
        - Divide: find the mid of the list and divide into sublist
        - Conquer: recursively sort the sublists created in previous step 
        - Merge: Merge the sorted sublists created in the previous step
    Run in O(n log n) time
    """
    
    # stoping condition
    if len(lst) <= 1:
        return lst
        
    left_half, right_half = split(lst)
    
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return merge(left, right)
    
def split(lst):
    """
    Divide the unsorted list at mid 
    return a sublist (left, right)
    
    tack O(log n) time
    """
    mid = len(lst) // 2
    
    # slicing tack O(k) time
    left_half = lst[: mid] #mid not include
    right_half = lst[mid :]
    return left_half, right_half
    
def merge(left, right):
    """
    merges two lists, sorting them in process
    return new merged list
    Run in O(n)
    """
    
    l = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
            
    # right list shorter than the left
    while i < len(left):
        l.append(left[i])
        i += 1
        
    # else
    while j < len(right):
        l.append(right[j])
        j += 1
    
    return l

def verify_sorted(lst):
    n = len(lst)
    
    if n == 0 or n == 1:
        return True
    return lst[0] <= lst[1] and verify_sorted(lst[1:])
        

lst = [3, 10, 2, 50, 1 , 4, 199, 1000, 1]
l = merge_sort(lst)
print(l)
print(verify_sorted(l))