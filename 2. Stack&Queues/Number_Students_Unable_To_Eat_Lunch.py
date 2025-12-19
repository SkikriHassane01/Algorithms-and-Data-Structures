"""
https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/submissions/1825897719/
"""

from collections import Counter
# counter is used to count the number of students wanting each type of sandwich
# example: Counter({1: 3, 0: 2}) means 3 students want sandwich type 1 and 2 students want sandwich type 0

class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        result = len(students)
        cnt = Counter(students)
        for s in sandwiches:
            # if we have a student who wants this sandwich
            if cnt[s] > 0:
                cnt[s] -= 1
                result -= 1
            else:
                return result

        return result