"""
Binary Recursion (Two Calls)
"""
def fibonacci(n):
    # base case 
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # recursive case 
        return fibonacci(n-1) + fibonacci(n-2)
    
if __name__ == "__main__":
    n = 5
    print(f"The {n}th Fibonacci number is {fibonacci(n)}")