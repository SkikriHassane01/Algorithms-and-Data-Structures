from typing import List
import random
from pathlib import Path
def quicksort(values: List):
    """
    Sort a list in ascending order 
    - 1. pick a pivot values (random values form the list )
    - divide the list into sub list that contain values less than pivot and another list that contain the values greater than pivot
    - recursively apply the above steps to the sub lists
    - combine the sorted sub lists and pivot to get the sorted list
    """
    # Base Case:
    if len(values) <= 1:
        return values
    
    # Divide and concur
    less_than_pivot = []
    greater_than_pivot = []
    pivot = random.choice(values)

    for value in values:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

if __name__ == "__main__":
    numbers_path = r"/mnt/d/Projects/Algorithms-and-Data-Structures/Sorting/numbers"
    full_path = Path(numbers_path, "1000000_numbers.txt")
    with open(full_path, "r") as f:
        content = f.read().strip()
        numbers = eval(content)
    print(quicksort(numbers))
    