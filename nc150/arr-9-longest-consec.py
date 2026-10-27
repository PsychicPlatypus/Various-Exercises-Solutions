from typing import *
from collections import defaultdict
from pprint import pprint


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        memory = defaultdict(int)

        for num in set(nums):
            curr = memory[num - 1] + memory[num + 1] + 1

            memory[num] = curr

            memory[num - memory[num - 1]] = curr
            memory[num + memory[num + 1]] = curr

        return max(memory.values())


print(Solution().longestConsecutive([2, 20, 4, 10, 3, 4, 5]))
