"""
Linear Recursion (One Call)
"""

def factorial(n):
     # Base case:
     if n <= 1:
          return 1
     
     # recursive case:
     return n * factorial(n-1)

if __name__ == "__main__":
    n = 5
    print(f"Factorial of {n} is {factorial(n)}")