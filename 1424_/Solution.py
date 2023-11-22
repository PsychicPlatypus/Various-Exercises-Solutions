from typing import List
from collections import defaultdict


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        traversed = []
        d = defaultdict(list)

        for x in range(len(nums)):
            for y in range(len(nums[x])):
                d[x + y].append(nums[x][y])

        for i in d.values():
            traversed.extend([i_ for i_ in reversed(i)])

        return traversed
