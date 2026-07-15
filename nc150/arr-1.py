from typing import *
from collections import defaultdict


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        passed = defaultdict(bool)

        for num in nums:
            if passed[num]:
                return True

            passed[num] = True

        return False


case_one = [1, 2, 3, 3]
case_two = [1, 2, 3, 4]

solution = Solution().hasDuplicate
print(solution(case_one))
print(solution(case_two))
