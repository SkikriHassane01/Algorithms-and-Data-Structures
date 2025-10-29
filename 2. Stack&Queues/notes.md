# Stacks
A **Stack** is a linear data structure that follow **LIFO (Last In First Out)** principle

## Visual Illustration
```
    Push →  |   5   |  ← Top (Pop)
            |   3   |
            |   1   |
            |_______|
```

## Operations & Time Complexity
| Operation | Description | Time Complexity |
|-----------|-------------|-----------------|
| `push()` | Add element to top | O(1) |
| `pop()` | Remove element from top | O(1) |
| `peek()` | View top element | O(1) |
| `is_empty()` | Check if stack is empty | O(1) |

---

# Queues
A **Queue** is a linear data structure that follows **FIFO (First In First Out)** principle 

## Visual Illustration
```
    Enqueue →  |_1_|_3_|_5_| → Dequeue
              Front      Rear
```

## Operations & Time Complexity
| Operation | Description | Time Complexity |
|-----------|-------------|-----------------|
| `enqueue()` | Add element to rear | O(1) |
| `dequeue()` | Remove element from front | O(1) |
| `front()` | View front element | O(1) |
| `is_empty()` | Check if queue is empty | O(1) |

# Stack vs Queue Comparison

| **Aspect** | **Stack** | **Queue** |
|------------|-----------|-----------|
| **Principle** | LIFO (Last In First Out) | FIFO (First In First Out) |
| **Insertion** | Push at top | Enqueue at rear |
| **Deletion** | Pop from top | Dequeue from front |
| **Access Point** | One end (top) | Two ends (front and rear) |
| **Real-world Examples** | - Stack of plates<br>- Browser back button<br>- Undo/Redo operations | - Line at ticket counter<br>- Print queue<br>- CPU task scheduling |
| **Python Implementation** | `list` with `append()`/`pop()` | `collections.deque` |
