# 1. Create an empty dynamic array (a list)
my_dynamic_list = []
print(f"Initial list: {my_dynamic_list}, Size: {len(my_dynamic_list)}")

# 2. Add elements to it. The list "grows" automatically.
print("...Adding elements...")
my_dynamic_list.append(10)
my_dynamic_list.append(20)
my_dynamic_list.append(30)
print(f"After adding: {my_dynamic_list}, Size: {len(my_dynamic_list)}")

# 3. Remove an element. The list "shrinks".
print("...Removing an element...")
removed_item = my_dynamic_list.pop() # Removes the last item
print(f"Removed '{removed_item}'")
print(f"After popping: {my_dynamic_list}, Size: {len(my_dynamic_list)}")