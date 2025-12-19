from typing import List
from pathlib import Path
def selection_sort(values: List):
    sorted_list = []
    n = len(values)
    for i in range(0, n):
        index_to_remove = index_of_min(values)
        sorted_list.append(values.pop(index_to_remove))
    return sorted_list

def index_of_min(values: List):
    min_index = 0
    for i in range(1, len(values)):
        if values[i] < values[min_index]:
            min_index = i
    return min_index

if __name__ == "__main__":
    numbers_path = r"/mnt/d/Projects/Algorithms-and-Data-Structures/Sorting/numbers"
    full_path = Path(numbers_path, "1000_numbers.txt")
    with open(full_path, "r") as f:
        content = f.read().strip()
        numbers = eval(content)
    print(selection_sort(numbers))
