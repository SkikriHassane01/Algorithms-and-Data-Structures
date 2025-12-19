"""
link: https://leetcode.com/problems/climbing-stairs/description/
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
class Solution:
    def climbStairs(self, n:int) -> int:
        # Solution 1: Recursion (Exponential Time Complexity)
        # # base case
        # if n == 0:
        #     return 0
        # elif n == 1:
        #     return 1
        # elif n == 2:
        #     return 2

        # # recursive case
        # return self.climbStars(n-1) + self.climbStars(n-2)

        # solution 2: Dynamic Programming 
        # steps = [1, 2]
        # for i in range(2, n):
        #     steps.append(steps[i-1] + steps[i-2])
        # return steps[n-1]
    
        # Solution 3: Optimized Dynamic Programming (Space Complexity O(1))
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        first, second = 1, 2
        for i in range(2, n):
            current = first + second
            first = second
            second = current
        return second