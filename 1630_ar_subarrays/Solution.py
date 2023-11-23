from typing import List


class Solution:
    def checkArithmeticSubarrays(
        self, nums: List[int], l: List[int], r: List[int]
    ) -> List[bool]:
        results = []

        for i, j in zip(l, r):
            sub_array = nums[i : j + 1]
            results.append(self.isArithmetic(sub_array))

        return results

    def isArithmetic(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        nums.sort()
        arithmetic_sum = abs(nums[0] - nums[1])

        for i in range(len(nums) - 1):
            sum_next = abs(nums[i] - nums[i + 1])
            if sum_next != arithmetic_sum:
                return False

        return True


nums = [4, 6, 5, 9, 3, 7]
l = [0, 0, 2]
r = [2, 3, 5]

print(Solution().checkArithmeticSubarrays(nums, l, r))
