from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        return_list = [sum + i for i in nums]
        return return_list
