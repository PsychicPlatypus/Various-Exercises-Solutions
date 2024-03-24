class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        marked = [0] * len(nums)
        for i in range(0, len(nums)):
            mark = nums[i]
            if marked[mark] == -1:
                return mark

            marked[mark] = -1

        return -1
