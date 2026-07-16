from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x, i in enumerate(nums):
            for y, j in enumerate(nums):
                if i + j == target:
                    return [x, y]


solution = Solution().twoSum

print(solution([3, 4, 5, 6], 7))
