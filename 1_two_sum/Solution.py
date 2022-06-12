class Solution(object):
    def twoSum(self, nums, target):
        for x, i in enumerate(nums):
            for y, j in enumerate(nums):
                if i + j == target:
                    return [x, y]