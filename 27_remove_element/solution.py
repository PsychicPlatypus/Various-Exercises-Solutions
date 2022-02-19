from typing import List

class Solution:
    def removeElement(self, nums, val):
        len_nums = 0
        for i in nums:
            if i != val:
                nums[len_nums] = i
                len_nums += 1
        return len_nums

test = Solution()
test.removeElement([0,1,2,2,3,0,4,2],2)

class Solution2:
    def removeElement(self, nums, val):
        lenght_var = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
                lenght_var -=- 1
        print(nums)
        return lenght_var