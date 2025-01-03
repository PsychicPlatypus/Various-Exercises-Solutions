from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix_sum = [nums[0]] * len(nums) 

        for i in range(len(nums) - 1):
            prefix_sum[i + 1] = prefix_sum[i]
            prefix_sum[i + 1] += nums[i + 1]

        res = 0

        arr_sum = prefix_sum[-1]

        for i in range(len(nums) - 1):
            if prefix_sum[i] >= arr_sum - prefix_sum[i]:
                res += 1

        return res
        


Solution().waysToSplitArray([1,2,3,4])
Solution().waysToSplitArray([10,4,-8,7])
Solution().waysToSplitArray([2,3,1,0])


