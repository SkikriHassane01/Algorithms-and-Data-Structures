from typing import List
import random
from pathlib import Path
def is_sorted(values: List):
    """
    Check if the values are sorted in Ascending order
    """
    n = len(values)
    for index in range(n - 1):
        if values[index] > values[index + 1]:
            return False
    return True

def bogo_sort(values: List):
    while not is_sorted(values):
        random.shuffle(values)
    return values


if __name__ == "__main__":
    numbers_path = r"/mnt/d/Projects/Algorithms-and-Data-Structures/Sorting/numbers"
    full_path = Path(numbers_path, "10_numbers.txt")
    with open(full_path, "r") as f:
        content = f.read().strip()
        numbers = eval(content)
    
    print(bogo_sort(numbers))