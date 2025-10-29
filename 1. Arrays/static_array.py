#=======================================================================================
# Option A: Using a tuple to represent a static array
# tuples are immutable, so their size cannot be changed after creation

# 1. create a tuple
static_array_tuple = (1, 2, 3, 4, 5)
print(f'Tuple (static array): {static_array_tuple}, Length: {len(static_array_tuple)}')

# 2. you cannot change an existing element
try:
    static_array_tuple[0] = 10
except Exception as e:
    print(f'Error when trying to modify tuple: {e}')

# 3. you cannot add or remove elements
try:
    static_array_tuple.append(40)
except AttributeError as e:
    print(f"Error adding: {e}")






#=======================================================================================
# Option B: The numpy.array (The True Static Array)
import numpy as np

# 1. Create a static array of 5 zeros. Its size is fixed.
my_static_array = np.zeros(5)
print(f"Initial array: {my_static_array}, Size: {my_static_array.size}")

# 2. You CAN change the elements inside it (it's mutable)
print("...Changing elements...")
my_static_array[0] = 100
my_static_array[1] = 200
print(f"After changing: {my_static_array}")

# 3. You CANNOT append to it to change its size
try:
    my_static_array.append(300) # This will fail
except AttributeError as e:
    print(f"Error appending: {e}")

# 4. To "add" an item, you create a new array
print("...Creating a new array...")
new_array = np.append(my_static_array, [300])
print(f"New array: {new_array}")
print(f"Original array is unchanged: {my_static_array}")