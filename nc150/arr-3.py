from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_targets = dict()

        for i in range(len(nums)):
            num_targets[target - nums[i]] = i

        for i in range(len(nums)):
            position = num_targets.get(nums[i])
            if position != None and i != position:
                return [i, position]


solution = Solution().twoSum

print(solution([3, 4, 5, 6], 7))
