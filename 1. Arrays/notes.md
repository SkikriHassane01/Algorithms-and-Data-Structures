# Arrays

## Array Definition 
an array is a fundamental data structure that stores collection of elements in a contiguous memory locations. Each element can be accessed directly using its index position, starting from 0

## Static Array vs Dynamic Array

| **Aspect** | **Static Array** | **Dynamic Array** |
|------------|------------------|-------------------|
| **Size** | Fixed at compile time, cannot be changed | Can grow or shrink at runtime |
| **Flexibility** | Less flexible, size must be known beforehand | More flexible, adjusts to needs |
| **Performance** | Faster access, no overhead | Slight overhead due to resizing operations |
| **Memory Usage** | May waste memory if oversized or cause overflow if undersized | Efficient memory usage, allocates as needed |
| **Example (C++)** | `int arr[10];` | `std::vector<int> arr;` |
| **Example (Python)** | `array.array()` or `numpy.ndarray()`| `list = []` (Python lists are dynamic) |