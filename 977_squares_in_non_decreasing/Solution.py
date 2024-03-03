from typing import *

"""
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
"""


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        negatives = []
        x = 0
        for i in range(len(nums)):
            if nums[i] < 0:
                negatives.append(nums[i] ** 2)
            else:
                nums[x] = nums[i] ** 2
                nums[i] = 0
                x += 1
        x = len(negatives) - 1
        for i in range(len(nums)):
            if x < 0:
                break
            if nums[i] > negatives[x]:
                nums.insert(i, negatives[x])
                nums.pop()
                x -= 1
        return nums
