from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_ = len(nums)
        res = [1] * len_

        for i in range(1, len_):
            res[i] = res[i - 1] * nums[i - 1]

        r = nums[-1]
        for i in range(len_ - 2, -1, -1):
            res[i] *= r
            r *= nums[i]

        return res


print(Solution().productExceptSelf([1, 2, 3, 4]))
