from typing import *


class Solution:
    # Naive solution
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        res = []
        for i in range(len(nums)):
            pre = nums[0:i]
            post = nums[i + 1 :]
            together = pre + post
            res_curr = together[0]

            for j in range(1, len(together)):
                res_curr *= together[j]

            res.append(res_curr)

        return res


class Solution:
    # Division version
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        total_product = 1
        zero_count = 0
        res = []

        for i in nums:
            if i == 0:
                zero_count += 1
                if zero_count > 1:
                    return [0] * len(nums)

            else:
                total_product *= i

        for num in nums:
            if zero_count == 0:
                res.append(total_product // num)
            else:
                if num == 0:
                    res.append(total_product)
                else:
                    res.append(0)

        return res


class Solution:
    # Prefix, Suffix solution
    def productExceptSelf(self, nums: List[int]) -> List[int]:  # [1, 2, 4, 6]
        res = [1] * (len(nums))  # [1, 1, 1, 1]

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # res_pref == [1, 1, 2, 8]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        # res_suffix = [48, 24, 6, 1]

        return res


nums = [1, 2, 4, 6]
print(Solution().productExceptSelf(nums=nums))
