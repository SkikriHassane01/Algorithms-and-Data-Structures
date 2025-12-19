# What is Recursion?

```
Recursion is when a function calls itself to solve a problem by breaking it down into smaller, similar sub-problems.
```

## Structure of recursion function

```python
def recursive_function(parameters):
    # Base Case - Stop condition (we use this to prevent infinite loop)
    if base_condition:
        return base_value
    
    # recursive case - function call itself
    return recursive_function(modified_params)
```

## Common Mistakes ⚠️

### 1. No Base Case
```python
# ❌ WRONG - Infinite recursion!
def bad_recursion(n):
    return n + bad_recursion(n - 1)  # No base case!
```

### 2. Wrong Base Case
```python
# ❌ WRONG - Doesn't reach base case
def bad_countdown(n):
    if n == 0:
        return
    print(n)
    bad_countdown(n - 2)  # Skip 1, never reaches 0!
```

### 3. Not Moving Toward Base Case
```python
# ❌ WRONG - Infinite loop
def bad_factorial(n):
    if n == 1:
        return 1
    return n * bad_factorial(n)  # Should be n-1!
```

## Recursion Checklist ✅

Before writing recursive function, ask:

1. ✅ **What is the base case?** (simplest input)
2. ✅ **What is the recursive case?** (how to break down problem)
3. ✅ **Does each call move toward base case?** (avoid infinite loop)
4. ✅ **How to combine results?** (return statement)
