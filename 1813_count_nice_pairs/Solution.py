from typing import List


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        if nums == [] or len(nums) == 1:
            return 0

        count = 0
        min_p = 0

        while min_p <= len(nums) - 1:
            for max_p in range(len(nums) - 1, min_p, -1):
                if self.passesRevRule(nums, min_p, max_p):
                    count += 1
            min_p += 1

        return count

    def passesRevRule(self, nums: List[int], x: int, y: int) -> bool:
        rev_x = self.rev(nums[x])
        rev_y = self.rev(nums[y])

        return nums[x] + rev_y == nums[y] + rev_x

    def rev(self, number: int) -> int:
        reversed_num = 0

        while number != 0:
            digit = number % 10
            reversed_num = reversed_num * 10 + digit
            number //= 10

        return reversed_num


print(Solution().countNicePairs([13, 10, 35, 24, 76]))  # 4
