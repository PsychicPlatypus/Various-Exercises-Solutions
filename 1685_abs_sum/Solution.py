from typing import List
from collections import defaultdict


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        psum = [0] * n
        ssum = [0] * n
        psum[0] = nums[0]
        ssum[n - 1] = nums[n - 1]
        for i in range(1, n):
            psum[i] = psum[i - 1] + nums[i]
            ssum[n - i - 1] = ssum[n - i] + nums[n - i - 1]
        for i in range(n):
            cad = ((nums[i] * i) - psum[i]) + (ssum[i] - (nums[i] * (n - i - 1)))
            result[i] = cad

        return result
