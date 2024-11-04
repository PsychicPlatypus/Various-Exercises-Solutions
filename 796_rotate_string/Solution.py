"""
796. Rotate String
Easy
Topics
Companies

Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

    For example, if s = "abcde", then it will be "bcdea" after one shift.

 

Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true

Example 2:

Input: s = "abcde", goal = "abced"
Output: false

 

Constraints:

    1 <= s.length, goal.length <= 100
    s and goal consist of lowercase English le
"""

"""
It only rotates on the left side
abcde
<---
bcdea
<---
cdeab "goal"
"""

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        target_char = goal[0]

        for i in range(len(s)):
            if s[i] == target_char:
                back = s[0:i]
                front = s[i:]
                if (front + back) == goal:
                    return True

        return False

print(Solution().rotateString("abcde", "cdeab"))

# Time to finish correctly 7 minutes