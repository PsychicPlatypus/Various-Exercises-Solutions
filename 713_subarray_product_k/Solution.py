class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        solutions = 0
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums) + 1):
                window = nums[i:j]
                product = 1
                for num in window:
                    product *= num
                if product < k:
                    solutions += 1

        return solutions
